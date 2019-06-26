from django.db import models

# Create your models here.

days = (
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
)


class Meals(models.Model):
    content = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Table(models.Model):
    position = models.CharField(max_length=50)
    number_of_chairs = models.PositiveIntegerField()

    def __str__(self):
        return self.position


class Restaurant(models.Model):
    holidays = models.CharField(max_length=15, choices=days)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    tables = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    take_away = models.BooleanField()
    image = models.ImageField()
    open_at = models.TimeField()
    close_at = models.TimeField()

    # relations
    menu = models.OneToOneField(Meals, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, null=False)
    order = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name
