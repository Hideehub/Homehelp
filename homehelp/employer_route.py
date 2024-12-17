import os,secrets
from flask import render_template,request,redirect,flash,session
from werkzeug.security import generate_password_hash, check_password_hash

from homehelp import app
from homehelp.models import db,Employer,Category,State
from homehelp.forms import LoginForm,SigninForm



@app.route("/registration/")
def register():
    return render_template('employer/registration.html')


@app.route('/login/',methods=["GET","POST"])
def login():
    loginform = LoginForm()
    if request.method == "GET":
        return render_template('employer/login.html',loginform=loginform)
    else:
        if loginform.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')
            #run a query
            record = db.session.query(Employer).filter(Employer.employer_email==email).first()
            print(record)
            if record:
                hashed_password = record.employer_password
                print(hashed_password)
                chk = check_password_hash(hashed_password,password)
                if chk:
                    session['loggedin'] = record.employer_id
                    return redirect('/employer/dashboard/')
                else:
                    flash('errormsg', 'Invalid Password')
                    return redirect('/login/')
            else:
                flash('errormsg', 'Invalid Email')
                return redirect('/login/')
        else:
            return render_template('employer/login.html', loginform=loginform)
    

# @app.route('/signup/',methods=['POST','GET'])
# def signup():
#    signinform =SigninForm()
#    states = State.query.all()
#    if request.method == 'GET':
#         return render_template('employer/signup.html',signinform=signinform,states=states)
#    else:
#         #retrieve forms value and validate
#         email = request.form.get('email')
#         password = request.form.get('password')
#         name = request.form.get('name')
#         gender =  request.form.get('gender')
#         phone =  request.form.get('phone')
#         address = request.form.get('address')

#         # Retrieve file data 
#         allowed_ext =['.jpg','.jpeg', '.png', '.gif']
#         file = request.files.get('image')
#         if not file or file.filename == '':
#             flash('errormsg','No file selected. Please upload an image file.')
#             return redirect('/signup/')
        
#         #secure filename and check file extension
#         _, ext = os.path.splitext(file.filename)
#         if ext.lower() not in allowed_ext:
#             flash('errormsg','Your cover image must be a valid image file.')
#             return redirect('/signup/')
        
#         #generate a secure random filename
#         rand_str = secrets.token_hex(10)
#         filename = f'{rand_str}{ext}'
#         upload_path= os.path.join('pkg/static/uploads/',filename)
#         file.save(upload_path)

#         hashed = generate_password_hash(password)
#         b = Employer(employer_name=name,employer_password=hashed,employer_email=email,employer_phoneno=phone,employer_gender=gender,employer_address=address,employer_picture=filename)
#         db.session.add(b)
#         db.session.commit()
#         flash( 'An account has been created for you')
#         return redirect('/login/')
   



@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    signinform = SigninForm()

    if request.method == 'GET':
        return render_template('employer/signup.html', signinform=signinform)
    
    if signinform.validate_on_submit():
        email = signinform.email.data
        password = signinform.password.data
        name = signinform.name.data
        gender = signinform.gender.data
        phone = signinform.phone.data
        address = signinform.address.data
        state = signinform.state.data

        try:
            hashed_password = generate_password_hash(password)
            new_employer = Employer(
                employer_name=name,
                employer_password=hashed_password,
                employer_email=email,
                employer_phoneno=phone,
                employer_gender=gender,
                employer_address=address,
                employer_stateid=state
            )
            db.session.add(new_employer)
            db.session.commit()
            flash('An account has been created for you!', 'success')
            return redirect('/login/')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'errormsg')
            return render_template('employer/signup.html', signinform=signinform)

    else:
        flash('Form validation failed.', 'errormsg')
        return render_template('employer/signup.html', signinform=signinform)

        

        

        # Handle file upload
        # allowed_ext = ['.jpg', '.jpeg', '.png', '.gif']
        # file = signinform.image.data

        # if not file or file.filename == '':
        #     flash('No file selected. Please upload an image file.', 'errormsg')
        #     return redirect('/signup/')

        # _, ext = os.path.splitext(file.filename)
        # if ext.lower() not in allowed_ext:
        #     flash('Invalid file type. Allowed types: jpg, jpeg, png, gif.', 'errormsg')
        #     return redirect('/signup/')

        # rand_str = secrets.token_hex(10)
        # filename = f'{rand_str}{ext}'
        # upload_folder = 'pkg/static/uploads/'
        # if not os.path.exists(upload_folder):
        #     os.makedirs(upload_folder)
        # upload_path = os.path.join(upload_folder, filename)
        # file.save(upload_path)

        # Hash password and save to database
        

    #     db.session.add(new_employer)
    #     db.session.commit()

    #     # Automatically log the user in
    #     session['loggedin'] = new_employer.employer_id
    #     flash('An account has been created for you!', 'success')
    #     return redirect('/employer/dashboard/')
    # else:
        # flash('Please check the form for errors.', 'errormsg')
        # return render_template('employer/signup.html', signinform=signinform, states=states)




@app.route('/employer/dashboard/',methods=["POST","GET"])
def dashboard():
    return render_template('employer/dashboard.html')

@app.route('/logout/')
def logout():
    session.pop('loggedin', None)
    flash('feedback', "You have logged out....")
    return redirect('/login/')





