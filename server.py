from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secrets don't make friends"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    if 'email_list' not in request.form:
        session['email_list'] = ''
    else:
        session['email_list'] = request.form['email_list']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
