
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.get_index,name="index"),
    path('layout/',views.get_layout,name="layout"),
    path('main/',views.main_layout,name="main"),
    path('student/',views.create_student,name="student"),
]
