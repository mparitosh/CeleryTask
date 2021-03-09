from celery.task import task
from django.conf import settings
import requests
import random

@task(bind=True, max_retries=3)
def fetch_conversion(self):
    # 3rd party api having irregular response or intermittent failures 
    # here for example currency conversion rates are fetched by using fixer api
    try:
        endpoint = 'latest'
        access_key = settings.CURRENCY_API_KEY
        base_currency = "$"
        url = 'http://data.fixer.io/api/' + endpoint + '?access_key=' + access_key + '&base=' + base_currency
        response = requests.post(url=url)
        response_json = response.json()
        currency = response_json["rates"]
    except Exception as exc:
        self.retry(exc=exc, countdown=int(random.uniform(2, 4) ** self.request.retries))