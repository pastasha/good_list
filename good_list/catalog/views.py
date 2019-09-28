from django.shortcuts import render
from .models import GoodDeedRecord

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    good_deed = GoodDeedRecord.objects.count()
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'good_deed':good_deed},  # num_visits appended
    )
