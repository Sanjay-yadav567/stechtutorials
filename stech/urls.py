from django.urls import path
from .views import home,post, category, about

urlpatterns = [
    path('',home),
    path('home/',home),
    path('about/',about),
    path('blog/<slug:url>', post),
    path('category/<slug:url>', category),

]