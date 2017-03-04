from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.StringField(max_length=30)
	school = models.StringField(max_length=30)
	classroom = models.StringField(max_length=30)

class Activity(models.Model):
	day = models.Date()
	dinner = models.SmallInt()
	transport = models.SmallInt()
	player = models.ForeignKey(Player)
