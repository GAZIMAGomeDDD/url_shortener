from rest_framework import serializers

from .models import ShortLink, CustomShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    short_link = serializers.CharField(
        read_only=True,
        max_length=10
    )
    url = serializers.CharField(max_length=253)

    class Meta:
        model = ShortLink
        fields = ('short_link', 'url')


class CustomShortLinkSerializer(serializers.ModelSerializer):
    custom_short_link = serializers.CharField(
        max_length=100
    )
    url = serializers.URLField()

    class Meta:
        model = CustomShortLink
        fields = ('custom_short_link', 'url')


class GetURLSerializer(serializers.Serializer):
    short_link = serializers.CharField()
