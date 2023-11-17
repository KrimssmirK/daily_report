# from django.http import HttpResponse
# from django.template import loader
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Transaction

# function-based
# def reportPageView(request):
#   template = loader.get_template('report.html')
#   return HttpResponse(template.render())

# class-based
class ReportPageView(CreateView):
  model = Transaction
  template_name = 'report.html'
  fields = "__all__"
  success_url = reverse_lazy('report')
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    messages.success(self.request, "Success to report!")
    return super(ReportPageView, self).form_valid(form)