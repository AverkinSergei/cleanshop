from django.views.generic import TemplateView

from .models import Product


class MainView(TemplateView):
    template_name = 'catalog/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.published()
        return context
