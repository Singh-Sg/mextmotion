from django.core import paginator
from rest_framework.settings import api_settings

from nextmotion import settings
from rest_framework import pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Invitation
from .serializer import (
    CreateInvitationSerializer,
    GetAllInvitationSerializer,
    UpdateInvitationSerializer,
)
from .service import (
    CreateInvitationsService,
    DeleteInvitationsService,
    GetAllInvitationsService,
    UpdateInvitationsService,
)


class InvitationsViews(APIView):
    """
    """
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    paginator = pagination_class()

    @classmethod
    def get(cls, request):
        """
        """
        invitation = GetAllInvitationsService.execute({})
        invitations = paginator.paginate_queryset(invitation, request)
        serializer = GetAllInvitationSerializer(invitations, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    @classmethod
    def post(cls, request):
        """
        """
        serializer = CreateInvitationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serial_data = serializer.validated_data
        try:
            invitaion = CreateInvitationsService.execute({"serial_data": serial_data})
            serializer = GetAllInvitationSerializer(invitaion)
            return Response({"data": serializer.data}, status.HTTP_201_CREATED,)
        except User.DoesNotExist:
            return Response(
                {"Error": "Invalid creator id{}".format("invitations_id")},
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def patch(cls, request, invitations_id):
        """
        """
        try:
            serializer = UpdateInvitationSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            serial_data = serializer.validated_data
            invitaion = UpdateInvitationsService.execute(
                {
                    "invitations_id": invitations_id,
                    "email": serial_data.get("email"),
                    "used": serial_data.get("used"),
                }
            )

            serializer = GetAllInvitationSerializer(invitaion)
            return Response({"data": serializer.data}, status.HTTP_200_OK,)

        except Invitation.DoesNotExist:
            return Response(
                {"Error": "Invalid Invitation id{}".format(invitations_id)},
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def delete(cls, request, invitations_id):
        """
        """
        try:
            DeleteInvitationsService.execute(
                {"invitations_id": invitations_id,}
            )
            return Response({}, status.HTTP_200_OK)
        except Invitation.DoesNotExist:
            return Response(
                {"Error": "Invalid Invitation id{}".format(invitations_id)},
                status.HTTP_404_NOT_FOUND,
            )
