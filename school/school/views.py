from django.conf import settings
from django.shortcuts import render
from django.views.generic import View

from courses.models import Course
from .email_worker import send_email, queue


class ContactView(View):

    def get(self, request):
        return render(request, 'contacts.html', {})

    def post(self, request):
        # отсылаем письмо заявителю
        queue.enqueue(
            send_email,
            request.POST["feedback_email"],
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
            f"We got feedback from {request.POST['feedback_email']!r}, "
            f"theme: {request.POST['feedback_theme']!r}, "
            f"message: {request.POST['feedback_message']!r}"
        )
        return render(request, 'contacts.html', {'message': True})


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        stats = {
            'course_count': Course.objects.count()
        }
        return render(request, self.template_name, {'stats': stats})


class FrontendView(View):
    template_name = 'frontend.html'

    def get(self, request):
        return render(request, self.template_name, {})
