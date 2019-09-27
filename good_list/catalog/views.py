from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={},  # num_visits appended
    )
