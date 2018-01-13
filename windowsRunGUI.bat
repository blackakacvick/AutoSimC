@echo off
uwsgi --http 127.0.0.1:3031 --wsgi-file gui/REST.py --callable app
timeout 5
start http://localhost:3031/