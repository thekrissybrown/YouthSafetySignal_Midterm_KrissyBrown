"""
Youth Safety Signal – Midterm Demo (INFO-C450 Systems Design)
Author: Krissy Brown
Semester: Fall 2025
Description:
    Flask prototype simulating the main functionality flow:
    - Submit a safety signal
    - Moderator review & approval
    - Dashboard display of approved signals
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ------------------------------
# Mock Data
# ------------------------------
mock_signals = [
    {"id": 1, "title": "Suspicious Instagram Account", "platform": "Instagram", "risk_level": "High", "status": "Approved"},
    {"id": 2, "title": "Fake Scholarship Emails Circulating", "platform": "Email", "risk_level": "Medium", "status": "Pending"},
    {"id": 3, "title": "Stranger Approaching Students at Bus Stop", "platform": "Community", "risk_level": "High", "status": "Approved"},
]

# ------------------------------
# Routes
# ------------------------------

@app.route("/")
def dashboard():
    """Displays approved safety signals."""
    approved_signals = [s for s in mock_signals if s["status"] == "Approved"]
    return render_template("dashboard.html", signals=approved_signals)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    """Mock submission form for new safety signals."""
    if request.method == "POST":
        title = request.form["title"]
        platform = request.form["platform"]
        risk = request.form["risk_level"]
        new_signal = {"id": len(mock_signals) + 1, "title": title, "platform": platform, "risk_level": risk, "status": "Pending"}
        mock_signals.append(new_signal)
        return redirect(url_for("moderation"))
    return render_template("submit.html")


@app.route("/moderation", methods=["GET", "POST"])
def moderation():
    """Moderator queue to approve or reject safety signals."""
    if request.method == "POST":
        signal_id = int(request.form["signal_id"])
        action = request.form["action"]

        for signal in mock_signals:
            if signal["id"] == signal_id:
                signal["status"] = "Approved" if action == "approve" else "Rejected"
        return redirect(url_for("moderation"))

    pending_signals = [s for s in mock_signals if s["status"] == "Pending"]
    return render_template("moderation.html", signals=pending_signals)


# ------------------------------
# Run App
# ------------------------------

if __name__ == "__main__":
    app.run(debug=True)
