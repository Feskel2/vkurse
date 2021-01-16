from django.shortcuts import render
from .models import Event, Category, Type
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import AuthUserForm, RegistrUserForm, AddEventsForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView


# Create your views here.

def index(request):
    """
    Псевдо главная страница  - можно использовать как страницу для логина или промо
    ...да и то лучше заменить...
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
    '''
    Просмотр всех событий - ГЛАВНАЯ СТРАНИЦА
    '''
    model = Event
    paginate_by = 10
    context_object_name = 'my_event_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Event.objects.filter(name__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположени

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(generic.ListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['form'] = AddEventsForm()
        return context




class EventsCreateView (CreateView):
    """
    Создание события
    """
    model = Event
    context_object_name = 'event'   # ваше собственное имя переменной контекста в шаблоне
    template_name = 'catalog/event_list.html'  # Определение имени вашего шаблона и его расположения
    form_class = AddEventsForm
    success_url = reverse_lazy ('events')

    def get_context_data(self, **kwargs):
        kwargs['my_event_list'] = Event.objects.all()
        return super().get_context_data(**kwargs)



class EventsUpdateView(UpdateView):
    """
    Редактирование события
    """
    model = Event
    context_object_name = 'event'  # ваше собственное имя переменной контекста в шаблоне
    template_name = 'catalog/event_list.html'  # Определение имени вашего шаблона и его расположения
    form_class = AddEventsForm
    success_url = reverse_lazy('events')






class EventDetailView(generic.DetailView):
    """
    Просмотр конкретного события
    """
    model = Event
    context_object_name = 'event'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Event.objects.filter(name__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'event_detail.html'  # Определение имени вашего шаблона и его расположения




class UserLoginView(LoginView):
    """
    Страница логина пользователя
    """
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy ('index')
    def get_success_url(self):
        return self.success_url



class UserRegistrView(CreateView):
    """
    Страница регистрации пользователя
    """
    template_name = 'registration.html'
    form_class = RegistrUserForm
    success_url = reverse_lazy ('index')
    success_msg = 'Пользователь успешно создан'
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate (username=username, password=password)
        login (self.request, aut_user)
        return form_valid

class UserLogout(LogoutView):
    """
    Выход пользователя
    """
    next_page = reverse_lazy ('index')
