from django.db import models

# one to one- music & one to many- gift
class Guestlist(models.Model):
    name = models.CharField(max_length=50)
    plus_one = models.CharField(max_length=50)
    rsvp = models.BooleanField(null=True)

# many to many guest to cuisine
class Cuisine(models.Model):
    title = models.CharField(max_length=50)
    allergens = models.CharField(max_length=50)
    guestlist = models.ManyToManyField(Guestlist)
    
# one to many- user may buy one or many gifts
class Gift(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    link = models.URLField()
    bought = models.BooleanField()
    guestlist = models.ForeignKey(Guestlist, on_delete=models.CASCADE)

# one guest to song choice
class Song_choice(models.Model):
    # guestlist = models.OneToOneField(
    #     Guestlist,
    #     on_delete=models.CASCADE,
    # )

    title = models.CharField(max_length=50)
    musician = models.CharField(max_length=50)

class To_do(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(null=True)