from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student, Marks, User
from django.shortcuts import redirect

def index(request):
    if request.session.get('user'):
        user = request.session['user']
        er = 0
        if request.session.get('error'):
            er = request.session['error']
            del request.session['error']

        context = {
            "students": Student.objects.all(),
            "error": er,
            "user" : user
        }
        return render(request, "index.html", context)
    else:
        return redirect(auth)


def detail(request, student_id):
    try:
        q = Student.objects.get(pk=student_id)
        m = Marks.objects.get(student=q)        
        context = {
            "mark": m
        }   
        return render(request, "detail.html", context)
    except Marks.DoesNotExist:
        request.session['error'] = 1
        return redirect(index)
    
    

def delete(request, student_id):
    try:
        q = Student.objects.get(pk=student_id)
        q.delete()
        request.session['error']=2
        return redirect(index)

    except Marks.DoesNotExist:
        raise Http404("Student record not found.")   


def add(request,  student_id):        
    context = {
        "id": student_id
    }
    request.session['add_id'] = student_id
    return render(request, "add.html", context)

    
def submitmark(request):
    if request.method == 'POST':
        p0 = request.session['add_id']  
        p1 = int(request.POST.get("s1"))
        p2 = int(request.POST.get("s2"))
        p3 = int(request.POST.get("s3"))
        p4 = (p1+p2+p3)//5
        stu = Student.objects.get(pk=p0)
        q = Marks(student=stu, firstSem=p1, secondSem=p2, thirdSem=p3, aggregate=p4)
        q.save()
        del request.session['add_id']
        return redirect(index)

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("error you open page directly")


def submit(request):
    if request.method == 'POST':
        p1 = request.POST.get("name")
        p2 = request.POST.get("rollno")
        try:
            q = Student.objects.get(rollNo=p2)            
        except Student.DoesNotExist:
            q = Student(fName=p1, rollNo=p2)
            q.save()
            return redirect(index)
        request.session['error']=3
        return redirect(index)
        

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("error you open page directly")

def auth(request):
    return render(request,"auth.html")

def authverify(request):
    if request.method == 'POST':
        p1 = request.POST.get("uname")
        p2 = request.POST.get("pass")
        try:
            q = User.objects.get(username=p1)     
            # return on the auth page to signup again       
        except User.DoesNotExist:
            q = User(username=p1, password=p2)
            q.save()
            #request.session['user']=p1
            # user created successfully
            return redirect(auth)
        

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("error you open page directly")

def login(request):
    if request.method == 'POST':
        p1 = request.POST.get("uname")
        p2 = request.POST.get("pass")
        try:
            q = User.objects.get(username=p1)     
            # return on the auth page to signup again       
        except User.DoesNotExist:
            # user does not exit             
            #request.session['user']=p1
            # user created successfully
            return redirect(auth)
        syspass = q.password
        if(p2==syspass):
            request.session['user']=p1
            return redirect(index)
        else:
            return HttpResponse("pass incorrect")
        

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("error you open page directly")

def logout(request):
    del request.session['user']
    return redirect(auth)