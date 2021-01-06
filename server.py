from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():

    return render_template('index.html')

# Ednostavno da bidi - t.e. dynamic


@app.route('/<string:page_name>')
def page_html(page_name):
    return render_template(page_name)


def writing_data(data: dict):
    with open('database.txt', mode='a') as d_base:
        email, subject, message = data['email'], data['subject'], data['message']
        d_base.write(f'\n {email}, {subject}, {message}')
        d_base.close()


def writing_to_scv(data: dict):
    with open('database.csv', mode='a', newline='') as d_base2:
        email, subject, message = data['email'], data['subject'], data['message']
        csv_writer = csv.writer(d_base2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        writing_to_scv(data)
        return redirect("/thankyou.html")
    else:
        return 'Neshto ne vajla'


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')
