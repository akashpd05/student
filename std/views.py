import razorpay
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import*

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contacts(request):
    return render(request, 'contacts.html')
def sign_in(request):
    return render(request, 'sign_in.html')
def sign_up(request):
    return render(request, 'sign_up.html')

def check_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/admin_homepage/")
        else:
            return redirect("/sign_in/")

def admin_homepage(request):
    return render(request, 'admin_homepage.html')

def courses(request):
   a =tbl_courses.objects.all()
   return render(request, "courses.html",{"a":a})

def add_courses(request):
    return render(request,"add_courses.html")


def save_courses(request):
    if  request.method=="POST":
        obj=tbl_courses()

        obj.Course_name =request.POST.get("course_name")
        obj.Duration=request.POST.get("course_duration")
        obj.fees=request.POST.get("course_fees")
        obj.Instructor=request.POST.get("course_instructor")
        obj.description=request.POST.get("course_description")
        obj.save()
        return redirect("/courses/")

def edit_courses(request,id):
    b = tbl_courses.objects.get(id=id)
    return render(request, "edit_courses.html", {"b": b})


def update_courses(request,id):
    b = tbl_courses.objects.get(id=id)
    b.Course_name = request.POST.get("course_name")
    b.Duration = request.POST.get("course_duration")
    b.fees = request.POST.get("course_fees")
    b.Instructor = request.POST.get("course_instructor")
    b.description = request.POST.get("course_description")
    b.save()
    return redirect("/courses/")

def delete_courses(request,id):
    b = tbl_courses.objects.get(id=id)
    b.delete()
    return redirect("/courses/")


def teachers(request):
    a = tbl_teachers.objects.all()
    return render(request,"teachers.html",{"a":a})

def add_teachers(request):
    return render(request, "add_teachers.html")

def save_teachers(request):
    if  request.method=="POST":
        obj=tbl_teachers()
        obj.Name = request.POST.get("name")
        obj.Email = request.POST.get("email")
        obj.Phone = request.POST.get("phone")
        obj.Subject_Taught = request.POST.get("subjects")
        obj.Years_of_Experience = request.POST.get("experience")
        obj.Additional_Information = request.POST.get("additional")
        obj.Grade_Level = request.POST.get("grade")
        obj.save()
        return redirect("/teachers/")

def edit_teachers(request,id):
    b = tbl_teachers.objects.get(id=id)
    return render(request,"edit_teachers.html",{"b":b})

def update_teachers(request,id):
        b = tbl_teachers.objects.get(id=id)
        b.Name = request.POST.get("name")
        b.Email = request.POST.get("email")
        b.Phone = request.POST.get("phone")
        b.Subject_Taught = request.POST.get("subjects")
        b.Years_of_Experience = request.POST.get("experience")
        b.Additional_Information = request.POST.get("additional")
        b.Grade_Level = request.POST.get("grade")
        b.save()
        return redirect("/teachers/")


def delete_teachers(request,id):
    b = tbl_teachers.objects.get(id=id)
    b.delete()
    return redirect("/teachers/")

def course_details(request):
    a = tbl_courses.objects.all()
    print(a)
    return render(request,"course_details.html",{"a":a})

def application_form(request,id):
    d=tbl_courses.objects.get(id=id)
    return render(request,"application_form.html",{"d":d})

def save_application(request,id):
   if  request.method=="POST":
     obj=tbl_application_form()
     obj.course_id=id
     obj.name = request.POST.get("name")
     obj.email = request.POST.get("email")
     obj.phone = request.POST.get("phone")
     obj.address = request.POST.get("address")
     obj.terms = request.POST.get("terms")
     obj.gender = request.POST.get("gender")
     obj.save()
     return redirect("summary",id=obj.id)

def teacher(request):
    a = tbl_teachers.objects.all()
    return render(request, "teacher.html", {"a": a})

razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG', 'oXUZ9Mf5zhjoZsTFLc7RpABO'))
def summary(request,id):
    a = tbl_application_form.objects.get (id=id)
    print(a)
    currency = "INR"
    amount = int(a.course.fees)*100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order_id =  razorpay_order['id']
    callback_url= 'payment_handler'


    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_amount']=amount
    context['razorpay_merchant_key'] = 'rzp_test_9zruMnoLDlsCLG'
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['a']=a


    return render(request, "summary.html",context)

def payment_handler(request):
    razorpay_order_id = request.POST.get('order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.


    amount = request.POST.get("amount") # Rs. 200
    razorpay_client.payment.capture(payment_id, amount)
    return redirect("/")








