# alumni-tracker

A web app for tracking TFN alumni across different career pathways

## User stories

- Authentication
  - Signup
  - Login
  - Logout
  - Reset password
- ProfileInfo
  - CRUD
- Career pathways

## Setup virtual env

- `git clone <repo-url>`
- `python -m venv <venv>`
- `Set-ExecutionPolicy -ExecutionPolicy Remote Signed -Scope CurrentUser`
- `.\venv\Scripts\activate`
  > install project & packages
  - `pip install django`
  - `django-admin --version`
  - `django-admin startproject alumni_tracker .`
  - `python manage.py runserver`
- `.\venv\Scripts\deactivate`

## Security

> Remove DJANGO SECRET in settings.py

    - `os.environ['ZZXXX_KEY']`
    - Do not checkin .env into VCS
