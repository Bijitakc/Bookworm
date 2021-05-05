from django.urls import path,include
from user.views import index
from .views import CustomUserCreate,LoginView,Bookall,BlacklistTokenView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
router=routers.DefaultRouter()
router.register(r'bookall',Bookall,basename='bookall')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('books/',BookList.as_view(),name="Books"),
    path('register/',CustomUserCreate.as_view(),name="create_user"),
    path('login/',LoginView.as_view(),name="login"),
    # path('logout/')
    path('logout/blacklist',BlacklistTokenView.as_view(),name='blacklist')  
]

urlpatterns+=router.urls
