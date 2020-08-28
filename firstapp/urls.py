from django.urls import path
from django import forms
from . import views

urlpatterns = [
    path("", views.auth, name="auth"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("login", views.login, name="login"),
    path("detail/<int:student_id>", views.detail, name="detail"),
    path("submit", views.submit, name="submit"),
    path("add/<int:student_id>", views.add, name="add"),
    path("submitmark", views.submitmark, name="submitmark"),
    path("delete/<int:student_id>", views.delete, name="delete"),
    
    #only index will open when auth is verify
    # index mainee faculty dashboard, open after faculty login
    path("index", views.index, name="index"),
]
