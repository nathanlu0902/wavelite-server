
from django.urls import path,include
from api.views import UserView,GoodsViewSet,GoodsCategoryViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register("GoodsCategory",GoodsCategoryViewSet)
router.register("Goods",GoodsViewSet)

urlpatterns = [
    # path('<str:openid>', UserView),
    path('<str:openid>/create',UserView.as_view()),
    # path('',include(router.urls)),
    path('<str:openid>/update',UserView.as_view()),
]