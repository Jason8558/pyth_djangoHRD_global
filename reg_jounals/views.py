from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    if request.user.is_authenticated:
        return render(request, 'reg_jounals/index.html')
    else: return render(request, 'reg_jounals/no_auth.html')
def outbound_docs(request):
    if request.user.is_authenticated:
        auth = request.user.is_authenticated
        documents = OutBoundDocument.objects.all()
        count = len(documents)
        method = str(request.method)
        usr = str(request.user.first_name)
        i = 0
        return render(request, 'reg_jounals/outbound_docs.html', context={'documents':documents, 'count':count, 'auth':auth, 'i':i})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OutBoundDocument(request):
    if request.method == "POST":
        doc_form = OutBoundDocument_form(request.POST)
        doc_form.doc_res_officer = str(request.user.first_name)
        if doc_form.is_valid():
            doc_form.doc_res_officer = str(request.user.first_name)
            doc_form.save()
    else:
        doc_form = OutBoundDocument_form()
    return render(request, 'reg_jounals/outboundDocs_add.html', {'form':doc_form})
