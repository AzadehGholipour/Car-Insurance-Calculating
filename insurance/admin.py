from django.contrib import admin
from .models import User, Car, Insurance, Post

# Register your models here.

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Insurance)
admin.site.register(Post)