from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import AGrammer51 as AG51
from .models import AGrammer54 as AG54
from .models import AGrammar54M as AG54M
from .models import AMorphology54 as AM54
from .models import AMorphology54M as AM54M
from .models import AMorphology51 as AM51
from .models import AGMA5GoldenM as AGMAG5M
from .models import AGMA5Golden as AGMAG5
from .models import AGMA5Priveos as AGMA5P
from .models import AGMA5PriveosS as AGMA5PS
from .models import APhilology as AI
from .models import HPhilology as HI
from .models import GPhilology as GI
from .models import PPhilology as PI
from .models import AAbbasiPoetry as AA
from .models import HAbbasiPoetry as HA
from .models import GAbbasiPoetry as GA
from .models import PAbbasiPoetry as PA
from .models import AAndalusianPoetry as AAn
from .models import HAndalusianPoetry as HAn
from .models import GAndalusianPoetry as GAn
from .models import PAndalusianPoetry as PAn
from .models import ADohman1 as AD1
from .models import ADohman4M as AD4M
from .models import ADohman4 as AD4
from .models import ANawal1 as AN1
from .models import ANawal4 as AN4
from .models import ANawal4M as AN4M
from .models import GCritique as GC
from .models import GCritiqueM as GCM
from .models import PCritique as PC
from .models import PCritiqueS as PCS
from .models import History31 as H1
from .models import History34 as H4
from .models import History34M as H4M
from .models import GHistory3 as GH
from .models import GHistory3M as GHM
from .models import PHistory3 as PH
from .models import PHistory3S as PHS



class Form1(forms.Form):
    file = forms.FileField()

# Create your views here.

def firstsemester(request):
    return render(request, 'thirdyear/firstsemester.html')


def AGMA5(request):
    return render(request, 'thirdyear/AGMA5/AGMA5.html')


def AGrammer5(request):
    return render(request, 'thirdyear/AGMA5/AGrammar5.html', )


def AGrammar51M(request):
    list = AG51.objects.all()

    return render(request, 'thirdyear/AGMA5/AGrammar51M.html', {'name': list})


