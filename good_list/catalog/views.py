from django.shortcuts import render

from .models import GoodDeedRecord


# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    good_deeds = list(GoodDeedRecord.objects.all())
    # переменной контекста context
    return render(
        request,
        'catalog.html',
        {'good_deeds': good_deeds}  # num_visits appended
    )


'''
    Заменен на свой обработчик

# Обработчик конкретного html шаблона
class BaseCatalogView(ListView):
    model = GoodDeedRecord
    template_name = 'index.html'

'''
