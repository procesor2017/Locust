import re
import datetime
from locust import TaskSet, task, between, tag


class IndexPage(TaskSet):
    wait_time = between(0.5, 15)

    def on_start(self):
        # Start when Locust call any task in scheduled
        with self.client.get("/", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("Request took too long")
            if response.text != "Succes":
                response.failure('Not succes')

    @task
    def index(self):
        self.client.get("/")
    
    @task
    def loop_for_articles(self):
        for i in range(3):
            self.client.get("/?p={0}".format(i))

    @task
    def home_page_title(self):
        home_page_title = re.compile('Ahoj všichni!') # Change for your language mutation
        response = self.client.get('/')
        assert home_page_title.search(response.text) is not None, "Expected title has not been found!"

    @task
    def asssert_with_response_code(self):
        response = self.client.get('/')
        assert response.status_code is 200, "Unexpected response code: " + response.status_code

    @task
    def assert_for_headers(self):
        with self.client.get('/', catch_response=True) as response:
            assert response.headers['Connection'] == 'keep-alive', "Unexpected connection header: " + response.headers['Connection']

    @task 
    def response_time_arcticles_1(self):
        with self.client.get("/?p=1", catch_response=True) as response:
            assert response.elapsed < datetime.timedelta(seconds = 1), response.failure("Request took more than 1 second, true time was:" + response.elapsed)
