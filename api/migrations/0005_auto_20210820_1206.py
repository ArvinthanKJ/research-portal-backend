# Generated by Django 3.2.4 on 2021-08-20 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.AddField(
            model_name='project',
            name='aor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='api.areaofresearch'),
            preserve_default=False,
        ),
    ]
