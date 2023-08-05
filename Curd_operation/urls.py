
from django.contrib import admin
from django.urls import path
from MyApp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Add_show,name='addandshow'),
    path('Delete/<int:id>/', views.delete_data,name='deletedata'),
    path('update/<int:id>/', views.update_data,name='updatedata'),

]
