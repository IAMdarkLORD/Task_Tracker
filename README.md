# Task_Tracker
In the Task tracker application, there are 2 types of users, team leader/manager, and team member. Team leaders can assign a task to a team member depending upon the team member's availability. One task can have one or more team members working on it. A task contains all the information related to the task such as task id, task name, priority, team leader, team member, start and end date, and status. Team leaders can update all the task fields but team members can only update the status of the task assigned to them. Status can be Assigned, In progress, under review, done. If an assigned team member misses the deadline of the task both team member and team leader will receive an email notifying missed deadline. At the end of each day, the team leader will get an email with a report on all the changes in statuses on that day.
# Requirements
1.Install Python Flask -  pip install -U Flask
2.Install Firestore - pip install google-cloud-firestore

# How to use the Application
1. Run TaskApis.py
2. There are 5 Apis we can use postman to call these APi's
3. Api's are 
4.  1./team - To create new Team
5.  2./availability - To check availability of the Team Members in a Team
6.  3./task - To create new task and assign it to the Team Member
7.  4./taskUpdate - To Update Task fields.
8.  5./report - To Get the status report's of the task's from a given a start date

# Detailed Api Usage
1. Create a team
a. Endpoint - POST /team
b. Authentication - only for team leaders
c. Data- team_name, list of user_ids of members
d. Responses -
i. Unauthorized /failed to authenticate
{“success”: False,” msg”:” Failed to
authenticate”}
ii. On success
{“success”: True,” msg”:” Team created
successfully”}

2. Get availability of team members
a. Endpoint - GET /availability
b. Authentication- only for team leaders
c. Parameters- team_id(req.)
d. Responses -
i. JSON with all team members with their
availability status e.g.{“success”:True,
“data”:[{“member1”:True},{“member2”:False}]}
ii. Unauthorized/failed to authenticate
{“success”: False,” msg”:” Authentication
failed”}

3. Create task
a. Endpoint - POST /task
b. Authentication- only for team leaders
c. Data- task_name, priority, start date, end date,
team member,status=assigned
d. Responses -
i. if a team member is not available.-
{“success”: False ,” msg”:” team member is
not available”}
ii. If the user is not a team leader
{“success”: False, “msg”:” Forbidden”}
iii. Incorrect parameters
{“success”: False,” msg”:” Incorrect
parameters”}
iv. Unauthorized/failed to authenticate
{“success”: False,”msg”:”Authentication
failed”}
v. On success
{“success”: True,”msg”:”Task created
successfully”}

4. Update task
a. Endpoint - PATCH /task
b. Authentication- Team leader -all fields Team
member - status field
c. Parameters - task_id & updated field
d. Responses -
i. If a team member tries to update field other
than status
{“success”: False,”msg”:”Forbidden”}
ii. Incorrect parameters
{“success”: False,”msg”:”Incorrect
parameters”}
iii. Unauthorized/ failed authentication
{“success”: False,”msg”:”authentication
failed”}
iv. On success
{“success”: True,”msg”:”Task updated
successfully”}

5. Get status change report
a. Endpoint - GET /report
b. Authentication- Team leaders only
c. Parameter - date
d. Responses -
i. Unauthorized/failed authentication
{“success”: False,”msg”:”Authentication
failed”}
ii. On success {“success”:
True,”data”:[{“name”:task_name , “team
member”:team_member , “status”:
task_status},....]}
