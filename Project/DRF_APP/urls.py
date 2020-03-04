# from django.urls import path
# from .views import PostView, SinglePostView
# app_name = "posts"
# # app_name will help us do a reverse look-up latter.

# urlpatterns = [
#     path('posts/', PostView.as_view()),
#     path('posts/<int:pk>', SinglePostView.as_view())
# ]


from rest_framework.routers import DefaultRouter
from .views import PostViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = router.urls