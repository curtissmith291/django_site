from django.db import models

# Create your models here.

class Beers(models.Model):
    beer_name = models.CharField(max_length=150)
    brewery = models.CharField(max_length=150)

    def __str__(self):
        return str(self.beer_name)

class Results(models.Model):
    abv = models.FloatField()
    astringency = models.IntegerField()
    body = models.IntegerField()
    alcohol = models.IntegerField()
    bitter = models.IntegerField()
    sweet = models.IntegerField()
    sour = models.IntegerField()
    salty = models.IntegerField()
    fruits = models.IntegerField()
    hoppy = models.IntegerField()
    spices = models.IntegerField()
    malty = models.IntegerField()
    main_class = models.IntegerField()
    subclass = models.IntegerField()
    class_subclass = models.CharField(max_length=10)
    beer_style = models.CharField(max_length=150)
    rating = models.FloatField()
    big_styles = models.CharField(max_length=150)
    beer_name = models.CharField(max_length=150)
    brewery = models.CharField(max_length=150)

    def __str__(self):
        return str(self.beer_name)