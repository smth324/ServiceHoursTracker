from django.contrib import admin
from .models import StudentProfile, OrgProfile, OAAProfile, Event, Participation

admin.site.register(StudentProfile)
admin.site.register(OrgProfile)
admin.site.register(OAAProfile)
admin.site.register(Event)
admin.site.register(Participation)
