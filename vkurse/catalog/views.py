from django.shortcuts import render
from .models import Event, Category, Type, User
from django.views import generic

"""
Удалить все что ниже если не буедт работать
"""
from django.contrib.auth.views import LoginView


# Create your views here.

def index(request):
    """
    Функция отображения домашней страницы
    """
    # Генерация количеств главных объектов
    num_events = Event.objects.all().count()
    num_categorys = Category.objects.all().count()
    num_types =  Type.objects.all().count()

    # Доступные события
    num_events_avalible = Event.objects.count()

    # Отрисовка HTML шаблона index.html с данными внутри
    # Переменной контекста context
    return render(
        request,
        'index.html',
        context={
            'num_events':num_events,
            'num_categorys':num_categorys,
            'num_types':num_types,
            'num_events_avalible':num_events_avalible,
        }
    )


class EventListView (generic.ListView):
    model = Event
    paginate_by = 10
    context_object_name = 'my_event_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Event.objects.filter(name__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположени


class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Event.objects.filter(name__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'catalog/event_detail.html'  # Определение имени вашего шаблона и его расположения


"""
Удалить все что ниже если не буедт работать
"""
class UserLoginView(LoginView):
    model = User
    template_name = 'login.thml'
    form_class = AuthUserForm
    success_url = reverse_lazy ('index')