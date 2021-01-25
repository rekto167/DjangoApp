from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse_lazy, reverse
# Create your views here.

from .models import MenuModel
from .forms import MenuForm


class IndexChefView(View):
    template_name = 'chef/index.html'
    context = {
        'judul': 'Halaman Login Chef',
    }

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class MenuList(ListView):
    model = MenuModel
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        category_menu = self.model.objects.values_list(
            'food_cat', flat=True).distinct()
        self.kwargs.update({'category_list': category_menu})
        kwargs = self.kwargs
        # context = super().get_context_data(**kwargs)
        # context['page_title'] = 'Daftar Menu'
        return super().get_context_data(*args, **kwargs)


class AddMenu(CreateView):
    model = MenuModel
    form_class = MenuForm
    template_name = "chef/add_menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Tambah Menu'
        # print(fields)
        return context
    # success_url = reverse_lazy('chef:listmakanan')

    # def form_valid(self, form):
    #     food_name = form.save(commit=False)
    #     image = form.cleaned_data('food_pic')
    #     obj.food_name = self.request.food_name
    #     food_name.save()
