import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from flask import Flask, render_template, request
from database.db import init, add_target, get_targets, update_status, save_result
from core.runner import run_scan
from ai.summary import AISummery
import threading
from flask import jsonify

app = Flask(__name__)
init()

@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        target = request.form["target"]
        add_target(target)

    targets = get_targets()
    return render_template("dashboard.html", targets=target)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/scan/<int:target_id>")
def scan_target(target_id):

    targets = get_targets()
    target = [t for t in targets if t[0] == target_id][0]

    def background_scan():
        update_status(target_id, "scanning")

        result = run_scan(target[1])

        summary = AISummery.summarize(result)

        final_output = f"{result}\n\n[AI SUMMARY]\n{summary}"

        save_result(target_id, final_output)

    threading.Thread(target=background_scan).start()

    return "Scan started"

@app.route("/api/targets")
def api_targets():
    return jsonify(get_targets())