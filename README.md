# Enhance your Playlists with Machine Learning: Spotify Automatic Playlist Continuation

This is the repository of the group project [Enhance your Playlists with Machine Learning: Spotify Automatic Playlist Continuation](https://medium.com/@enjui.chang/enhance-your-playlists-with-machine-learning-spotify-automatic-playlist-continuation-2aae2c926e77). The four articles in the series is linked below:

**Part I**: [Extracting song data from Spotify’s API in Python](https://cameronwwatts.medium.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50)

**Part II**: EDA and Clustering

**Part III**: [Building a Song Recommendation System with Spotify](https://medium.com/@enjui.chang/part-iii-building-a-song-recommendation-system-with-spotify-cf76b52705e7)

**Part IV**: [Deploying a Spotify Recommendation Model with Flask](https://medium.com/@yaremko.nazar/deploying-a-spotify-recommendation-model-with-flask-20007b76a20f)

The code for all four articles is in this repository.

## Introduction

The goal of this project is to recommend songs for a given playlist. This project starts from data collection all the way to model deployment to ensure you have a working model to showcase.

## How to use

To clone the repository:
```sh
git clone https://github.com/enjuichang/PracticalDataScience-ENCA.git
```

## Process

The following image is the flow chart of the project:

<img width="810" alt="Screen Shot 2021-12-18 at 12 02 45 AM" src="https://user-images.githubusercontent.com/55577469/146573138-09798463-c9fe-45b9-adc3-f95556e30564.png">

### Data extraction

Here are a couple of things you should know before starting the project.

#### Spotfiy API Acquisition
If you haven’t used an API before, the use of various keys for authentication, and the sending of requests can prove to be a bit daunting. The first thing we’ll look at is getting keys to use. For this, we need a [Spotify for developers] (https://developer.spotify.com/) account. This is the same as a Spotify account, and doesn’t require Spotify Premium. From here, go to the dashboard and “create an app”. Now, we can access a public and private key, needed to use the API.

#### Spotify Credentials Storage and Access

Now that we have an app, we can get a client ID and a client secret for this app. Both of these will be required to authenticate with the Spotify web API for our application, and can be thought of as a kind of username and password for the application. It is best practice not to share either of these, but especially don’t share the client secret key. To prevent this, we can keep it in a separate file, which, if you’re using Git for version control, should be Gitignored.

Spotify credentials should be stored the in the a `secret.txt` file with the first line as the **credential id** and the second line as the **secret key**:

<img width="293" alt="Screen Shot 2021-12-18 at 12 10 03 AM" src="https://user-images.githubusercontent.com/55577469/146574104-804def73-54ec-449a-931c-86372d3a07a6.png">

To access this credentials, please use the following code:

```python
with open("secret.txt") as f:
    secret_ls = f.readlines()
    cid = secret_ls[0][:-2]
    secret = secret_ls[1]
```
### EDA and clustering

### Recommendation Model
The recommendation model is summarized in the `content_based_recsys.ipynb` notebook. In this section, we will go through the process of building a content-based filtering recommendation. The following parts will be covered:

1. Package Setup
2. Preprocessing
3. Feature Generation
4. Content-based Filtering Recommendation

Please follow the instruction in the notebook to produce the result.

### Deployment

In order to access the final version of the app, please visit the following link: [nazaryaremko1.pythonanywhere.com](nazaryaremko1.pythonanywhere.com)
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
│   ├── processed      <- The preprocessed data sets for training.
│   ├── test           <- The test data sets for testing.
│   └── final          <- The final data sets for modeling.
│
├── models             <- Trained models, model predictions, or model summaries.
│
├── notebooks          <- Serialized Jupyter notebooks created in the project.
│   ├── script         <- Script for data extraction and loading data
│   ├── Extraction     <- Data extraction using Spotify API
│   ├── EDA            <- Exploratory data analysis process.
│   └── Recsys         <- The training of traditional statistical models.
│
├── recommendation_app <- Model deployment folder
│   ├── application    <- Code for model deployment and website design
│   ├── data1          <- Pretrained data for model
│   └── venv           <- Environment
│
└── requirements.txt   <- The requirements file for reproducing the analysis environment.
```
