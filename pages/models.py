from django.db import models

Years_in_school = [("FR","Fresh"),("JR","Junior"),("SR", "Senior")]

class Musician(models.Model):
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  instrument = models.CharField(max_length=20)
  artist_name = models.CharField(max_length=20)
  level = models.CharField(max_length=20, choices=Years_in_school,)

  def __str__(self) -> str:
    return self.artist_name

class Album(models.Model):
  artist=models.ForeignKey(Musician, on_delete=models.CASCADE)
  name= models.CharField(max_length=20)
  release_date = models.DateField()
  num_star = models.IntegerField

  def __str__(self) -> str:
    return self.name
