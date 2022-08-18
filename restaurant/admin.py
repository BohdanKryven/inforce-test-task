from django.contrib import admin

from restaurant.models import Restaurant, Vote

admin.site.register(Restaurant)
admin.site.register(Vote)
