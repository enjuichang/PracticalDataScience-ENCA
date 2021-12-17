from application import app
from flask import Flask, render_template, request
from application.features import *
from application.model import *

songDF = pd.read_csv("./data1/allsong_data.csv")
complete_feature_set = pd.read_csv("./data1/complete_feature.csv")

@app.route("/")
def home():
   #render the home page
   return render_template('home.html')

@app.route("/about")
def about():
   #render the about page
   return render_template('about.html')

@app.route('/recommend', methods=['POST'])
def recommend():
   #requesting the URL form the HTML form
   URL = request.form['URL']
   #using the extract function to get a features dataframe
   df = extract(URL)
   #retrieve the results and get as many recommendations as the user requested
   edm_top40 = recommend_from_playlist(songDF, complete_feature_set, df)
   number_of_recs = int(request.form['number-of-recs'])
   my_songs = []
   for i in range(number_of_recs):
      my_songs.append([str(edm_top40.iloc[i,1]) + ' - '+ '"'+str(edm_top40.iloc[i,4])+'"', "https://open.spotify.com/track/"+ str(edm_top40.iloc[i,-6]).split("/")[-1]])
   return render_template('results.html',songs= my_songs)