from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.education, name="education"),
    path('/education', view=views.home, name="home"),
]