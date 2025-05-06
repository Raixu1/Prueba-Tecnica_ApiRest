from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .models import Voter, Candidate, Vote
from .serializers import VoterSerializer, CandidateSerializer, VoteSerializer

class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        voter_id = request.data.get('voter')
        candidate_id = request.data.get('candidate')

        # Validar existencia
        voter = get_object_or_404(Voter, id=voter_id)
        candidate = get_object_or_404(Candidate, id=candidate_id)

        if voter.has_voted:
            return Response({'error': 'Este votante ya ha votado.'}, status=status.HTTP_400_BAD_REQUEST)

        vote = Vote(voter=voter, candidate=candidate)
        vote.save()
        serializer = VoteSerializer(vote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def vote_statistics(request):
    total_votes = Vote.objects.count()
    candidates = Candidate.objects.all()

    stats = []
    for candidate in candidates:
        percentage = (candidate.votes / total_votes * 100) if total_votes > 0 else 0
        stats.append({
            'candidate': candidate.name,
            'votes': candidate.votes,
            'percentage': round(percentage, 2)
        })

    voted_count = Voter.objects.filter(has_voted=True).count()

    return Response({
        'total_voted': voted_count,
        'statistics': stats
    })

