# Generated by Django 2.1 on 2018-08-21 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_auto_20180819_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(help_text='Image that will be shown on the category preview.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='image.Image'),
        ),
    ]
