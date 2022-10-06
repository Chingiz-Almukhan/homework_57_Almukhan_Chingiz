from django.contrib import admin

from tracker.models import IssueTracker, Type, Status

# Register your models here.
admin.site.register(IssueTracker)
admin.site.register(Type)
admin.site.register(Status)

