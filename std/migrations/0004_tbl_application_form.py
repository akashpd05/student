# Generated by Django 5.1 on 2024-09-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0003_rename_years_of_experirnce_tbl_teachers_years_of_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_application_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('course', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('terms', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('select_course', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
