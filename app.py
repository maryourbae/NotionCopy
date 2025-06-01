from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from collections import deque

app = Flask(__name__)

milestones = deque()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("user").strip()
        name = request.form.get("name").strip()
        status = request.form.get("status")
        date = request.form.get("date")
        deadline = request.form.get("deadline") or None

        if user and name and date:
            milestone = {
                "user": user,
                "name": name,
                "status": status,
                "date": date,
                "deadline": deadline,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            milestones.append(milestone)
        return redirect("/")

    # Berikan enumerate ke context
    return render_template("index.html", milestones=list(milestones), history=list(milestones), enumerate=enumerate)

@app.route("/toggle_status/<int:idx>")
def toggle_status(idx):
    if 0 < idx <= len(milestones):
        milestone = milestones[idx - 1]
        if milestone["status"] == "pending":
            milestone["status"] = "in_progress"
        elif milestone["status"] == "in_progress":
            milestone["status"] = "done"
        else:
            milestone["status"] = "pending"
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
