# GATE DA StudyOS — Multiuser Edition v3

An 89-day GATE DA 2027 learning website with 158 detailed concepts, interactive mini-labs, 186 original practice questions, full-length mock simulations, flashcards and now **multiple private user accounts**.

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

The original database `data/progress.sqlite3` is not reused because it has no user IDs. It remains untouched. Export a JSON backup from your old StudyOS, create an account in the new StudyOS, and import that backup under **Settings & backup**. Your old data is added to your personal account only; no other learner is affected.

## Details

- Study content: `content.json`, `lessons.tsv`, `questions.tsv`, `enrichment.tsv` and material-building scripts.
- Frontend: `static/index.html`, `static/app.js`, `static/style.css`.
- Backend and authentication: `server.py` (Python standard library, salted scrypt passwords, random session cookies, CSRF protection, SQLite).
- Private per-user data: `STUDYOS_DATA_DIR/accounts.sqlite3`, default `data/accounts.sqlite3`. Never commit it.
- Study guides: `DETAILED_STUDY_GUIDE_158_CONCEPTS.md`, `STUDY_WORKBOOK_158_CONCEPTS.md`, and `ROADMAP_89_DAYS.md`.

## Developer tests

```bash
python -m unittest discover -s tests -v
node --check static/app.js
```

`tests/browser_check.py` is optional; it requires Playwright and a Chromium browser, and some restricted environments block browser localhost requests. Backend integration tests run without Playwright.

## Public deployment cautions

Designed for a small group, not audited as a production identity service. You must use HTTPS, secure cookies, a persistent disk, regular off-site backups, and sensible registration controls. There is no built-in email verification or forgotten-password email flow. Operators can reset passwords through the server CLI. See [DEPLOYMENT.md](DEPLOYMENT.md).
