from django.urls import path
from . import views

urlpatterns=[
    path('',views.userpage,name='user'),
    path('add/',views.add_med,name='addmed'),
    path('list/',views.list_med,name='listmed'),
    path('update/<int:id>/',views.update_med,name='updatemed'),
    path('delete/<int:id>/',views.del_med,name='delmed'),
    path('search/',views.search_med,name='searchmed')
]