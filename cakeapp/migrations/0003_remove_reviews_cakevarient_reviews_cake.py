# Generated by Django 4.2.5 on 2023-11-09 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0002_alter_reviews_cakevarient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='cakevarient',
        ),
        migrations.AddField(
            model_name='reviews',
            name='cake',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakeapp.cakes'),
        ),
    ]
