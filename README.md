<div align="center">

# 🛡️ Youth Safety Signal
### *INFO-C450: Systems Design · Midterm Project*  
**Author:** Krissy Brown  
**Indiana University · Luddy School of Informatics, Computing, and Engineering**  
**Semester:** Fall 2025  

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![VS Code](https://img.shields.io/badge/Built%20With-VS%20Code-007ACC?logo=visualstudiocode)](https://code.visualstudio.com/)
[![GitHub](https://img.shields.io/badge/Version%20Control-GitHub-black?logo=github)](https://github.com/thekrissybrown)

</div>

---

# 🛡️ Youth Safety Signal  
**INFO-C450: Systems Design – Midterm Project**  
**Author:** Krissy Brown · Indiana University – Luddy School of Informatics, Computing, and Engineering  
**Semester:** Fall 2025  

---

## 🎯 Project Overview
Youth Safety Signal is a lightweight **Flask web prototype** designed to simulate a community-driven alert system that helps identify and share **youth safety risks** online or within local environments.

This midterm demonstration shows the **core system flow** from report submission to moderation and approval—illustrating how a safety signal might move through the system before being visible on the public dashboard.

---

## 🧩 Features
- **Submit a Safety Signal** – users can quickly report suspicious or unsafe online activity.  
- **Moderate Reports** – mock moderation queue allows approving or rejecting signals.  
- **View Dashboard** – displays approved safety signals with platform and risk level details.  
- **Demo Mode** – uses mock, in-memory data only (no database connection required).  
- **Responsive UI** – clean and minimal design with IU-inspired crimson and white theme.  

---

## 🖥️ Technology Stack
| Layer | Tool |
|-------|------|
| **Frontend** | HTML5, CSS3 (static templates) |
| **Backend** | Python 3.14 + Flask |
| **Environment** | Virtual Environment (`.venv`) |
| **IDE** | Visual Studio Code |
| **Version Control** | Git + GitHub |

---

## ⚙️ Installation & Run Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/thekrissybrown/YouthSafetySignal_Midterm_KrissyBrown.git
cd YouthSafetySignal_Midterm_KrissyBrown
````

### 2️⃣ Activate Virtual Environment

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
cd 1_code
pip install -r requirements.txt
```

### 4️⃣ Run the App (Two Easy Options)

#### 🟢 Option 1 — Run Directly in VS Code

* Ensure your virtual environment (`.venv`) is active (bottom-right shows **Python: .venv**).
* Press **F5** or click ▶️ **Run and Debug**.
* When prompted, choose **“Flask (midterm app.py)”**.
* The app will launch automatically inside VS Code’s terminal window.

#### 🧠 Option 2 — Run from Terminal

```bash
python app.py
```

Then visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 System Flow (Demo)

```
Submit  →  Review (Moderation)  →  Approve/Reject  →  Display on Dashboard
```

All data is stored in memory and resets when the app restarts for demo concept validation, Pending database approval from instructor.

---

## 📂 Project Structure

```
YouthSafetySignal_Midterm_KrissyBrown/
├── .venv/                     # Virtual environment (ignored by Git)
├── .vscode/                   # Editor configuration
├── 1_code/
│   ├── app.py                 # Flask main app
│   ├── static/                # CSS, favicon, etc.
│   └── templates/             # HTML templates
├── 2_unit_testing/            # Placeholder for future testing
├── 3_integration_testing/
├── 4_data_collection/
├── 5_documentation/
└── requirements.txt           # Project dependencies
```

---

## 💡 Notes

* This project is a **prototype**, not a production system.
* It demonstrates **user flow design, system architecture, and data handling concepts**.
* All content is mock data for demonstration purposes only.

---

## 🧑‍💻 Credits

Created by **Krissy Brown**
📍 Indiana University · Luddy School of Informatics, Computing, and Engineering
🔗 [LinkedIn](https://www.linkedin.com/in/thekrissybrown) · [GitHub](https://github.com/thekrissybrown)

---

## 🏁 License


This project is licensed for **academic demonstration use**.
All rights reserved © 2025 Krissy Brown.


