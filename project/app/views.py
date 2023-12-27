"""
control request and response for respectively views of app
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import ContactForm
from .models import UserInfo, Project


class BaseView(TemplateView):
    """
    base view for some other views
    """
    user = UserInfo.objects.get(username='hangochieu123')
    object_list = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info'] = self.user
        return context


class IndexView(BaseView):
    """
    index view for home page/starting page
    """
    model = UserInfo
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.user.projects.order_by('-start_date')
        context['skills'] = self.user.skills.all()
        context['project_list'] = projects
        return context


class ContactView(BaseView):
    """
    contact view
    """
    template_name = 'contact.html'
    # form_class = ContactForm

    def get(self, request, *args, **kwargs):
        # form = self.form_class()
        form = ContactForm()
        return render(request, self.template_name, {"form": form, "user_info": self.user})

    def post(self, request):
        """
        create contact form
        """
        # form = self.form_class(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # new_contact = Contact(name=name, email=email, message=message)
            # new_contact.save()
            form.save()
            return HttpResponseRedirect("/")
        print(form)
        return render(request, self.template_name, {"form": form, "user_info": self.user})


class AboutView(BaseView):
    """
    about view
    """
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['short_introduction'] = self.user.get_short_introduction()
        return context


# pylint: disable=too-many-ancestors
class ProjectsView(ListView, BaseView):
    """
    project view
    """
    model = Project
    template_name = 'projects.html'
    # queryset = Project.objects.all()
    # context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = self.user.projects.all()
        # print(context['project_list'])
        return context

    def get_queryset(self):
        return self.user.projects.all()
