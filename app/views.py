from .models import Taom
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm

class StudentListView(ListView):
    model = Taom
    context_object_name = 'users'
    template_name = 'myapp/user_list.html'

class StudentDetailView(DetailView):
    model = Taom
    context_object_name = 'user'
    template_name = 'myapp/user_detail.html'

class StudentCreateView(CreateView):
    model = Taom
    form_class = StudentForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_list') 

class StudentUpdateView(UpdateView):
    model = Taom
    form_class = StudentForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Taom
    template_name = 'myapp/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')