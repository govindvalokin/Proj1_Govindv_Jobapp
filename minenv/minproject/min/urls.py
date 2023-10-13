from django.urls import path
from . import views
# from min import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path("",views.index,name="index"),
    path('newform/',views.newform,name="jobform"),
    path('dform/',views.dform),
    path('dformstore/',views.dformstore),
    # path('addnew',views.addnew,name="addnew"),
    path('updateform/',views.updateform,name="updateform"),
    path('deleteform/',views.deleteData,name="delete"),
]