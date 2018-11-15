from rest_framework import permissions, generics
from django.shortcuts import render
from .serializers import DepartmentSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsEmployer
from .models import Department
from rest_framework import filters


# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsEmployer)

    def perform_create(self, serializer):
            """Save the post data when creating a new department."""
            serializer.save(employer=self.request.user) 

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer  
    permission_classes = (permissions.IsAuthenticated, IsEmployer)      


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer