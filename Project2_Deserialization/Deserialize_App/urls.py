from django.urls import path
from Deserialize_App import views


urlpatterns = [
    path('', views.student_create)
]
