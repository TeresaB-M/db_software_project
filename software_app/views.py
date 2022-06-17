from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from .models import Software, Person, SoftRequest, SortOfSoftware, TypeOfSoftware, MySoftware
from .forms import LoginForm, ContactForm, SearchByNameForm, PersonForm, SortOfSoftwareFormSet
from .forms import SearchByTypeOfSoftwareForm, SearchBySortOfSoftwareForm
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


class MainView(View):
    """Create a main form and display it on the GET method page"""

    def get(self, request):
        return render(request, "index.html")


class LoginView(View):
    """Create a form of login view and display it on the GET method page,
       sending data using the POST method
       applying the is_valid method when the form is valid"""

    def get(self, request):
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                next_parameter = request.GET.get('next')
                if next_parameter:
                    return redirect(next_parameter)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Błędny login lub hasło.')
        return render(request, 'login_form.html', {'form': form})


class LogoutView(View):
    """Create logout view"""

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ThanksView(View):
    def get(self, request):
        return render(request, 'thanks.html')


class SoftwareView(View):
    """Detailed view of the software, application pagination"""

    def get(self, request):
        software = Software.objects.order_by("id")
        paginator = Paginator(software, 25)
        page = request.GET.get('page')
        softwares = paginator.get_page(page)

        counter_software = Software.objects.count()
        return render(request, 'software.html', {'softwares': softwares,
                                                 'range': range(1, paginator.num_pages + 1),
                                                 'counter_software': counter_software})


class SoftwareAddView(LoginRequiredMixin, View):
    """View for adding new software after login,
       with form field validation"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'add_software.html')

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        message = ''
        ctx = {
            'name': name,
            'description': description,
            'message': message
        }

        if name == '':
            ctx['message'] = 'Wprowadź nazwę programu'
            return render(request, 'add_software.html', context=ctx)
        if description == '':
            ctx['message'] = 'Wprowadź opis programu'
            return render(request, 'add_software.html', context=ctx)

        Software.objects.create(name=name,
                                description=description)
        ctx = {
            'message': f'Dodano program: {name}'
        }
        return render(request, 'add_software.html', context=ctx)


class SoftwareUpdateView(LoginRequiredMixin, UpdateView):
    """View modifying the program downloaded from the database after logging in"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Software
    fields = ['name', 'description']
    template_name = 'software_update_form.html'
    success_url = '/software'


class SoftwareDeleteView(LoginRequiredMixin, DeleteView):
    """View of removal from the database after login and approval"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Software
    template_name = 'software_confirm_delete.html'
    success_url = '/software'


class SearchSoftwareView(LoginRequiredMixin, View):
    """View of searching for items in the database after logging"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        name = request.GET.get("name")
        software = Software.objects.order_by("id")

        if name:
            software = Software.objects.filter(name__contains=name)
            return render(request, "search_software.html", context={"software": software})
        else:
            return render(request, "search_software.html", context={"software": software})


class SoftwareInLine(InlineFormSetFactory):
    model = Software
    fields = '__all__'


class SortOfSoftwareListView(LoginRequiredMixin, ListView):
    model = SortOfSoftware
    fields = '__all__'
    template_name = 'sortofsoftware_list.html'
    paginate_by = 8
    queryset = SortOfSoftware.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(SortOfSoftwareListView, self).get_context_data(**kwargs)
        context['counter_sortofsoftware'] = SortOfSoftware.objects.count()
        return context


class SortOfSoftwareAddView(TemplateView):
    template_name = 'add_sortofsoftware.html'

    def get (self, *args, **kwargs):
        formset = SortOfSoftwareFormSet(queryset=SortOfSoftware.objects.none())
        return self.render_to_response({'sortofsoftware_formset': formset})

    def post(self, *args, **kwargs):
        formset = SortOfSoftwareFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('sortofsoftware_list'))

        return self.render_to_response({'sortofsoftware_formset': formset})


class TypeOfSoftwareInLine(InlineFormSetFactory):
    model = TypeOfSoftware
    fields = '__all__'


