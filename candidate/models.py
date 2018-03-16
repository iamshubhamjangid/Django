# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class candidates(models.Model):
    c_name=models.CharField(max_length=250)
    c_aadhar=models.CharField(max_length=100,primary_key=True)
    c_id=models.CharField(max_length=100,unique=True)
    c_age=models.IntegerField()
    def __str__(self):
        return self.c_name
