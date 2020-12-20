from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serve Single Page Application
HerokuWebIndex = never_cache(TemplateView.as_view(template_name='herokufe/index.html'))
