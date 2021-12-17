# Spotify Playlist Recommendation

The goal of this repo is to recommend songs for a given playlist based on 1) audio features 2) text features 3) playlist title.

## How to use:
```sh
git clone https://github.com/enjuichang/PracticalDataScience-ENCA.git
```

## Process
### Data extraction

### EDA and clustering

### Recommendation Model
In this project, we tried to create a recommendation based on only the audio features and also combining the audio features and text features.

### Deployment

In order to access the final version of the app, please visit the following link: nazaryaremko1.pythonanywhere.com
A demo version of the website can be accessed and tested out there. Due to the limitations of file sizes that can be uploaded to pythonanywhere, it the model there is trained only on a subset of the data. To test the full functionality of the model, please, download the repository data, cd into the folder and run the following commands:
```sh
cd recommendation_app
python wsgi.py
```
Then visit the local host and try out the model using any playlist!

To create a virtual environment, you can run the following commands:
```sh
python3 -m venv venv
source venv/bin/activate (or venv\Scripts\activate if you are using Windows)
```
Installing dependencies in virtual environment:
```
pip3 install -r requirements.txt
```

## Repo Structure
```
│
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── raw            <- The original, immutable data dump.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── models             <- Trained and serialized models, model predictions, or model summaries.
│
├── images             <- Images for the notebooks.
│
├── notebooks          <- Serialized Jupyter notebooks created in the project.
│   ├── All            <- Notebook that includes all codes.
│   ├── EDA            <- Exploratory data analysis process.
│   └── Recsys         <- The training of traditional statistical models.
│
├── templates          <- HTML code for model deployment.
│
├── app.py             <- Code for deploying of the model.
│
├── Procfile           <- Procfile for Heroku.
│
└── requirements.txt   <- The requirements file for reproducing the analysis environment.
```
