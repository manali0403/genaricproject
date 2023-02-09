from django.shortcuts import render
from .models import Student
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView
from .models import Student

# Create your views here.

class add_view(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/a1/sv'


class simplebasedshow_view(ListView):
    model = Student

class simplebasedUpdate_view(UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/a1/sv'

class simplebasedDelete_view(DeleteView):
    model = Student
    fields = '__all__'
    success_url = 'a1/sv'

class simpledetail_view(DetailView):
    model = Student
    