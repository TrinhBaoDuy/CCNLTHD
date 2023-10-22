# Generated by Django 4.2.6 on 2023-10-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngaytao', models.DateField(auto_now_add=True, null=True)),
                ('ngaysua', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('monhoc', models.CharField(max_length=255)),
                ('mota', models.TextField()),
                ('hinhanh', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='ngaysua',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='ngaytao',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]