from rest_framework import generics
from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer, SimplePostSerializer

# カテゴリ一覧View
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 記事一覧view
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer

# 記事詳細view
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer