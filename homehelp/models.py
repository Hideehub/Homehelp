from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_username = db.Column(db.String(100), nullable=False)
    admin_password = db.Column(db.String(200), nullable=False)
    admin_email = db.Column(db.String(255), nullable=False, unique=True)
    admin_logindate = db.Column(db.DateTime(), default=datetime.utcnow)

class State(db.Model):
    state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(100), nullable=False)

class Employer(db.Model):
    employer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employer_name = db.Column(db.String(100), nullable=False)
    employer_email = db.Column(db.String(255), nullable=False, unique=True)
    employer_password = db.Column(db.String(200), nullable=False)
    employer_address = db.Column(db.Text(), nullable=True)
    employer_gender = db.Column(db.String(45), nullable=True)
    employer_picture = db.Column(db.LargeBinary, nullable=True)
    employer_phoneno = db.Column(db.String(100), nullable=True)
    date_registered = db.Column(db.DateTime(), default=datetime.utcnow)

    employer_stateid = db.Column(db.Integer, db.ForeignKey('state.state_id'), nullable=True)



class Worker(db.Model):
    worker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    worker_fname = db.Column(db.String(100), nullable=False)
    worker_lname = db.Column(db.String(100), nullable=False)
    worker_email = db.Column(db.String(255), nullable=False, unique=True)
    worker_phoneno = db.Column(db.String(100), nullable=False)
    worker_password = db.Column(db.String(200), nullable=False)
    worker_status = db.Column(db.Enum('0','1'), nullable=False, server_default=('0'))
    worker_registrationdate = db.Column(db.DateTime(), default=datetime.utcnow)
    worker_gender = db.Column(db.String(45), nullable=False)
    worker_picture = db.Column(db.LargeBinary, nullable=False)
    worker_availability = db.Column(db.Enum('0','1'), nullable=False, server_default=('0'))
    worker_verification = db.Column(db.Enum('0','1'), nullable=False, server_default=('0'))


class Experience(db.Model):
    exp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_jobtitle = db.Column(db.String(50), nullable=False)
    exp_startdate = db.Column(db.DateTime, nullable=False)
    exp_enddate = db.Column(db.DateTime, nullable=False)
    
    exp_workerid = db.Column(db.Integer, db.ForeignKey('worker.worker_id'),nullable=True)


class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat_name = db.Column(db.String(100), nullable=False)


class JobApplication(db.Model):
    __tablename__ ='jobapplication'
    app_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_status = db.Column(db.Enum('0','1'), nullable=False, server_default=('0'))
    app_dateapplied = db.Column(db.DateTime(), default=datetime.utcnow)
    app_agreedamount = db.Column(db.Numeric, nullable=False)

    app_workerid = db.Column(db.Integer, db.ForeignKey('worker.worker_id'),nullable=True)


class JobPosting(db.Model):
    __tablename__ = 'jobposting'
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_title = db.Column(db.String(100), nullable=False)
    post_description = db.Column(db.Text(), nullable=False)
    post_payrate = db.Column(db.Numeric, nullable=False)
    post_dateadded = db.Column(db.DateTime(), nullable=False)
    post_closingdate = db.Column(db.DateTime(), nullable=False)
    post_status = db.Column(db.Enum('0','1'), nullable=False, server_default=('0'))
    post_categoryid = db.Column(db.Integer, db.ForeignKey('category.cat_id'),nullable=True)
    post_employerid = db.Column(db.Integer, db.ForeignKey('employer.employer_id'),nullable=True)


class Payment(db.Model):
    pay_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pay_amount = db.Column(db.Numeric, nullable=False)
    pay_date = db.Column(db.DateTime(), nullable=False)
    pay_status = db.Column(db.Enum('0','1'), nullable=False, server_default=('0'))
    pay_employerid =  db.Column(db.Integer, db.ForeignKey('employer.employer_id'),nullable=True)
    pay_appid =  db.Column(db.Integer, db.ForeignKey('worker.worker_id'),nullable=True)


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_rating = db.Column(db.Float(), nullable=False)
    review_comment = db.Column(db.Text(), nullable=False)
    review_workerid = db.Column(db.Integer, db.ForeignKey('worker.worker_id'),nullable=True)
    review_employerid = db.Column(db.Integer, db.ForeignKey('employer.employer_id'),nullable=True)







    



