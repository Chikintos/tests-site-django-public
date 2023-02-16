from contextlib import redirect_stderr
from multiprocessing import context
import re
from telnetlib import PRAGMA_HEARTBEAT
from django.shortcuts import render,redirect
import time

from .models import *
# Create your views here.
def index(request):
    return render(request, "test_app\index.html")

def testedit(request,id):
    test = Test.objects.filter(id=id)
    answers=Answer.objects.filter(Test=id)
    variants=[]
    for el in answers:
        variants.append(Variants.objects.filter(Answer=el.id))        
    # variants=[Variants.objects.filter(Answer=el)]
    
    context={
        'Test':test,
        'Answer':answers,
        'Variants':variants,
    }
    return render(request, "test_app/testedit.html",context)

def add_question(request,testid):
    answr=Answer()
    answr.name=''
    answr.description='Не вказано'
    answr.Test_id=testid
    answr.save()
    return redirect( f"/test/{testid}")

def remove_question(request,testid,questid):
    Answer.objects.filter(id=questid).delete()

    return redirect( f"/test/{testid}")
    pass

def add_variant(request,id,testid):
    vars=Variants()
    vars.name=''

    vars.Answer_id=id #Answer.objects.filter(id=testid)
    vars.save()
    return redirect( f"/test/{testid}")

def delete_variant(request,id,testid):
    Variants.objects.filter(id=id).delete()
    return redirect( f"/test/{testid}") 

def savetest(request):
    
    reqdict=request.POST
    test=Test.objects.get(id=reqdict["test_id"])
    time1=time.time()
    vars=Variants.objects
    anses=Answer.objects
    for el in reqdict:
        splited_el=el.split(",")
        
        if splited_el[0]=="variant":
            var=vars.get(id=splited_el[2])
            var.is_right=False
            var.save()
    for el in reqdict:
        splited_el=el.split(",")
        if splited_el[0]=="test_name":
            test.name=reqdict["test_name"]
        if splited_el[0]=="answer":
            answer=anses.get(id=splited_el[1])
            answer.name=reqdict[el]
            answer.save()
        if splited_el[0]=="answer_point":
            answer=anses.get(id=splited_el[1])
            answer.point=reqdict[el]
            answer.save()
        if splited_el[0]=="variant":
            var=vars.get(id=splited_el[2])
            var.name=reqdict[el]
            var.save()
        if splited_el[0]=="variant_isright": 
            var=vars.get(id=reqdict[el])
            var.is_right=True
            var.save()
        time.sleep(0.15)
    test.save()
    time2=time.time()
    print(round(time2-time1,1))
    return redirect( f"/test/1")

   
def testview(request,page):
    tests=Test.objects.all()
    context={
        "tests":tests    
    }
    if len(tests)>10:
        context={
        "tests":tests[(page-1)*10:(page-1)*10+10],
        "pagenumb":[el+1 for el in range(0,int(round(len(tests)/10,0)))],
        "curpage":page
        }

        return render(request, "test_app/testview.html",context)
    return render(request, "test_app/testview.html",context)


def pass_test(request,id):
    test = Test.objects.filter(id=id)
    answers=Answer.objects.filter(Test=id)
    variants=[]
    for el in answers:
        variants.append(Variants.objects.filter(Answer=el.id))        
    # variants=[Variants.objects.filter(Answer=el)]
    
    context={
        'Test':test,
        'Answer':answers,
        'Variants':variants,
    }    

    return render(request,"test_app/passtest.html",context)


def testsubmit(request):
 
    reqdict=request.POST
    vars=Variants.objects
    points=0
    fullpoint=0
    anslist=Answer.objects.filter(Test=reqdict["test_id"])

    for el in anslist:
        fullpoint+=el.point
    for el in reqdict:
        splited_el=el.split(",")
        if splited_el[0]=="variant_isright": 
            var=vars.get(id=reqdict[el])
            if var.is_right:
                points+=var.Answer.point

    prs=points*100/fullpoint
   
    context={
        "resultPoints":points,
        "possiblePoints":fullpoint,
        "prs":round(prs,1),
    }
    return render(request,"test_app/resultpage.html",context)
    