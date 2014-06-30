Kitchen Assistant
=================

A Django-based web application optimized for mobile devices. This application
assists the user in keeping track of ingredients in his/her kitchen. The user
can then:
* Search for recipes *a la* a reverse cookbook
* Create shopping lists and import items directly to his/her kitchen
* Discuss and share recipes via a web forum

### How to Use the Current Source Code
First, clone the current repository:

`git clone https://github.com/bmclear/kitchen-assistant.git`

Then, add a `SECRET_KEY` to line 25 of `my_kitchen/settings.py`. For the
purposes of Django web applications, this key is a long string of 
alphanumeric characters. There are applications online that can generate keys,
but we're too sure of their validity. For more information about Django
`SECRET_KEY`s, see their [page](https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-SECRET_KEY) about the subject.

From the project's root directory, run the following command:

`python manage.py syncdb`

This will create the databases necessary for the application to properly
function. It should ask you to create a superuser account. Just follow the
command-line instructions to do so.

Finally, run the command:

`python manage.py runserver`

This starts a development server which hosts the application via
[localhost](http://localhost:8000/kitchen/). See this [page](https://docs.djangoproject.com/en/1.6/ref/django-admin/#runserver-port-or-address-port) for more
information about running a server.

### Current Progress
* The models have pretty much been designed at this point. These can be found
in `kitchen/models.py`.
* Login/logout features have been implemented (a registration page should be
complete within the next couple of days).
* A mockup of the user's main page has been designed and should be implemented
soon.
