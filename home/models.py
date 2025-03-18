# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    steps = models.CharField(max_length=255, null=True, blank=True)
    iso clause = models.CharField(max_length=255, null=True, blank=True)
    annex control = models.CharField(max_length=255, null=True, blank=True)
    progress = models.CharField(max_length=255, null=True, blank=True)
    responsible = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Isms(models.Model):

    #__Isms_FIELDS__
    instructions = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Isms_FIELDS__END

    class Meta:
        verbose_name        = _("Isms")
        verbose_name_plural = _("Isms")



#__MODELS__END
