from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class PostListPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page
    page_size_query_param = 'page_size'

class PostListView(APIView):
    def get(self, request):
        # Fetch all posts ordered by timestamp (latest first)
        posts = Post.objects.order_by('-timestamp')
        paginator = PostListPagination()
        print("paginator", paginator)
        paginated_posts = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(paginated_posts, many=True)
        return paginator.get_paginated_response(serializer.data)
