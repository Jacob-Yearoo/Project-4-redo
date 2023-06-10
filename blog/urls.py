from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # path('report/<slug:slug>/', views.ReportView.as_view(), name='report_post'),
    path('report/<slug:slug>/', views.report_post, name='report_post'),
]
