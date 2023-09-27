from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Worker

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass



