from django.urls import path,include
#Import views from current directory
from . import views
urlpatterns = [
    path("",views.all_chai,name="all_chai"),
]