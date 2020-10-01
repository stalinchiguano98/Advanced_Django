"""Users URLs."""
# Django
from django.urls import path

# Views
from cride.users.views import (
    AccountVerificationAPIView,
    UserLoginAPIView,
    UserSignUpAPIView
)

urlpatterns = [
    path('emails/login/', UserLoginAPIView.as_view(), name='login'),
    path('emails/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('emails/verify/', AccountVerificationAPIView.as_view(), name='verify'),
]
