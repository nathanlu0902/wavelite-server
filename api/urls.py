
from django.urls import path
from api.views import login,registerUser,updateUser

app_name='login'
urlpatterns = [
    path('login', login),
    path('registerUser',registerUser),
    path('updateUser',updateUser)
]