"""
WSGI config for mood_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

from __future__ import division, print_function, unicode_literals
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pickle

if not os.path.isfile('trained_model_obj'):
    # Data loading and cleaning
    songs = pd.read_csv("genres_v2.csv")
    songs = songs.drop(
        ['energy','valence','tempo','type','id','uri','track_href','analysis_url',
         'duration_ms','time_signature','genre','Unnamed: 0','title','key','mode'],axis=1)

    loudness = songs[['loudness']].values
    min_max_scaler = preprocessing.MinMaxScaler()
    loudness_scaled = min_max_scaler.fit_transform(loudness)
    songs['loudness'] = pd.DataFrame(loudness_scaled)

    songs_features = songs.copy()
    songs_features = songs_features.drop(['song_name'], axis=1)

    # Calculating silhouette score to get optimum no of clusters
    """for n_clusters in range(2,6):
        clusterer = KMeans(n_clusters=n_clusters)
        preds = clusterer.fit_predict(songs_features)
        centers = clusterer.cluster_centers_
        score = silhouette_score (songs_features, preds, metric='euclidean')
        print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))"""

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(songs_features)
    X = songs_features
    y_kmeans = kmeans.predict(songs_features)
    y = y_kmeans

    # Doing test-train split of 95% training data and 5% testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
    songs['label'] = y_kmeans

    # Fitting MLP model
    mlp = MLPClassifier()
    mlp.fit(X_train, y_train)
    obj_file = open('trained_model_obj', 'wb')
    pickle.dump(mlp, obj_file)

else:
    print("Model already pickled ... starting server")

# mlp_pred = mlp.predict(X_test)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mood_tracker.settings')

application = get_wsgi_application()
