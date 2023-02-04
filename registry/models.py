from django.db import models

# one to one- music & one to many- gift
class Guestlist(models.Model):
    name = models.CharField(max_length=50)
    plus_one = models.CharField(max_length=50)
    rsvp = models.BooleanField(null=True)

# many to many guest to meal
# class Meal(models.Model):
#     title = models.CharField(max_length=50)
#     allergens = models.CharField(max_length=50)
#     guestlist = models.ManyToManyField(Guestlist)
    
# one to many- user may buy one or many gifts
# class Gift(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.TextField()
#     price = models.DecimalField()
#     bought = models.BooleanField()
#     slug = models.SlugField()
#     guestlist = models.ForeignKey(Guestlist, on_delete=models.CASCADE)
#     picture = models.ImageField 
    # (optional)

# one guest to song choice
# class Song_choice(models.Model):
#     guestlist = models.OneToOneField(
#         Guestlist,
#         on_delete=models.CASCADE,
#         prinary_key=True
#     )

#     title = models.CharField(max_length=50)
#     musician = models.CharField(max_length=50)

class To_do(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(null=True)