from django.contrib import admin
from .models import Student
from .models import Subject
from .models import Enrollments
#from .models import Professor

# Register your models here.

admin.site.register(Student)
#admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Enrollments)