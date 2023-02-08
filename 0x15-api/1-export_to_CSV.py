#!/usr/bin/python3
""" a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    import csv

    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    emp_id = argv[1]
    row = []
    EMPLOYEE_NAME = None
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = ""
    start_url = "https://jsonplaceholder.typicode.com/users"
    req_user_details = f"{start_url}/{emp_id}"
    req_user_todos = f"{start_url}/{emp_id}/todos"
    user_details = requests.get(req_user_details)
    user_todos = requests.get(req_user_todos)
    if user_details.status_code == 200:
        details = user_details.json()
        todos = user_todos.json()
        username = (details.get("username"))
        for i in todos:
            obj = {}
            obj["USER_ID"] = i["userId"]
            obj["USERNAME"] = username
            obj["TASK_COMPLETED_STATUS"] = i["completed"]
            obj["TASK_TITLE"] = i["title"]
            row.append(obj)

        with open(f'{emp_id}.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            # writer.writeheader()
            writer.writerows(row)
    else:
        print('None')
