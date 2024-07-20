from django.urls import path

from .views import BackOfficeView, MainListView

app_name = 'main'

urlpatterns = [
    path('', MainListView.as_view(template_name='main/main_list.html'), name='home'),
    path('backend/', BackOfficeView.as_view(), name='backoffice')
]

