from rest_framework import serializers
from .models import Department, User


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    admin = serializers.ReadOnlyField(source='employer.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Department
        fields = ('id', 'department', 'firstname', 'lastname', 'email', 'description', 'admin','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    departments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Department.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'departments')