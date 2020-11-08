from django.urls import path
from .views import get_user_position_view, authorize_user_view, \
    update_user_info_view, update_interests_view, get_users_geo


urlpatterns = [
    path('auth/', authorize_user_view),
    path('info/update/', update_user_info_view),
    path('position/update', get_user_position_view),
    path('position/', get_users_geo),
    path('interest/update', update_interests_view)
]
