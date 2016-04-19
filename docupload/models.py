from django.db import models

# Create your models here.

class Documentation(models.Model):
    name = models.CharField(max_length=200);
    doc_file = models.FilePathField('../static/docs/');
    pub_date = models.DateTimeField('date published');
