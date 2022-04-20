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

