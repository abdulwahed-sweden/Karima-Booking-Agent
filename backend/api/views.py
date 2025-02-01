# api/views.py
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Client, Translator
from .serializers import TranslatorSerializer
from ai.matching import calculate_compatibility

class MatchingViewSet(viewsets.ViewSet):
    def list(self, request):
        client_id = request.GET.get('client_id')

        # إذا لم يتم إرسال `client_id`، قم بإرجاع رسالة خطأ
        if not client_id:
            return Response({'error': 'Missing required parameter: client_id'}, status=400)

        # التأكد من أن العميل موجود
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            return Response({'error': f'Client with id {client_id} not found'}, status=404)

        # جلب المترجمين المطابقين
        translators = Translator.objects.filter(languages__contains=client.language)
        results = [{
            'translator': TranslatorSerializer(t).data,
            'score': calculate_compatibility(client, t)
        } for t in translators]

        return Response(sorted(results, key=lambda x: x['score'], reverse=True)[:3])
