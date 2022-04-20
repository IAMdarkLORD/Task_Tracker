import firebase_admin
from firebase_admin import credentials, firestore
from datetime import *
import datetime


class Task_Tracker():
    def __init__(self) -> None:
        self.cred = credentials.Certificate("C:/Users/darkl/OneDrive/Desktop/Task-Tracker/task-tracker-f2d0e-firebase-adminsdk-ax5nn-7f93d0a403.json")
        firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()
        self.absentMem = self.db.collection('TodayAbsentMembers').document('AbsentMembers').get().to_dict()
        self.absentMemList = list(self.absentMem.values())[0]

    def team(self,teamName,members):
        collection = self.db.collection('Team')
        collection.document(teamName).set(members)
        resp = {"success": True ,"msg":"Team created successfully"}

        return resp

    def availability(self,teamName):
        Memb = self.db.collection('Team').document(teamName).get()
        members = Memb.to_dict().items()
        data = {}
        print('Absent',self.absentMemList)
        for m in members:
            if(m[1] in self.absentMemList):
                data[m[0]] = 'False'
            else:
                data[m[0]] = 'True'
        resp = {"success": True ,"data":data}

        print(resp)

        return resp

    def task(self,task_name, priority, start_date, end_date,team_member,status):
        collection = self.db.collection('Tasks')
        coll = collection.get()
        s_date =  start_date.split('/')
        e_date =  end_date.split('/')
        # print(coll)
        addTask = {}
        addTask['Id'] = 'Tid'+str(len(coll)+1)
        addTask['priority'] = priority
        addTask['start_date'] = datetime.datetime(int(s_date[2]), int(s_date[1]), int(s_date[0]))
        # addTask['start_date'] = date(int(s_date[2]), int(s_date[1]), int(s_date[0]))
        addTask['end_date'] = datetime.datetime(int(e_date[2]), int(e_date[1]), int(e_date[0]))       
        # addTask['end_date'] = date(int(e_date[2]), int(e_date[1]), int(e_date[0]))
        addTask['team_member'] = team_member
        addTask['status'] = status
        
        msg = 'No Update'
        if( team_member in self.absentMemList ):
            msg = "Team member is not available."

        else:
            collection.document(task_name).set(addTask)
            msg = "Task created successfully"

        resp = {"success": True ,"msg":msg}
        return resp

    def taskUpdate(self,tid,fieldName,val):
        collection = self.db.collection('Tasks')
        docs = collection.stream()
        taskToUpdate={}
        taskName=''
        for doc in docs:
            tmpDoc = doc.to_dict()
            taskId = tmpDoc.get('Id')
            if(taskId==tid):
                taskToUpdate=doc.to_dict()
                taskName = doc.id
                break


        taskToUpdate[fieldName] = val
        msg = 'Task updated successfully'
        collection.document(taskName).set(taskToUpdate)
        resp = {"success": True ,"msg":msg}


        return resp

    def report(self, sdate):
        
        print('In Report')
        docs = self.db.collection(u'Tasks').stream()

        tasks = {}
        taskList=[]
        report = []
        s_date = sdate.split('/')
        
        sDate = date(int(s_date[2]), int(s_date[1]), int(s_date[0]))

        for doc in docs:
            tasks[doc.id] = doc.to_dict()
            # tmp={'Name':doc.id}
            tasks[doc.id].update({'Name':doc.id})
            taskList.append(tasks[doc.id])
            print(f'{doc.id} => {doc.to_dict()}')

        print(taskList)
        for task in taskList:
            s_d = task.get('start_date')
            s_d = s_d.date()
            if(sDate<=s_d):
                print('sDate',sDate)
                print('s_d',s_d)
                report.append(task)
        resp = {"success": True ,"data":report}

        return resp
        
    
       
