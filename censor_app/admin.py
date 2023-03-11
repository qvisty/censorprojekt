from django.contrib import admin
from .models import Skole, Lærer, Eksamen, Censor, EksamensCensor, Skoleklasse

admin.site.register(Skole)
admin.site.register(Lærer)
admin.site.register(Eksamen)
admin.site.register(Censor)
admin.site.register(EksamensCensor)
admin.site.register(Skoleklasse)
