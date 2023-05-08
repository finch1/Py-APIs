# https://medium.com/geekculture/asynchronously-updating-a-webpage-in-a-standard-html-css-js-frontend-8496a3388c01
from flask import Flask, render_template # import class
app = Flask(__name__, template_folder='templates') # set instance to flask, so flask knows where to look for 

posts = [
    {
        'author': 'Jack White',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jack Black',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2019'        
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)