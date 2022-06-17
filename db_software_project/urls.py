"""db_software_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from software_app.views import (
    MainView,
    LoginView,
    LogoutView,
    SoftwareView,
    PersonView,
    SoftwareAddView,
    SoftwareUpdateView,
    SoftwareDeleteView,
    SearchSoftwareView,
    SoftRequestCreateView,
    SoftRequestListView,
    SoftRequestDeleteView,
    UpdateSoftRequestView,
    ContactFormView,
    ThanksView,
    SearchSoftRequestView,
    SortOfSoftwareAddView,
    SortOfSoftwareListView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', MainView.as_view()),
    path('software/', SoftwareView.as_view(), name="software"),
    path('person/<int:person_id>/', PersonView.as_view(), name="person"),
    path('software/add/', SoftwareAddView.as_view(), name="add_software"),
    path('software_update/<int:pk>/', SoftwareUpdateView.as_view()),
    path('software_delete/<int:pk>/', SoftwareDeleteView.as_view()),
    path('search_software/', SearchSoftwareView.as_view(), name='search_software'),
    path('request_list', SoftRequestListView.as_view(), name='request_list'),
    path('request/add/', SoftRequestCreateView.as_view(), name='request_software'),
    path('request_delete/<int:pk>/', SoftRequestDeleteView.as_view(), name='request_delete'),
    path('request_update/<int:pk>/', UpdateSoftRequestView.as_view(), name="request_update"),
    path('contact_form/', ContactFormView.as_view(), name='contact_form'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('search/',SearchSoftRequestView.as_view(), name='search'),
    path('add_sortofsoftware/', SortOfSoftwareAddView.as_view(), name='add_sortofsoftware'),
    path('sortofsoftware_list/', SortOfSoftwareListView.as_view(), name='sortofsoftware_list')
]

