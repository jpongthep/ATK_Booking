# Generated by Django 3.2.6 on 2021-08-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserve', '0006_alter_atk_queue_atk_lot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_atk',
            name='PID',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='เลขบัตรประชาชน'),
        ),
    ]
