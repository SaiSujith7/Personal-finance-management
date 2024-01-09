from .views import UsernameValidationView, EmailValidationView
from django.urls import path
from Authentication import views

urlpatterns=[
    path('register',views.RegistrationView,name="register"),
    path('login',views.LoginView,name="login"),
    path('logout',views.LogoutView,name="logout"),
    path('validate-username',UsernameValidationView.as_view(),name="validate-username"),
    path('validate_email',EmailValidationView.as_view(), name='validate_email'),
]