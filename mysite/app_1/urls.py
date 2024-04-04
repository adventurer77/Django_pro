from django.urls import path
from .views import index
# app_1,
app_name="app_1"

urlpatterns = [

    # path('', app_1, name="app_1"),
    path('',index, name='index'),
    # path('',main, name='main'),
    

]


