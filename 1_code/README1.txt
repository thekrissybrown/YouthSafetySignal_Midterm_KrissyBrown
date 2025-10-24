# Application Code – Youth Safety Signal Midterm (Week 8)

Author: Krissy Brown  
Course: INFO-C450 Systems Design  
Semester: Fall 2025


## Purpose
This folder contains the **Flask-based prototype** developed for the Week 8 midterm demo.  
The current version demonstrates the core functionality flow of the Youth Safety Signal platform, using mock data and placeholder templates to simulate the user experience.


## Current Features
✅ Flask application structure established (`app.py`, routes, templates)  
✅ Mock data rendering on dashboard and moderation pages  
✅ Functional HTML form submission (non-persistent)  
✅ Static folder organization for CSS and images  
🕓 Database integration and user authentication planned for final release  


## File Overview
```

1_code/
│
├── app.py                # Flask entry point with mock routes
├── templates/
│   ├── base.html         # Layout template with navbar/footer
│   ├── dashboard.html    # Displays approved community signals
│   ├── submit.html       # Form for submitting new safety signals
│   └── moderation.html   # Mock review panel for moderator use
├── static/
│   ├── css/              # Basic styling (Bootstrap 5)
│   └── img/              # Placeholder icons or screenshots
└── README1.txt           # (This file)

````


## How to Run the Demo
### Requirements
- Python 3.12+
- Flask 3.0+
- (Optional) Virtual environment

### Setup Commands
```bash
# 1️⃣ Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2️⃣ Install Flask
pip install flask

# 3️⃣ Run the demo
flask run
````

Visit **[http://localhost:5000](http://localhost:5000)** in your browser.

## Next Steps (Post-Midterm)

* Connect app to MySQL via SQLAlchemy ORM
* Add user authentication and moderator roles
* Implement data persistence for safety signals
* Integrate glossary and risk-level filters
* Conduct usability testing and collect feedback

---

*Placeholder file for midterm submission.
This folder represents the working Flask prototype demonstrated in the Week 8 video presentation.*

