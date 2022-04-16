from django.urls import path

from post.views import PostDetail

urlpatterns = [
    path('detail/<pk>/', PostDetail.as_view()),
]