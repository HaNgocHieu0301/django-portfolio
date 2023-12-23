import mimetypes

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserInfo


# Create your views here.
class IndexView(TemplateView):
    model = UserInfo
    template_name = 'index.html'
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = UserInfo.objects.get(username='hangochieu123')
        context['user_info'] = user
        context['skills'] = user.skills.all()
        print('test')
        print()
        return context


def contact(request):
    return render(request, 'contact.html')


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_info = UserInfo.objects.get(username='hangochieu123')
        context['short_introduction'] = user_info.get_short_introduction()
        return context


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'projects.html')


# def download_file(request):
#     # fill these variables with real values
#     fl_path = '../static/uploads/cd.pdf'
#     filename = 'cv.pdf'
#
#     fl = open(fl_path, 'r')
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response
