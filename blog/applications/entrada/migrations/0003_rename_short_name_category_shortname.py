# Generated by Django 4.0.1 on 2022-01-20 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0002_alter_category_id_alter_category_short_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='short_name',
            new_name='shortname',
        ),
    ]
