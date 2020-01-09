from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    users = {
        15: { 'username': 'Edmund Duke of Edinburgh', 'description': 'great stinking fartbomb in a dopey hat' },
        22: { 'username': 'Gertrude of Ghent', 'description': 'most beautiful and gracious lady' },
        8: { 'username': 'Richard IV of England', 'description': 'magnificent piece of horse flesh, you' },
    }
    posts = [
        {
            'author': 15,
            'body': 'Percy, you idiot!'
        },
        {
            'author': 8,
            'body': 'Fresh Horse!'
        },
        {
            'author': 15,
            'body': 'Baldrick, Have you a cunning plan?!'
        },
        {
            'author': 8,
            'body': 'More Fresh Horse!'
        },
        {
            'author': 8,
            'body': 'Rumpy Pumpy! A Ha Ha Ha Ha Ha!!'
        }
    ]
    return render_template('index.html', title='series 1', user=8, users=users, posts=posts)
