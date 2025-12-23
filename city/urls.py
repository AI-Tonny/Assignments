from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    re_path(r'^news/(?P<slug>[a-zA-Z]+)/$', views.news_extra, name='news_extra'),

    path('management/', views.management, name='management'),

    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
    re_path(r'^history/(?P<slug>.+)/$', views.history_extra, name='history_extra'),

    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts')
]