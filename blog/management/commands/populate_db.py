from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog import models

class Command(BaseCommand):
    help = "Populates the database with testing data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Started database population process"))

        if User.objects.filter(username="manuelinfosec").exists():
            self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
            return
        
        # Create users
        user_1 = User.objects.create_user(username="manuelinfosec", password="2ojklhiih24i2b0ui20-!")
        user_1.first_name = "Manuel"
        user_1.last_name = "Infosec"
        user_1.save()

        user_2 = User.objects.create_user(username="mary", password="kn(84084-48)!")
        user_2.first_name = "Mary"
        user_2.last_name = "Ake"
        user_2.save()

        user_3 = User.objects.create_user(username="Jonah", password="isal2449282__")
        user_3.first_name = "Jonah"
        user_3.last_name = "Clinton"
        user_3.save()

        # Create categories
        system_admin = models.Category.objects.create(name="System Administration")