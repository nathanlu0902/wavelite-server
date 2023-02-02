
from django.urls import path
from api.views import login

app_name='login'
urlpatterns = [
    path('login', login),
]