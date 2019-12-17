from django.urls import path

from . import views

urlpatterns = [
    path("invitations/", views.InvitationsViews.as_view(), name="invitations"),
    path(
        "invitations/<invitations_id>/",
        views.InvitationsViews.as_view(),
        name="delete_invitations",
    ),
]
