from django.urls import path
from . import views

urlpatterns = [
    path("getstudentlist/", views.getstudentlist.as_view()),
    path("getspecificstudentslist/<stu_id>/", views.getspecificstudentslist.as_view()),
    path('poststudentdetails/', views.poststudentdetails.as_view()),
]
