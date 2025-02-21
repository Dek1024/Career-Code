This is the UI plan for the webapp.
Window 1: 
    Buttons in window 1 - create tasks, inprogress tasks, completed tasks. 
Window 2: 
    Creating tasks button opens create tasks window.
    
    Form in create tasks window with the given options - title, description, start date, start time, end date, end time & create task, creating task opens window 1.
Window 3: 
    After clicking inprogress tasks, Shows all the tasks as cards, there are buttons (filters) for past, today & future tasks, default window will be today's tasks. 

    There will be next page button to see all the tasks not visible in current window. 

    There a task card can be clicked and complete button will appear. Complete button once clicked will send the task to completed tasks window.

    Important Note: Complete task button once clicked with create a throwing in the dustbin sound or a victory sound.

    This will also have a delete task button to delete a task.
Window 4:
    This window contains all the completed tasks.

    This window will have a send-to-inprogress button incase of emergencies.

Database 
The database will be a simple SQL table containing the following columns: id: primary key, title, description, start date, start time, end date, end time, status (yes,no) 

The above link is a starting point to build the app within Sunday
https://www.quora.com/Where-do-I-start-learning-how-to-make-a-simple-web-app 

It has been decided that streamlit.io will be used to build the web-app considering my skill requirements.
