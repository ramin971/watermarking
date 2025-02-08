import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','watermarking.settings')


app = Celery('watermarking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('#####s####')
    print('Request:{0!r}'.format(self.request))
    print('#####e####')