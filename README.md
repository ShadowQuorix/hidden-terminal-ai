#  Hidden Terminal — Red Team Learning Framework

Autonomous Offensive Security Framework designed for:

* OSCP-style learning and methodology
* CTF platforms like TryHackMe and Hack The Box
* Structured red team skill development
* Teaching real-world penetration testing workflows

---

##  Purpose

Hidden Terminal is built to bridge the gap between:

> Running tools ❌
> Understanding what you're doing ✅


Hidden Terminal is NOT designed to solve boxes for you.

It is built to:
- Guide your thinking
- Highlight attack surfaces
- Support manual enumeration

If you rely only on this tool, you will NOT improve.


This framework helps learners:

* Think like a penetration tester
* Identify attack surfaces systematically
* Interpret scan results intelligently
* Practice OSCP-style workflows

Use this framework like a coach, not a crutch.

Correct usage:
✔ Run scan → Analyze output → Think → Act manually

Incorrect usage:
❌ Run scan → wait for answers → copy results
---

## ⚡ Features

* 🔍 Automated Recon (Nmap-based scanning)
* 🌐 Web Enumeration Modules
* 🔌 API Discovery Engine
* 🧠 AI-Powered Vulnerability Explanation
* 📊 Risk Scoring System
* 🧾 Report Generation (JSON / HTML)
* 🌐 Web Dashboard (Flask UI)
* 🔄 Multi-target Scanning Support

---

##  Modes

| Mode     | Purpose                 |
| -------- | ----------------------- |
| fast     | Quick recon (CTF speed) |
| balanced | Real-world default      |
| full     | Deep enumeration        |
| oscp     | Manual-style hints      |

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/ShadowQuorix/hidden-terminal-ai.git
cd hidden-terminal-ai
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. (Linux / THM) Install tools

```bash
sudo apt update
sudo apt install -y nmap whatweb enum4linux ffuf
```

---

### 4. (Optional) Set AI key

```bash
export OPENAI_API_KEY="your_key_here"
```

---

##  Usage
How to Learn With This Tool (IMPORTANT)

Hidden Terminal is designed as a learning framework, not an auto-solver.

If you use it incorrectly, you will not improve.

✅ Correct Workflow (OSCP-Style)
1. Run scan (oscp mode)
2. Identify services manually
3. Ask: "What can I control?"
4. Expand enumeration (full mode)
5. Test inputs manually
6. Find vulnerability
7. Use AI summary to understand WHY
❌ Incorrect Workflow
Run tool → wait for answer → copy output → move on

This will:

prevent skill growth
create dependency on automation
hurt real-world performance
Recommended Learning Path
Step 1 — Start with OSCP Mode
python3 main.py -t <target_ip> -m oscp

Focus on:

open ports
service types
initial attack surface

Step 2 — Think Before Acting
Ask yourself:

- What service is exposed?
- Where can I interact with the system?
- What looks unusual?

Step 3 — Expand Enumeration
python3 main.py -t <target_ip> -m full

Now look for:

directories
endpoints
hidden functionality

Step 4 — Manual Testing (MOST IMPORTANT)

Test:

inputs
forms
parameters
uploads

This is where real skill is built.

Step 5 — Use AI as a Coach

AI output should be used to:

understand risks
guide next steps
reinforce concepts

NOT to:

skip thinking
replace manual testing

Goal:

By using this framework correctly, you will learn to:

Think like a penetration tester
Approach targets methodically
Understand vulnerabilities deeply
Perform better in OSCP-style environments

⚠️ Reminder

This tool supports your thinking — it does not replace it.
```bash
python3 main.py -t <target_ip> -m oscp
python3 main.py -t <target_ip> -m full
```

---

##  Dashboard

```bash
python -m web.app
```

Then open:

```
http://127.0.0.1:5000
```

##  Example Workflow

```text
OSCP Mode → Analyze services
↓
Full Mode → Expand enumeration
↓
Manual testing → Identify vulnerability
↓
Use AI insights → Understand WHY it works
```

---

##  Creator — @ShadowQuorix

Cybersecurity educator focused on:

* Helping beginners break into offensive security
* Teaching real workflows (not shortcuts)
* Sharing practical cybersecurity knowledge

---
##  What This Project Demonstrates

* Modular Python architecture
* Async scanning pipelines
* AI-assisted analysis layer
* Web-based dashboard integration
* Real-world pentesting workflow design

---

##  Disclaimer

This tool is intended for:

* Educational use
* Authorized testing environments only

Do not use against systems without permission.

---

##  Philosophy

> “Automation should support thinking — not replace it.”

Hidden Terminal is designed to:

* Guide your process
* Not solve everything for you
* Build real skill over time
