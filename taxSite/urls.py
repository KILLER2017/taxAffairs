from django.urls import path
from . import views

app_name = 'tax'
urlpatterns = [
    # ex: /polls/
    path('hello', views.hello),
    path('search', views.search),
    path('read', views.read_by_pdf),
    path('test', views.test)
]