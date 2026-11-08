# Contribution Rules

## Per-member requirements (from the project spec)
- At least **6 commits between Weeks 5-13**
- Work on **your own branch**
- Meaningful commit messages
- Contribute to **at least one notebook section and one modelling task**
- **Review or comment on at least one pull request**

## Branches
- `main` is protected. Never push to it directly.
- Use `feature/<name>-<topic>`, e.g. `feature/b-dataset-rf`.

## Commit messages
Format: `<type>: <what and why>`
Types: `data`, `feat`, `model`, `eval`, `docs`, `fix`, `refactor`
Examples:
- `data: generate 1200 synthetic loan records with GenAI prompt v2`
- `model: tune Random Forest max_depth via 5-fold CV`
- `docs: add AI usage log entry for sentiment extraction`

Bad: `update`, `final`, `asdf`.

## Pull requests
1. Push your branch and open a PR into `main`.
2. Fill in the PR template.
3. Assign the reviewer below; they must comment or approve before merge.
4. Merge only after approval. Do not delete your branch (keeps history clear).

Review rotation: B reviews C, C reviews D, D reviews Leader, Leader reviews B.

## Shared rules for fair model comparison
- Use `src/evaluation.py` for the train/test split and metrics.
- Fixed seed: `RANDOM_STATE = 42`.
- Do not change the shared split without telling the leader.

## AI usage
Log every GenAI/LLM prompt that affects the data or analysis in `docs/ai_usage_log.md`.
