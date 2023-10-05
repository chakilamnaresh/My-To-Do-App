from django.urls import path
from . import signup_views
from . import signin_views

urlpatterns = [
    path('signup', signup_views.signup, name="signup"),
    path('signin', signin_views.signin, name="signin"),
    path('logout', signin_views.logout_user, name="logout")
]