from django.shortcuts import render,redirect
from .models import UserModel
from .forms import UserForm,UserloginForm
from django.contrib import messages
# Create your views here.
def showhome(request):
    return render(request,'home.html')

def add_user(request):
    if request.method == 'POST':
        # print("IT IS POST REQUEST")
        fm=UserForm(request.POST,request.FILES)
        if fm.is_valid():
            # print("Form is validated")
            # fm.save()
            nm=fm.cleaned_data['name']
            dob=fm.cleaned_data['dob']
            con=fm.cleaned_data['contact_no']
            gen=fm.cleaned_data['gender']
            pin=fm.cleaned_data['pin']
            city=fm.cleaned_data['city']
            state=fm.cleaned_data['state']
            gmail=fm.cleaned_data['gmail']
            password=fm.cleaned_data['password']
            img=fm.cleaned_data['profile_image']
            res = UserModel(
                name=nm,dob=dob,gender=gen,contact_no=con,pin=pin,
                city=city,state=state,gmail=gmail,
                password=password,profile_image=img).save()
            messages.success(request, 'Data Save Successfully')
    else:
        fm = UserForm()
    fm=UserForm()
    return render(request,'add_user.html',{'forms':fm})


def checked_user(request):
    fm=UserloginForm()
    return render(request,'login_user.html',{'forms':fm})

def logincheck(request):
    if request.method == 'POST':
        un = request.POST.get('gmail')
        pa = request.POST.get('password')
        try:
            u_data = UserModel.objects.get(gmail=un, password=pa)
            request.session['user_data'] = u_data.id
            return redirect('show_data',pk=u_data.id)
        except UserModel.DoesNotExist:
            messages.error(request,'invalid user')
            return redirect('checked_user')
    else:
        request.session['u_data']=False
        return redirect('login_user')


def userhome(request,pk):
    data = UserModel.objects.get(id=pk)
    return render(request,'show_data.html',{'data':data})


def search_data(request):
    user_name = request.POST.get('name')
    print(user_name)
    try:
        res=UserModel.objects.get(contact_no=user_name)
        return render(request,'home.html',{'info':res})
    except UserModel.DoesNotExist:
        return render(request,'home.html',{'error':'Invalid user'})