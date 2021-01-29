from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    IndexChefView,
    MenuList,
    AddMenu,
    MenuCategoryList,
)

app_name = 'chef'
urlpatterns = [
    path('listmenu/category/<kategori>',
         MenuCategoryList.as_view(), name='category'),
    path('addmenu/', AddMenu.as_view(), name='addmenu'),
    path('listmenu/<page>', MenuList.as_view(), name='listmenu'),
    path('', IndexChefView.as_view(), name='index'),
]
