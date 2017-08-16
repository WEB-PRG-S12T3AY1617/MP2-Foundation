from django.contrib import admin
from .models import Course
admin.site.register(Course)
from .models import Item
admin.site.register(Item)
from .models import Tag
admin.site.register(Tag)
from .models import Offer
admin.site.register(Offer)
# Register your models here.
