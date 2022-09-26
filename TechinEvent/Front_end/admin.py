from django.contrib import admin

from .models import  Event, Speaker, Program, Venue, Logo, Sponsor, Galary, Summary

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Program)
admin.site.register(Venue)
admin.site.register(Logo)
admin.site.register(Sponsor)
admin.site.register(Galary)
admin.site.register(Summary)

