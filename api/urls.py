from django.urls import path,include
from user.views import index
from .views import Bookall,AllBooks
from .authviews import CustomUserCreate,LoginView,BlacklistTokenView,UserChangePassword
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
router=routers.DefaultRouter()
router.register(r'bookall',Bookall,basename='bookall')

authpatterns=[
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist',BlacklistTokenView.as_view(),name='blacklist'),
    path('register/',CustomUserCreate.as_view(),name="create_user"),
    path('login/',LoginView.as_view(),name="login"),  
]

bookpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls)),    
    # path('books/',BookList.as_view(),name="Books"),  
    path('allbooks/',AllBooks.as_view(),name="AllBooks"),  
    path('changepass/',UserChangePassword.as_view(),name="changepass")
   
]

urlpatterns=router.urls+authpatterns+bookpatterns
