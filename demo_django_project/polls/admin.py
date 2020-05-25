from django.contrib import admin
from .models import Poll, PollResult

# Register your models here.
admin.site.register(Poll)
admin.site.register(PollResult)