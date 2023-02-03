from rest_framework import serializers
from .models import Guestlist
# Meal, Gift, Song_choice, Task_list

class GuestlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestlist
        fields = '__all__'

# class MealSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guestlist
#         fields = '__all__'

# class GiftSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guestlist
#         fields = '__all__'

# class Song_choiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guestlist
#         fields = '__all__'

# class Task_listSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guestlist
#         fields = '__all__'
