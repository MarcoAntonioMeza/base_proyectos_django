from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

#def pages(request):
#    context = {}
#    # All resource paths end in .html.
#    # Pick out the html file name from the url. And load that template.
#    try:
#
#        load_template = request.path.split('/')[-1]
#
#        if load_template == 'admin':
#            return HttpResponseRedirect(reverse('admin:index'))
#        context['segment'] = load_template
#
#        html_template = loader.get_template('home/' + load_template)
#        return HttpResponse(html_template.render(context, request))
#
#    except template.TemplateDoesNotExist:
#        #pass
#        html_template = loader.get_template('home/page-404.html')
#        return HttpResponse(html_template.render(context, request))
#
#    except:
#        html_template = loader.get_template('home/page-500.html')
#        return HttpResponse(html_template.render(context, request))
