# Generated by Django 5.0.2 on 2024-03-19 07:08

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Olsi_App', '0018_location_state_trainer_trainer_type_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer_type',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=True, populate_from='name'),
        ),
    ]
