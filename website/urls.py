from django.urls import path
from . import views

urlpatterns = [
    path('faculty_members/',views.faculty_members_api),
    path('staff_members/',views.staff_members_api),
    path('research_area/',views.research_area_api),
    path('research_scholars/',views.research_scholars_api),
    path('education/',views.education_api),
    path('society/',views.society_api),
    path('event/',views.event_api),
]