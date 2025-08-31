from django.urls import path
from . import views

app_name = 'accounts' 

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/setup/', views.ProfileSetupView.as_view(), name='profile_setup'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('preferences/edit/', views.PreferencesEditView.as_view(), name='preferences_edit'),
    path('availability/edit/', views.AvailabilityEditView.as_view(), name='availability_edit'),
    path('password/change/', views.ChangePasswordView.as_view(), name='change_password'),
    path('delete/', views.DeleteAccountView.as_view(), name='delete_account'),
]

