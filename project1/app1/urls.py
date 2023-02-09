from django.urls import path
from . import views

urlpatterns = [
    path('av/',views.add_view.as_view(),name='add_url'),
    path('sv/',views.simplebasedshow_view.as_view(),name='show_url'),
    path('uv/<int:pk>/',views.simplebasedUpdate_view.as_view(),name='update_url'),
    path('dv/<int:pk>/',views.simplebasedDelete_view.as_view(),name='delete_url'),
    path('<pk>/',views.simpledetail_view.as_view(),name='detail_url')
]