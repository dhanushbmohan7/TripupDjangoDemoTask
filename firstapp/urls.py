from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='homepage'),
    path('search/',views.search,name='search'),
    path('language_change/<language_key>',views.language,name='language'),
   

]