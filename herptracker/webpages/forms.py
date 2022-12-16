from django import forms

class HerpForm(forms.Form):
    species = forms.CharField(label="Species:", max_length=50)
    sex = forms.CharField(label="Sex:", max_length=1)
    svl = forms.IntegerField(label="SVL:")
    tail = forms.IntegerField(label="Tail:")
    tibia = forms.IntegerField(label="Tibia:")
    notes = forms.CharField(label="Notes:", widget=forms.Textarea)

class ObservationForm(forms.Form):
    herp = forms.IntegerField(label="Herp ID:")
    trapType = forms.CharField(label="Trap Type:", max_length=30)
    latitute = forms.DecimalField(label="Latitute:", max_digits=9, decimal_places=6)
    longitude = forms.DecimalField(label="Longitude:", max_digits=9, decimal_places=6)
    timeSet = forms.DateTimeField(label="Time Trap was Set:")
    timeChecked = forms.DateTimeField(label="Time Trap was Checked:")