### Building Url Dynamically
### Variable Rule
### Jinja 2 Template Engine

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        pass
    return render_template('jinja.html')

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        res = 'PASSED'
    else:
        res = 'FailED'

    return render_template('jinja.html', results=res)

###Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{% ... %} conditions, for loops
{# ... #} this is for comments
'''

if __name__=="__main__":
    app.run(debug=True)