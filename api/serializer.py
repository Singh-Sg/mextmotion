import dateutil.parser
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Invitation


class GetAllInvitationSerializer(serializers.ModelSerializer):
    """
    'id': <str>, 
    'createdTime': <str iso 8601 format>,
    'seconds': <int> The time since the invitation has been created in seconds
    'email': <str>,
    'used': <bool>
    'creatorEmail': <str>, 
    'creatorFullname': <str> Example: John Oliver,
    """

    id = serializers.CharField()
    createdTime = serializers.SerializerMethodField("iso_8601_format")
    seconds = serializers.SerializerMethodField("get_seconds")
    email = serializers.CharField()
    used = serializers.BooleanField()
    creatorEmail = serializers.ReadOnlyField(source="creator.email", read_only=True)
    creatorFullname = serializers.SerializerMethodField("get_full_name")

    class Meta:
        model = Invitation
        fields = [
            "id",
            "createdTime",
            "seconds",
            "email",
            "used",
            "creatorEmail",
            "creatorFullname",
        ]

    def get_full_name(self, obj):
        return "{} {}".format(obj.creator.first_name, obj.creator.last_name)

    def get_seconds(self, obj):
        return "{}".format(str(obj.created_time.time())[6:8])

    def iso_8601_format(self, obj):
        return dateutil.parser.parse(str(obj.created_time))


class CreateInvitationSerializer(serializers.ModelSerializer):
    """
    """

    email = serializers.EmailField()
    creator = serializers.IntegerField()

    class Meta:
        model = Invitation
        fields = ["email", "creator"]


class UpdateInvitationSerializer(serializers.ModelSerializer):
    """
    """

    email = serializers.EmailField(required=False)
    used = serializers.NullBooleanField(required=False)

    class Meta:
        model = Invitation
        fields = ["email", "used"]
