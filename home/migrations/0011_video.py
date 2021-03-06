# Generated by Django 3.0.3 on 2020-07-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0010_auto_20200703_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('img', models.ImageField(upload_to='home/thumbnails/')),
                ('data', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
    ]
