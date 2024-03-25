#!/usr/bin/python3
"""a Python script that returns information about their TODO list progress."""
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
"""The API's URL."""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todo_list = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todo_list))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
