# Generated by Django 4.0.2 on 2022-02-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sort', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='identifier',
            field=models.CharField(choices=[('email', 'Email'), ('phone_number_sms', 'Phone')], max_length=200),
        ),
    ]