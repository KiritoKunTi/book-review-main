# Generated by Django 4.0.3 on 2022-05-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_info', models.TextField()),
                ('cat_image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]