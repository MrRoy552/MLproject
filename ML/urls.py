from django.urls import path

from ML import views

urlpatterns = [

    path("",views.home),
    path("predict",views.predict)
]