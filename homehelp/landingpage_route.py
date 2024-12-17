from flask import render_template,request

from homehelp import app
from homehelp.models import db,Category



# @app.errorhandler(404)
# def page_not_found(error):
#     # return "The page you are looking for does not exist"
#     return render_template("landingpage/error_file.html",error=error),404

# @app.errorhandler(503)
# def error_five_zero_three(error):
#     # return "The page you are looking for does not exist"
#     return render_template("landingpage/error_file503.html",error=error),503

# @app.errorhandler(500)
# def error_five(error):
#     # abort(403) #401 unauthorzed #404 not found #403 forbidden
#     return render_template('landingpage/error_file500.html', error=error),500

@app.route('/about/')
def about():
    return render_template('landingpage/about.html')

@app.route('/')
def index():
    return render_template('landingpage/index.html')

@app.route('/blog')
def blog():
    return render_template('landingpage/blog.html')

@app.route('/ajax/search/', methods=['POST']) 
def ajax_search():
    search_data = request.form.get('search')
    search_result = ''
    if search_data != '':
        search_filter = f'%{search_data}%'
        categories = Category.query.filter(Category.cat_name.like(search_filter)).all()
        search_result = ''
        for category in categories:
            search_result += f'<span>{category.cat_name}</span><br>'
        return search_result
    else:
        return search_result