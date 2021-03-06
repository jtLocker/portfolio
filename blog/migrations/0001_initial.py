# Generated by Django 2.2.5 on 2019-09-29 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Test')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('body', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
