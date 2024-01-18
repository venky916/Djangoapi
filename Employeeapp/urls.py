from Employeeapp import views

from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path('department',views.departmentApi),
    path('department/<int:id>',views.departmentApi),

    re_path('employee',views.employeeApi),
    re_path(r'^employee/([0-9]+)/$',views.employeeApi),

    re_path('employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)