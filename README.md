# WhatTodo

 
## Python Virtual Environment

 ```bash
 cd {HOME_PATH}/WhatTodo/venv/bin
 source activate
 ```

### Setup

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Packages (Flask, SQLAlchemy ...)
```console
$ pip install -r requirements.txt
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```
