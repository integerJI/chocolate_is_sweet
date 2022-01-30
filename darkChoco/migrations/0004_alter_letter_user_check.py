# Generated by Django 4.0.1 on 2022-01-30 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('darkChoco', '0003_letter_user_check_alter_letter_from_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='user_check',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
