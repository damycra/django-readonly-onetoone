When upgrading from 1.7 to 1.8(.8) I started encountering errors in the admin with a reverse one to one relationship when it was in readonly_fields.  I assume this is a regression.  Naturally, I am happy to help fix it (if it is not by design), given a steer!  

Tested with Python 2.7.10, the project template was created with Django 1.8.8. 

    cd /tmp
    git clone https://github.com/damycra/django-readonly-onetoone.git
    cd django-readonly-onetoone/
    mkvirtualenv dj_onetoone

    # make sure virtualenv is activated, then:
    pip install -r requirements.txt 
    ./manage.py migrate
    ./manage.py createsuperuser 
    ./manage.py runserver
    # open http://127.0.0.1:8000/admin/simple/a/add/
    # create an A object 
    # create a B object referencing the A http://127.0.0.1:8000/admin/simple/b/add
    # return to original A object http://127.0.0.1:8000/admin/simple/a/1/

    # now upgrade to Django 1.8.8
    pip install Django==1.8.8
    ./manage.py migrate
    ./manage.py runserver
    # return to http://127.0.0.1:8000/admin/simple/a/1/
    ### AttributeError at /admin/simple/a/1/
    ### OneToOneRel object has no attribute 'rel'

    # now upgrade to Django 1.9.1
    pip install Django==1.9.1
    ./manage.py migrate
    ./manage.py runserver
    # go to http://127.0.0.1:8000/admin/simple/a/1/change/
    ### AttributeError at /admin/simple/a/1/change/
    ### 'OneToOneRel' object has no attribute 'flatchoices'

A simple workaround is to use a method on ModelAdmin

    class WorkingAAdmin(admin.ModelAdmin):
        readonly_fields = ['working_b']
        def working_b(self, instance):
            return instance.b
        working_b.short_description = 'working'

See also [https://code.djangoproject.com/ticket/24851#comment:8 https://code.djangoproject.com/ticket/24851#comment:8]
 