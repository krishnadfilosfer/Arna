# GATE DA StudyOS v4 — deploy from GitHub (multi-user edition)

**Version 4 is a content-only schema-compatible upgrade from v3. Deploy source to the existing Railway service and keep its persistent `/data` volume. Existing accounts and progress are preserved.**

**GitHub is for your source code, not the running backend.** GitHub Pages cannot run Python. Use a Python-capable host with a persistent volume for account and study data.

## 1. Test locally

Install Python 3.10 or later, extract the project and open a terminal in this folder:

```bash
python3 server.py
# Windows: python server.py
```

Visit `http://127.0.0.1:8765`. Select **Create account**, choose a unique username, display name, and password with at least 10 characters. Another person can create a separate account and will see their own blank progress. Log out and log back in to check it is saved.

Database file: `data/accounts.sqlite3` locally. Session tokens and salted password hashes are stored in it. **Do not place this file on GitHub.**

## 2. Push source to your GitHub repository

The `.gitignore` prevents local databases and backups from being committed. Review files before committing.

```bash
git init
git add .
git status
git commit -m "StudyOS with separate learner accounts"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

First create the empty repository on GitHub, or use your existing StudyOS repository. If your repository already has Git history, skip `git init`, and add/commit/push the revised files there. Do not run a force-push unless you understand its effect.

## 3. Deploy on Railway (persistent volume)

1. Create a Railway project and deploy from your GitHub repository. Use a Python service; the project includes a Dockerfile.
2. In Railway, add a **Volume** to this service and mount it at `/data`.
3. In your service settings, set environment variables:

   - `STUDYOS_DATA_DIR=/data`
   - `STUDYOS_SECURE_COOKIES=1`
   - `STUDYOS_ALLOW_SIGNUPS=1` (or `0` after your intended learners register)

4. The default Docker command runs `python server.py --host 0.0.0.0` and uses the platform-provided `PORT` environment variable. If the host demands a start command, use `python server.py --host 0.0.0.0`.
5. Generate a public HTTPS domain for the service. Test sign-up, quiz completion and login again from a different browser.
6. Redeploy and verify data still exists. The database must be under `/data` for progress to persist.

Railway volumes are a separate resource and may involve plan limits / charges. See [Railway volume docs](https://docs.railway.com/volumes/reference).

## 4. Alternative: Render (persistent disk)

1. Connect your GitHub repository as a **Python Web Service**.
2. Build command: `pip install -r requirements.txt` (nothing extra is required).
3. Start command: `python server.py --host 0.0.0.0`.
4. Attach a persistent disk (for example mount path `/var/data`) and configure:

   - `STUDYOS_DATA_DIR=/var/data`
   - `STUDYOS_SECURE_COOKIES=1`
   - `STUDYOS_ALLOW_SIGNUPS=1`

5. Use its HTTPS URL. Test persistence after redeployment.

**Warning:** Render's Free web services do **not** support persistent disks. Deploying this unchanged on free ephemeral storage will lose SQLite accounts and progress when that storage is reset. Use a paid disk-supported instance or adapt the project to a durable external database. See [Render disks](https://render.com/docs/disks) and [Free limitations](https://render.com/docs/free).

## 5. Multiple learners: what is private?

Each login has its own data rows in SQLite for: completed topics, daily checklists, saved notes, quiz attempts, flashcard intervals, activity streak and preferred daily minutes. All relevant routes check the logged-in account server-side. Exports, imports and resets are restricted to the current account. Users cannot see other learners' progress through the application. The server operator can access the database on disk, so this is **account separation**, not end-to-end encryption.

Passwords are stored as unique salted `scrypt` hashes, not plaintext. Sessions are random tokens in an HttpOnly, SameSite=Strict cookie; only token hashes are stored in SQLite. All authenticated mutations require a session-specific CSRF header. Public deployments must use HTTPS and `STUDYOS_SECURE_COOKIES=1`.

## 6. Manage users

From a terminal with access to the **same persistent database volume**:

```bash
python server.py --list-users
python server.py --reset-user-password some_username
python server.py --disable-user some_username
python server.py --enable-user some_username
```

Password reset prompts privately for a new password and signs out the user's existing sessions. Disable blocks new logins and revokes their sessions. If hosted on a platform without interactive shell access, do not assume these admin commands are available; you may need a separate authenticated management workflow later.

To close enrollment after your friends sign up, set `STUDYOS_ALLOW_SIGNUPS=0` in hosting environment and redeploy. Existing users can still log in.

## 7. Preserve current single-user StudyOS data

Old StudyOS had `data/progress.sqlite3` and a version-1 JSON export. The new version intentionally uses a **different database** `accounts.sqlite3`, without auto-assigning earlier data to the first stranger who registers.

1. In the old version go to **Settings & backup → Download backup**.
2. Deploy/run this new version and **create your own account**.
3. Go to **Settings & backup → Restore backup** and choose your original JSON file.
4. Your old topic completion, quiz results, notes and revision schedule are restored **only into your new account**.
5. Export a fresh personal backup periodically. Import replaces that account's existing progress, not other users'.

Do not upload the old SQLite database or JSON backups to a public repository.

## 8. Operational limits and next steps

- This is a small-group beta with SQLite and one server instance, **not a security-audited large public platform**.
- A persistent disk avoids loss from ordinary restarts/redeploys but is **not a backup**. Configure volume snapshots and keep off-site backups. On the old/single-user version, use personal JSON export as the migration path.
- Email verification, self-service password recovery, admin web dashboard, abuse detection, moderation, MFA, GDPR tooling, and Postgres are not included.
- SQLite on a single volume should be run as **one app instance**; avoid horizontal replicas sharing the same DB file.
- If many learners join, migrate authentication to a managed provider and use a managed PostgreSQL database, plus an audited web framework / rate limiting.

## Quick verification before inviting anyone

- Open the HTTPS URL on another device and register a second test account.
- Mark one topic complete under account A. Log in as B: it must stay unchecked.
- Add a private note, attempt a quiz, change daily minutes under A. B must not see any of those.
- Sign out A and sign back in: A must see their previous progress.
- Redeploy with the persistent volume attached and check the data survives.
- Confirm your `.gitignore` excludes `.sqlite3`, `data/`, backups and `.env` before pushing to GitHub.
