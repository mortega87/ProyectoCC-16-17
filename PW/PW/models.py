
# Create your models here.
# *- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.core.validators import RegexValidator
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.core.files import File

class DiscoGenerator(models.Model):
	artista = models.CharField(max_length=40)
	titulo = models.CharField(max_length=40)
	estilo = models.CharField(max_length=13)
	portada = models.FileField(blank=True, upload_to='/')
