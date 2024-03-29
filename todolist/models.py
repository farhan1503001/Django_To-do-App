from django.db import models
import datetime

# Create your models here.
class List(models.Model):
    item=models.CharField(max_length=200)
    date=models.DateField(('Date'),default=datetime.date.today)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.item+" || "+str(self.date)+" || "+str(self.completed)