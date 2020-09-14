from django.shortcuts import render
from django.views.generic import View

from courses.models import Course


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        stats = {
            'course_count': Course.objects.count()
        }
        return render(request, self.template_name, {'stats': stats})
