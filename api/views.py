
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import EmailSerializer


class SendEmailAPI(APIView):
    @swagger_auto_schema(
        operation_description="Ajout Register",

        request_body=EmailSerializer,

    )
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            to_email = serializer.validated_data['to_email']
            send_mail(subject, message, 'iffenquizz@gmail.com', [to_email])
            return Response({"message": "Email sent successfully"})
        return Response(serializer.errors, status=400)
