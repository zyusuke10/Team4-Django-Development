# Team 4 Online Training

A project created in an attempt to boost Rakuten sales for users in their 20's

# Git Commit Naming Convention

A commit message should start with a category of change. You can pretty much use the following 4 categories for everything: feat, fix, refactor, and chore.

feat is for adding a new feature
fix is for fixing a bug
refactor is for changing code for peformance or convenience purpose (e.g. readibility)
chore is for everything else (writing documentation, formatting, adding tests, cleaning useless code etc.)

example git commit message:
```
feat: add new button
```

```
fix: fix render bug
```

```
refactor: rewrite function x to be more reusable
```

```
chore: write documentation
```

# Setup

Create python venv to isolate the project modules from others
```
python -m venv env
```
Activate the python virtual environment
Mac
```
source env/bin/activate
```

Install the python modules
```
pip3 install -r requirements.txt
```

If you've added a new python module or updated one
```
pip3 freeze > requirements.txt 
```

Create a conf/.env file, see conf/.example.env as reference

Migrate database if you haven't done it
```
python3 manage.py migrate
```

Run server
```
python3 manage.py runserver
```
