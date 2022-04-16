from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post.serializers import PostPolymorphicSerializer
from root_config.permissions import IsOwnerOrReadOnly
from post.models import Post


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostPolymorphicSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_count = obj.view_count + 1
        obj.save(update_fields=("view_count",))
        return super().retrieve(request, *args, **kwargs)

@login_required
@api_view(['GET'])
def get_post_list(request):
    posts = Post.objects.filter(owner=request.user)
    serializer = PostPolymorphicSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)