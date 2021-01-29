from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from .models import MenuModel
from .forms import MenuForm


class IndexChefView(View):
    template_name = 'chef/index.html'
    context = {
        'judul': 'Halaman Login Chef',
    }

    def post(self, request, *args, **kwargs):
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request, username=username_login,
                            password=password_login)
        if user is not None:
            login(request, user)
        return redirect('chef:listmenu')

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class MenuCategoryList(ListView):
    model = MenuModel
    template_name = 'chef/chef_category_menu.html'
    context_object_name = 'menu_category'
    paginate_by = 4

    def get_queryset(self):
        menu_category = self.model.objects.filter(
            food_cat=self.kwargs['kategori'])
        return super().get_queryset()


class MenuList(ListView):
    model = MenuModel
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        category_menu = self.model.objects.values_list(
            'food_cat', flat=True).distinct()
        self.kwargs.update({'category_list': category_menu})
        kwargs = self.kwargs
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
