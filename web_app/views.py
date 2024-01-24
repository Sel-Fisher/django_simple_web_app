from django.shortcuts import render

from web_app.models import Vacancy


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    return render(request, "web_app/vacancies_list.html", context=context)
