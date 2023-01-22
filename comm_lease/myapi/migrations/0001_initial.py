# Generated by Django 4.1.4 on 2023-01-22 10:56

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
                ('Retailer', models.TextField()),
                ('BHK', models.TextField()),
                ('Locality', models.TextField()),
                ('City', models.TextField()),
                ('Price', models.TextField()),
                ('Carpet_Area', models.TextField()),
                ('Washroom', models.TextField()),
                ('Facing', models.TextField()),
                ('Pantry', models.TextField()),
                ('Parking', models.TextField()),
                ('Water_Availability', models.TextField()),
                ('Price_Sqft', models.TextField()),
                ('Property_Age', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
