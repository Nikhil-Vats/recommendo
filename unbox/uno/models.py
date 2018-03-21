from django.db import models
import datetime

Profession = (
    ('Student','Student'),
    ('Job','Job'),
    ('Business','Buisness'),
    ('Elderly Person','Elderly Person'),
)

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

Location = (
    ('Urban','Urban'),
    ('Rural','Rural'),
)

Assertion = (
    ('Yes','Yes'),
    ('No','No'),
)

Major_use = (
    ('Calling','Calling'),
    ('Photography','Photography'),
    ('Gaming','Gaming'),
    ('Social Media','Social Media'),
    ('Videos & Movies','Videos & Movies'),
    )

class Question_m(models.Model):
    profession = models.CharField(max_length=100, choices=Profession, default='Student')
    gender = models.CharField(max_length=100, choices=Gender, default='Male')
    budget = models.CharField(max_length=100, default='5000')
    location = models.CharField(max_length=100, choices=Location, default='Urban')
    prefer_to_chinese = models.CharField(max_length=100, choices=Assertion, default='No')
    #majoruse = models.CharField(max_length=100, choices=Major_use, default=['Calling'])
    size = models.CharField(max_length=100, choices=Assertion, default='No')

    class Meta:
      verbose_name_plural = 'Questions'

    def __str__(self):
      return self.item
