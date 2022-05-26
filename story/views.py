from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Story, Chapter
from .serializers import StorySerializer, ChapterlistSerializer
from rest_framework.permissions import IsAuthenticated

#
# class StoryList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     # queryset = Story.objects.all()
#     serializer_class = StorySerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Story.objects.filter(user=user)
#
# class review_request(generics.ListAPIView):
#
#
#     user = request.user
#     review_list = Story.objects.filter(reviewer=user)
#
#             serializer = self.get_serializer(review_list, many=True)
#             return Response(serializer.data)
#
#
# class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     # queryset = Story.objects.all()
#     serializer_class = StorySerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Story.objects.filter(user=user)
#
#
# class Chapterlist(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ChapterlistSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Chapter.objects.filter(Q(user=user) | Q(reviewer=user))


class StoryList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Story.objects.all()
    serializer_class = StorySerializer

    def get_queryset(self):
        user = self.request.user
        return Story.objects.filter(user=user)

    @action(detail=False)
    def review_list(self, request, pk=None):
        user = self.request.user
        review_list = Story.objects.filter(reviewer=user)

        serializer = self.get_serializer(review_list, many=True)
        return Response(serializer.data)


class Chapterlist(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChapterlistSerializer

    def get_queryset(self):
        user = self.request.user
        return Chapter.objects.filter(Q(user=user) | Q(reviewer=user))

