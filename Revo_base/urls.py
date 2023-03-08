from django.contrib import admin
from django.urls import path
from RevoHome import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('builds', views.build_sections, name='build_sections'),
    path('builds/<int:pk>/', views.build_section_detail, name='build_section_detail'),
    # path('build_section/<int:pk>/amount_made/', views.add_amount_made, name='add_amount_made'),

]
