from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie_items.models import Items


class ItemsView(LoginRequiredMixin, ListView):
    model = Items
    template_name = 'aplicatie_items/items_index.html'
    paginate_by = 5
    queryset = model.objects.filter(status=1)
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        data = super(ItemsView, self).get_context_data(*args, **kwargs)
        # data['locations'] = self.model.objects.filter(active=1)
        return data

class CreateItemView(LoginRequiredMixin, CreateView):
    model = Items
    fields = '__all__'
    template_name = 'aplicatie_items/item_form.html'

    def get_success_url(self):
        return reverse('items:items_list')

class EditItemView(LoginRequiredMixin, UpdateView):
    model = Items
    fields = '__all__'
    template_name = 'aplicatie_items/item_form.html'

    def get_success_url(self):
        return reverse('items:items_list')

@login_required
def delete_item(request, pk):
    Items.objects.filter(id=pk).update(status=0)
    return redirect('items:items_list')

@login_required
def activate_item(request, pk):
    Items.objects.filter(id=pk).update(status=1)
    return redirect('items:items_list')

class GetItemView(LoginRequiredMixin, UpdateView):
    model = Items
    fields = ['quantity']
    template_name = 'aplicatie_items/item_form.html'

    def get_success_url(self):
        return reverse('items:items_list')


class ItemsInactiveView(LoginRequiredMixin, ListView):
    model = Items
    template_name = 'aplicatie_items/items_index.html'
    paginate_by = 5
    queryset = model.objects.filter(status=0)
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        data = super(ItemsInactiveView, self).get_context_data(*args, **kwargs)
        # data['locations'] = self.model.objects.filter(active=0)
        return data


def search_item(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        result = Items.objects.filter(name__containts=searched)
        return render(request, 'aplicatie_items/search.html', {'searched': searched, 'result': result})
    else:
        return render(request, 'aplicatie_items/search.html', {})