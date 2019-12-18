from django.contrib.auth.models import User
from django.core.mail import send_mail
from nextmotion.settings import EMAIL_HOST_USER
from service_objects.services import Service

from .models import Invitation


def send_varification_email(subject, message, email):
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        html_message=message,
        fail_silently=False,
    )


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
        try:
            email = invitation.email
            subject = "You got invitation for this email "
            message = 'Invitation Email for this {0}'.format(email)
            send_varification_email(subject, message, email)
        except Exception:
            # DOTO: I'm temp it's becouse if user not add EMAIL_HOST_USER and pwd.
            pass
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
            try:
                email = invitation.email
                subject = "You change invitation"
                message = 'Update Invitation Email for this email {0}'.format(email)
                send_varification_email(subject, message, email)
            except Exception:
                # DOTO: I'm temp it's becouse if user not add EMAIL_HOST_USER and pwd.
                pass
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
