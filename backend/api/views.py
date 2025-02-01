from rest_framework.response import Response
from rest_framework import viewsets
from .models import Client, Translator
from .serializers import ClientSerializer, TranslatorSerializer
from ai.matching import calculate_compatibility


class MatchingViewSet(viewsets.ViewSet):
    def list(self, request):
        client = Client.objects.get(pk=request.query_params['client_id'])
        translators = Translator.objects.filter(languages__contains=client.language)

        results = [{
            'translator': TranslatorSerializer(t).data,
            'score': calculate_compatibility(client, t)
        } for t in translators]

        return Response(sorted(results, key=lambda x: x['score'], reverse=True)[:3])
