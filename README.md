# Django-Elasticsearch

## Project Objective
Aimed at integrating Django REST Framework (DRF) with Elasticsearch, using Django to model data and DRF to seriailze and serve it. Data is indexed and made searchable with ElasticSearch from the ELK Stack.

## Routes
The application has the following URLs:

`/blog/user/` lists all users.
`/blog/user/<USER_ID>/` fetches a specific user.
`/blog/category/` lists all categories.
`/blog/category/<CATEGORY_ID>/` fetches a specific category.
`/blog/article/` lists all articles.
`/blog/article/<ARTICLE_ID>/` fetches a specific article.