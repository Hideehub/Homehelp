from flask import render_template,request,redirect,flash,session

from homehelp import app
from homehelp.models import Admin,db
from homehelp.forms import AdminLoginForm

from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/admin/login/',methods=['GET','POST'])
def admin():
    adminloginform = AdminLoginForm()
    if request.method == 'GET':
        return render_template('admin/admin_login.html',adminloginform=adminloginform)
    else:
        if adminloginform.validate_on_submit():
            email = adminloginform.email.data
            password = adminloginform.password.data
            record = db.session.query(Admin).filter(Admin.admin_email==email).first()
            if record:
                hashed_password = record.admin_password
                chk = check_password_hash(hashed_password,password)
                if chk:
                    session['loggedin'] = record.admin_id
                    return redirect('/admin/dashboard/')
                else:
                    flash('errormsg', 'Invalid Password')
                    return redirect('/admin/login/')
            else:
                flash('errormsg', 'Invalid Email')
                return redirect('/admin/login/')
        else:
            return render_template('admin/admin_login.html', adminloginform=adminloginform)

    

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')