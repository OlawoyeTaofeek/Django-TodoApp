from django.contrib import admin
from .models import Task
# Register your models here.

#to import all apps
# use from .models import *

admin.site.register(Task)