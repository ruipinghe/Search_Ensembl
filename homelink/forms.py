from django import forms



DBTYPE_CHOICES = (('core', 'core'), ('funcgen', 'funcgen'), ('otherfeatures', 'otherfeatures'),('rnaseq', 'rnaseq'),('variation','variation'),('cdna','cdna'),('vega','vega'))



class HouseChoiceForm(forms.Form):
    dbname = forms.CharField(label='Specie', max_length=50)
    release = forms.IntegerField(label='Release')
    dbtype = forms.CharField(label="Type", widget=forms.RadioSelect(choices=DBTYPE_CHOICES), required=False)




