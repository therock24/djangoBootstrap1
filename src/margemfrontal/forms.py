from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=50)
    Country = forms.CharField(max_length=30)
    Subject = forms.CharField(max_length=100)
    Message = forms.CharField(max_length=500)

class OportunitiesForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=50)
    DistrictHome = forms.CharField(max_length=30)
    DistrictWork = forms.CharField(max_length=30)
    Preference = forms.CharField(max_length=30)
    Service = forms.CharField(max_length=30)
    Message = forms.CharField(max_length=500)
