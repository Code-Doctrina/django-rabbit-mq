from django.urls import path 
from core.views import GenerateRandomUserView


app_name="core"

urlpatterns = [
path('', GenerateRandomUserView.as_view()),
]