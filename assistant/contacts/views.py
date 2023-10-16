from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
@login_required
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        birthdate = request.POST['birthdate']

        new_contact = Contact(name=name, address=address, phone=phone, email=email, birthdate=birthdate)
        new_contact.save()

        return redirect('contact_list')

    return render(request, 'contacts/add_contact.html')
@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.address = request.POST['address']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.birthdate = request.POST['birthdate']

        contact.save()
        return redirect('contact_list')

    return render(request, 'contacts/edit_contact.html', {'contacts': contact})
@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'contacts/delete_contact.html', {'contacts': contact})
@login_required
def search_contacts(request):
    search_query = request.GET.get('search_query')
    if search_query:
        # Якщо search_query не порожній, виконуємо пошук
        contacts = Contact.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
    else:
        # Якщо search_query порожній, показуємо всі контакти
        contacts = Contact.objects.all()
    return render(request, 'contacts/search_contacts.html', {'contacts': contacts})
@login_required
def upcoming_birthdays(request):
    from datetime import date
    today = date.today()
    next_month = today.replace(day=1, month=today.month + 1)
    contacts = Contact.objects.filter(
        birthdate__gte=today,
        birthdate__lt=next_month
    )
    return render(request, 'contacts/upcoming_birthdays.html', {'contacts': contacts})
