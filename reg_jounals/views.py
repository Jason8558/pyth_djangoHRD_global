from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator



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
        if doc_form.is_valid():
            user_ = request.user.first_name

            doc_form.doc_res_officer = user_
            print(str(doc_form.doc_res_officer))
            doc_form.save(user_)
            return redirect('../outbound_docs/')
    else:
        doc_form = OutBoundDocument_form()
    return render(request, 'reg_jounals/outboundDocs_add.html', {'form':doc_form})

def letter_of_resignation(request):
    if request.user.is_authenticated:
        letters = LetterOfResignation.objects.all()
        count = len(letters)
        p_letters = Paginator(letters, 10)
        page_number = request.GET.get('page', 1)
        page = p_letters.get_page(page_number)

        return render(request, 'reg_jounals/letters_of_resignation.html', context={'letters':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')


def nr_LetterOfResignation(request):
    if request.user.is_authenticated:
        letter_form = LetterOfResignation_form()
        if request.method == "POST":
            letter_form = LetterOfResignation_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_)
                return redirect('../letters_of_resignation/')


    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/LetterOfResignation_add.html', context={'form':letter_form})

def upd_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            letter = LetterOfResignation.objects.get(id__iexact=id)
            bound_form = LetterOfResignation_form(instance=letter)
            return render(request, 'reg_jounals/LetterOfResignation_upd.html', context={'form':bound_form, 'letter':letter})
        else:
            letter = LetterOfResignation.objects.get(id__iexact=id)
            bound_form = LetterOfResignation_form(request.POST, instance=letter)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/letters_of_resignation')

def del_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        letter = LetterOfResignation.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/journals/letters_of_resignation')




def letter_of_invite(request):
        if request.user.is_authenticated:
            letters = LetterOfInvite.objects.all()
            count = len(letters)
            return render(request, 'reg_jounals/letters_of_invite.html', context={'letters':letters, 'count':count})
        else:
            return render(request, 'reg_jounals/no_auth.html')

def nr_LetterOfInvite(request):
    if request.user.is_authenticated:
        letter_form = LetterOfInvite_form()
        if request.method == 'POST':
            letter_form = LetterOfInvite_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.save(user_)
                return redirect('../letters_of_invite/')
        return render(request, 'reg_jounals/LetterOfInvite_add.html', context={'form':letter_form})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def order_other_matters(request):
    if request.user.is_authenticated:
        orders = OrdersOnOtherMatters.objects.all()
        count = len(orders)
        return render(request, 'reg_jounals/orders_on_others.html', context={'orders':orders, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOnOtherMatters(request):
    if request.user.is_authenticated:
        order_form = OrdersOnOtherMatters_form()
        if request.method == "POST":
            order_form =OrdersOnOtherMatters_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_others/')


            else:
                return render(request, 'reg_jounals/no_auth.html')
        return render(request, 'reg_jounals/OrdersOnOtherMatters_add.html', context={'form':order_form})