def AGrammer51(request):
    list = AG51.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AG51(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AGrammar51M')

    return render(request, 'thirdyear/AGMA5/AGrammar51.html', {'names': list, 'form': file})


def AGrammar51E(request, number):
    list = AG51.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AGrammar51M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGrammar51M')

    return render(request, 'thirdyear/AGMA5/AGrammar51E.html', {'name': list})


def AGrammar54M(request):
    list = AG54M.objects.all()

    return render(request, 'thirdyear/AGMA5/AGrammar54M.html', {'names': list})


def AGrammar54E(request, number):
    list = AG54M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AGrammar54M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGrammar54M')

    return render(request, 'thirdyear/AGMA5/AGrammar54E.html', {'name': list})


def AGrammar54Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AG54M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGrammar54M')
    return render(request, 'thirdyear/AGMA5/AGrammar54Add.html')


def AGrammar54(request, number):
    db = AG54M.objects.get(number=number)
    list = AG54.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AG54(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AG54.objects.get(number=number, ExNo=db)
            instance = AG54.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/AGMA5/AGrammar54.html', {'names': list})



def AMorphology5(request):
    return render(request, 'thirdyear/AGMA5/AMorphology5.html')


def AMorphology51M(request):
    list = AM51.objects.all()

    return render(request, 'thirdyear/AGMA5/AMorphology51M.html', {'name': list})


def AMorphology51(request):
    list = AM51.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AM51(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AMorphology51M')

    return render(request, 'thirdyear/AGMA5/AMorphology51.html', {'names': list, 'form': file})


def AMorphology51E(request, number):
    list = AM51.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AMorphology51M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMorphology51M')

    return render(request, 'thirdyear/AGMA5/AMorphology51E.html', {'name': list})


def AMorphology54M(request):
    list = AM54M.objects.all()

    return render(request, 'thirdyear/AGMA5/AMorphology54M.html', {'names': list})


def AMorphology54E(request, number):
    list = AM54M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AMorphology54M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMorphology54M')

    return render(request, 'thirdyear/AGMA5/AMorphology54E.html', {'name': list})


def AMorphology54Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AM54M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AMorphology54M')
    return render(request, 'thirdyear/AGMA5/AMorphology54Add.html')


def AMorphology54(request, number):
    db = AM54M.objects.get(number=number)
    list = AM54.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AM54(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AM54.objects.get(number=number, ExNo=db)
            instance = AM54.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/AGMA5/AMorphology54.html', {'names': list})


def AGMA5GoldenM(request):
    list = AGMAG5M.objects.first()

    return render(request, 'thirdyear/AGMA5/AGMA5GoldenM.html', {'names': list})


def AGMA5GoldenE(request):
    list = AGMAG5M.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AGMA5GoldenM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGMA5GoldenM')

    return render(request, 'thirdyear/AGMA5/AGMA5GoldenE.html', {'name': list})


def AGMA5GoldenAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AGMAG5M(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGMA5GoldenM')
    return render(request, 'thirdyear/AGMA5/AGMA5GoldenAdd.html')


def AGMA5Golden(request):
    db = AGMAG5M.objects.first()
    list = AGMAG5.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = AGMAG5(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGMAG5.objects.get(number=number)
            instance = AGMAG5.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'thirdyear/AGMA5/AGMA5Golden.html', {'names': list})


def AGMA5PriveosS(request):
    list = AGMA5PS.objects.all()
    return render(request, 'thirdyear/AGMA5/AGMA5PriveosS.html', {'name': list})


def AGMA5PriveosAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = AGMA5PS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AGMA5PriveosS')

    return render(request, 'thirdyear/AGMA5/AGMA5PriveosAdd.html')


def AGMA5PriveosM(request, ExNo, semestery):
    list = AGMA5PS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('AGMA5PriveosS')

    return render(request, 'thirdyear/AGMA5/AGMA5PriveosM.html', {'name': list})


def AGMA5Priveos(request, ExNo, semestery):
    PreviosS = AGMA5PS.objects.get(ExNo=ExNo, semestery=semestery)
    list = AGMA5P.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AGMA5P(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                          No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGMA5P.objects.get(number=number, PreviosS=PreviosS)
            instance = AGMA5P.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/AGMA5/AGMA5Priveos.html', {'names': list})


#----------------------------Philology----------------------------------------

def Philology(request):

    return render(request, 'thirdyear/Philology/Philology.html')


def APhilologyM(request):
    list = AI.objects.all()

    return render(request, 'thirdyear/Philology/APhilologyM.html', {'name': list})


def APhilology(request):
    list = AI.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AI(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('APhilologyM')

    return render(request, 'thirdyear/Philology/APhilology.html', {'names': list, 'form': file})


def APhilologyE(request, number):
    list = AI.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('APhilologyM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('APhilologyM')

    return render(request, 'thirdyear/Philology/APhilologyE.html', {'name': list})


def HPhilologyM(request):
    list = HI.objects.all()

    return render(request, 'thirdyear/Philology/HPhilologyM.html', {'name': list})


def HPhilology(request):
    list = HI.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = HI(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('HPhilologyM')

    return render(request, 'thirdyear/Philology/HPhilology.html', {'names': list, 'form': file})


def HPhilologyE(request, number):
    list = HI.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('HPhilologyM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('HPhilologyM')

    return render(request, 'thirdyear/Philology/HPhilologyE.html', {'name': list})


def PhilologyGM(request):
    list = GI.objects.first()
    return render(request, 'thirdyear/Philology/PhilologyGM.html', {'name': list})


def PhilologyG(request):
    list = GI.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = GI(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('PhilologyGM')
    return render(request, 'thirdyear/Philology/PhilologyG.html', {'names': list, 'form': file})


def PhilologyGE(request):
    list = GI.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('PhilologyGM')

    if 'delete' in request.POST:
        member = GI.objects.all()
        member.delete()
        return redirect('PhilologyGM')

    return render(request, 'thirdyear/Philology/PhilologyGE.html', {'name': list})


def PhilologyPM(request):
    list = PI.objects.all()
    return render(request, 'thirdyear/Philology/PhilologyPM.html', {'name': list})


def PhilologyPE(request, pyear, number):
    list = PI.objects.get(pyear=pyear, number=number)
    print(list)
    if 'add' in request.POST:
        pyear = request.POST.get('pyear')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.pyear = pyear
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('PhilologyPM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('PhilologyPM')
    return render(request, 'thirdyear/Philology/PhilologyPE.html', {'name': list})


def PhilologyP(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = PI(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('PhilologyPM')

    return render(request, 'thirdyear/Philology/PhilologyP.html', {'form': file})

#-------------------------------------------AbbasiPoetry-------------------------------------

def AbbasiPoetry(request):

    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetry.html')


def AAbbasiPoetryM(request):
    list = AA.objects.all()

    return render(request, 'thirdyear/AbbasiPoetry/AAbbasiPoetryM.html', {'name': list})


def AAbbasiPoetry(request):
    list = AA.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AA(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AAbbasiPoetryM')

    return render(request, 'thirdyear/AbbasiPoetry/AAbbasiPoetry.html', {'names': list, 'form': file})


def AAbbasiPoetryE(request, number):
    list = AA.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AAbbasiPoetryM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AAbbasiPoetryM')

    return render(request, 'thirdyear/AbbasiPoetry/AAbbasiPoetryE.html', {'name': list})


def HAbbasiPoetryM(request):
    list = HA.objects.all()

    return render(request, 'thirdyear/AbbasiPoetry/HAbbasiPoetryM.html', {'name': list})


def HAbbasiPoetry(request):
    list = HA.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = HA(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('HAbbasiPoetryM')

    return render(request, 'thirdyear/AbbasiPoetry/HAbbasiPoetry.html', {'names': list, 'form': file})


def HAbbasiPoetryE(request, number):
    list = HA.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('HAbbasiPoetryM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('HAbbasiPoetryM')

    return render(request, 'thirdyear/AbbasiPoetry/HAbbasiPoetryE.html', {'name': list})


def AbbasiPoetryGM(request):
    list = GA.objects.first()
    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetryGM.html', {'name': list})


def AbbasiPoetryG(request):
    list = GA.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = GA(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('AbbasiPoetryGM')
    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetryG.html', {'names': list, 'form': file})


def AbbasiPoetryGE(request):
    list = GA.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AbbasiPoetryGM')

    if 'delete' in request.POST:
        member = GA.objects.all()
        member.delete()
        return redirect('AbbasiPoetryGM')

    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetryGE.html', {'name': list})


def AbbasiPoetryPM(request):
    list = PA.objects.all()
    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetryPM.html', {'name': list})


def AbbasiPoetryPE(request, pyear, number):
    list = PA.objects.get(pyear=pyear, number=number)
    print(list)
    if 'add' in request.POST:
        pyear = request.POST.get('pyear')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.pyear = pyear
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AbbasiPoetryPM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AbbasiPoetryPM')
    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetryPE.html', {'name': list})


def AbbasiPoetryP(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = PA(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('AbbasiPoetryPM')

    return render(request, 'thirdyear/AbbasiPoetry/AbbasiPoetryP.html', {'form': file})


#-------------------------------------------AndalusianPoetry-------------------------------------

def AndalusianPoetry(request):

    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetry.html')


def AAndalusianPoetryM(request):
    list = AAn.objects.all()

    return render(request, 'thirdyear/AndalusianPoetry/AAndalusianPoetryM.html', {'name': list})


def AAndalusianPoetry(request):
    list = AAn.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AAn(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AAndalusianPoetryM')

    return render(request, 'thirdyear/AndalusianPoetry/AAndalusianPoetry.html', {'names': list, 'form': file})


def AAndalusianPoetryE(request, number):
    list = AAn.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AAndalusianPoetryM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AAndalusianPoetryM')

    return render(request, 'thirdyear/AndalusianPoetry/AAndalusianPoetryE.html', {'name': list})


def HAndalusianPoetryM(request):
    list = HAn.objects.all()

    return render(request, 'thirdyear/AndalusianPoetry/HAndalusianPoetryM.html', {'name': list})


def HAndalusianPoetry(request):
    list = HAn.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = HAn(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('HAndalusianPoetryM')

    return render(request, 'thirdyear/AndalusianPoetry/HAndalusianPoetry.html', {'names': list, 'form': file})


def HAndalusianPoetryE(request, number):
    list = HAn.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('HAndalusianPoetryM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('HAndalusianPoetryM')

    return render(request, 'thirdyear/AndalusianPoetry/HAndalusianPoetryE.html', {'name': list})


def AndalusianPoetryGM(request):
    list = GAn.objects.first()
    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetryGM.html', {'name': list})


def AndalusianPoetryG(request):
    list = GAn.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = GAn(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('AndalusianPoetryGM')
    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetryG.html', {'names': list, 'form': file})


def AndalusianPoetryGE(request):
    list = GAn.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AndalusianPoetryGM')

    if 'delete' in request.POST:
        member = GAn.objects.all()
        member.delete()
        return redirect('AndalusianPoetryGM')

    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetryGE.html', {'name': list})


def AndalusianPoetryPM(request):
    list = PAn.objects.all()
    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetryPM.html', {'name': list})


def AndalusianPoetryPE(request, pyear, number):
    list = PAn.objects.get(pyear=pyear, number=number)
    print(list)
    if 'add' in request.POST:
        pyear = request.POST.get('pyear')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.pyear = pyear
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AndalusianPoetryPM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AndalusianPoetryPM')
    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetryPE.html', {'name': list})


def AndalusianPoetryP(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = PAn(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('AndalusianPoetryPM')

    return render(request, 'thirdyear/AndalusianPoetry/AndalusianPoetryP.html', {'form': file})

#--------------------------------------------Critique----------------------------------------------------------


def Critique(request):
    return render(request, 'thirdyear/Critique/Critique.html')


def ADohman(request):
    return render(request, 'thirdyear/Critique/ADohman.html', )


def ADohman1M(request):
    list = AD1.objects.all()

    return render(request, 'thirdyear/Critique/ADohman1M.html', {'name': list})


def ADohman1(request):
    list = AD1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AD1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('ADohman1M')

    return render(request, 'thirdyear/Critique/ADohman1.html', {'names': list, 'form': file})


def ADohman1E(request, number):
    list = AD1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('ADohman1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ADohman1M')

    return render(request, 'thirdyear/Critique/ADohman1E.html', {'name': list})


def ADohman4M(request):
    list = AD4M.objects.all()

    return render(request, 'thirdyear/Critique/ADohman4M.html', {'names': list})


def ADohman4E(request, number):
    list = AD4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('ADohman4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ADohman4M')

    return render(request, 'thirdyear/Critique/ADohman4E.html', {'name': list})


def ADohman4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AD4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('ADohman4M')
    return render(request, 'thirdyear/Critique/ADohman4Add.html')


def ADohman4(request, number):
    db = AD4M.objects.get(number=number)
    list = AD4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AD4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AD4.objects.get(number=number, ExNo=db)
            instance = AD4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/Critique/ADohman4.html', {'names': list})



def ANawal(request):
    return render(request, 'thirdyear/Critique/ANawal.html')


def ANawal1M(request):
    list = AN1.objects.all()

    return render(request, 'thirdyear/Critique/ANawal1M.html', {'name': list})


def ANawal1(request):
    list = AN1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AN1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('ANawal1M')

    return render(request, 'thirdyear/Critique/ANawal1.html', {'names': list, 'form': file})


def ANawal1E(request, number):
    list = AN1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('ANawal1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ANawal1M')

    return render(request, 'thirdyear/Critique/ANawal1E.html', {'name': list})


def ANawal4M(request):
    list = AN4M.objects.all()

    return render(request, 'thirdyear/Critique/ANawal4M.html', {'names': list})


def ANawal4E(request, number):
    list = AN4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('ANawal4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ANawal4M')

    return render(request, 'thirdyear/Critique/ANawal4E.html', {'name': list})


def ANawal4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AN4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('ANawal4M')
    return render(request, 'thirdyear/Critique/ANawal4Add.html')


def ANawal4(request, number):
    db = AN4M.objects.get(number=number)
    list = AN4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AN4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AN4.objects.get(number=number, ExNo=db)
            instance = AN4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/Critique/ANawal4.html', {'names': list})


def CritiqueGoldenM(request):
    list = GCM.objects.first()

    return render(request, 'thirdyear/Critique/CritiqueGoldenM.html', {'names': list})


def CritiqueGoldenE(request):
    list = GCM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('CritiqueGoldenM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('CritiqueGoldenM')

    return render(request, 'thirdyear/Critique/CritiqueGoldenE.html', {'name': list})


def CritiqueGoldenAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = GCM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('CritiqueGoldenM')
    return render(request, 'thirdyear/Critique/CritiqueGoldenAdd.html')


def CritiqueGolden(request):
    db = GCM.objects.first()
    list = GC.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = GC(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = GC.objects.get(number=number)
            instance = GC.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'thirdyear/Critique/CritiqueGolden.html', {'names': list})


def CritiquePriveosS(request):
    list = PCS.objects.all()
    return render(request, 'thirdyear/Critique/CritiquePriveosS.html', {'name': list})


def CritiquePriveosAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = PCS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('CritiquePriveosS')

    return render(request, 'thirdyear/Critique/CritiquePriveosAdd.html')


def CritiquePriveosM(request, ExNo, semestery):
    list = PCS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('CritiquePriveosS')

    return render(request, 'thirdyear/Critique/CritiquePriveosM.html', {'name': list})


def CritiquePriveos(request, ExNo, semestery):
    PreviosS = PCS.objects.get(ExNo=ExNo, semestery=semestery)
    list = PC.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = PC(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                          No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = PC.objects.get(number=number, PreviosS=PreviosS)
            instance = PC.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/Critique/CritiquePriveos.html', {'names': list})


#----------------------------political history3-------------------------------------------------------------------------


def AHistory3(request):
    return render(request, 'thirdyear/History3/AHistory3.html')


def AHistory31M(request):
    list = H1.objects.all()

    return render(request, 'thirdyear/History3/AHistory31M.html', {'name': list})


def AHistory31(request):
    list = H1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = H1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AHistory31M')

    return render(request, 'thirdyear/History3/AHistory31.html', {'names': list, 'form': file})


def AHistory31E(request, number):
    list = H1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AHistory31M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AHistory31M')

    return render(request, 'thirdyear/History3/AHistory31E.html', {'name': list})


def AHistory34M(request):
    list = H4M.objects.all()

    return render(request, 'thirdyear/History3/AHistory34M.html', {'names': list})


def AHistory34E(request, number):
    list = H4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AHistory34M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AHistory34M')

    return render(request, 'thirdyear/History3/AHistory34E.html', {'name': list})


def AHistory34Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = H4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AHistory34M')
    return render(request, 'thirdyear/History3/AHistory34Add.html')


def AHistory34(request, number):
    db = H4M.objects.get(number=number)
    list = H4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans3')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = H4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = H4.objects.get(number=number, ExNo=db)
            instance = H4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'thirdyear/History3/AHistory34.html', {'names': list})


def AHistory3GM(request):
    list = GHM.objects.first()

    return render(request, 'thirdyear/History3/AHistory3GM.html', {'names': list})


def AHistory3GE(request):
    list = GHM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AHistory3GM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AHistory3GM')

    return render(request, 'thirdyear/History3/AHistory3GE.html', {'name': list})


def AHistory3GAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = GHM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AHistory3GM')
    return render(request, 'thirdyear/History3/AHistory3GAdd.html')


def AHistory3G(request):
    db = GHM.objects.first()
    list = GH.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans3')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = GH(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = GH.objects.get(number=number)
            instance = GH.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'thirdyear/History3/AHistory3G.html', {'names': list})


def AHistory3PS(request):
    list = PHS.objects.all()
    return render(request, 'thirdyear/History3/AHistory3PS.html', {'name': list})


def AHistory3PAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = PHS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AHistory3PS')

    return render(request, 'thirdyear/History3/AHistory3PAdd.html')


def AHistory3PM(request, ExNo, semestery):
    list = PHS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('AHistory3PS')

    return render(request, 'thirdyear/History3/AHistory3PM.html', {'name': list})


def AHistory3P(request, ExNo, semestery):
    PreviosS = AEPS.objects.get(ExNo=ExNo, semestery=semestery)
    list = PH.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans3')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = PH(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                        No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AEP.objects.get(number=number, PreviosS=PreviosS)
            instance = PH.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()
    return render(request, 'thirdyear/History3/AHistory3P.html', {'names': list})