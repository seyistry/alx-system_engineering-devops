#!/usr/bin/python3
""" a Python script that, using this REST API"""

if __name__ == "__main__":
    import requests
    import json

    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    row = []
    json_dict = {}
    EMPLOYEE_NAME = None
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = ""
    start_url = "https://jsonplaceholder.typicode.com/users"
    user_details = requests.get(start_url)
    if user_details.status_code == 200:
        users = user_details.json()
        for user in users:
            req_user_todos = requests.get(f"{start_url}/{user['id']}/todos")
            todos = req_user_todos.json()
            for i in todos:
                obj = {}
                obj["task"] = i["title"]
                obj["completed"] = i["completed"]
                obj["username"] = user['username']
                row.append(obj)
            json_dict[f"{user['id']}"] = row
            row = []
        json_object = json.dumps(json_dict)
        with open('todo_all_employees.json', 'w',
                  encoding='UTF8', newline='') as f:
            f.write(json_object)
