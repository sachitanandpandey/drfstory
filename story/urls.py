from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import StoryList, StoryDetail, Chapterlist
from .views import StoryList, Chapterlist

# urlpatterns = [
#     path('story/', StoryList.as_view(), name="StoryDisplay"),
#     # path('storydetails/<int:pk>/', StoryDetail.as_view(), name="StoryDetails"),
#     path('chapter/<int:pk>/', Chapterlist.as_view(), name="ChapterList"),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'story', StoryList, basename="Story")
router.register(r'chapter', Chapterlist, basename="Chapters")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

