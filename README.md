### Tasklist 

This is a simple implementation of tasklist application.
It consists of Django server side and React client side.

## Server

Python 3 is required.
It is recommended to use python virtualenv.
There is requirements.txt with requirements for the project.

After installing dependencies, go to server directory and run

```
python manage.py makemigrations tasklist
python manage.py migrate 
```

Now you will need users as registration is not implemented
To load users run
``` 
python manage.py loaddata tasklist/fixtures/user.json
```
After that server is ready to be started with
```
python manage.py runserver
```

To run the tests, run
```
python manage.py test
```

## Client

Client is a standard CreateReactApp with material-ui and axios dependencies.
To install the dependencies, change your working folder to client and run

```
npm install
```
After that you can run
```
REACT_APP_SERVER_ADDRESS=http://127.0.0.1:8000 npm start
```
If your server is running by default on address 127.0.0.1, port 8000
