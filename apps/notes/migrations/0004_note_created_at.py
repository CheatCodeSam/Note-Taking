# Generated by Django 4.0.4 on 2022-04-20 02:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_note_comment_alter_note_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
