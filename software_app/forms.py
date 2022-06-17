from django import forms
from django.forms import modelformset_factory

from .models import SortOfSoftware, TypeOfSoftware, SoftRequest, Person, Software, MySoftware


SORT = []
sort_of_software = SortOfSoftware.objects.all()
for soft in sort_of_software:
    SORT.append((soft.id, soft.name))


TYPE = []
type_of_software = TypeOfSoftware.objects.all()
for soft in type_of_software:
    TYPE.append((soft.id, soft.name))


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class SoftRequestForm(forms.ModelForm):
    class Meta:
        model = SoftRequest
        exclude = ['status']


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'


class MySoftwareForm(forms.ModelForm):
    class Meta:
        model = MySoftware
        exclude = ['status']


SortOfSoftwareFormSet = modelformset_factory(SortOfSoftware, fields=['name', 'description_sort'], extra=1
)


class TypeOfSoftwareForm(forms.ModelForm):
    class Meta:
        model = TypeOfSoftware
        fields = '__all__'


class LoginForm(forms.Form):
    """ Form definition for logging in, inheriting from the form class """

    login = forms.CharField(label='Login', required=False)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput, required=False)


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(max_length=254)
    message = forms.CharField(widget=forms.Textarea())

    def send_email(self):
        print('Mail wysłany')


class SearchByNameForm(forms.Form):
    name = forms.CharField(label="Nazwa programu", max_length=128)


class SearchBySortOfSoftwareForm(forms.Form):
    sort_of_software = forms.ChoiceField(label="Rodzaj licencji", choices=SORT)


class SearchByTypeOfSoftwareForm(forms.Form):
    type_of_software = forms.ChoiceField(label="Typ licencji", choices=TYPE)
