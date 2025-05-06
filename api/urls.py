from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VoterViewSet, CandidateViewSet, VoteViewSet, vote_statistics

router = DefaultRouter()
router.register(r'voters', VoterViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('votes/statistics/', vote_statistics),
]
