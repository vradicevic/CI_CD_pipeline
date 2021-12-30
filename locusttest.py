from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def index(self):
        self.client.get('/')

    @task
    def post_predict_house_price(self):
        self.client.post("/predict",json={
        "CHAS":{
            "0":0
        },
        "RM":{
            "0":5.676
        },
        "TAX":{
            "0":285.0
        },
        "PTRATIO":{
            "0":14.2
        },
        "B":{
            "0":400.5
        },
        "LSTAT":{
            "0":4.95
        }
        })