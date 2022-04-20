from firebase_connect import Task_Tracker
from flask import Flask,request

app = Flask(__name__)
tt = Task_Tracker()


@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/team', methods=['POST'])
def team():
    teamName = request.args.get('TeamName')
    membersStr = request.args.get('members')
    membersStr = membersStr.removeprefix('[').removesuffix(']')
    members = membersStr.split(",")
    print(teamName,members)
    # print(type(members))
    mem = {}
    for i in range(0,len(members)):
        key = 'Mem'+str(i+1)
        mem[key]=members[i]
    return tt.team(teamName,mem)

@app.route('/availability',  methods=['POST'])
def availability():
    teamName = request.args.get('TeamName')

    return tt.availability(teamName)


@app.route('/task', methods=['POST'])
def task():

    task_name = request.args.get('TaskName')
    priority = request.args.get('Priority')
    start_date = request.args.get('StartDate')
    end_date = request.args.get('EndDate')
    team_member = request.args.get('Member')
    status = request.args.get('Status')
    return tt.task(task_name, priority, start_date, end_date,team_member,status)


@app.route('/taskUpdate', methods=['POST'])
def taskUpdate():
    taskId = request.args.get('TaskId')
    fname = request.args.get('FieldName')
    val = request.args.get('Value')

    if(fname=='status'):
        return tt.taskUpdate(taskId,fname,val)
    if(fname=='priority'):
        return tt.taskUpdate(taskId,fname,val)
    if(fname=='start_date'):
        return tt.taskUpdate(taskId,fname,val)
    if(fname=='end_date'):
        return tt.taskUpdate(taskId,fname,val)
    if(fname=='team_member'):
        return tt.taskUpdate(taskId,fname,val)

    return {'success': False,'msg':'Incorrect parameters'}


@app.route('/report', methods=['GET'])
def report():
    startDate = request.args.get('StartDate')
    return tt.report(startDate)

if __name__ == '__main__':
   app.run(debug = True)