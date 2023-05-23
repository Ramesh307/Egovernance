
from django.urls import path
from . import views 
from .views import SearchResultsListView

urlpatterns = [
   path('',views.homepage,name='home'),
   path('save',views.savecomments,name='save_comment'),
   path('search_by_category/<int:category_id>',views.categoryfilter,name='category_filter'),
   path('search_by_news/<int:post_id>',views.newsfilter,name='post_filter'),
   path('search_keyword',views.SearchResultsListView.as_view(),name='search'),
   path('about',views.about,name='about')
]