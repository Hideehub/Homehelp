from flask import render_template,request,redirect,session,flash
from werkzeug.security import generate_password_hash, check_password_hash

from homehelp.models import db,Worker
from homehelp.forms import HelpLoginForm, HelpSigninForm
from homehelp import app

@app.route('/helper/register/')
def helper_signup():
   pass


    # return render_template('helper/helper_register.html')

@app.route('/helper/login/',methods=["GET","POST"])
def helper_login():
    helploginform = HelpLoginForm()
    if request.method == "GET":
        return render_template('helper/helper_login.html', helploginform=helploginform)
    else:
        if helploginform.validate_on_submit():
            email = helploginform.email.data
            password = helploginform.password.data
            #run a query
            record = db.session.query(Worker).filter(Worker.worker_email==email).first()
            if record:
                hashed_password = record.worker_password
                chk = check_password_hash(hashed_password,password)
                if chk:
                    session['loggedin'] = record.worker_id
                    return redirect('/helper/dashboard/')
                else:
                    flash('errormsg', 'Invalid Password')
                    return redirect('/login/')
            else:
                flash('errormsg', 'Invalid Email')
                return redirect('/login/')
        else:
            return render_template('helper/helper_login.html', helploginform=helploginform)





@app.route('/helper/dashboard/')
def helper_dashboard():
    return render_template('helper/helper_dashboard.html')

@app.route('/helper/logout/')
def helper_logout():
    session.pop('loggedin', None)
    flash('feedback', "You have logged out....")
    return redirect('/login/')
