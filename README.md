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

Sysytem s??u??y do ewidencji posiadanego przez firm?? oprogramowania.
Praca wykonywana w ramach projektu ko??cowego kursu. 

ZA??O??ENIA
Projekt musi spe??nia?? nast??puj??ce za??o??enia:

    1. Projekt musi by?? aplikacj?? webow??, napisan?? w Django.
    2. Projekt musi posiada?? minimalnie 5 modeli.
    3. Projekt musi mie?? baz?? danych PostgreSQL.
    4. W bazie danych projektu powinny znajdowa?? si?? co najmniej 3 tabele i 2 relacje mi??dzy tabelami.
    5. W projekcie musz?? zosta?? wykorzystane co najmniej relacje jeden do wielu i wiele do wielu.
    6. W aplikacji projektu powinno znajdowa?? si?? minimum 5 widok??w (obs??ugiwane przez r????ne adresy URL).
    7. Aplikacja projektu powinna mie?? co najmniej jeden widok dost??pny tylko dla zalogowanego u??ytkownika (u??ywaj??c Django Auth system).
    8. Aplikacja projektu powinna posiada?? przynajmniej jeden formularz, obs??ugiwany metod?? POST.
    9. G????wne funkcjonalno??ci aplikacji projektu powinny by?? pokryte testami (co najmniej 3 testy jednostkowe napisane przy u??yciu pytest'a). Do ka??dego widoku powinny by?? co najmniej dwa testy.
    10. Projekt powinien posiada?? dokumentacj??.

PODSTAWOWE WYMAGANIA PROJEKTOWE

    1. Aplikacja webowa napisana w Django.  
    2. Aplikacja powinna korzysta?? z bazy danych PostgreSQL. 
    3. Widoki powinny by?? utworzone w oparciu o j??zyk HTML. 
    4. Testy powinny korzysta?? z frameworka pytest. 

Aplikacja b??dzie s??u??y?? uporz??dkowaniu procesu zarz??dzania oprogramowaniem wykorzystywanym w firmie. 

Aplikacja b??dzie zapewnia?? dost??p do nast??puj??cych informacji: 

    a) jakie oprogramowanie posiada firma;
    b) zg??oszenie potrzeby w zakresie oprogramowania;
    c) aktualne wykorzystanie oprogramowania (co u??ywa); 
    d) uprawnienia do aplikacji;
    e) Aplikacja b??dzie pozwala??a na ewidencj?? atrybut??w minimum:
        a. rodzaj (np. czasowa, wieczysta) licencji danego oprogramowania;
        b. typ licencji (np. EDU, komercyjna) danego oprogramowania;  
        c. czas wa??no??ci zakupionego oprogramowania i mo??liwo???? terminowego jego utrzymania wybranych os??b; 
        d. klucze licencji.
Przy zakupie i przed??u??aniu licencji oprogramowania b??dzie mo??liwo????:

    a) sprawdzenia czy firma posiada dany rodzaj oprogramowania, z jak?? licencj?? i na jaki czas;
    b) kontrola czasu wa??no??ci oprogramowania, mo??liwo???? efektywnego zarz??dzania danym oprogramowaniem w firmie np. konieczno???? odnowienia licencji;
    c) dost??p do informacji o typie licencji wykorzystywanego oprogramowania, co ma prze??o??enie, na produkty kt??re firma sprzedaje/udost??pnia na zewn??trz; 
    d) dost??p do informacji kto i kiedy u??ywa jakie oprogramowanie, co umo??liwi zarz??dzanie u??ytkowaniem oprogramowania;
    e) racjonalne wykorzystanie oprogramowania;
    f) mo??liwo???? wp??ywania na koszty utrzymania oprogramowania. 

URUCHOMIENIE

Uruchomienie nast??puje poprzez zastosowanie komendy:
python3 manage.py runserver 
Testy uruchamiane s?? komend?? z software_app: pytest tests/tests.py

U??ytkownik bez zalogowania ma mo??liwo???? zobaczenia listy oprogramowania. 
U??ytkownik po zalogowaniu ma mo??liwo????: 
a) wprowadzenia, usuni??cia, modyfikacji oraz przeszukiwania program??w;
b) przegl??dania os??b, kt??re u??ytkuj?? programy.
