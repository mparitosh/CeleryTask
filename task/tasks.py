from celery.task import task
import random

@task(bind=True, max_retries=3)
def update_status(self):
    try:
        # 3rd party api having irregular response or intermittent failures 
    except Error as exc:
        self.retry(exc=exc, countdown=int(random.uniform(2, 4) ** self.request.retries))