SMARTEXPENSETRACKER - FLASK ADMIN MODULE

The React files you shared have been converted into Flask routes, Jinja HTML templates and CSS. The existing app remains Python/Flask; no React/Vite dependency is required.

ADMIN PAGE: /admin
LOGIN PAGE: /admin/login
DEMO LOGIN (same credentials from your React file):
Email: admin@expense.com
Password: admin123

IMPORTANT SECURITY:
- Set ADMIN_EMAIL and ADMIN_PASSWORD as environment variables in your local .env / Render environment.
- Change the demo password before deploying.
- The module reads real users and expenses from the existing PostgreSQL/Supabase tables.
- It currently provides read-only user, transaction and category reporting. It does not block/delete user accounts because the supplied database schema has no admin-role or blocked-account fields.
- This archive intentionally excludes .env, .git, and the local expenses.db so secrets and stale local data are not bundled. Keep your existing .env and database settings in your working project.

RUN:
1. Extract this ZIP.
2. Copy/merge its files into your existing SmartExpenseTracker folder (keep your own .env file).
3. Install dependencies from requirements.txt if needed: pip install -r requirements.txt
4. Run: python app.py
5. Open: http://127.0.0.1:5000/admin

The admin module uses the same DATABASE_URL and users/expenses tables as your existing Flask app.
