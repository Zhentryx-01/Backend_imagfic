from django.urls import path
from .views import RegisterView, CustomLoginView, LogoutView
from .views import ImageCategoryListView, ImageListByCategoryView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('categories/', ImageCategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/images/', ImageListByCategoryView.as_view(), name='images-by-category'),
]
