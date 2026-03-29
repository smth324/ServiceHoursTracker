from django.urls import path

from . import views # This . package just means "the current package; we are importing the sister file "views.py"

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("login", views.login_view, name="login_view"),
    path('logout', views.logout_view, name='logout_view'),
    path("register", views.register_view, name="register_view"),
    path("student_dashboard", views.student_dashboard, name="student_dashboard"),
    path("student_opportunities/", views.student_opportunities, name="student_opportunities"),
    path("student_opportunities_details/<int:event_id>", views.student_opportunities_details, name="student_opportunities_details"),
    path("student_calendar", views.student_calendar, name="student_calendar"),
    path("org_dashboard", views.org_dashboard, name="org_dashboard"),
    path("org_eventsform", views.org_eventsform, name="org_eventsform"),
    path("org_events_detail/<int:event_id>", views.org_events_detail, name="org_events_detail"),
    path("org_scanner", views.org_scanner, name="org_scanner"),
    path("oaa_dashboard", views.oaa_dashboard, name="oaa_dashboard"),
    path("oaa_students", views.oaa_students, name="oaa_students"),
    path("oaa_students_detail/<int:student_id>", views.oaa_students_detail, name="oaa_students_detail"),    
    path("oaa_events", views.oaa_events, name="oaa_events"),
    path("oaa_events_detail/<int:event_id>", views.oaa_events_detail, name="oaa_events_detail"),
]