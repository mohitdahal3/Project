
from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.home , name = "home"),
    path('services/' , views.services , name = "services"),
    path('courses/' , views.courses , name = "courses"),
    path('videos/' , views.videos , name = "videos"),
    path('contact/' , views.contact , name = "contact"),
    path('help/' , views.help , name = "help"),
    path('joinus/' , views.joinus , name = "joinus")
]