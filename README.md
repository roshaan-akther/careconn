# CareConn

Connects people needing everyday help with volunteers.

## Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```
Open http://127.0.0.1:5000

Demo accounts: admin@care.com/admin123, alice@care.com/pass123, bob@care.com/pass123.

## Architecture: Layered (Presentation/Service/Domain/Data/SQLite)
## Pattern: Strategy (volunteer matching)

## Tests
```
pytest -v
```
