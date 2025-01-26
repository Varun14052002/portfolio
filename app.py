
from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('portfolio.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Back To Home')
def back_to_home():
    return render_template('/')


if __name__=="__main__":
    app.run(debug=True,port=8000)