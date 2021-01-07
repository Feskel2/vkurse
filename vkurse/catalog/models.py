from django.db import models

# Create your models here.
from django.urls import reverse


class Event(models.Model):
    """
    Model representing an event
    """
    name = models.CharField(max_length=200, help_text="Название мероприятия")
    slug = models.CharField(blank=True, null=True, max_length=200, help_text="Название на английском")
    subject = models.TextField (blank=True, null=True, max_length=5000, help_text="Описание")
    picture = models.ImageField(blank=True, null=True, upload_to='images/', help_text="Картинка")
    link = models.CharField(blank=True, null=True, max_length=200, help_text="Ссылка на мероприятие")
    create_date_time = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания")
    renew = models.DateTimeField(auto_now=True, help_text="Дата и время обновления")
    start_date_time = models.DateTimeField(blank=True, null=True, help_text="Дата и время начала")
    end_date_time = models.DateTimeField(blank=True, null=True, help_text="Дата и время конца")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, help_text="Категория")
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, help_text="Тип", blank=True)
    tags = models.TextField (max_length=1000,blank=True, null=True,  help_text="Тэги")
    place = models.TextField (max_length=100,blank=True, null=True,  help_text="Координаты места (для карты)")
    adress = models.TextField (max_length=100,blank=True, null=True,  help_text="Адрес")
    estimates = models.IntegerField (blank=True, null=True, help_text="Оценка")
    count_estimates = models.IntegerField (blank=True, null=True, help_text="Колво-оценок")
    payed = models.BooleanField(default=False, help_text="Оплачено")
    moderated = models.BooleanField(default=True, help_text="Модерация пройдена?")


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        #return reverse('event-detail', args=[str(self.id)])
        #return reverse('event-detail', args={'slug': str(self.slug)})
        #return self.slug
        #return 'id' + str(self.id) +'_'+self.slug
        return 'id' + str(self.id)

class Category(models.Model):
    """
    Model representing an Category of event
    """
    name = models.CharField(max_length=200, help_text="Название категории")
    slug = models.CharField(max_length=200, help_text="Название на английском")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Type(models.Model):
    """
    Model representing an Category of event
    """
    name = models.CharField(max_length=200, help_text="Название типа")
    slug = models.CharField(max_length=200, help_text="Название на английском")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name