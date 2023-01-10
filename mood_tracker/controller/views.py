from django.shortcuts import render

# Create your views here.
from django.views import View
from http import HTTPStatus
from django.http import JsonResponse, HttpResponse
from .utils import normalise_loudness_param, cluster_mapper
from .query import get_users_all, create_record_users, get_users_id, update_record_users
import json
import pandas as pd
import pickle
import numpy as np
from datetime import datetime


class MoodTracer(View):
    # allowed rest calls for this class
    http_method_names = ['get']

    def __init__(self):
        pass

    def get(self, request):
        output = get_users_all()
        return JsonResponse({"Response": output})


class CallBackSpotify(View):
    http_method_names = ['get', 'post']

    def __init__(self):
        pass

    # Just for the spotify developer auth callback
    def get(self, request):
        k = request.GET
        print(k)
        print(k.get('code'))
        return JsonResponse({"hello": "wip"})

    def post(self, request):
        request_body_draft = request.body.decode('utf-8')
        request_body = json.loads(request_body_draft)
        if request_body.get('recentTracks'):
            df_test = pd.DataFrame(request_body['recentTracks'])
            normalise_loudness_param(df_test)
            df_names = df_test['name']
            df_test = df_test.drop(
                ['energy', 'valence', 'tempo', 'id', 'name'], axis=1)
            print(f"Loaded test data into data frame - {df_test}")
            model = pickle.load(open('trained_model_obj', 'rb'))
            prediction = model.predict(df_test)
            if max(np.unique(prediction, return_counts=True)[1]) == \
                    np.unique(prediction, return_counts=True)[1][0]:
                print("Mood of late has been that of thoughtful - "
                      "deep feels driven by lyrics more than music.")
                mood_string = cluster_mapper.get(0)
            elif max(np.unique(prediction, return_counts=True)[1]) == \
                    np.unique(prediction, return_counts=True)[1][1]:
                print("Mood of late has been that of thoughtful - "
                      "driven by music more than lyrics.")
                mood_string = cluster_mapper.get(1)
            else:
                print("Mood of late has been that of upbeat "
                      "/ energetic songs mainly.")
                mood_string = cluster_mapper.get(2)
            pred_cluster = [cluster_mapper.get(x) for x in prediction]
            result_df = pd.DataFrame(pred_cluster, columns=['Clusters'])
            result_df['song_name'] = df_names
            print(result_df)
            date_string = datetime.today().strftime('%Y-%m-%d')
            user_db_record = create_record_users(
                {"music_mood": mood_string, "date_stamp": date_string})
        return JsonResponse({"Status": "Success"})
