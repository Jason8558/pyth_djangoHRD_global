from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm



class LetterOfResignation_form(forms.ModelForm):
    class Meta:
        model = LetterOfResignation
        fields = ['id', 'lor_date',
    'lor_employee',
    'lor_position',
    'lor_departament',
    'lor_dateOfRes',
    'lor_additionalData']





    def saveFirst(self, user_):
        new_letter = LetterOfResignation.objects.create(
        lor_date = self.cleaned_data['lor_date'],
        lor_employee = self.cleaned_data['lor_employee'],
        lor_position = self.cleaned_data['lor_position'],
        lor_departament = self.cleaned_data['lor_departament'],
        lor_dateOfRes = self.cleaned_data['lor_dateOfRes'],
        lor_additionalData = self.cleaned_data['lor_additionalData'],
        lor_res_officer = user_
        )

        return new_letter




# class  LetterOfResignation_form(forms.Form):
#     lor_date = forms.DateField(label='Дата поступления заявления', help_text="Введите дату поступления заявления", input_formats=['%d.%M.%Y'])
#
#     lor_employee =  forms.CharField(label='Увольняемый сотрудник',max_length=100, help_text="Введите ФИО увольняемого сотрудника")
#
#     lor_position = forms.CharField(max_length=256, help_text="Введите должность увольняемого сотрудника", label="Должность")
#
#     lor_departament = forms.CharField(max_length=256, help_text="Введите подразделение увольняемого сотрудника", label="Подразделение")
#
#     lor_dateOfRes = forms.DateField(label='Дата увольнения', help_text="Введите дату увольнения сотрудника", input_formats=['%d.%M.%Y'])
#
#     class Meta:
#         model = LetterOfResignation
#         fields = ['id', 'lor_date',
# 'lor_employee',
# 'lor_position',
# 'lor_departament',
# 'lor_dateOfRes',
# 'lor_res_officer' ]
#
#     def save(self, user_):
#         new_letter = LetterOfResignation.objects.create(
#         lor_date = self.cleaned_data['lor_date'],
#         lor_employee = self.cleaned_data['lor_employee'],
#         lor_position = self.cleaned_data['lor_position'],
#         lor_departament = self.cleaned_data['lor_departament'],
#         lor_dateOfRes = self.cleaned_data['lor_dateOfRes'],
#         lor_res_officer = user_
#         )
#
#         return new_letter

class OutBoundDocument_form(forms.Form):
    doc_type = forms.CharField(label='Вид документа',max_length=100, help_text="Введите вид документа (письмо, справка, и.т.д)")
    doc_date = forms.DateField(label='Дата документа',help_text="Введите дату документа", input_formats=['%d.%M.%Y'])
    doc_dest = forms.CharField(label='Адресат',max_length=256, help_text="Введите адресата")
    doc_additionalData = forms.CharField(label='Содержание', help_text="Введите содержание",widget=forms.Textarea)


    def save(self, user_):
        new_document = OutBoundDocument.objects.create(
            doc_type = self.cleaned_data['doc_type'],
            doc_date = self.cleaned_data['doc_date'],
            doc_dest = self.cleaned_data['doc_dest'],
            doc_additionalData = self.cleaned_data['doc_additionalData'],
            doc_res_officer = user_
)

        return new_document

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'lform-input', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'lform-input',
            'placeholder': '',
            'id': 'hi',
        }
))

class LetterOfInvite_form(forms.Form):
    loi_date = forms.DateField(label='Дата поступления заявления',help_text="Введите дату поступления заявления", input_formats=['%d.%M.%Y'])
    loi_employee = forms.CharField(label='ФИО принимаемого',max_length=256, help_text="Введите ФИО принимаемого сотрудника")
    loi_position = forms.CharField(label='Должность принимаемого',max_length=256, help_text="Введите должность принимаемого сотрудника")
    loi_department = forms.CharField(label='Подразделение', max_length=256, help_text="Введите подразделение, куда принимается сотрудник")
    loi_dateOfInv = forms.DateField(required=False, label='Дата начала работы (необязательно)',help_text="Введите дату начала работы сотрудника", input_formats=['%d.%M.%Y'])

    def save(self, user_):
        new_letter = LetterOfInvite.objects.create(
            loi_date = self.cleaned_data['loi_date'],
            loi_employee = self.cleaned_data['loi_employee'],
            loi_position = self.cleaned_data['loi_position'],
            loi_department = self.cleaned_data['loi_department'],
            loi_dateOfInv = self.cleaned_data['loi_dateOfInv'],
            loi_res_officer = user_
        )
        return new_letter
