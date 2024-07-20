from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView

from .models import SampleRecord


class MainListView(ListView):
    model = SampleRecord
    template_name = 'main/main_list.html'
    context_object_name = 'records'


class BackOfficeView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'main/back_office.html'
        return render(request, template_name=template_name)

