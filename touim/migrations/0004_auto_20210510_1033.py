# Generated by Django 3.1.8 on 2021-05-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touim', '0003_rename_id_sites_id_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='id_site',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
