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
  

class Author(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  occupation = models.CharField(max_length=1000)

  def __str__(self) -> str:
    return self.first_name
  
  def __str__(self) -> str:
    return self.last_name
  
  def __str__(self) -> str:
    return self.occupation


list_of_field = [("S","SPORT"),("M","MUSIC"),("H","HEALTH"),("F","FITNESS"),("E","EDUCATION")]


class Article(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  released_date =models.DateField()
  category = models.CharField(max_length=20, choices=list_of_field)
  topic =  models.CharField(max_length=1000)
  body = models.TextField()

  def __str__(self) -> str:
    return self.topic
  
  def __str__(self) -> str:
    return self.released_date
  
  def __str__(self) -> str:
    return self.category
  
  def __str__(self) -> str:
    return self.body
  

  