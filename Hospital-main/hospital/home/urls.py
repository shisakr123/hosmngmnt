from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('base/',views.base),
    path('booking/',views.booking,name='booking'),
    path('contacts/',views.contacts,name='contacts'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
]