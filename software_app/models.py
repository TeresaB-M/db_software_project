from django.db import models
from datetime import datetime


class SortOfSoftware(models.Model):
    """
    The class contains data about the types of software available: e.g. temporary, perpetual.
    Inherits from the Model class.
    """
    name = models.CharField(max_length=250, verbose_name="Rodzaj licencji")
    description_sort = models.CharField(max_length=250, verbose_name="Opis")

    @property
    def main_name(self):
        return "{} {}".format(self.name, self.description_sort)

    def __str__(self):
        return self.main_name


class TypeOfSoftware(models.Model):
    name = models.CharField(max_length=250, verbose_name="Typ licencji")
    description_type = models.CharField(max_length=250, verbose_name="Opis")

    @property
    def main_name(self):
        return "{} {}".format(self.name, self.description_type)

    def __str__(self):
        return self.main_name


class Software(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nazwa programu")
    description = models.CharField(max_length=250, verbose_name="Opis programu")

    @property
    def main_name(self):
        return "{} {}".format(self.name, self.description)

    def __str__(self):
        return self.main_name


class Person(models.Model):
    name = models.CharField(max_length=250, verbose_name="Imię")
    surname = models.CharField(max_length=250, verbose_name="Nazwisko")
    email = models.EmailField(blank=False)

    @property
    def main_name(self):
        return "{} {} {}".format(self.name, self.surname, self.email)

    def __str__(self):
        return self.main_name


class MySoftware(models.Model):
    software = models.ForeignKey('Software', on_delete=models.CASCADE)
    type_of_software = models.ForeignKey('TypeOfSoftware', on_delete=models.CASCADE)
    sort_of_software = models.ForeignKey('SortOfSoftware', on_delete=models.CASCADE)
    time_from = models.DateTimeField(verbose_name="Od kiedy wypożyczono")
    time_to = models.DateTimeField(verbose_name="Do kiedy wypożyczono")
    status = models.BooleanField(null=True)

    @property
    def main_name(self):
        return "{} {} {} {} {}".format(self.software, self.type_of_software,
                                       self.sort_of_software, self.time_from, self.time_to)

    def __str__(self):
        return self.main_name


class SoftRequest(models.Model):
    time_request = models.DateTimeField(auto_now=False, default=datetime.now, verbose_name="Termin odbioru")
    status = models.BooleanField(null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, verbose_name="Osoba")
    my_software = models.ForeignKey('MySoftware', on_delete=models.CASCADE,
                                    null=True, verbose_name="Wymagane oprogramowanie")

    @property
    def main_name(self):
        return "{} {} {} {}". format(self.time_request, self.status, self.person, self.my_software)

    def __str__(self):
        return self.main_name


class BorrowSoftware(models.Model):
    time_from = models.DateTimeField(auto_now=False, default=datetime.now)
    time_to = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)
    soft_request = models.ForeignKey('SoftRequest', on_delete=models.CASCADE, null=True)


class KeyOfSoftware(models.Model):
    nr_key = models.CharField(max_length=250, verbose_name="Nr klucza oprogramowania")
    my_software = models.ForeignKey('MySoftware', on_delete=models.CASCADE, null=True)
    borrow_software = models.ManyToManyField('BorrowSoftware', through='BorrowKey')


class BorrowKey(models.Model):
    borrow_software = models.ForeignKey('BorrowSoftware', on_delete=models.CASCADE)
    key_of_software = models.ForeignKey('KeyOfSoftware', on_delete=models.CASCADE)
