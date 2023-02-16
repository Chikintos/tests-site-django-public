from sqlite3 import adapt
from django.contrib import admin
from .models import *

admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(Variants)
