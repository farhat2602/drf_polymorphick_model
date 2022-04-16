from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser, Profile
from accounts.serializers import CustomUserSerializer, ProfileSerializer
from post.models import Post
from root_config.permissions import IsOwnerOrReadOnly
from post.serializers import PostSerializer


class GoogleLogin(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000"
    client_class = OAuth2Client


class CustomUserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProfileView(APIView):

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )

    def get_profile(self, id):
        try:
            return Profile.objects.get(owner_id=id)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        profile = self.get_profile(id)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        profile = self.get_profile(id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilePosts(generics.ListAPIView):
    serializer_class = serializers.Post

    def get_queryset(self):
        return Post.objects.filter(owner_id=self.kwargs['owner_id'])

# class ProfilePosts(APIView):
#
#     def get_profile(self, id):
#         try:
#             return Profile.objects.get(owner_id=id)
#         except Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         profile = self.get_profile(id)
#         posts = profile.posts.all()
#         serializer = ProfileSerializer(posts, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
