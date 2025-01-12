from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/control-panel/', views.admin_control_panel, name='admin_control_panel'),
    path('demo/phase1/', views.demo_phase1, name='demo_phase1'),
    path('demo/phase2/', views.demo_phase2, name='demo_phase2'),
    path('demo/phase3/', views.demo_phase3, name='demo_phase3'),
    
    path('contact/', views.contact, name='contact'),
    path('participation/', views.participation_page, name='participation_page'),
    path('ta_overview/', views.ta_overview, name='ta_overview'),
    path('ta_overview2/', views.ta_overview2, name='ta_overview2'),
    path('student_overview/', views.student_overview, name='student_overview'),
    
    path('form/problem1/', lambda request: redirect('problem1', page_number=1)),
    path('problem1/<int:page_number>/', views.problem1, name='problem1'),
    path('problem2/<int:page_number>/', views.problem2, name='problem2'),
    path('problem3/<int:page_number>/', views.problem3, name='problem3'),
    path('problem4/<int:page_number>/', views.problem4, name='problem4'),
    path('problem5/<int:page_number>/', views.problem5, name='problem5'),
    path('problem6/<int:page_number>/', views.problem6, name='problem6'),
    path('problem7/<int:page_number>/', views.problem7, name='problem7'),
    
    path('form/taproblem1/', lambda request: redirect('taproblem1', page_number=1)),
    path('taproblem1/<int:page_number>/', views.taproblem1, name='taproblem1'),
    path('taproblem2/<int:page_number>/', views.taproblem2, name='taproblem2'),
    path('taproblem3/<int:page_number>/', views.taproblem3, name='taproblem3'),
    path('taproblem4/<int:page_number>/', views.taproblem4, name='taproblem4'),
    path('taproblem5/<int:page_number>/', views.taproblem5, name='taproblem5'),
    path('taproblem6/<int:page_number>/', views.taproblem6, name='taproblem6'),
    path('taproblem7/<int:page_number>/', views.taproblem7, name='taproblem7'),
    
    path('form/tafeedback1/', lambda request: redirect('tafeedback1', page_number=1)),
    path('tafeedback1/<int:page_number>/', views.tafeedback1, name='tafeedback1'),
    path('tafeedback2/<int:page_number>/', views.tafeedback2, name='tafeedback2'),
    path('tafeedback3/<int:page_number>/', views.tafeedback3, name='tafeedback3'),
    path('tafeedback4/<int:page_number>/', views.tafeedback4, name='tafeedback4'),
    path('tafeedback5/<int:page_number>/', views.tafeedback5, name='tafeedback5'),
    path('tafeedback6/<int:page_number>/', views.tafeedback6, name='tafeedback6'),
    path('tafeedback7/<int:page_number>/', views.tafeedback7, name='tafeedback7'),
    
    path('unauthorized/', views.unauthorized_access, name='unauthorized_access_page'),
    path('success/', views.success, name='success'),
]
