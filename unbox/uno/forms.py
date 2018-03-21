from uno.models import Question_m
from django import forms

Profession = (
    ('Student','Student'),
    ('Job','Job'),
    ('Business','Business'),
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

class Question_f(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender,help_text="Gender")
    profession = forms.ChoiceField(choices=Profession, help_text="Profession")
    location = forms.ChoiceField(choices=Location, help_text="Where do you live ?")
    budget = forms.IntegerField(min_value=5000, help_text="Budget in INR", required = True, widget=forms.Textarea(attrs={'rows':'1','width': '100%'}))
    majoruse = forms.MultipleChoiceField(choices=Major_use, help_text="What is your main requirement ?", widget=forms.CheckboxSelectMultiple)
    prefer_to_chinese = forms.ChoiceField(choices=Assertion, help_text="Will you prefer chinese brand for better specification at low price ?")
    size = forms.ChoiceField(choices=Assertion, help_text="Will you prefer small and compact phones ?")

    class Meta:
        model = Question_m
        fields = ['profession', 'gender', 'budget', 'location', 'prefer_to_chinese','majoruse', 'size']
