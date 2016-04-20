from django import forms


class DocUploadForm(forms.Form):
    '''Form for documentation file upload'''

    name = forms.CharField(max_length=100)
    doc_file = forms.FileField()
