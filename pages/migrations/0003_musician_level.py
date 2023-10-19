# Generated by Django 4.2.6 on 2023-10-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_album_musician_delete_person_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='level',
            field=models.CharField(choices=[('FR', 'Fresh'), ('JR', 'Junior'), ('SR', 'Senior')], default='Fresh man', max_length=20),
            preserve_default=False,
        ),
    ]