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
        seo_optimization = models.Category.objects.create(name="SEO Optimization")
        programming = models.Category.objects.create(name="Programming")

        # Create articles
        website_articles = models.Article.objects.create(
            title="How to code and deploy a website?",
            author=user_1,
            type="TU",
            content="There are numerous ways to code and deploy a website..."
        )
        website_articles.save()
        website_articles.categories.add(programming, system_admin, seo_optimization)

        google_articles = models.Article.objects.create(
            title = "How to rank higher on Google",
            author=user_2,
            type="RS",
            content="The best programming languages are: 1. Python\n2. JavaScript\n3. C/C++" 
        )
        google_articles.save()
        google_articles.categories.add(seo_optimization)

        ubuntu_article = models.Article.objects.create(
           title="Installing the latest version of Ubuntu",
           author=user_3,
           type="TU",
           content="In this tutorial, we'll take a look at how to setup the latest version of Ubuntu. Ubuntu "
                   "(/ʊ'bʊntu:/ is a Linux distribution based on Debian and composed mostly of free and open-source"
                   " software. Ubuntu is officially released in three editions: Desktop, Server, and Core for "
                   "Internet of things devices and robots.",
        )
        ubuntu_article.save()
        ubuntu_article.categories.add(system_admin)

        django_article = models.Article.objects.create(
           title="Django REST Framework and Elasticsearch",
           author=user_3,
           type="TU",
           content="In this tutorial, we'll look at how to integrate Django REST Framework with Elasticsearch. "
           "We'll use Django to model our data and DRF to serialize and serve it. Finally, we'll index the data "
           "with Elasticsearch and make it searchable.",
        )
        django_article.save()
        django_article.categories.add(system_admin)


        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))