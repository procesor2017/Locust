from locust import TaskSet, task, tag, between
from lxml import html

class Wp_admin(TaskSet):
    wait_time = between(0.5, 15)

    def login(self):
        self.client.post("/wp-login.php", {"user_login":"tesena", "user_pass":"tesena"})

    def logout(self):
        self.client.post("/wp-login.php?action=logout", {"user_login":"tesena", "user_pass":"tesena"})


    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    @task
    def index(self):
        self.client.get("/wp-admin/profile.php") 

    @task
    def check_wp_admin(self):
        with self.client.get("/", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("Request has time: " + response.elapsed)
            elif response.status_code != 200:
                response.failure("Repsonse code is: " + response.status_code)
            elif response.headers['Connection'] != 'keep-alive':
                response.failure("Unexpected connection header: " + response.headers['Connection'])
    
