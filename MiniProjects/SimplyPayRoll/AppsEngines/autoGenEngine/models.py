from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField
class Author(models.Model):
  name = models.CharField(max_length=100,null=False)
  reg = models.IntegerField(default=None,null=True,blank=True)
  date = models.DateTimeField(auto_now=True,default=datetime.now())
  history = DictField(default={'house_rent':0,'food':0,'traval':0},null=True,blank=True)
  tags = ListField(default=[1,2,3],null=True,blank=True)



class Publication(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Book(models.Model):
  name = models.CharField(max_length=100,null=False)
  author = models.ManyToManyField(to=Author)
  publications = models.ForeignKey(to=Publication)


