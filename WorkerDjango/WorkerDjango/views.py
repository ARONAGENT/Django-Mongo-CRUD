from django.shortcuts import render
from .services import WorkersOperation
def home(request):
    return render(request,'index.html')

def workerform(request):
    return render(request,'WorkersEntryForm.html')

def insertWorker(request):
    if request.method=='POST':
        status={}
        try:
            wid=int(request.POST.get("workerId"))
            nm=request.POST.get("name")
            dp=request.POST.get("department")
            post=request.POST.get("post")
            sal=float(request.POST.get("salary"))
            loc=request.POST.get("location")
            dic={}
            dic['workerId']=wid
            dic['name']=nm
            dic['department']=dp
            dic['post']=post
            dic['salary']=sal
            dic['location']=loc
            obj=WorkersOperation()
            data=obj.insertWorker(dic)
        except:
            print("Can't Insert")
    return render(request,'DoneWorkerInsert.html',{'status':data})

def allworkers(request):
    dic={}
    obj=WorkersOperation()
    data=obj.listworkers()
    return render(request,"AllWorkers.html",{'values':data})

def upsalform(request):
    return render(request,"UpSalaryForm.html")

def upincstat(request):
    if request.method=="POST":
        dic={}
        wid=int(request.POST.get('workerId'))
        incsal=float(request.POST.get('salary'))
        dic['workerId']=wid
        dic['salary']=incsal
        obj=WorkersOperation()
        data=obj.incrementsal(dic)
    return render(request,"DoneIncSal.html",{'status':data})

def delworkerform(request):
    return render(request,"DeleteWorkerForm.html")

def delworker(request):
    if request.method=="POST":
        wid=int(request.POST.get('workerId'))
        dic={}
        dic['workerId']=wid
        obj=WorkersOperation()
        data=obj.deleteWorker(dic)
    return render(request,"DoneDeleteWorker.html",{'status':data})

    

        