# Generated by Django 4.1.7 on 2023-03-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("censor_app", "0002_alter_censor_options_alter_eksamen_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="censor",
            name="fag",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
