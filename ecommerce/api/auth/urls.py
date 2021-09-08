from django.urls import path,include


from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import RegisterAPIView,LoginAPIView,UserAPIView

from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="create_user"),
    path('login/', LoginAPIView.as_view(), name="login_view"),
    path('logout/', knox_views.LogoutView.as_view(), name="knox_logout"),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name="login_view"),
    path('user/', UserAPIView.as_view(), name="user"),
]