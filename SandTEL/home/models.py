from django.db import models
#makemigrations= create change and store in file
#migrate=  apply the pending changes created by makemigration
# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=40 )
   email = models.CharField(max_length=30)
   phone = models.CharField(max_length=10)
   desc = models.TextField()
   date = models.DateField()

   def __str__(self):
      return self.name

       
