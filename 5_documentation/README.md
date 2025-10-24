# 🧠 Youth Safety Signal – Midterm Demo (INFO-C450 Systems Design)

A Flask-based community alert prototype enabling parents and guardians to share and verify youth safety signals through a trusted moderation workflow.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow.svg)
![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)

---

## 👩‍💻 Author
**Krissy Brown**  
B.S./M.S. Informatics (Human-Computer Interaction) – IU Luddy School  
**Course:** INFO-C450 Systems Design  
**Instructor:** Jafrina Jabin  
**Semester:** Fall 2025  
**Status:** Week 8 Midterm Submission – Demo & Documentation  

---

## 🧭 Overview
**Youth Safety Signal** addresses the need for a **centralized, parent-friendly system** to report and validate potential youth safety threats—online or in the community.  

This midterm submission demonstrates **system design progress** through a functional mock Flask prototype.  
The demo highlights the core user flow:
- Parents submit a **safety signal**  
- Moderators review and **approve or reject**  
- Approved signals appear in the **community dashboard feed**

Database integration and advanced features (authentication, glossary, digest emails) are scheduled for completion by the **final December 2025** milestone.

---

## 🎯 Midterm Objectives
- ✅ Establish Flask environment and project structure  
- ✅ Demonstrate functional mock data routes (Submit → Moderate → Feed)  
- ✅ Present updated documentation and diagrams  
- 🕓 Prepare for database migration (SQLite → MySQL)  
- 🕓 Define roadmap for next sprint toward final deliverable  

---

## 🧩 Folder Structure
```text
YouthSafetySignal_Midterm_KrissyBrown/
│
├── 1_code/
│   ├── app.py                 # Flask prototype with mock data
│   ├── templates/             # HTML UI (dashboard, submit, moderation)
│   ├── static/                # CSS + image assets
│   └── README1.txt            # Run instructions
│
├── 2_unit_testing/
│   └── README2.txt            # Placeholder
│
├── 3_integration_testing/
│   └── README3.txt            # Placeholder
│
├── 4_data_collection/
│   └── README4.txt            # Placeholder
│
├── 5_documentation/
│   ├── System_requirements_documentation.pdf
│   ├── Brochure.pdf
│   └── Presentation_slides.pdf
│
└── explanation.pdf            # Explanation of placeholder folders
````

---

## ⚙️ Running the Demo

### Requirements

* Python 3.12+
* Flask 3.0+
* (Optional) Virtual environment

### Setup

```bash
# 1️⃣ Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2️⃣ Install dependencies
pip install flask sqlalchemy flask-login email-validator

# 3️⃣ Run the demo
flask run
```

Visit [http://localhost:5000](http://localhost:5000) to open the mock prototype.

---

## 🎥 Demo Video

🎬 **[View Midterm Demo (Kaltura)](https://placeholder.link)**  
*(Link will be updated after video upload.)*

This 6-minute video walks through:

1. Dashboard overview
2. Signal submission process
3. Moderator review queue
4. Feed update after approval
5. Project roadmap and next steps

---

## 📄 Documentation

Located in the `/5_documentation/` folder:

* **System_requirements_documentation.pdf** → Combined Modules 1–4 + updates
* **Brochure.pdf** → Two-page marketing flyer with demo link
* **Presentation_slides.pdf** → 5-slide overview used in demo video

---

## 🔮 Next Steps (Post-Midterm)

| Milestone | Task                                         | Target        |
| --------- | -------------------------------------------- | ------------- |
| Phase 2   | Integrate MySQL database + SQLAlchemy models | Nov 2025      |
| Phase 3   | Add authentication & moderation roles        | Late Nov 2025 |
| Phase 4   | UI enhancements + Glossary system            | Dec 2025      |
| Final     | Weekly digest + live presentation            | Dec 2025      |

---

## 🧠 Reflection

This demo marks a functional midpoint in the development cycle.
Although database connectivity and automated features remain ahead, the prototype successfully models:

* Core information flow (Submit → Review → Display)
* Scalable folder and code architecture
* Consistent UX direction guided by ethical and accessible design principles

---

## 📜 License

Educational use only © 2025 **Krissy Brown**
All rights reserved.
Redistribution or modification prohibited without instructor permission.

---

## 🩵 Acknowledgment

Developed as part of **Indiana University – Luddy School of Informatics, Computing & Engineering (Indianapolis)**
for **INFO-C450: Systems Design**.

> *“Building safety for families begins with awareness, trust, and thoughtful design.”*
> — Krissy Brown
