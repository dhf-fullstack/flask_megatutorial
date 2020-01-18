# Miguel Grinberg's Flask megatutorial

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

```
FLASK_APP=microblog.py FLASK_ENV=development FLASK_DEBUG=1 SECRET_KEY='...whatever...' flask run
flask db migrate -m "...commit message..."
flask db upgrade
FLASK_APP=microblog.py flask shell # microblog.py shell context
```
