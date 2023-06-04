# CEN4010-Bookstore-API
Summer 2023 Bookstore API 
Sure, here's a README that only includes macOS instructions:


This project provides a Python Flask backend that interfaces with a MySQL database. 


## Setup




Set up a Python virtual environment. 

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Now install the Python packages that the project depends on:

```bash
pip install -r requirements.txt
```

Before you run the application, ensure you have set up your MySQL database and replaced `'user:password@localhost/dbname'` in `config.py` with your actual database credentials.

## Running the project

Now you're ready to run the project:

```bash
python run.py
```

This starts the Flask development server
