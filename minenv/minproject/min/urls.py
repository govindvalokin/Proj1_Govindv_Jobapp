from django.urls import path
from . import views
# from min import views

urlpatterns = [
    path('index/',views.index),
    path("",views.index),
    path('newform/',views.newform,name="jobform"),
    path('dform/',views.dform),
    path('dformstore/',views.dformstore),
    # path('addnew',views.addnew,name="addnew"),
    path('updateform/',views.updateform,name="updateform"),
]