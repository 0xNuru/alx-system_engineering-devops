#!/usr/bin/python3
"""a script that extends your Python script to export data in the CSV format"""
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
            user_name = user.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todo_list))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
