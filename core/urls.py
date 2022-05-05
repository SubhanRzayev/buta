from django.urls import path
from . import views
from core.views import *


app_name = 'core'


urlpatterns = [
    path("", ServiceListView.as_view(),name="index"),
    
    path("corporate/", AboutListView.as_view(), name="corporate"),
    
    
    path('cases/',views.project_list,name='cases'),
    
    
    path('cases/<slug:category_slug>',views.project_list,name='cases_category'),
    
    path('cases/<slug:category_slugs>',views.project_list,name='project_category'),
    
    
    
    path('cases/<slug:slug>/',ProjectDetailView.as_view(),name='case_detail'),
    
    
    
    path('service/<slug:slug>/',ServiceDetailView.as_view(),name='service_detail'),
    
    
    path("career/", CareerListView.as_view(), name="career"),
    
    path("contact/", ContactCreateView.as_view(), name="contact"),
    
    path("innovations/", InnovationsListView.as_view(), name="innovations"),
    
    path("innovations/<slug:slug>/", InnovationsDetailView.as_view(), name="news_details"),
    
    
]
