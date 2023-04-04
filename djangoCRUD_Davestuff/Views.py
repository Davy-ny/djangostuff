from django.shortcuts import redirect, render
from .models import Student


def displayindex(request):
    return render(request, 'index.html')


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        stuff = Student(name=name, email=email, phone=phone)
        stuff.save()
        return redirect("/")
    return render(request, 'index.html')


def displayData(request):
    data = Student.objects.all()
    trial = {"data": data}
    return render(request, 'index.html', trial)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, 'index.html')


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.phone = phone
        edit.save()
        return redirect("/")
    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html', context)


