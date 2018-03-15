# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class voters(models.Model):
    v_name=models.CharField(max_length=250)
    v_aadhar=models.CharField(max_length=100,primary_key=True)
    v_id=models.CharField(max_length=100,primary_key=True)
    v_age=models.IntegerField()
    def __str__(self):
        return self.v_name

