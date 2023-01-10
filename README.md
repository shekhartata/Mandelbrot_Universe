# Mandelbrot_Universe

This repository contains code for an MLP based music mood predictor which takes in the 
spotify recently played 50 tracks and describes the recent music mood you've been in !

The codebase consists of a django based server which hosts the MLP amodel - which trains upon service startup and
gets pickled, which can then be unloaded and run against the test data each time we make a POST call to the server
(http://localhost:port/controller/callback/).

Besides, there is a caller script - get_liked_songs.py which acts as the driver script - making spotify API calls to
fetch 50 recently played tracks and then does a POST call upon the django server with the playlist data.

A GET call on the django service (http://localhost:port/controller/rest/tracker) gives the list of all the 
mood predictions along with the datetime stamp.

The database used here is apache cassandra which is essentially a NoSQL dB capable of high end performance offering high scalability.

NOTE -> The work done here is open to improvements and suggestions. Feel free to clone/raise PR with further improvements and suggestions.
