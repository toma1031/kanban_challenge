from django.urls import path
from .views import IndexView

app_name = 'kanban_challenge'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]