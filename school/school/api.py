from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .email_worker import send_email, queue


@api_view(['POST'])
def contacts_view(request):

    # отсылаем письмо заявителю
    queue.enqueue(
        send_email,
        request.data["email"],
        settings.FROM_EMAIL,
        "Thank for you feedback!",
        "Your feedback was sent to admins!"
    )

    # отсылаем письмо админу о новом сообщении
    queue.enqueue(
        send_email,
        settings.ADMIN_EMAIL,
        settings.FROM_EMAIL,
        "New feedback!",
        f"We got feedback from {request.data['email']!r}, "
        f"theme: {request.data['theme']!r}, "
        f"message: {request.data['message']!r}"
    )
    response = {
      "status": "ok",
      "response": "Your feedback was sent."
    }

    return Response(response)
