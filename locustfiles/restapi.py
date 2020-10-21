import json
from locust import HttpUser, TaskSet, task, between, tag

''' 
These code works for some api rest services.

For your hapoinest a I use  castlemock / castlemock in docker

'''


class UserCallingApi(HttpUser):
    wait_time = between(0.5, 15)


    @task(1)    
    def create_post(self):
        post_adress = "/post" # chang for new adress
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        jsondata = json.dumps({"title": "foo" })
        with self.client.post(post_adress ,data= jsondata, headers=headers) as postal:
            if postal.status_code != 200:
                postal.failure('Post has status_cod :' + postal.status_code)
            elif postal.elapsed.total_seconds() > 1:
                postal.failure('Post has elapsed time :' + postal.elapsed)

    @task(2)
    def create_get(self):
        with self.client.get("/ha", catch_response=True) as response:
            res = response.json()
            if response.elapsed.total_seconds() > 1:
                response.failure("Request has time: " + response.elapsed)
            elif response.status_code != 200:
                response.failure("Repsonse code is: " + response.status_code)
            elif res['author'] != "Jan Egermaier":
                response.failure('Response is : ' + str(res))