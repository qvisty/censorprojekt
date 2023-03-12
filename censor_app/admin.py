from django.contrib import admin
from .models import Skole, Lærer, Eksamen, Censor, Skoleklasse


class LærerAdmin(admin.ModelAdmin):
    list_display = ("navn", "email", "skole")


class SkoleAdmin(admin.ModelAdmin):
    list_display = ("navn", "adresse")


class CensorAdmin(admin.ModelAdmin):
    list_display = ("navn", "fag", "skole", "email")


class SkoleklasseAdmin(admin.ModelAdmin):
    list_display = ("navn", "skole")


class EksamenAdmin(admin.ModelAdmin):
    list_display = ("navn", "dato", "skoleklasse", "lærer", "censor")


admin.site.register(Lærer, LærerAdmin)
admin.site.register(Skole, SkoleAdmin)
admin.site.register(Censor, CensorAdmin)
admin.site.register(Skoleklasse, SkoleklasseAdmin)
admin.site.register(Eksamen, EksamenAdmin)
