from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.utils.http import is_safe_url
from django.views.generic import DeleteView, UpdateView, View

from .forms import CourseForm, LessonForm
from .models import Course, Lesson


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
        return render(request, 'courses/course_add.html', {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj.get_absolute_url())
        else:
            return render(request, 'courses/course_add.html', {"form": form})


class CourseDeleteView(DeleteView):
    template_name = 'courses/course_delete.html'
    model = Course

    def get_success_url(self):
        return reverse('courses:course_list')


class CourseEditView(UpdateView):
    template_name = 'courses/course_edit.html'
    form_class = CourseForm
    model = Course


class CourseSubmitView(LoginRequiredMixin, View):

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.participants.add(request.user)
        course.save()
        return redirect(course.get_absolute_url())

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.participants.remove(request.user)
        course.save()
        return redirect(course.get_absolute_url())


class LessonCreateView(View):

    form = LessonForm

    def get(self, request):
        form = self.form()
        return render(request, 'courses/lesson_add.html', {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj.course.get_absolute_url())
        else:
            return render(request, 'courses/lesson_add.html', {"form": form})


class LessonDeleteView(DeleteView):
    template_name = 'courses/lesson_delete.html'
    model = Lesson

    def get_success_url(self):
        return reverse('courses:course_list')


class LessonEditView(UpdateView):
    template_name = 'courses/lesson_edit.html'
    form_class = LessonForm
    model = Lesson

    def get_success_url(self):
        fields = self.get_form_kwargs()
        course = get_object_or_404(Course.objects.all(), pk=fields["data"]["course"])
        return course.get_absolute_url()
