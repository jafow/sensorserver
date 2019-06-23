# sensorserver
service for collecting and storing sensor data

## install
```bash
git clone https://github.com/jafow/sensorserver.git
```
### dependencies
(optional but recommended)
create a virtual env

```bash
python3 -m venv env
source env/bin/activate
```

```bash
pip3 install -r requirements.txt
```

## start the app
```bash
$ python3 startup.py
INFO:sensorserver:instance folder already exists; moving on
INFO:sensorserver:starting sensor server! 🙌 🚀
 * Serving Flask app "sensorserver" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
INFO:werkzeug: * Restarting with stat
INFO:sensorserver:instance folder already exists; moving on
INFO:sensorserver:starting sensor server! 🙌 🚀
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 278-316-477
```

in a browser go to localhost:5000/temperature

# license
Apache 2.0
