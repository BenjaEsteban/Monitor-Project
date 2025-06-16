from flask import Flask, render_template
from livereload import Server
from monitor.manager import MonitorManager

monitor = MonitorManager()
app = Flask(__name__)

@app.route("/")
def index():
    status = monitor.check_all()
    return render_template("index.html", status=status)

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('templates/')
    server.watch('monitor/*.py')
    server.serve(host='0.0.0.0', port=5001, debug=True)
