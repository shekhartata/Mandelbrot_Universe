from django.urls import path, re_path
from .views import MoodTracer, CallBackSpotify

app_name = 'controller'

urlpatterns = [
    path('rest/tracker', MoodTracer.as_view(), name='Test'),
    path('callback/', CallBackSpotify.as_view(), name='TestAuth')
]
