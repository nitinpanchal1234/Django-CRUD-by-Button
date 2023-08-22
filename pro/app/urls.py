from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('add_action', views.add_action, name='add_action'),
    path('view_all_emp', views.view_all_emp, name='view_all_emp'),
    path('update_emp/<int:id>', views.update_emp, name='update_emp'),
    path('update_action/<int:id>', views.update_action, name='update_action'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
