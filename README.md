# WhatTodo

 
## 파이썬 가상환경으로 실행하기

 ```bash
 cd {HOME_PATH}/WhatTodo/venv/bin
 source activate
 ```

 ## 파이썬 flask run
 ```bash
 flask run
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

Install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
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
