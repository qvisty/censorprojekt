from django.contrib import admin
from .models import School, Teacher, Exam, Censor, ExamCensor, MissingData, SchoolClass

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Exam)
admin.site.register(Censor)
admin.site.register(ExamCensor)
admin.site.register(MissingData)
admin.site.register(SchoolClass)
