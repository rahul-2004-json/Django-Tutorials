from django import forms
from .models import ChaiVariety

"""
There are three cases of form:
1.When the form is rendering
2.When the form is just in display format or default case
3.When the form is submitted
"""
class ChaiVarietyForm(forms.Form):
    # below is chai variety field
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(),label="Select chai variety")