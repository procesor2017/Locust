from locust import HttpUser

from locustfiles.webpage import IndexPage
from locustfiles.wp_admin import  Wp_admin


class PrimaryUser(HttpUser):
    tasks = [IndexPage, Wp_admin]
