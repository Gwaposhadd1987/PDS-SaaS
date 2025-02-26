from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> primary key -> auto field 1,2,3
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)