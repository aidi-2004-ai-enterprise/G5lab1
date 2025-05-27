# Grou5 - lab1 - Real-World Git Workflow Simulation



This repository demonstrates a full-scale simulation of a professional Git collaboration workflow. The lab was completed by a team of three members: *Satya, **Rakesh, and **Saketh*.



We followed realistic developer practices including branching, code reviews, rebasing, undoing changes, and proper version control management using GitHub.



---



## 🎯 Lab Objectives



- Install and configure Git and GitHub
- Clone and manage a shared repository
- Use GitHub Flow with feature branches
- Submit and review pull requests (PRs)
- Handle rebasing and undoing changes
- Collaborate through pair programming and reviews
- Document work using a PR template and README
- Evaluate and reflect on Git practices



---



## 👥 Team Members & Responsibilities



### 🧑‍💼 Satya (Repo Owner)
- Created the GitHub repository and added collaborators
- Set up virtual environment using uv (pyproject.toml, uv.lock)
- Added PR template under .github/
- Created base main.py with penguins dataset loader
- Reviewed PRs submitted by Rakesh and Saketh
- Merged all PRs into main branch



### 🧑‍💻 Rakesh
- Created branch feat-rakesh-train-model
- Added data preprocessing, label encoding (via loop), and model training using XGBoost
- Added evaluation using *Precision, **Recall, **F1-score, and **Calibration Curve*
- Responded to PR review feedback and made necessary updates
- Submitted PR and got it reviewed and approved



### 🧑‍🔬 Saketh
- Created branch feat-saketh-model-fit
- Added .fit() training logic and completed the pipeline
- Simulated *undoing changes* using git restore --staged
- Performed *rebasing* of a stale branch onto updated main
- Submitted PR, assigned reviewers, and got merged



---



## 🛠 Technologies Used



- Python
- Git & GitHub
- uv (environment & dependency manager)
- pandas, seaborn, xgboost, scikit-learn, matplotlib



---
---

## 📬 Contact

If you have any questions or want to learn from our project:

- *Satya Mohan* – GitHub: [@SatyaMohan95](https://github.com/SatyaMohan95)  
- *Rakesh Kasaragadda* – GitHub: [@rak340](https://github.com/rak340)  
- *Saketh* – GitHub: [@Saketh0804](https://github.com/Saketh0804)

---



## 🚀 Project Setup



To run this project locally:



```bash
uv sync                         # Install dependencies
.\.venv\Scripts\activate        # Activate virtual environment (Windows CMD)
uv run python main.py           # Run the progra
