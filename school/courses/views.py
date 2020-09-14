from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views.generic import DeleteView, UpdateView, View

from .forms import CourseForm
from .models import Course


class CourseListView(View):
    template_name = 'courses/course_list.html'

    def get(self, request):
        courses = Course.objects.all()
        return render(request, self.template_name, {'courses': courses})


class CourseView(View):
    template_name = 'courses/course.html'

    def get(self, request, pk):
        course = get_object_or_404(Course.objects.all(), pk=pk)
        return render(request, self.template_name, {'course': course})


class CourseCreateView(View):

    form = CourseForm

    def get(self, request):
        form = self.form()
        return render(request, 'courses/course_add.html', context={"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:course_list')
        else:
            return render(request, 'courses/course_add.html', context={"form": form})


class CourseDeleteView(DeleteView):
    template_name = 'courses/course_delete.html'
    model = Course

    def get_success_url(self):
        return reverse('courses:course_list')


class CourseEditView(UpdateView):
    template_name = 'courses/course_add.html'
    form_class = CourseForm
    model = Course
