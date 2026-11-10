# Team Setup Guide (Windows + VS Code)

Follow these steps once to get ready. Do them in order. If a step fails, copy the error and send it in the group chat.

## 0. Install the tools
- **Python 3.12 or newer** from python.org (tick **Add python.exe to PATH**). Check with `python --version`.
- **VS Code** from code.visualstudio.com
- **Git** from git-scm.com. Check with `git --version`.

## 1. VS Code extensions
Press `Ctrl+Shift+X` and install **Python** and **Jupyter** (both by Microsoft).
(If you see an "IntelliCode" error pop-up, ignore it.)

## 2. Accept the GitHub invite
Check your email for the collaborator invitation and accept it. You cannot push until you do.

## 3. Clone the repo
Open a terminal in VS Code (`` Ctrl+` ``). Go to a folder that is NOT inside another project, for example:
```
cd Documents\GitHub
git clone https://github.com/kemar-khan/wie3007-group-project.git
```
Then **File -> Open Folder** and select `wie3007-group-project`. Click **Yes** if it asks whether you trust the authors.

## 4. Set your Git name and email (once)
Use the email linked to your GitHub account, so your commits count for you:
```
git config --global user.name "Your Name"
git config --global user.email "your-github-email"
```

## 5. Create your own branch
Never work on `main`. Use the branch name from the README table:
```
git checkout -b feature/<yourname>-<topic>
```
Example: `feature/ali-random-forest`

## 6. Create the virtual environment
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install ipykernel
```
You should see `(.venv)` at the start of the terminal line.
If activation says "running scripts is disabled", run this once and try again:
```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
If VS Code asks "create a virtual environment?", close the pop-up. You already made one.

## 7. Create your notebook
1. Right-click the `notebooks` folder -> **New File** -> name it like `03_models_<yourname>.ipynb`.
2. Top right: **Select Kernel -> Python Environments -> `.venv`**.
3. In the first cell, run:
```python
import sys
sys.path.append("..")
from src.evaluation import split_data, evaluate
import pandas as pd
print(pd.__version__)
```
If it prints a version number with no error, you are ready.

## 8. First commit and push
Save the notebook (`Ctrl+S`), then:
```
git add notebooks/<your-notebook>.ipynb
git commit -m "feat: add <yourname> notebook skeleton"
git push -u origin feature/<yourname>-<topic>
```
GitHub may open a sign-in window the first time. Sign in.

## Daily workflow
```
git checkout feature/<yourname>-<topic>
git pull origin main          # get the latest team work
# ... work ...
git add <files>
git commit -m "model: short clear message"
git push
```
- Commit small and often. **Minimum 6 commits each between Weeks 5-13.**
- Message format: `type: what and why` (types: data, feat, model, eval, docs, fix, refactor). Write `docs: fix` NOT `docs : fix`.
- Before committing a notebook, use **Clear All Outputs** if outputs are large.

## Pull requests
1. Push your branch, then on GitHub click **Compare & pull request** (base: `main`).
2. Fill in the template and ask the reviewer in CONTRIBUTING.md to review.
3. Merge after approval.
4. Every member must **review or comment on at least one PR**.

## Rules
- Never push directly to `main`.
- Never commit API keys or passwords. Keep them in a `.env` file (already ignored by Git).
- Use `src/evaluation.py` for the train/test split and metrics so all models are comparable.
- Log every AI/LLM use in `docs/ai_usage_log.md`.
- Edit shared files (`README.md`, `docs/*.md`) in small changes, and pull `main` first.
