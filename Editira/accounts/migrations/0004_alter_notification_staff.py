# Generated by Django 3.2.9 on 2021-12-13 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211213_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.staff'),
        ),
    ]