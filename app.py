from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run()