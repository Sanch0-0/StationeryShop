🎯 Идеальный вариант:

    web-app (Django + Gunicorn)
    postgres (База данных)
    nginx (Reverse Proxy)
    redis (Брокер и кеш)
    celery-worker (Обработчик задач)
    celery-beat (Если есть периодические задачи)

Elasticsearch и Logstash на рассмотрение
не забыть про Flower


<!-- gunicorn.socket -->
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/app/gunicorn.sock

[Install]
WantedBy=sockets.target


<!-- gunicorn.service -->
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/app
ExecStart=/app/venv/bin/gunicorn --config /app/gunicorn.conf main.wsgi:application

[Install]
WantedBy=multi-user.target
