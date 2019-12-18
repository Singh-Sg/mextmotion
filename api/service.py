from datetime import datetime
from django.contrib.auth.models import User
from service_objects.services import Service

from .models import Invitation


class GetAllInvitationsService(Service):
    """
    This class can fetch all invitation item .
    """

    def process(self):
        """
        :return: invitations lists detail
        """
        invitations = Invitation.objects.all()
        return invitations


class CreateInvitationsService(Service):
    """
    This class can create invitation.
    """

    def process(self):
        """
        :return:invitation
        """
        creator = User.objects.get(id=self.data.get("serial_data").get("creator"))
        invitation = Invitation.objects.create(
            email=self.data.get("serial_data").get("email"), creator=creator
        )
        return invitation


class UpdateInvitationsService(Service):
    """
    This class can fetch specific item and partial update.
    """

    def process(self):
        """
        :return:Update invitation
        """
        invitation = Invitation.objects.get(id=self.data.get("invitations_id"))
        email = self.data.get("email")
        if email:
            invitation.email = self.data.get("email")
        used = self.data.get("used")
        if used:
            invitation.used = self.data.get("used")
        invitation.save()
        return invitation


class DeleteInvitationsService(Service):
    """
    This call will delete Invitations objects.
    """

    def process(self):
        """
        :return:None
        """
        invitations = Invitation.objects.get(id=self.data.get("invitations_id"))
        invitations.delete()
