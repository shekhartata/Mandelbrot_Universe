# Mandelbrot_Universe

This repository contains code for a Multi-Layer Perceptron (MLP) based music mood predictor which takes in the 
user's recently played 50 tracks on spotify and describes the recent music mood you've been in !

The training dataset used here is available on Kaggle (https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify).
The model is run against the test data which is fetched from Spotify API (https://developer.spotify.com/documentation/web-api/). 

The codebase consists of a django based server hosting the MLP model - which trains upon service startup and is then
unloaded and run against the test data each time we make a POST call to the server
(http://localhost:port/controller/callback/).

Besides, there is a caller script - get_liked_songs.py which acts as the driver script - making spotify API calls to
fetch 50 recently played tracks and then does a POST call upon the django server with the playlist data.

A GET call on the django service (http://localhost:port/controller/rest/tracker) gives the list of all the 
mood predictions along with the datetime stamp.

The database used here is apache cassandra which is essentially a NoSQL dB capable of high end performance offering high scalability.

Directives on how to run the server and driver script:

1. Django server hosting the model -> <br/><br/> a. Create a venv, install django and then clone the server codebase (mood_tracker/) <br/>
                                      b. Start a venv - venv/Scripts/activate.bat <br/>
                                      c. Install apache-cassandra and start a cassandra dB session by running bin/run-cassandra.bat 
                                         file in the installation directory <br/>
                                      d. Run dB migrations for cassandra using python manage.py sync_cassandra in the django server directory <br/>
                                      e. Start the django server with python manage.py runserver, which by default starts at localhost:8000 <br/>

2. Caller script to fetch spotify data and call the server -> <br/><br/> Get the user client id and client secret from spotify development API and insert that
in the authentication codeflow of the script.

The model as of now is capable of predicting only 3 moods based on the track list provided - upbeat / entropic, thoughtful and energetic. 
<br/><br/>
NOTE -> The work done here is open to development and suggestions. Feel free to clone/raise PR with further improvements. 
The model used here is inspired in part from the work done by <strong>Sylvester Cardorelle</strong> (https://github.com/SylCard/Spotify-Emotions-Project), who
has also written an exquisite article on the same (https://towardsdatascience.com/predicting-my-mood-using-my-spotify-data-2e898add122a). <br/>
It is a Multi-Layer Perceptron (MLP) based deep learning algorithm driven by K-means clustering.
Besides, as part of future track work plan is to have the model hosted as a containerised service, so that's another area to work upon.
