from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import IndexView

urlpatterns = [
    path('chef/', include('chef.urls', namespace='chef')),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
