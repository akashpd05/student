# Generated by Django 5.1 on 2024-09-10 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0005_alter_tbl_application_form_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_application_form',
            name='select_course',
        ),
    ]
