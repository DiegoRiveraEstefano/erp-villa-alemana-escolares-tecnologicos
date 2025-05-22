from functools import cached_property

from django.views.generic import ListView

CACHE_ERROR_MESSAGE = "Cache timeout exceeded"
CACHE_KEY_ERROR_MESSAGE = "Cache key not set"
CACHE_TIMEOUT_ERROR_MESSAGE = "Cache timeout not set"
FILTER_SET_ERROR_MESSAGE = "Filterset class not set"
CACHE_KEY_ERROR_MESSAGE = "Cache key not set"


class PaginatedFilteredListView(ListView):
    filterset_class = None
    paginate_by = 10

    @cached_property
    def get_filterset_class(self):
        if not hasattr(self, "filterset_class") or self.filterset_class is None:
            raise AttributeError(FILTER_SET_ERROR_MESSAGE)
        return self.filterset_class

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.get_filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context
