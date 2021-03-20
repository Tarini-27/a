from django.contrib import admin
from .models import Logical,Verbal,Test,Result

admin.site.register(Logical)
admin.site.register(Verbal)
admin.site.register(Test)
admin.site.register(Result)