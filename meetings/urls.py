from django.urls import path
from .views import get_list_meetings_view, get_meeting_view, meeting_action_view, \
    create_meeting_view, update_meeting_view


urlpatterns = [
    path('', get_list_meetings_view),
    path('<int:meeting_id>', get_meeting_view),
    path('<int:meeting_id>/action', meeting_action_view),
    path('create', create_meeting_view),
    path('<int:meeting_id>/update', update_meeting_view),
]
