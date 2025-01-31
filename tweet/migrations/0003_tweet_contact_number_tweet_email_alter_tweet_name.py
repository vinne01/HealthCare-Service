# Generated by Django 5.1 on 2025-01-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_remove_tweet_photo_remove_tweet_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='name',
            field=models.CharField(default='enter name', max_length=255),
        ),
    ]
