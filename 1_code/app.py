"""
Youth Safety Signal : Midterm Demo (INFO-C450 Systems Design)
Author: Krissy Brown
Semester: Fall 2025

Description:
    Flask prototype simulating the main functionality flow:
    - Submit a safety signal
    - Moderator review & approval
    - Dashboard display of approved signals
"""

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

# ------------------------------
# Mock Data (in-memory only)
# ------------------------------
mock_signals = [
    {
        "id": 1,
        "title": "Suspicious Instagram Account",
        "platform": "Instagram",
        "risk_level": "High",
        "status": "Approved",
    },
    {
        "id": 2,
        "title": "Fake Scholarship Emails Circulating",
        "platform": "Email",
        "risk_level": "Medium",
        "status": "Pending",
    },
    {
        "id": 3,
        "title": "Stranger Approaching Students at Bus Stop",
        "platform": "Community",
        "risk_level": "High",
        "status": "Approved",
    },
]


# ------------------------------
# Favicon Route (fixes tab icon warning)
# ------------------------------
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


# ------------------------------
# Routes
# ------------------------------
@app.route("/")
def dashboard():
    """Displays approved safety signals (mock)."""
    approved = [s for s in mock_signals if s["status"] == "Approved"]
    return render_template("dashboard.html", signals=approved)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    """Mock submission form for new safety signals."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        platform = request.form.get("platform", "Other")
        risk = request.form.get("risk_level", "Low")

        if title:
            new_signal = {
                "id": len(mock_signals) + 1,
                "title": title,
                "platform": platform,
                "risk_level": risk,
                "status": "Pending",
            }
            mock_signals.append(new_signal)
        return redirect(url_for("moderation"))

    return render_template("submit.html")


@app.route("/moderation", methods=["GET", "POST"])
def moderation():
    """Moderator queue to approve or reject safety signals (mock)."""
    if request.method == "POST":
        signal_id = int(request.form["signal_id"])
        action = request.form["action"]  # 'approve' or 'reject'
        for s in mock_signals:
            if s["id"] == signal_id:
                s["status"] = "Approved" if action == "approve" else "Rejected"
                break
        return redirect(url_for("moderation"))

    pending = [s for s in mock_signals if s["status"] == "Pending"]
    return render_template("moderation.html", signals=pending)


# ------------------------------
# Run the App
# ------------------------------
if __name__ == "__main__":
    # Run from the 1_code directory:
    #   (.venv) PS ...\1_code> python app.py
    app.run(debug=True)
