# Generated by Django 2.0 on 2017-12-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20171225_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_host_model',
            name='select_vm_profile',
            field=models.CharField(choices=[('bn', 'bn')], default=None, max_length=10),
        ),
    ]