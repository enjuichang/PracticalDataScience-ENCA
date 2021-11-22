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

#### Only Audio features

#### Audio + text features

### Deployment

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
