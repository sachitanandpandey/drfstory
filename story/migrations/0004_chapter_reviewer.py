# Generated by Django 4.0.4 on 2022-05-26 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('story', '0003_story_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chp_reviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]
