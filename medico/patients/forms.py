from django import forms


class PatientIntakeForm(forms.Form):

    first_name = forms.CharField(max_length = 200)
    last_name =  forms.CharField(max_length=200)
    gender = forms.CharField(max_length=50)
    birth = forms.DateField()
    height = forms.IntegerField()
    weight = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    reason_for_consultation = forms.CharField(max_length=50)
    patient_medical_hostory = forms.CharField(max_length=50)
    list_operation =  forms.CharField(max_length=50)
    current_medication = forms.CharField(max_length=50)
    list_allergies = forms.CharField(max_length=200)
    health_unhealth = forms.CharField(max_length=300)
    exercises = forms.CharField(max_length=200)
    diet = forms.CharField(max_length=200)
    alcohol = forms.BooleanField(initial="False")
    caffiene = forms.BooleanField(initial="False")
    smoke = forms.BooleanField(initial="False")
    father = forms.CharField(max_length=30)
    mother = forms.CharField(max_length=30)
    grandfather = forms.CharField(max_length=50)
    grandmother = forms.CharField(max_length=50)
    brother = forms.CharField(max_length=50)
    sister = forms.CharField(max_length=50)
    uncle =  forms.CharField(max_length=50)
    aunts = forms.CharField(max_length=50)
    mental_health_symptoms = forms.BooleanField(initial="False")
    had_feeling_didnt_want_to_live = forms.BooleanField(initial="False")
    currently_feeling_didnt_live = forms.BooleanField(initial="False")
    how_often_negative_feeling = forms.CharField(max_length=24)
    recent_negative_thoughts = forms.CharField(max_length=100)
    mental_health_expert_recent = forms.BooleanField(initial="False")
    seek_any_help = forms.BooleanField(initial="False")
    question1 = forms.CharField(max_length=50)
    question2 = forms.CharField(max_length=50)
    question3 = forms.CharField(max_length=50)
    question4 = forms.CharField(max_length=50)
    question5 = forms.CharField(max_length=50)
    comments = forms.CharField(max_length=50)
    img1 = forms.ImageField()
    img = forms.ImageField()
