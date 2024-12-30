from celery import Celery

app = Celery('messaging',
             broker='pyamqp://guest:guest@localhost:5672//',
             backend='rpc://',
             include=['messaging.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
