""""""
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.generic.base import TemplateResponseMixin


class CustomTemplateMixin(TemplateResponseMixin):
    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        if HttpRequest == 'POST':
            return redirect(reverse('main_page'))
        else:
            return [self.template_name]
