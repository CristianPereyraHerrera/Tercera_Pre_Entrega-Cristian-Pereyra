# Generated by Django 4.1.7 on 2023-03-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEdukate', '0002_deliverables_delete_delivery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deliverables',
            new_name='Deliverable',
        ),
    ]