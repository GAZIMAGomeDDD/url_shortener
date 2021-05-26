from django.db import IntegrityError
from django.db.models import Q
from hashids import Hashids
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import ShortLink, CustomShortLink, URL
from .serializers import ShortLinkSerializer, CustomShortLinkSerializer, GetURLSerializer
from rest_framework import status
from urllib import request


def valid_url(url):
    try:
        request.urlopen(url)
        return True
    except:
        return False


class CreateShortLinkView(CreateAPIView):
    serializer_class = ShortLinkSerializer

    def create(self, *args, **kwargs):
        data = self.request.data
        url = data.get('url')
        scheme = url.split('://')[0].lower()

        if scheme not in ('http', 'https'):
            url = 'https://' + url

        query_set = URL.objects.all()

        try:
            url_object = query_set.get(url=url)

            try:
                short_link_object = ShortLink.objects.create(
                    url=url_object,
                    short_link=Hashids(
                        salt=url
                    ).encode(1, 2, 3)
                )

            except IntegrityError:
                short_link_object = url_object.shortlink

            return Response(
                data={
                    'url': url,
                    'short_link': short_link_object.short_link
                },
                status=status.HTTP_201_CREATED
            )

        except query_set.model.DoesNotExist:
            if not valid_url(url):
                return Response(
                    {'error': 'Unable to shorten that link. It is not a valid url.'}
                )

            url_object = URL.objects.create(url=url)
            short_link_object = ShortLink.objects.create(
                url=url_object,
                short_link=Hashids(
                    salt=url
                ).encode(1, 2, 3)
            )

            return Response(
                data={
                    'url': url,
                    'short_link': short_link_object.short_link
                },
                status=status.HTTP_201_CREATED
            )


class CreateCustomShortLinkView(CreateAPIView):
    serializer_class = CustomShortLinkSerializer

    def create(self, *args, **kwargs):
        data = self.request.data
        custom_short_link = data.get('custom_short_link')
        url = data.get('url')
        scheme = url.split('://')[0].lower()

        if scheme not in ('http', 'https'):
            url = 'https://' + url
        if CustomShortLink.objects.filter(custom_short_link=custom_short_link):
            return Response({'error': 'Such a custom link already exists!'})

        if not valid_url(url):
            return Response(
                {'error': 'Unable to shorten that link. It is not a valid url.'}
            )

        query_set = URL.objects.all()

        try:
            url_object = query_set.get(url=url)
            custom_short_link_object = CustomShortLink.objects.create(
                url=url_object,
                custom_short_link=custom_short_link
            )

            return Response(
                data={
                    'url': url,
                    'custom_short_link': custom_short_link_object.custom_short_link
                },
                status=status.HTTP_201_CREATED
            )

        except query_set.model.DoesNotExist:
            url_object = URL.objects.create(url=url)
            custom_short_link_object = CustomShortLink.objects.create(
                url=url_object,
                custom_short_link=custom_short_link
            )

            return Response(
                data={
                    'url': url,
                    'custom_short_link': custom_short_link_object.custom_short_link
                },
                status=status.HTTP_201_CREATED
            )


class GetURL(RetrieveAPIView):
    serializer_class = GetURLSerializer

    def retrieve(self, *args, **kwargs):
        short_link = self.request.path.split('/')[-1]
        url = URL.objects.filter(
            Q(short__short_link=short_link) | Q(custom_short__custom_short_link=short_link)
        )

        return Response({'url': url[0].url})
