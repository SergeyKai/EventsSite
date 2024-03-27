from django.contrib import admin

from . import models

admin.site.register(models.Event)
admin.site.register(models.Speaker)
admin.site.register(models.Location)
admin.site.register(models.Topic)
