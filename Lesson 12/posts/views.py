from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    API View for listing and creating posts.

    GET: Returns paginated list of all posts (2 per page)
    POST: Creates a new post
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        """
        List all posts with pagination
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new post
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Post muvaffaqiyatli yaratildi!", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
