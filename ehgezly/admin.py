from django.contrib import admin
from ehgezly.models import Restaurant, Client, Table, Meals
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Client)
admin.site.register(Table)
admin.site.register(Meals)
