#!/usr/bin/python3
"""Gathering data from API jsonplaceholder"""
import json
import requests


def dictionary_of_list_of_dictionary():
    dictionary = {}
    for employee_id in range(1, 11):
        url = 'https://jsonplaceholder.typicode.com/'
        employee_id_url = f'{url}/users/{employee_id}'
        todo_url = f'{url}/users/{employee_id}/todos'

        user_data = requests.get(employee_id_url).json()
        todo_data = requests.get(todo_url).json()

        name = user_data.get('username')
        all_tasks = {task['title']: task['completed'] for task in todo_data}

        json_data = {
            employee_id: list({
                'username': name,
                'task': task,
                'completed': done_tasks,
            }
                for task, done_tasks in all_tasks.items()
            )}
        dictionary.update(json_data)
        with open(f"todo_all_employees.json", mode='w') as jsonfile:
            json.dump(dictionary, jsonfile)


if __name__ == '__main__':
    dictionary_of_list_of_dictionary()
