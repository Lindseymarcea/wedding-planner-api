from rest_framework import serializers
from .models import Guestlist, To_do, Cuisine, Song_choice, Gift


class GuestlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestlist
        fields = '__all__'

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'

class Song_choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song_choice
        fields = '__all__'

class To_doSerializer(serializers.ModelSerializer):
    class Meta:
        model = To_do
        fields = '__all__'
