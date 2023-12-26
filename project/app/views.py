import mimetypes

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .forms import ContactForm
from .models import UserInfo, Project, Contact


class BaseView(TemplateView):
    user = UserInfo.objects.get(username='hangochieu123')
    object_list = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info'] = self.user
        return context


# Create your views here.
class IndexView(BaseView):
    model = UserInfo
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all().order_by('-start_date')
        # context['user_info'] = self.user
        context['skills'] = self.user.skills.all()
        context['project_list'] = projects
        return context


class ContactView(BaseView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            new_contact = Contact(name=name, email=email, message=message)
            new_contact.save()
            return HttpResponseRedirect("/")
        return render(request, self.template_name, {"form": form})


class AboutView(BaseView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['short_introduction'] = self.user.get_short_introduction()
        return context


class ProjectsView(ListView, BaseView):
    model = Project
    template_name = 'projects.html'
    # queryset = Project.objects.all()
    # context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()
        # print(context['project_list'])
        return context

    def get_queryset(self):
        return Project.objects.all()

