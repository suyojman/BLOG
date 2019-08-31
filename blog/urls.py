from django.urls import path
from . import views

urlpatterns = [
	path('',views.BlogListView.as_view(),name='blog'),
	path('post/<int:pk>',views.BlogDetailView.as_view(),name='detail'),
	path('addpost/',views.BlogCreateView.as_view(),name='add_post'),
	path('post/<int:pk>/edit',views.BlogEditView.as_view(),name='edit_post'),
	path('post/<int:pk>/delete',views.BlogDeleteView.as_view(),name='delete_post'),
]