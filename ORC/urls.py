from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as ORC_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'ORC'
urlpatterns = [

    path('', views.about, name='about'),
    re_path(r'^home/$', views.about, name='home'),
    url('about/', views.about, name='about'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('ORC:password_reset_done')),
         {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^signup/$', ORC_views.signup, name='signup'),
    url('workorder_list/', views.workorder_list, name='workorder_list'),
    path('workorder/new/', views.workorder_new, name='workorder_new'),
    path('workorder/<int:pk>/edit/', views.workorder_edit, name='workorder_edit'),
    path('workorder/<int:pk>/delete/', views.workorder_delete, name='workorder_delete'),
    url('property_list/', views.property_list, name='property_list'),
    path('property/new/', views.property_new, name='property_new'),
    path('property/<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('property/<int:pk>/delete/', views.property_delete, name='property_delete'),
    url('resident_list/', views.resident_list, name='resident_list'),
    path('resident/new/', views.resident_new, name='resident_new'),
    path('resident/<int:pk>/edit/', views.resident_edit, name='resident_edit'),
    path('resident/<int:pk>/delete/', views.resident_delete, name='resident_delete'),
    path('resident/<int:pk>/workorderview/', views.resident_workorderview, name='resident_workorderview'),
    url('maintenance_worker_list/', views.maintenance_worker_list, name='maintenance_worker_list'),
    path('maintenance_worker/new/', views.maintenance_worker_new, name='maintenance_worker_new'),
    path('maintenance_worker/<int:pk>/edit/', views.maintenance_worker_edit, name='maintenance_worker_edit'),
    path('maintenance_worker/<int:pk>/delete/', views.maintenance_worker_delete, name='maintenance_worker_delete'),
    url('equipment_list/', views.equipment_list, name='equipment_list'),
    path('equipment/new/', views.equipment_new, name='equipment_new'),
    path('equipment/<int:pk>/edit/', views.equipment_edit, name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),
    url('orc_staff_list/', views.orc_staff_list, name='orc_staff_list'),
    path('orc_staff/new/', views.orc_staff_new, name='orc_staff_new'),
    path('orc_staff/<int:pk>/edit/', views.orc_staff_edit, name='orc_staff_edit'),
    path('orc_staff/<int:pk>/delete/', views.orc_staff_delete, name='orc_staff_delete'),
    path('maintenancework_list/', views.maintenancework_list, name='maintenancework_list'),
    path('maintenancework/new/', views.maintenancework_new, name='maintenancework_new'),
    path('maintenancework/<int:pk>/edit/', views.maintenancework_edit, name='maintenancework_edit'),
    path('maintenancework/<int:pk>/delete/', views.maintenancework_delete, name='maintenancework_delete'),
    path('maintenancework/<int:pk>/workerview/', views.maintenancework_workerview, name='maintenancework_workerview'),

    url(r'export/xls/$', views.export_workorders_excel, name='export_workorders_xls'),
    url(r'^workorders_json/', views.WorkorderList.as_view()),
    url(r'^residents_json/', views.ResidentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
