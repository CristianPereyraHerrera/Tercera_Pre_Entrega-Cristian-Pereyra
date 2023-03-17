# Generated by Django 4.1.7 on 2023-03-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEdukate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('commission', models.IntegerField(unique=True)),
                ('delivery_date', models.DateField()),
                ('delivered', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]