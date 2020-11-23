from django.urls import path

from mainapp.views import increment_counter

urlpatterns = [
    path('index/', increment_counter, name='index_url')
]