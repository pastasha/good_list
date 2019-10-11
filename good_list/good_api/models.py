from django.db import models
from datetime import datetime


# Абстрактная модель для заявок формы (Просьб о помощи)
class GoodDeedAbstract(models.Model):
    class Meta:
        abstract = True

    # список выбора
    STATUS_DISTURBANCES = (
        ('0', 'На рассмотрении'),
        ('1', 'Рассмотрено'),
        ('2', 'Выполнено')
    )
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    problem_description = models.TextField()
    adres = models.CharField(max_length=60)
    file = models.FileField(null=True)
    date_added = models.DateField(default=datetime.today)
    status = models.CharField(max_length=30,
                              choices=STATUS_DISTURBANCES,
                              default=0)

    def __str__(self):
        return self.problem_description

    #def get_absolute_url(self):
    #    return reverse('good_deed', args=[str(self.id)])



# Абстрактная модель для постов в приложении
class PostAbstract(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    published_date = models.DateField(default=datetime.today)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('good_deed', args=[str(self.id)])


# Модель для физического лица
class HumanRecord(GoodDeedAbstract):
    LIST_NEEDED_HELP = (
        ('Лечение', 'Лечение'),
        ('Интернет', 'Интернет'),
        ('Многодетная семья', 'Многодетная семья'),
        ('Животным', 'Животным'),
        ('Временно премещенные лица', 'Временно премещенные лица'),
        ('Дома пристарелых', 'Дома пристарелых'),
        ('Донорство', 'Донорство'),
        ('Другое', 'Другое')
    )
    birthday = models.DateField(default=datetime.today)
    type_needed_help = models.CharField(choices=LIST_NEEDED_HELP,
                                        default='Другое',
                                        max_length=30)

    class Meta:
        verbose_name = 'Заявка физического лица'
        verbose_name_plural = 'Заявки физических лиц'


# Модель для организации
class OrganizationRecord(GoodDeedAbstract):
    organization_name = models.CharField(max_length=60)
    info_about_organization = models.CharField(max_length=200)
    special_code = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Заявка юридического лица'
        verbose_name_plural = 'Заявки юридических лиц'


# Пост на просьбу о помощи
class NeedHelpPost(PostAbstract):
    organization_request = models.ForeignKey(OrganizationRecord,
                                             null=True,
                                             on_delete=models.CASCADE)
    human_request = models.ForeignKey(HumanRecord,
                                      null=True,
                                      on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост заявки помощи'
        verbose_name_plural = 'Пост заявок помощи'


# хранит данныо об откликнувшихся
class Respondent(models.Model):
    linked_post = models.ForeignKey(NeedHelpPost,
                                    on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=10,
                              null=True)

    class Meta:
        verbose_name = 'Отозвавшийся'
        verbose_name_plural = 'Отозвавшиеся'


# Пост новостной ленты

class NewsPost(PostAbstract):
    #FIXME: Затычка для инициализации этого класса
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# Пост отчетности
class ReportPost(PostAbstract):
    organization_request = models.ForeignKey(OrganizationRecord,
                                             null=True,
                                             on_delete=models.CASCADE)
    human_request = models.ForeignKey(HumanRecord,
                                      null=True,
                                      on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
