from django.db import models
import datetime

# Create your models here.

class Day(models.Model):
	today = models.DateField(default = datetime.date.today)
	firstItem = models.TextField(blank = False, null = True);
	secondItem = models.TextField(blank = False, null = True);
	thirdItem = models.TextField(blank = False, null = True);