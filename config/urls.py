# chart/urls.py
from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('', include('chart.urls')),
    path('covid19_korea/',
         views.covid19_korea, name='covid19_korea'),  # !!!
    path('covid19_death/',
         views.covid19_death, name='covid19_death'),  # !!!
    path('covid19_recover/',
         views.covid19_recover, name='covid19_recover'),  # !!!
    path('covid19_country/',
         views.covid19_country, name='covid19_country'),  # !!!
    path('admin/', admin.site.urls),
]