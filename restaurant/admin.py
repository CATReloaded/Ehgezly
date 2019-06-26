from django.contrib import admin
from restaurant.models import Client, Restaurant, Table, Meal

# Register your models here.
admin.site.register(Client)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Meal)
