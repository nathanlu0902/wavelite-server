
from django.urls import path,include
from api.views import UserView,GoodsViewSet,GoodsCategoryViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register("GoodsCategory",GoodsCategoryViewSet)
router.register("Goods",GoodsViewSet)

urlpatterns = [
    path('<str:wx_code>/create', UserView.as_view()),
    path('<str:wx_code>/login',UserView.as_view()),
    path('<str:openid>/update',UserView.as_view()),
    # path('',include(router.urls)),
]