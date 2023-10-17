from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cakeapp.views import SignUpView,SignInView,IndexView,CategoryCreateView,remove_category,active_category\
    ,CakeCreateView,CakeListView,CakeUpdateView,remove_cakeview,CakeDetailView,CakeVarientCreateView


urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("index/",IndexView.as_view(),name="index"),
    path("add/",CategoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("categories/<int:pk>/active",active_category,name="active-category"),
    path("cake/add",CakeCreateView.as_view(),name="cake-add"),
    path("cake/list",CakeListView.as_view(),name="cake-list"),
    path("cake/<int:pk>/edit",CakeUpdateView.as_view(),name="cake-edit"),
    path("cake/<int:pk>/remove",remove_cakeview,name="cake-remove"),
    path("cake/<int:pk>",CakeDetailView.as_view(),name="cake-detail"),
    path("cake/<int:pk>/varient/add",CakeVarientCreateView.as_view(),name="varient-add"),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)