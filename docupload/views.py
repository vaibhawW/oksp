from django.http import HttpResponse
from django.template import loader

from .models import Documentation
from .forms import DocUploadForm

def index(request):
    doc_list = Documentation.objects.all()
    template = loader.get_template('docupload/index.html')
    form = DocUploadForm()

    context = {
        'doc_list': doc_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def upload(request):

    pass
