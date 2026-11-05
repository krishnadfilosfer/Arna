# GATE DA StudyOS — Deep Course v4 (Multi-user)

An 89-day GATE DA 2027 learning website with eight original beginner foundation handbooks (70 reading sections), 158 detailed concepts, 158 additional ungraded topic-specific application problems with revealed worked solutions, interactive mini-labs, 186 original scored practice questions, full-length mock simulations, flashcards and **multiple private user accounts**.

## Start it

```bash
python3 server.py
# or on Windows: python server.py
```

Open **http://127.0.0.1:8765**, create your account or log in. There are no third-party Python requirements (Python 3.10+).

Users can register with a username, display name and password. They each get **their own** saved topics, daily checks, notes, quiz history, review schedule and settings. Log in from a different device using the *same website domain and account* to get the same progress.

## Deploy online

Read **[DEPLOYMENT.md](DEPLOYMENT.md)** for complete GitHub + Railway/Render instructions. The crucial point: **attach a persistent disk or volume and set `STUDYOS_DATA_DIR`**. GitHub Pages alone cannot run this Python backend. For a public HTTPS website, set `STUDYOS_SECURE_COOKIES=1`.

## Upgrade from the single-user edition

Only when upgrading from **v1/v2**: The original database `data/progress.sqlite3` is not reused because it has no user IDs. It remains untouched. Export a JSON backup from your old StudyOS, create an account in the new StudyOS, and import that backup under **Settings & backup**. Your old data is added to your personal account only; no other learner is affected.

## What is new in v4

- **Foundation courses** in the sidebar: eight coherent, self-contained subject handbooks. They give beginners context before individual topic lessons, and cover formulas, common assumptions and worked exercises.
- **Every one of the 158 topic lessons** links to its most relevant foundation chapter and now includes an additional original applied problem with a hidden answer. Answer reveal is for self-checking; these additional problems are **not** automatically scored.
- **Unchanged**: multi-user registration/login, 89-day preparation plan, SQLite progress, spaced repetition, 186 existing scored questions, mock simulations and backup/restore.
- **Offline companion**: `DEEP_COURSE_HANDBOOK.md` includes all eight foundation readings plus the 158 extra problems and worked answers.
- **Editing**: update `foundations/*.md` or `topic_challenges.tsv`, then run `python compile_deep_course.py`. `python build_data.py` also rebuilds the deep-course additions.

### Updating an existing Railway v3 deployment

Replace the **application source files** via a Git commit and push, then redeploy the **same Railway service**. Keep `STUDYOS_DATA_DIR=/data` and the **same mounted persistent volume**. No database schema change or account reset is required in v4. Avoid committing `data/`, `.env`, or `.sqlite3`. Before changing hosting settings, export a personal backup from the Settings page and make sure your persistent volume is included in your backup strategy.

## Details

- Study content: `content.json`, `lessons.tsv`, `questions.tsv`, `enrichment.tsv`, `topic_challenges.tsv`, `foundations/*.md` and their compilation scripts.
- Frontend: `static/index.html`, `static/app.js`, `static/style.css`.
- Backend and authentication: `server.py` (Python standard library, salted scrypt passwords, random session cookies, CSRF protection, SQLite).
- Private per-user data: `STUDYOS_DATA_DIR/accounts.sqlite3`, default `data/accounts.sqlite3`. Never commit it.
- Study guides: `DETAILED_STUDY_GUIDE_158_CONCEPTS.md`, `DEEP_COURSE_HANDBOOK.md`, `STUDY_WORKBOOK_158_CONCEPTS.md`, and `ROADMAP_89_DAYS.md`.

## Developer tests

```bash
python -m unittest discover -s tests -v
node --check static/app.js
# Optional offline browser preview (requires Playwright and Chromium)
python tests/browser_v4_offline.py
```

`tests/browser_check.py` is optional; it requires Playwright and a Chromium browser, and some restricted environments block browser localhost requests. Backend integration tests run without Playwright.

## Public deployment cautions

Designed for a small group, not audited as a production identity service. You must use HTTPS, secure cookies, a persistent disk, regular off-site backups, and sensible registration controls. There is no built-in email verification or forgotten-password email flow. Operators can reset passwords through the server CLI. See [DEPLOYMENT.md](DEPLOYMENT.md).
