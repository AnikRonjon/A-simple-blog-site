from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import rest_views
from . import views


router = DefaultRouter()
router.register('category', rest_views.CategoryModelViewSet)
router.register('post', rest_views.PostModelViewSet)


app_name = 'classapp'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.PostDetailView, name='post_detail'),
    path('dashboard/', views.user_dashboard_view, name='dashboard_redirect'),
    path('registration/', views.user_registration_view, name='registration_redirect'),
    path('login/', views.user_login_view, name='login_redirect'),
    path('logout/', views.user_logout_view, name='logout_redirect'),

]

urlpatterns += [
    path('', include(router.urls)),
]


