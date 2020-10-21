# Examples in Locust
There is small repository for [Locust](https://locust.io/). This small library contains docker-compose with wordpress and locusts tests which connect on docker and test webpage from wordpress

## Folder structure
```
Locust
└── common                      # folder with auth.py config.py etc.
└── locustfiles                 # Locust test file 
│    └── __init__.py            # File for export class to locustfile more in python documentation
│    └── locustfile.py          # File for start tests
│    └── restapi.py             # File for calling rest api, doesnt use locust.conf
│    └── webpage.py             # Tests for webpage
│    └── wp_admin.py            # Test for wp-admin page
└── wp                          # Folder with docker file
│    └── docker-compose.yml     # Docker compose which starts wordpress on your computer
└── locust.conf                 # File with config for locust
```

## Installation
### Docker and wordpress
 - Go to folder with ```cd <path_to_root_repository>/wp```
 - Use these two commands, first command is starts wordpress second for mocking api
 ```
 docker-compose up -d
 docker run -d -p 8080:8080 castlemock/castlemock
 ```
 - After that you can setUp your wordpress on link http://localhost:8000 (Every usefull link you find below)
 - Then set up castlemock (If you want try api rest call)

### Link
 - http://localhost:8000/?rest_route=/ - Api wordpressu
 - http://localhost:8000 - Adress where Wordpress running
 - http://localhost:8089/ - Adress where you find locust
 - http://localhost:8080/castlemock - adress for castle mock


## Some calling from CMD
Go to repository folder:
```cd <path to folder>```

If u dont wanna use locust.conf :
```locust -f <path to file>```

You need change in code Taskset to HttpUsers or add to code new class for webpage and wp_admin. Restapi working solo

```
class AwesomeUser(HttpLocust):
   task_set = BrowseDocumentation
   host = "http://blazedemo.com"
   min_wait = 1 * 1000
   max_wait = 5 * 1000

```

Call if you wanna use locust.conf

```locust```

Call without GUI
```locust -f <path_to_file> --no-web -c 50 -r 10```


## Locust Terminology
Locust has a little different terminology than normaly library has, so there is some names command:

**Tasktu** = In Locust, a Task is the smallest unit of a test suite. Usually, it means, any function or method that is decorated with the @task decorator.

**TaskSet** = A TaskSet is a class that establishes a contextual boundary between different groups of Tasks. You can essentially group multiple similar Tasks inside a TaskSet. Then you use the TaskSets from your User class.

**User** = In Locust, a User is a class that executes the tests either by directly calling the Task methods or via using TaskSets.
