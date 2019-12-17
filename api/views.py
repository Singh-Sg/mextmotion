from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import GetAllInvitationSerializer, CreateInvitationSerializer, UpdateInvitationSerializer
from .service import GetAllInvitationsService, DeleteInvitationsService, CreateInvitationsService, UpdateInvitationsService
from nextmotion import settings
from rest_framework import pagination
from .models import Invitation


class InvitationsViews(APIView):
    """
    """

    @classmethod
    def get(cls, request):
        """
        """
        invitaions = GetAllInvitationsService.execute({})
        serializer = GetAllInvitationSerializer(invitaions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @classmethod
    def post(cls, request):
        """
        """
        serializer = CreateInvitationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serial_data = serializer.validated_data
        try:
            invitaion = CreateInvitationsService.execute(
                {
                    "serial_data": serial_data
                }
            )
            serializer = GetAllInvitationSerializer(invitaion)
            return Response(
                {"data": serializer.data},
                status.HTTP_201_CREATED,
            )
        except User.DoesNotExist:
            return Response(
                {
                    'Error': 'Invalid creator id{}'.format(
                        'invitations_id'
                    )
                },
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
            return Response(
                {"data": serializer.data},
                status.HTTP_200_OK,
            )

        except Invitation.DoesNotExist:
            return Response(
                {
                    'Error': 'Invalid Invitation id{}'.format(
                        invitations_id
                    )
                },
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def delete(cls, request, invitations_id):
        """
        """
        try:
            DeleteInvitationsService.execute(
                {
                    "invitations_id": invitations_id,
                }
            )
            return Response({}, status.HTTP_200_OK)
        except Invitation.DoesNotExist:
            return Response(
                {
                    'Error': 'Invalid Invitation id{}'.format(
                        invitations_id
                    )
                },
                status.HTTP_404_NOT_FOUND,
            )
