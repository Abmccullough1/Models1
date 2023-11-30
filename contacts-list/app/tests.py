from django.test import TestCase
from app import models


class TestContact(TestCase):
    def test_can_create_contact(self):
        contact = models.create_contact(
            "megamind",
            "megamind@villans,com",
            "191288",
            True,
        )

        self.assertEqual(contact.id, 1)
        self.assertEqual(contact.name, "megamind")
        self.assertEqual(contact.email, "megamind@villans,com")
        self.assertTrue(contact.is_favorite)

    def test_can_view_all_contacts_at_once(self):
        contacts_data = [
            {
                "name": "Batman",
                "email": "Batman@robincantfight.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Megamind",
                "email": "MegaMind@villans.com",
                "phone": "018",
                "is_favorite": False,
            },
            {
                "name": "Ben",
                "email": "Beniswierd@google.com",
                "phone": "9292821",
                "is_favorite": True,
            },
        ]

        for contact_data in contacts_data:
            models.create_contact(
                contact_data["name"],
                contact_data["email"],
                contact_data["phone"],
                contact_data["is_favorite"],
            )

        contacts = models.all_contacts()

        self.assertEqual(len(contacts), len(contacts_data))

        contacts_data = sorted(contacts_data, key=lambda c: c["name"])
        contacts = sorted(contacts, key=lambda c: c.name)

        for data, contact in zip(contacts_data, contacts):
            self.assertEqual(data["name"], contact.name)
            self.assertEqual(data["email"], contact.email)
            self.assertEqual(data["phone"], contact.phone)
            self.assertEqual(data["is_favorite"], contact.is_favorite)

    def test_can_search_by_name(self):
        contacts_data = [
            {
                "name": "Batman",
                "email": "Batman@robincantfight.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Megamind",
                "email": "MegaMind@villans.com",
                "phone": "018",
                "is_favorite": False,
            },
            {
                "name": "Ben",
                "email": "Beniswierd@google.com",
                "phone": "9292821",
                "is_favorite": True,
            },
        ]

        for contact_data in contacts_data:
            models.create_contact(
                contact_data["name"],
                contact_data["email"],
                contact_data["phone"],
                contact_data["is_favorite"],
            )

        self.assertIsNone(models.find_contact_by_name("gyubyiov"))

        contact = models.find_contact_by_name("Batman")

        self.assertIsNotNone(contact)
        self.assertEqual(contact.email, "Batman@robincantfight.com")

    def test_can_view_favorites(self):
        contacts_data = [
            {
                "name": "Batman",
                "email": "Batman@robincantfight.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Megamind",
                "email": "MegaMind@villans.com",
                "phone": "018",
                "is_favorite": False,
            },
            {
                "name": "Ben",
                "email": "Beniswierd@google.com",
                "phone": "9292821",
                "is_favorite": True,
            },
        ]

        for contact_data in contacts_data:
            models.create_contact(
                contact_data["name"],
                contact_data["email"],
                contact_data["phone"],
                contact_data["is_favorite"],
            )

        self.assertEqual(len(models.favorite_contacts()), 2)

    def test_can_update_contacts_email(self):
        contacts_data = [
            {
                "name": "Batman",
                "email": "Batman@robincantfight.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Megamind",
                "email": "MegaMind@villans.com",
                "phone": "018",
                "is_favorite": False,
            },
            {
                "name": "Ben",
                "email": "Beniswierd@google.com",
                "phone": "9292821",
                "is_favorite": True,
            },
        ]

        for contact_data in contacts_data:
            models.create_contact(
                contact_data["name"],
                contact_data["email"],
                contact_data["phone"],
                contact_data["is_favorite"],
            )

        models.update_email("Ben", "Beniswierd@gmail.com")

        self.assertEqual(
            models.find_contact_by_name("Ben").email, "Beniswierd@gmail.com"
        )

    def test_can_delete_contact(self):
        contacts_data = [
            {
                "name": "Batman",
                "email": "Batman@robincantfight.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Megamind",
                "email": "MegaMind@villans.com",
                "phone": "018",
                "is_favorite": False,
            },
            {
                "name": "Ben",
                "email": "Beniswierd@google.com",
                "phone": "9292821",
                "is_favorite": True,
            },
        ]
        for contact_data in contacts_data:
            models.create_contact(
                contact_data["name"],
                contact_data["email"],
                contact_data["phone"],
                contact_data["is_favorite"],
            )

        models.delete_contact("Batman")

        self.assertEqual(len(models.all_contacts()), 2)
