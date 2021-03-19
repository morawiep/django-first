from django.contrib import admin
from .models import Klub, Liga, Piłkarz, Agent

# Register your models here.
admin.site.register(Klub)
admin.site.register(Liga)
admin.site.register(Piłkarz)
admin.site.register(Agent)