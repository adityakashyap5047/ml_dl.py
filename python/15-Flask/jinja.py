### Building Url Dynamically
### Variable Rule
### Jinja 2 Template Engine

from flask import Flask, render_template, request, url_for, redirect

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
    res = ''
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

@app.route('/eva/<int:score>')
def ev(score):
    res = ''
    if score >= 50:
        res = 'PASSED'
    else: 
        res = 'FAILED'

    exp = {'score': score, 'res': res}

    return render_template('result.html', exp=exp)

@app.route('/submitres', methods=['GET', 'POST'])
def submitres():
    score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        score = (science + maths + c + datascience) / 4
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('ev', score=score))

if __name__=="__main__":
    app.run(debug=True)