The system is used to record the software owned by the company. 
Work done as part of the final course project.


ASSUMPTIONS
The project must meet the following assumptions:

     1. The project must be a web application written in Django.
     2. The project must have a minimum of 5 models.
     3. The project must have a PostgreSQL database.
     4. There should be at least 3 tables and 2 relationships between tables in the project database.
     5. At least one-to-many and many-to-many relationships must be used in the design.
     6. There should be at least 5 views in the project application (supported by different URLs).
     7. The project application should have at least one view available only to the logged in user (using Django Auth system).
     8. The project application should have at least one form supported by the POST method.
     9. The main functionalities of the project application should be covered with tests (at least 3 unit tests written with the help of a query test). There should be at least two tests for each view.
     10. The project should have documentation.

BASIC DESIGN REQUIREMENTS

     1. A web application written in Django.
     2. The application should use a PostgreSQL database.
     3. Views should be based on HTML.
     4. Tests should use the Pytest framework.

The application will be used to organize the software management process used in the company.

The application will provide access to the following information:

     a) what software does the company have;
     b) reporting a need for software;
     c) the current use of the software (what it uses);
     d) application permissions;
     e) The application will allow the registration of minimum attributes:
         a. the sort (e.g., temporary, perpetual) license of the software concerned;
         b. license type (eg EDU, commercial) of the software concerned;
         c. the validity period of the purchased software and the possibility of its timely maintenance for selected persons;
         d. license keys.

----------------------------------------------------------------------

Sysytem służy do ewidencji posiadanego przez firmę oprogramowania.
Praca wykonywana w ramach projektu końcowego kursu. 

ZAŁOŻENIA
Projekt musi spełniać następujące założenia:

    1. Projekt musi być aplikacją webową, napisaną w Django.
    2. Projekt musi posiadać minimalnie 5 modeli.
    3. Projekt musi mieć bazę danych PostgreSQL.
    4. W bazie danych projektu powinny znajdować się co najmniej 3 tabele i 2 relacje między tabelami.
    5. W projekcie muszą zostać wykorzystane co najmniej relacje jeden do wielu i wiele do wielu.
    6. W aplikacji projektu powinno znajdować się minimum 5 widoków (obsługiwane przez różne adresy URL).
    7. Aplikacja projektu powinna mieć co najmniej jeden widok dostępny tylko dla zalogowanego użytkownika (używając Django Auth system).
    8. Aplikacja projektu powinna posiadać przynajmniej jeden formularz, obsługiwany metodą POST.
    9. Główne funkcjonalności aplikacji projektu powinny być pokryte testami (co najmniej 3 testy jednostkowe napisane przy użyciu pytest'a). Do każdego widoku powinny być co najmniej dwa testy.
    10. Projekt powinien posiadać dokumentację.

PODSTAWOWE WYMAGANIA PROJEKTOWE

    1. Aplikacja webowa napisana w Django.  
    2. Aplikacja powinna korzystać z bazy danych PostgreSQL. 
    3. Widoki powinny być utworzone w oparciu o język HTML. 
    4. Testy powinny korzystać z frameworka pytest. 

Aplikacja będzie służyć uporządkowaniu procesu zarządzania oprogramowaniem wykorzystywanym w firmie. 

Aplikacja będzie zapewniać dostęp do następujących informacji: 

    a) jakie oprogramowanie posiada firma;
    b) zgłoszenie potrzeby w zakresie oprogramowania;
    c) aktualne wykorzystanie oprogramowania (co używa); 
    d) uprawnienia do aplikacji;
    e) Aplikacja będzie pozwalała na ewidencję atrybutów minimum:
        a. rodzaj (np. czasowa, wieczysta) licencji danego oprogramowania;
        b. typ licencji (np. EDU, komercyjna) danego oprogramowania;  
        c. czas ważności zakupionego oprogramowania i możliwość terminowego jego utrzymania wybranych osób; 
        d. klucze licencji.
Przy zakupie i przedłużaniu licencji oprogramowania będzie możliwość:

    a) sprawdzenia czy firma posiada dany rodzaj oprogramowania, z jaką licencją i na jaki czas;
    b) kontrola czasu ważności oprogramowania, możliwość efektywnego zarządzania danym oprogramowaniem w firmie np. konieczność odnowienia licencji;
    c) dostęp do informacji o typie licencji wykorzystywanego oprogramowania, co ma przełożenie, na produkty które firma sprzedaje/udostępnia na zewnątrz; 
    d) dostęp do informacji kto i kiedy używa jakie oprogramowanie, co umożliwi zarządzanie użytkowaniem oprogramowania;
    e) racjonalne wykorzystanie oprogramowania;
    f) możliwość wpływania na koszty utrzymania oprogramowania. 

URUCHOMIENIE

Uruchomienie następuje poprzez zastosowanie komendy:
python3 manage.py runserver 
Testy uruchamiane są komendą z software_app: pytest tests/tests.py

Użytkownik bez zalogowania ma możliwość zobaczenia listy oprogramowania. 
Użytkownik po zalogowaniu ma możliwość: 
a) wprowadzenia, usunięcia, modyfikacji oraz przeszukiwania programów;
b) przeglądania osób, które użytkują programy.
