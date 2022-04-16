from django.urls import path
from accounts.views import GoogleLogin, CustomUserRegisterView, ProfileView, ProfilePosts

urlpatterns = [
    path('create/', CustomUserRegisterView.as_view()),
    path('social_login/google/', GoogleLogin.as_view(), name='google_login'),
    path('profile/<int:id>/', ProfileView.as_view()),
    path('profile_posts/', ProfilePosts.as_view()),
]
