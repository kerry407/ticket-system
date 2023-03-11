from django.urls import path 
from . import views 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("sign-up/", views.CreateAccountView.as_view(), name="create-account"),
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("event-profile/create/", views.HostProfileCreateView.as_view(), name="create-event-host-profile")
]
