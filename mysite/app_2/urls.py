from django.urls import path
from .views import index

# app_2,
app_name = "app_2"

urlpatterns = [

    # path('',app_2,name='app_2'),
    path('', index, name='index'),

]