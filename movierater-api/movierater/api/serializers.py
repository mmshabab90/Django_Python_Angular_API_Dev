from django.contrib.auth.models import User, Group
from rest_framework import serializers
from movierater.api.models import Movie, Rating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'avg_rating', 'no_of_ratings')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('stars', 'user', 'movie')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
