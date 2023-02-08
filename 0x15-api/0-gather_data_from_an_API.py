#!/usr/bin/python3
""" a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    emp_id = argv[1]
    EMPLOYEE_NAME = None
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = ""
    start_url = "https://jsonplaceholder.typicode.com/users"
    req_user_details = "{}/{}".format(start_url, emp_id)
    req_user_todos = "{}/{}/todos".format(start_url, emp_id)
    user_details = requests.get(req_user_details)
    user_todos = requests.get(req_user_todos)
    if user_details.status_code == 200:
        details = user_details.json()
        todos = user_todos.json()
        EMPLOYEE_NAME = (details.get("name"))
        for i in todos:
            if i.get("completed") is True:
                if NUMBER_OF_DONE_TASKS == 0:
                    TASK_TITLE = TASK_TITLE + ("\t {}".format(i.get("title")))
                else:
                    TASK_TITLE = TASK_TITLE + ("\n\t {}".format(i.get("title")))
                NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
        TOTAL_NUMBER_OF_TASKS = len(todos)
        print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
              NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        print(TASK_TITLE)
    else:
        print('None')
