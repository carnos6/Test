from flask import Flask, render_template, url_for
from flask import request, redirect
import csv
app = Flask(__name__)



# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     #print(url_for('static', filename='favicon.ico'))
#     return render_template('./indexold.html', name=username, post_idHTML=post_id)
@app.route('/')
def Home():
    #print(url_for('static', filename='favicon.ico'))
    return render_template('./index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        file = database.write(f'\n{email},{subject},{body}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,body])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'ooops'
    else:
        return 'oooops'

#
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')
# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')
# @app.route('/components.html')
# def components():
#     return render_template('./components.html')
# @app.route('/index.html')
# def index():
#     return render_template('./index.html')
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'Hello, blog2!!!!!!!!!!!!!!!!'
