from django import forms

from django.db import models

#forms without db associated

class FormName(forms.Form):
    # placeholder = 'Git Username'
    name = forms.CharField(initial='Git Username', required=True)


class FormStackOverflow(forms.Form):
    id = forms.CharField(initial='StackOverflow id', required=True)