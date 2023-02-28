from django.urls import path
from . import views 


urlpatterns = [
    path("category-list/", views.CategoryListView.as_view(), name="category-list"),
    path("create-category/", views.CategoryCreateView.as_view(), name="create-category"),
    path("category-detail/<slug:slug>/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("create-event/", views.CreateEventView.as_view(), name="create-event"), 
    path("event-details/<slug:slug>/", views.EventDetailView.as_view(), name="event-details"),
    path("event-list/", views.EventListView.as_view(), name="event-list"),
    path("event-update/<slug:slug>/", views.EventUpdateView.as_view(), name="event-update")
]
