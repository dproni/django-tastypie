from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Entry(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
