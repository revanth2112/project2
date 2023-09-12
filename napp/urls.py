from django.urls import path,include
from . import views

urlpatterns = [
     path('home/', views.home),
    path('hr/', views.hr),
    path('employee/', views.emp),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('empform/', views.emp_form),
    path('empdata/', views.emp_data),
    path('logout/', views.logout),
    path('signup/', views.signup),
]