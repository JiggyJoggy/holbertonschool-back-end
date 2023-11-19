#!/usr/bin/python3
"""Gathering data from API jsonplaceholder"""
import requests
from sys import argv


def gather_data_api(employee_id):
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id_url = f'{url}/users/{employee_id}'
    todo_url = f'{url}/users/{employee_id}/todos'

    user_data = requests.get(employee_id_url).json()
    todo_data = requests.get(todo_url).json()

    name = user_data.get('name')
    task_done = 0

    for task in todo_data:
        if task['completed']:
            task_done += 1

    print(f"Employee {name} is done with tasks({task_done}/{len(todo_data)}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == '__main__':
    employee_id = int(argv[1])
    gather_data_api(employee_id)
