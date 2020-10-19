from locust import HttpUser, task, between

class IndexPage(HttpUser):
    wait_time = between(0.5, 15)

    def on_start(self):
        # Start when Locust call any task in scheduled
        with self.client.get("/", catch_response = True) as response:
            if response.elapsed.total_seconds() > 0.9:
                response.failure("Request took too long")

    @task
    def index(self):
        self.client.get("/")
    
    @task
    def loopForArticles(self):
        for i in range(3):
            self.client.get("/?p={0}".format(i))
    
