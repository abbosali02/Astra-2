# Generated by Django 4.0.6 on 2022-11-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('age', models.CharField(max_length=100, verbose_name='Age')),
                ('residence', models.CharField(max_length=300, verbose_name='Place of Residence')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('education', models.CharField(max_length=300, verbose_name='Education Status')),
                ('university', models.CharField(max_length=300, verbose_name='University Major')),
                ('ielts', models.CharField(max_length=300, verbose_name='IELTS BAND Score')),
                ('other', models.CharField(max_length=300, verbose_name='Other Achievements')),
                ('job1', models.CharField(max_length=300, verbose_name='Employer#1')),
                ('job2', models.CharField(max_length=300, verbose_name='Employer#2')),
                ('languages', models.CharField(max_length=300, verbose_name='Other Languages')),
                ('telegram', models.CharField(max_length=300, verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'Apply Us',
                'verbose_name_plural': 'Apply Us',
            },
        ),
        migrations.CreateModel(
            name='contactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('last', models.CharField(max_length=300, verbose_name='Last')),
                ('age', models.CharField(max_length=100, verbose_name='Age')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telegram', models.CharField(max_length=300, verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Eight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=10000, verbose_name='Title')),
                ('desciption', models.CharField(max_length=10000, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=10000, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=10000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=10000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'eight',
                'verbose_name_plural': 'eight',
            },
        ),
        migrations.CreateModel(
            name='EightHalf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=10000, verbose_name='Title')),
                ('desciption', models.CharField(max_length=10000, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=10000, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=10000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=10000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'EightHalf',
                'verbose_name_plural': 'EightHalf',
            },
        ),
        migrations.CreateModel(
            name='FirstTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('little', models.CharField(max_length=300, verbose_name='Position')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=300, verbose_name='Name')),
                ('desciption', models.CharField(max_length=500, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=1000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'MukhammadAli',
                'verbose_name_plural': 'MukhammadAli',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('seven', models.CharField(max_length=300, verbose_name='seven')),
                ('sevenhalf', models.CharField(max_length=300, verbose_name='sevenhalf')),
                ('eight', models.CharField(max_length=300, verbose_name='eight')),
                ('eighthalf', models.CharField(max_length=300, verbose_name='eighthalf')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Result',
            },
        ),
        migrations.CreateModel(
            name='SecondTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('little', models.CharField(max_length=300, verbose_name='Position')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=300, verbose_name='Name')),
                ('desciption', models.CharField(max_length=500, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=1000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'Alisher',
                'verbose_name_plural': 'Alisher',
            },
        ),
        migrations.CreateModel(
            name='Seven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=10000, verbose_name='Title')),
                ('desciption', models.CharField(max_length=10000, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=10000, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=10000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=10000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'Seven',
                'verbose_name_plural': 'Seven',
            },
        ),
        migrations.CreateModel(
            name='SevenHalf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=10000, verbose_name='Title')),
                ('desciption', models.CharField(max_length=10000, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=10000, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=10000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=10000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'SevenHalf',
                'verbose_name_plural': 'SevenHalf',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='unique number')),
                ('img', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=300, verbose_name='Name')),
                ('desciption', models.CharField(max_length=500, verbose_name='Description')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Subtitle')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('img3', models.ImageField(db_index=True, upload_to='', verbose_name='Image')),
                ('headtitle', models.CharField(max_length=1000, verbose_name='Headtitle')),
            ],
            options={
                'verbose_name': 'Team Members',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]
