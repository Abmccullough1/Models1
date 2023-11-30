from django.db import models
from typing import Optional


# Create your models here.
class Contacts(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()
    
def create_contact(name, email, phone, favorite) -> Contacts:
    contact = Contacts(name=name, email=email, phone=phone, is_favorite=favorite)
    contact.save()
    return contact
def favorite_contacts() -> Contacts:
    contacts = Contacts.objects.filter(is_favorite=True)
    return contacts
def all_contacts() -> Contacts:
    contacts = Contacts.objects.all()
    return contacts
def update_email(name, new_email) -> Contacts:
    contact = Contacts.objects.get(name=name)
    contact.email = new_email
    contact.save()
    return contact
def find_contact_by_name(name) -> Optional[Contacts]:
    try:
        contacts = Contacts.objects.get(name=name)
        return contacts
    except:
        return None
def delete_contact(name):
    contact = Contacts.objects.get(name=name)
    contact.delete()
    return contact

