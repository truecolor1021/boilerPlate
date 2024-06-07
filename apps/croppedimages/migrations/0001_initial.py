# Generated by Django 4.0.6 on 2022-07-28 18:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrigImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_image', models.ImageField(upload_to='images', validators=[django.core.validators.validate_image_file_extension])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orig_images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CroppedImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cropped_images')),
                ('orig_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cropped_images', to='croppedimages.origimagefile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cropped_images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]