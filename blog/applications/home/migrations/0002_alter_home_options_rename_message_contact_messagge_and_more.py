# Generated by Django 4.0.1 on 2022-01-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Pagina Principal', 'verbose_name_plural': 'Pagina Principal'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='messagge',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='home',
            name='about_title',
            field=models.CharField(max_length=50, verbose_name='Titulo Nosotros'),
        ),
    ]
