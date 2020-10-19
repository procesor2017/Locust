## Link
 - http://localhost:8000/?rest_route=/ - api wordpressu
 - http://localhost:8000 - wordpress web

## Directory
wp - docker compsoe for wordpress running in docker

## Call from terminal
``` locust -f webpage.py --host=http://localhost:8080 ```

## Example code
```
import time
from locust import HttpUser, task, between

# Simulated user
class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task # This methods for every runing user create greenlet which call those methods.
    def index_page(self):
        self.client.get("/?p=5") # Self.client make it posible http call

    @task(3) # taks(3) The Quests is random but u can choose weight
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)
    
    # Metoda, která se zapne pro každéího uživatele
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
```

## Locust Terminology

Task: In Locust, a Task is the smallest unit of a test suite. Usually, it means, any function or method that is decorated with the @task decorator.

TaskSet: A TaskSet is a class that establishes a contextual boundary between different groups of Tasks. You can essentially group multiple similar Tasks inside a TaskSet. Then you use the TaskSets from your User class.

User: In Locust, a User is a class that executes the tests either by directly calling the Task methods or via using TaskSets.
