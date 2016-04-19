from django import forms

class DocUploadForm(forms.Form):
    name = forms.CharField(max_length=100);
    doc_file = forms.FileField();
