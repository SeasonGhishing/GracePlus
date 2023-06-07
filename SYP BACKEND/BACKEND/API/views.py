from rest_framework import generics
from .models import Member
from .serializers import MemberSerializer

class MemberGetCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    
class MemberGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer