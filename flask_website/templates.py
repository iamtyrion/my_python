from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [

    {
        'author': 'gsk',
        'title': 'blog post',
        'contenet': 'post1',
        'date': 'July 1 2018'
    },
    {
        'author': 'gsk2',
        'title': 'blog post 2',
        'contenet': 'post2',
        'date': 'July 1 2018'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
