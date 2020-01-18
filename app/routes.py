from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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
    user = 8
    ps = [p for p in posts if p['author'] == user]
    return render_template('index.html', title='series 1', user=user, users=users, posts=ps)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    dir(form)
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
