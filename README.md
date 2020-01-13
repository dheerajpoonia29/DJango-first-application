# Django-first-application

## START DJANGO PROJECT
django-admin startproject projectMame

## START DJANGO APP
python3 manage.py startapp appName '''

## INIT SETTING

    1.  make change to urls.py
            from djangofir.contrib import admin
            from django.urls import include, path
            urlpatterns = [
                path('', include('appName.urls')),
                path('admin/', admin.site.urls)
            ]
    2.  make change to app/urls.py
            from django.urls import path
            from . import views
            urlpatterns = [
                path("", views.index, name="index"),
            ]
    3.  build app.views.py
            from django.shortcuts import render
            from django.http import HttpResponse
            def index(request):
                return HttpResponse("Application is successfully run")
    4. tell setting.py about over new app
            // look for installed app
            '<appName>.apps.<appName>Config', // paste into at above

## MAKE DATABASE & TABLE

    1.  create model  // modelName = tableName
            class <modelName>(models.Model):
                attributesName = modelName.dataType(constraints)  
                // E.g dataType = IntegerField(), CharField(max_length=64)
    2.  make migrations
            $ python3 manage.py makemigrations // look change in models.py
            $ python3 manage.py migrate        // make table corressponding to models
    3.  look automatic sql generated by django
            $ python manage.py sqlmigrate appName <migrationNo with extention>
  
## INSERT DATA INTO DATABASE THROUGH PYTHON SHELL

    1.  open shell
            $ python3 manage.py shell
    2.  import modelName/tableName in which we want to insert data
            $ from <appName>.models import <modelName>
    3.  insert data 
            f = tableName( col1="data1", col2="data2", ....)
    4.  commit insertion
            f.save()
    Note: every particular data entry is treated as class oject

## PRINT OR MAKE QUERY TO DATABASE

    1.  $ <modelName>.objects.all()
        return : <QuerySet [<GetData: GetData object (1)>, <GetData: GetData object (2)>]>
    
    2.  print attributes/col value instead of object no
        2.1 open <appName>.models.py & inside particular mode wirte str function
            Note: def __str__(self): > define that what the object look like & print to screen/html
            def modelName(models.Model):
                var1=models.datatype(contraint)
                var2=models.datatype(contraint)
                    def __str__(self):
                        return f"{self.var1} and {self.var2}"
    
    3.  $ <modelName>.objects.all()
        return : <QuerySet [<GetData: kratik, 65 >, <GetData: ashish, 2 >]>
    
    4.  select particular field/object from table 
            $ obj = modelName.objects.get(colName="instanceName")

## OPERATION ON STORED DATABASE

    1. access to particular object 
        1.1 select field by coloumn
            $ obj = <modelName>.objects.get(colName="value")
            $ obj
            return : <modelName: val1, val >
        1.2 f = <modelName>.objects.first()
        f
            return : <QuerySet [<GetData: kratik, 65 >
        f.fname
            return : kratik
        f.rollNo
            return : 65
    
    2. delete to particular object
        f.delete()

## WORKING WITH <appName>/views.py file

    1. basic initialize function
        from django.shortcuts import render // for rendering template
        from django.http import HttpResponse // for return http response
    
    note: function name in view called view
    
    2. return http response
        return HttpResponse("response working")
    
    3. render html template
        return render(request, "<appName>/index.html")

## WORKING WITH APP ADMIN FILE

    Note:   django come with built in app could admin which 
            make very easy to add or modify existing data, we no need to 
            open over database
    
    1.  admin interface want know about the model created in models.py
        from .models import modelName1, modalName2
    
    2.  registering modal at admin panel, which manipulate via panel
        admin.site.register(modelName1)
        admin.site.register(modelName2)
    3.  before access to admin first need to login to admin site
        $ python manage.py createsuperuser