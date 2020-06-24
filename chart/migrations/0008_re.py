import csv
import os
from django.db import migrations
from django.conf import settings

##Date,Australia,China,Japan,"Korea, South",Malaysia
# Date,Country,Confirmed,Recovered,Deaths
Date = 0
Australia = 1
China = 2
Japan = 3
Korea_South =  4
Malaysia = 5

def add_Recoverer(apps, schema_editor):
    Recoverer = apps.get_model('chart', 'Covid19_re')
    csv_file = os.path.join(settings.BASE_DIR, 'Recovered.csv')
    with open(csv_file) as dataset:
        reader = csv.reader(dataset)
        next(reader)
        for entry in reader:
            Recoverer.objects.create(
                Date=entry[Date],
                Australia=entry[Australia],
                China=entry[China],
                Japan=entry[Japan],
                Korea_South=entry[Korea_South],
                Malaysia=entry[Malaysia]
            )

class Migration(migrations.Migration):
    dependencies = [                            # 선행 관계
        ('chart', '0007_covid19_re'),
    ]
    operations = [                              # 작업
        migrations.RunPython(add_Recoverer),
    ]