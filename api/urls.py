
from django.urls import path,include
from api.views import UserView,GoodsCategoryView,GoodsView,UserListView,UserListDestroyView
from rest_framework import routers

# router=routers.DefaultRouter()
# router.register("GoodsCategory",GoodsCategoryViewSet)
# router.register("Goods",GoodsViewSet)

urlpatterns = [
    path('<str:wx_code>/create', UserView.as_view()),
    path('<str:wx_code>/login',UserView.as_view()),
    path('<str:openid>/update',UserView.as_view()),
    #admin接口
    path('UserList',UserListView.as_view()),
    path('deleteUsers',UserListDestroyView.as_view()),
    path('goodsCategory',GoodsCategoryView.as_view()),
    path('goods',GoodsView.as_view())
    # path('',include(router.urls)),
]