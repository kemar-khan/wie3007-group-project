# WIE3007 Group Project: AI-Enhanced Data Mining

Universiti Malaya, WIE 3007 Data Mining (2026/2027 Sem 1). Due Week 14.

**Domain:** _TBD (e.g. loan default / customer churn / fraud risk)_
**Target variable:** _TBD_

## Team

| Member | GitHub    | Branch                   | Model owned                                   | Notebook section                       |
| ------ | --------- | ------------------------ | --------------------------------------------- | -------------------------------------- |
| Akmal  | @username | `feature/akmal-baseline` | Decision Tree (baseline), Logistic Regression | Setup, evaluation harness, integration |
| Dianah | @username | `feature/b-dataset-rf`   | Random Forest                                 | Dataset simulation, EDA                |
| Fahiim | @username | `feature/c-features-xgb` | XGBoost / Gradient Boosting                   | LLM/SLM feature engineering            |
| Veron  | @username | `feature/d-eval-mlp`     | MLP                                           | Evaluation and interpretation          |

## Repository structure

```
data/raw/         generated (simulated) data
data/processed/   data after LLM feature extraction
notebooks/        Jupyter notebooks (one section per member)
src/              shared code (evaluation harness)
docs/             AI usage log, contribution summary
reports/          final report and presentation
scripts/          helper scripts (commit counter)
```

## Workflow

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: own branch, small commits, PR into `main`, one reviewer.

## Deliverables

- [ ] GitHub repository
- [ ] Jupyter notebook
- [ ] Final report (5-7 pages, PDF/DOCX)
- [ ] Recorded presentation
