# 🛡️ Automated DevSecOps Pipeline: The Security "Quality Gate"

![AWS CodePipeline](https://img.shields.io/badge/AWS_CodePipeline-CI%2FCD-FF9900?style=plastic&logo=amazonaws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized_Scan-2496ED?style=plastic&logo=docker&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-Security_Gate-00549A?style=plastic&logo=owasp&logoColor=white)
![Python Flask](https://img.shields.io/badge/Target_App-Python_Flask-3776AB?style=plastic&logo=python&logoColor=white)

> **Mission:** Stop vulnerable code before it ever reaches the production server. This project demonstrates "Shift-Left" security by integrating Dynamic Application Security Testing (DAST) directly into the continuous integration workflow.

---

## 🎥 Project Demonstration (The Block)

**What you are watching:** The pipeline actively attacking the staging environment. ZAP detects a High-Severity Cross-Site Scripting (XSS) vulnerability, immediately fails the build, and blocks the deployment. 

Click the image below to watch a live demonstration of the DevSecOps security pipeline ⬇️

[![Watch the AWS DevSecOps Pipeline Demonstration](https://github.com/user-attachments/assets/9614920d-e429-405e-8887-edfefbc2b91c)](https://youtu.be/L_TNvdfz9PM)

---

## 🏗️ Architecture & Workflow



**The Flow:** `GitHub` ➡️ `AWS CodeBuild` ➡️ `OWASP ZAP` ➡️ `Elastic Beanstalk`

### 🧠 How It Works (The "Bouncer" Analogy)
Think of this pipeline like a VIP bouncer at a nightclub. 
1. **The Guest Arrives (Source):** A developer pushes new application code to GitHub.
2. **The ID Check (Build & Scan):** AWS CodeBuild spins up a secure Docker container and unleashes the OWASP ZAP scanner to attack the new code.
3. **The Quality Gate (Decision):**
   * ✅ **Access Granted:** ZAP finds zero critical vulnerabilities. The code is safe and deploys to Elastic Beanstalk.
   * ❌ **Access Denied:** ZAP detects a vulnerability. It triggers a system failure (Exit Code 1), immediately halting the pipeline and bouncing the bad code out.

---

## 📄 The Vulnerability Report (Artifacts)

When ZAP attacks the code, it doesn't just fail the build—it generates a comprehensive HTML medical chart (`zap_report.html`) detailing exactly what went wrong. 

During the recorded test, the pipeline automatically identified and mitigated the following risk:

* 🛑 **Identified Threat:** Cross-Site Scripting (Reflected)
* ⚠️ **Risk Level:** High
* 🛡️ **Automated Action:** Deployment Blocked. CodeBuild marked as `FAILED`.

---

## 🛠️ Replicate This Project Locally

Want to test this security gate yourself? You can pull the code directly from this repository.

**1. Clone the secure repository:**
```bash
git clone https://github.com/shreyaskatta/aws-devsecops-pipeline.git
cd aws-devsecops-pipeline
