from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student, Marks, User
from django.shortcuts import redirect

# faculty dashboard 
def index(request):
    # if faculty sign in
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
    # else return to auth page
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
    if(request.session.get('user')):
        context = {
            "id": student_id
        }
        request.session['add_id'] = student_id
        return render(request, "add.html", context)
    else:
        request.session['err'] = 5
        return redirect(auth)
    
def submitmark(request):
    if request.method == 'POST' and request.session.get('user'):
        p0 = request.session['add_id']  
        p1 = int(request.POST.get("s1"))
        p2 = int(request.POST.get("s2"))
        p3 = int(request.POST.get("s3"))
        p4 = int(((p1+p2+p3)/300)*100)
        stu = Student.objects.get(pk=p0)
        q = Marks(student=stu, firstSem=p1, secondSem=p2, thirdSem=p3, aggregate=p4)
        q.save()
        del request.session['add_id']
        request.session['error'] = 2
        return redirect(index)

    # if a GET (or any other method) we'll create a blank form
    else:
        request.session['err'] = 5
        return redirect(auth)

def submit(request):
    if request.method == 'POST' and request.session.get('user'):
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
        request.session['err'] = 5
        return redirect(auth)


def auth(request):
    # having err set mean there is err which have eithe success or failed 
    auth_err = 0

    if request.session.get('err'):
        auth_err = request.session['err']
    else:  
        # err 0 : provide auth to open faculty dashboard
        request.session['err']=0    
    context = {
        "auth_err": str(auth_err)
    }
    return render(request,"auth.html", context)

def signup(request):
    if request.method == 'POST':
        

        p1 = request.POST.get("uname")
        p2 = request.POST.get("pass")
        # return HttpResponse('{0} {1}'.format(p1, p2))

        try:
            q = User.objects.get(username=p1)     
            # account already exist 
            request.session['err'] = 2
            return redirect(auth)

        except User.DoesNotExist:
            # populating data and saving into database
            q = User(username=p1, password=p2)
            q.save()   # new account is created 
            #request.session['user']=p1
            request.session['err'] = 1
            return redirect(auth)

def login(request):
    if request.method == 'POST':
        p1 = request.POST.get("uname")
        p2 = request.POST.get("pass")
        try:
            q = User.objects.get(username=p1)     
        except User.DoesNotExist:
            request.session['err'] = 3
            return redirect(auth)

        
        syspass = q.password
        if(p2==syspass):
            request.session['user']=p1
            del request.session['err'] # user in dashboard
            return redirect(index)
        else:
            request.session['err'] = 4
            return redirect(auth)
        

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("error you open page directly")

def logout(request):
    del request.session['user']
    return redirect(auth)