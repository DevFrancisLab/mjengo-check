from django.contrib import admin

# Register your models here.
from .models import Site, Worker, CheckInLog, IncidentReport

admin.site.register(Site)
admin.site.register(Worker)
admin.site.register(CheckInLog)
admin.site.register(IncidentReport)
