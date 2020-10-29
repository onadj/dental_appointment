from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('blog-details.html', views.blogdetails, name="blogdetails"),
    path('blog.html', views.blog, name="blog"),
    path('pricing.html', views.pricing, name="pricing"),
    path('service.html', views.service, name="service"),
]
