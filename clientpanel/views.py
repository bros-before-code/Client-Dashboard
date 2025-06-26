from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Service
from .forms import ClientForm, ClientServiceForm
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

def dashboard(request):
    clients = Client.objects.all()
    return render(request, 'clientpanel/dashboard.html', {'clients': clients})

@login_required
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    total_service_cost = sum(service.price for service in client.services.all())

    return render(request, 'clientpanel/client_detail.html', {
        'client': client,
        'total_service_cost': total_service_cost
    })

@login_required
def client_edit(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully!')  # ✅ new line
            return redirect('dashboard')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clientpanel/client_edit.html', {'form': form})

@login_required
def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # adjust this to your actual list view name
    else:
        form = ClientForm()
    return render(request, 'clientpanel/client_form.html', {'form': form})

@require_POST
def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('dashboard')

def manage_services(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    all_services = Service.objects.all()

    if request.method == 'POST':
        selected_service_ids = request.POST.getlist('services')
        selected_services = Service.objects.filter(id__in=selected_service_ids)
        client.services.set(selected_services)
        messages.success(request, "Services updated!")
        return redirect('client_detail', client_id=client.id)

    return render(request, 'clientpanel/manage_services.html', {
        'client': client,
        'all_services': all_services,
        'selected_services': client.services.all()
    })

@login_required
def download_invoice(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    services = client.services.all()
    total_service_cost = sum(service.price for service in services)

    template = get_template('clientpanel/invoice.html')
    html = template.render({
        'client': client,
        'total_service_cost': total_service_cost
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Invoice_{client.name}.pdf"'

    pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), dest=response)

    return response