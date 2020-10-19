from locust import HttpUser

from locustfiles.webpage import IndexPage


class PrimaryUser(HttpUser):
    tasks = [IndexPage]
