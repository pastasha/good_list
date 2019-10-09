from django.shortcuts import render

from .models import HumanRecord
from .models import OrganizationRecord
from .models import NeedHelpPost
from .models import Respondent
from .models import NewsPost
from .models import ReportPost
from django.views import generic


# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # подсчитывает -???-
    good_deed = GoodDeedRecord.objects.count()
    # подсчитывает количество добрых дел
    num_good_deeds = GoodDeedRecord.objects.all().count()
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'good_deed':good_deed, 'num_good_deeds': num_good_deeds},  # num_visits appended
    )

#TODO: решить что с этим делать. Конфликтует с новыми моделями
'''
class IWantHelpList(generic.ListView):
    model = GoodDeedRecord
    template_name = 'catalog/i_want_help_list.html'

class HelpMeList(generic.ListView):
    model = GoodDeedRecord
    template_name = 'catalog/help_me_list.html'

class IWantHelpPost(generic.DetailView):
    model = GoodDeedRecord
    paginate_by = 10
    template_name = 'catalog/i_want_help_post.html'

class INeedHelpPost(generic.DetailView):
    model = GoodDeedRecord
    paginate_by = 10
    template_name = 'catalog/i_need_help_post.html'
'''
