from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cakeapp.views import SignUpView,SignInView,HomeView,CategoryCreateView,remove_category,active_category\
    ,CakeCreateView,CakeListView,CakeUpdateView,remove_cakeview,CakeDetailView\
        ,CakeVarientCreateView,CakeVarientUpdateView,remove_varientview,OfferCreateView,signoutview,remove_offerview,DashboardView,remove_review,OrderListView\
            ,dispatched,intransit,delivered

urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("login/",SignInView.as_view(),name="signin"),
    path("logout/",signoutview,name="signout"),
    path("",HomeView.as_view(),name="home"),
    path("dashboard/",DashboardView.as_view(),name="dashboard"),
    path("add/",CategoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("categories/<int:pk>/active",active_category,name="active-category"),
    path("cake/add",CakeCreateView.as_view(),name="cake-add"),
    path("cake/list",CakeListView.as_view(),name="cake-list"),
    path("cake/<int:pk>/edit",CakeUpdateView.as_view(),name="cake-edit"),
    path("cake/<int:pk>/remove",remove_cakeview,name="cake-remove"),
    path("cake/<int:pk>",CakeDetailView.as_view(),name="cake-detail"),
    path("cake/<int:pk>/varient/add",CakeVarientCreateView.as_view(),name="varient-add"),
    path("varients/<int:pk>/edit",CakeVarientUpdateView.as_view(),name="edit-varient"),
    path("varients/<int:pk>/remove",remove_varientview,name="remove-varient"),
    path("varients/<int:pk>/offer/add",OfferCreateView.as_view(),name="offer-add"),
    path("varients/<int:pk>/offer/remove",remove_offerview,name="offer-remove"),
    path('cake/<int:pk>/review/remove',remove_review, name="review_delete"),
    path("orders/list",OrderListView.as_view(),name="order-list"),
    path("order/<int:pk>/dispatched",dispatched,name="order-dispatched"),
    path("order/<int:pk>/intransit",intransit,name="order-intransit"),
    path("order/<int:pk>/delivered",delivered,name="order-delivered"),


    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)