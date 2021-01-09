from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^ev/$', views.EventListView.as_view(), name='events'),
    #url(r'^ev/(?P<pk>\d+)$', views.EventDetailView.as_view(), name='event-detail'),
    #path('ev/<str:slug>/', views.EventDetailView.as_view(), name='event-detail'),
    #path('ev/<slug>/', views.EventDetailView.as_view(), name='event-detail'),  # работал такой вариант в файле models.py в функции get_absolute_url нужно чтобы был return self.slug
    #path(r'^ev/(?Pid_<id>_<slug>\d+)$', views.EventDetailView.as_view(), name='event-detail'),
    #path('ev/id<str:id>_<str:slug>/', views.EventDetailView.as_view(), name='event-detail'),
    #path(r'^ev/(?Pid<id>_<slug>\d+)$', views.EventDetailView.as_view(), name='event-detail'),
    path('ev/id<pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('login', views.UserLoginView.as_view(), name='login_page'),
]
