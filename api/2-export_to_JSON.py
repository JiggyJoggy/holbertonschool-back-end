#!/usr/bin/python3
"""Gathering data from API jsonplaceholder"""
import json
import requests
from sys import argv


def export_to_csv(employee_id):
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id_url = f'{url}/users/{employee_id}'
    todo_url = f'{url}/users/{employee_id}/todos'

    user_data = requests.get(employee_id_url).json()
    todo_data = requests.get(todo_url).json()

    name = user_data.get('username')
    all_tasks = {task['title']: task['completed'] for task in todo_data}

    json_data = {
        employee_id: list({
            'task': task,
            'completed': done_tasks,
            'username': name
        }
            for task, done_tasks in all_tasks.items()
        )}
    
    with open(f"{employee_id}.json", mode='w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == '__main__':
    employee_id = int(argv[1])
    export_to_csv(employee_id)
