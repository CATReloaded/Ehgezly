# Generated by Django 2.2 on 2019-06-26 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('order', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('number_of_chairs', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holidays', models.CharField(choices=[('Sat', 'Saturday'), ('Sun', 'Sunday'), ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday')], max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('tables', models.PositiveIntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('take_away', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
                ('open_at', models.TimeField()),
                ('close_at', models.TimeField()),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Meal')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Table')),
            ],
        ),
    ]