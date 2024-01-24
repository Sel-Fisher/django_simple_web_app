from django.urls import path

from web_app.views import vacancies_list

urlpatterns = [
    path("vacancies/", vacancies_list, name="vacancies_list"),
]
