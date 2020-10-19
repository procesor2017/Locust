from locust import HttpUser, task, tag, between

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}

class wpAdmin(HttpUser):
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
    
