from application import app
from flask import Flask, render_template, request, redirect, url_for

@app.route("/")
def home():
   #the home template is rendered
   return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def add():
   URL = request.form['field1']
    #here I need to send the URL to our model and retrieve results
   return redirect(url_for('recommend'))