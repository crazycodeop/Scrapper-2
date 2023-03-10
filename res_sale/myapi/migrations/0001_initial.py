# Generated by Django 4.1.4 on 2023-01-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Date_Posted', models.TextField()),
                ('Proptype', models.TextField(null=True)),
                ('Link', models.TextField()),
                ('Owner', models.TextField()),
                ('BHK', models.TextField()),
                ('Locality', models.TextField()),
                ('City', models.TextField()),
                ('Price', models.TextField()),
                ('Carpet_Area', models.TextField()),
                ('Furnishing', models.TextField()),
                ('Bathrooms', models.TextField()),
                ('Facing', models.TextField()),
                ('Status', models.TextField()),
                ('Transaction', models.TextField()),
                ('Price_Sqft', models.TextField()),
                ('Floor', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
