
from django.contrib import admin
from django.urls import path

from review.views import sample, sample1, Posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inc/', sample, name='sample'),
    path('comment/<int:post_id>', sample1, name='sample1'),
    path('',Posts.as_view(), name='post_list'),
]
