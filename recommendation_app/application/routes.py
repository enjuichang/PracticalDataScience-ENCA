from application import app
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from application.features import *
from application.model import *

songDF = pd.read_csv("./data/allsong_data.csv")
complete_feature_set = pd.read_csv("./data/complete_feature.csv")

@app.route("/")
def home():
   return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
   URL = request.form['URL']
   df = extract(URL)
   edm_top40 = recommend_from_playlist(songDF, complete_feature_set, df)
   number_of_recs = int(request.form['number-of-recs'])
   my_songs = []
   for i in range(number_of_recs):
      my_songs.append(str(edm_top40.iloc[i,1]) + ' - '+ '"'+str(edm_top40.iloc[i,4])+'"')
   return render_template('results.html',songs= my_songs)