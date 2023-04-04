from django.urls import path
from . import views
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import News

urlpatterns = [
    path('', ListView.as_view(queryset=News.objects.all().order_by("-news_date")[:10],
                              template_name='main.html')),
    path('<int:pk>/', DetailView.as_view(model=News, template_name='post.html')),
    path('supply-news/', views.supply_news, name='supply-news'),
]
