from flask import Flask, render_template, redirect, request, session
import random
ass = Flask(__name__)
ass.secret_key = "billshouse"

@ass.route('/')
def index():
    session['correct'] = random.randrange(0,101)
    session['message'] = ""
    print session['correct']
    return render_template('index.html')

@ass.route('/lose')
def lose():
    return render_template('lose.html')

@ass.route('/win')
def win():
    return render_template('win.html')

@ass.route('/result',methods=['POST'])
def result():
    session['guess'] = int(request.form['guess'])
    if session['guess'] == session['correct']:
        session['message'] = "CORRECT, you win!"
        return redirect('/win')
    else:
        if session['guess'] > session['correct']:
            session['message'] = "Too high"
            session['guess'] = request.form['guess']
            return redirect('/lose')
        else:
            session['guess'] = request.form['guess']
            session['message'] = "Too low"
            return redirect('/lose')

ass.run(debug=True)
