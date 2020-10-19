from locust import TaskSet, task, between

class IndexPage(TaskSet):
    wait_time = between(0.5, 15)

    def on_start(self):
        # Start when Locust call any task in scheduled
        with self.client.get("/", catch_response = True) as response:
            if response.elapsed.total_seconds() > 0.9:
                response.failure("Request took too long")
            if response.text != "Succes":
                response.failure('Cant connect')

    @task
    def index(self):
        self.client.get("/")
    
    @task
    def loopForArticles(self):
        for i in range(3):
            self.client.get("/?p={0}".format(i))
    
    @task
    def logInToAdmin(self):
        response = self.client.post("/wp-login.php", {"user_login":"tesena", "password":"tesena"})
        if response.status_code != 400:
            response.failure('Repsonse code is:', response.status_code)