import os

from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import DocUploadForm
from .htmlify import HTMLifier
from .models import Documentation

DOC_DIR = os.path.abspath(os.path.dirname(__name__)) + "/docupload/docs/"


def index(request):
    '''View for /doc/'''

    doc_list = Documentation.objects.all()
    template = loader.get_template('docupload/index.html')
    form = DocUploadForm()

    context = {
        'doc_list': doc_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def upload(request):
    '''View for /doc/upload/'''

    html = HTMLifier(doc_base_path=DOC_DIR)

    if request.method == 'POST':
        form = DocUploadForm(request.POST, request.FILES)
        if form.is_valid():
            filename = html.convert(request.FILES['doc_file'])
            doc = Documentation(name=request.POST['name'],
                                doc_file=filename,
                                pub_date=datetime.now())
            doc.save()
    return HttpResponseRedirect('/doc/')

def display(request, id):
    db_doc = Documentation.objects.filter(id=id)[0]

    print(db_doc)

    with open('docupload/docs/' + db_doc.doc_file) as doc:
        return HttpResponse(doc)

