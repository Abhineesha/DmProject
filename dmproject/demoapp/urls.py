from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),


]





















# urlpatterns = [
#     path('',views.demo,name='demo'),
#     path('add/',views.addition,name='addition'),


# urlpatterns = [
#     path('',views.demo,name='demo'),
#     path('add/',views.addition,name='addition'),
#     path('add/',views.subtraction,name='subraction'),
#     path('add/',views.multiplication,name='multiplication'),
#     path('add/',views.division(),name='division'),
#
# ]

# urlpatterns = [
#     path('',views.home,name='home'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('details/',views.details,name='details'),
#     path('thanks/',views.thanks,name='thanks')
#
# ]