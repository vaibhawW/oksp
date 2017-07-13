from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class Documentation(models.Model):
    '''
    Documentation: Model class which holds details of uploaded documentation file
    '''

    name = models.CharField(max_length=200)
    description=models.TextField(default="")
    doc_file = models.FileField(upload_to = '%s/media/' %settings.BASE_DIR[1:])
    pub_date = models.DateTimeField('date published')
    extension = models.CharField(max_length=20, default='docx')
    tags = TaggableManager()

    def __str__(self):
        return self.name
