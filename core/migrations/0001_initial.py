# Generated by Django 3.2.4 on 2022-05-05 03:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_about_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_about_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_about_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mission_description', models.TextField(max_length=3000)),
                ('mission_description_az', models.TextField(max_length=3000, null=True)),
                ('mission_description_en', models.TextField(max_length=3000, null=True)),
                ('mission_description_ru', models.TextField(max_length=3000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Haqqımızda',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='Xəzər rayonu, Binə Sovxoz Sahəsi', max_length=200)),
                ('address_az', models.CharField(default='Xəzər rayonu, Binə Sovxoz Sahəsi', max_length=200, null=True)),
                ('address_en', models.CharField(default='Xəzər rayonu, Binə Sovxoz Sahəsi', max_length=200, null=True)),
                ('address_ru', models.CharField(default='Xəzər rayonu, Binə Sovxoz Sahəsi', max_length=200, null=True)),
                ('phone_number', models.CharField(default='+994 51 201 85 70', max_length=200)),
                ('email', models.EmailField(blank=True, default='INFO@BUTACONSTRUCTION.COM', max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_az', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Vakansiyalar',
            },
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sertificate_image', models.FileField(blank=True, null=True, upload_to='media')),
                ('name', models.CharField(max_length=200)),
                ('name_az', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('pdfile', models.FileField(blank=True, null=True, upload_to='pdf')),
            ],
            options={
                'verbose_name_plural': 'Sertifikatlar',
            },
        ),
        migrations.CreateModel(
            name='ConditionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('name_az', models.CharField(blank=True, max_length=50, null=True)),
                ('name_en', models.CharField(blank=True, max_length=50, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=120)),
                ('message', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Əlaqə',
            },
        ),
        migrations.CreateModel(
            name='Innovations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_az', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=4000)),
                ('description_az', models.TextField(max_length=4000, null=True)),
                ('description_en', models.TextField(max_length=4000, null=True)),
                ('description_ru', models.TextField(max_length=4000, null=True)),
                ('news_image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Yenilikler',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Tərəfdaşlarımız',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('name_az', models.CharField(blank=True, max_length=120, null=True)),
                ('name_en', models.CharField(blank=True, max_length=120, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Project Categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon_image', models.FileField(upload_to='media')),
                ('name', models.CharField(max_length=200)),
                ('name_az', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('title_az', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('service_content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('service_content_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('service_content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('service_content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('service_content_image', models.ImageField(default='JPG', upload_to='media')),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('service_head_image', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Xidmətlər',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('title_az', models.CharField(blank=True, max_length=120, null=True)),
                ('title_en', models.CharField(blank=True, max_length=120, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_az', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.FileField(blank=True, default='JPG', null=True, upload_to='media')),
                ('service', models.ManyToManyField(blank=True, db_index=True, default=None, related_name='service_title', to='core.Service')),
            ],
            options={
                'verbose_name_plural': 'Xidmət Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_az', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=3000)),
                ('description_az', models.TextField(max_length=3000, null=True)),
                ('description_en', models.TextField(max_length=3000, null=True)),
                ('description_ru', models.TextField(max_length=3000, null=True)),
                ('condition', models.CharField(max_length=100)),
                ('condition_az', models.CharField(max_length=100, null=True)),
                ('condition_en', models.CharField(max_length=100, null=True)),
                ('condition_ru', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=100)),
                ('area_az', models.CharField(max_length=100, null=True)),
                ('area_en', models.CharField(max_length=100, null=True)),
                ('area_ru', models.CharField(max_length=100, null=True)),
                ('place', models.CharField(max_length=100)),
                ('place_az', models.CharField(max_length=100, null=True)),
                ('place_en', models.CharField(max_length=100, null=True)),
                ('place_ru', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('type_az', models.CharField(max_length=100, null=True)),
                ('type_en', models.CharField(max_length=100, null=True)),
                ('type_ru', models.CharField(max_length=100, null=True)),
                ('term', models.CharField(max_length=100)),
                ('term_az', models.CharField(max_length=100, null=True)),
                ('term_en', models.CharField(max_length=100, null=True)),
                ('term_ru', models.CharField(max_length=100, null=True)),
                ('customer', models.CharField(max_length=100)),
                ('project_image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='Slug')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_categories', to='core.projectcategory')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition_categories', to='core.conditioncategory')),
            ],
            options={
                'verbose_name_plural': 'Layihələr',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('projects_images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_images', to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='CareerCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=120)),
                ('cv', models.FileField(upload_to='career/cvler/')),
                ('career', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='careers', to='core.career')),
            ],
        ),
    ]