class MySoftwareInLine(InlineFormSetFactory):
    model = MySoftware
    exclude = ['status']


class SoftRequestInLine(InlineFormSetFactory):
    model = SoftRequest
    exclude = ['status']


class SoftRequestCreateView(LoginRequiredMixin, CreateWithInlinesView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Person
    inlines = [SoftRequestInLine]
    template_name = 'softrequest_formset.html'
    form = PersonForm
    fields = '__all__'
    success_url = '/request_list'


class UpdateSoftRequestView(LoginRequiredMixin, UpdateWithInlinesView):
    """View modifying the program downloaded from the database after logging in"""
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Person
    inlines = [SoftRequestInLine]
    template_name = 'softrequest_formset.html'
    fields = '__all__'
    success_url = '/request_list'


class SoftRequestListView(LoginRequiredMixin, ListView):
    """Detailed view of the software request, after login"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = SoftRequest
    paginate_by = 5
    template_name = 'request_list.html'
    context_object_name = 'request_list'
    queryset = SoftRequest.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(SoftRequestListView, self).get_context_data(**kwargs)
        context['counter_softrequest'] = SoftRequest.objects.count()
        return context


class SoftRequestDeleteView(LoginRequiredMixin, DeleteView):
    """View of removal from the database after login and approval"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = SoftRequest
    template_name = 'request_confirm_delete.html'
    success_url = '/request_list'


class SearchSoftRequestView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        name_form = SearchByNameForm()
        sort_of_software_form = SearchBySortOfSoftwareForm()
        type_of_software_form = SearchByTypeOfSoftwareForm()
        return render(request, "search.html", {'name_form': name_form,
                                               'sort_of_software_form': sort_of_software_form,
                                               'type_of_software_form': type_of_software_form})

    def post(self, request):
        name_form = SearchByNameForm(request.POST)
        if name_form.is_valid():
            name = name_form.cleaned_data['name']
            softrequest = SoftRequest.objects.filter(my_software__software__name=name).order_by('id')
            name_form = SearchByNameForm()
            sort_of_software_form = SearchBySortOfSoftwareForm()
            type_of_software_form = SearchByTypeOfSoftwareForm()
            return render(request, 'search.html', {'softrequest': softrequest,
                                                   'name_form': name_form,
                                                   'sort_of_software_form': sort_of_software_form,
                                                   'type_of_software_form': type_of_software_form})

        sort_of_software_form = SearchBySortOfSoftwareForm(request.POST)
        if sort_of_software_form.is_valid():
            sort_of_software = sort_of_software_form.cleaned_data['sort_of_software']
            softrequest = SoftRequest.objects.filter(my_software__sort_of_software=sort_of_software)\
                .order_by('id')
            sort_of_software_form = SearchBySortOfSoftwareForm()
            type_of_software_form = SearchByTypeOfSoftwareForm()
            name_form = SearchByNameForm()
            return render(request, 'search.html', {'softrequest': softrequest,
                                                   'name_form': name_form,
                                                   'sort_of_software_form': sort_of_software_form,
                                                   'type_of_software_form': type_of_software_form})

        type_of_software_form = SearchByTypeOfSoftwareForm(request.POST)
        if type_of_software_form.is_valid():
            type_of_software = type_of_software_form.cleaned_data['type_of_software']
            softrequest = SoftRequest.objects.filter(my_software__type_of_software=type_of_software)\
                .order_by('id')
            type_of_software_form = SearchByTypeOfSoftwareForm()
            sort_of_software_form = SearchBySortOfSoftwareForm()
            name_form = SearchByNameForm()
            return render(request, 'search.html', {'softrequest': softrequest,
                                                   'name_form': name_form,
                                                   'sort_of_software_form': sort_of_software_form,
                                                   'type_of_software_form': type_of_software_form})


class PersonView(LoginRequiredMixin, View):
    """View of person using the software after login"""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, person_id):
        person = Person.objects.get(id=person_id)
        return render(request, 'person.html', {'person': person})
