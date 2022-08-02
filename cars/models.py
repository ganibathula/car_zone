from django.db import models
from datetime import datetime
# Create your models here.
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
class car_model(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    car_title=models.CharField(max_length=300)
    city=models.CharField(max_length=400)
    state=models.CharField(max_length=400)
    color=models.CharField(max_length=300)
    model=models.CharField(max_length=300)
    year=models.IntegerField(('year'),choices=year_choice)
    condition=models.CharField(max_length=300)
    price=models.IntegerField()
    description=RichTextField(max_length=400)
    car_photo=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    car_photo1=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    car_photo2=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    car_photo3=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    car_photo4=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    features=MultiSelectField(max_length=300,choices=features_choices)
    body_style=models.CharField(max_length=300)
    engine=models.CharField(max_length=300)
    transmission=models.CharField(max_length=300)
    interior=models.CharField(max_length=300)
    miles=models.IntegerField()
    door=models.CharField(max_length=300,choices=door_choices)
    passenger=models.IntegerField()
    vin_no=models.CharField(max_length=300)
    mileage=models.IntegerField()
    fuel_type=models.CharField(max_length=300)
    no_of_owners=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now(),blank=True)



    def __str__(self):
        return self.car_title





