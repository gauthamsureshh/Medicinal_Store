from django.urls import path
from api_med import views

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',views.api_login,name='login'),
    path('add/',views.med_add,name='medadd'),
    path('list/',views.med_list,name='medlist'),
    path('edit/<int:id>/',views.med_edit,name='mededit'),
    path('remove/<int:id>/',views.med_delete,name='meddelete'),
    path('search/',views.med_search,name='medsearch')
]