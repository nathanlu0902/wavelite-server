
from django.urls import path,include
from api.views import login,registerUser,updateUser,GoodsViewSet,GoodsCategoryViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register("GoodsCategory",GoodsCategoryViewSet)
router.register("Goods",GoodsViewSet)

urlpatterns = [
    path('login', login),
    path('registerUser',registerUser),
    path('',include(router.urls)),
    path('updateUser',updateUser),
]