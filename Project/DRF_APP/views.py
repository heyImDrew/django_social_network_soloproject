from rest_framework import viewsets

from Thoughts.models import Post, Comment
from Communication.models import Message
from .serializers import PostSerializer, MessageSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


# from rest_framework.generics import get_object_or_404
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from ExtendsUserModel.models import User
# from Thoughts.models import Post
# from .serializers import PostSerializer

# class PostView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def perform_create(self, serializer):
#         connected_to = get_object_or_404(User, id=self.request.data.get('connected_to_id'))
#         return serializer.save(connected_to=connected_to)

# class SinglePostView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer