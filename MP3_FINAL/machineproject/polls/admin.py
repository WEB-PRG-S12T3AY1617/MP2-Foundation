from django.contrib import admin

from . models import Users

admin.site.register(Users)

from . models import Degree

admin.site.register(Degree)

from . models import Office

admin.site.register(Office)

