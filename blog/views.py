from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import Usercontact,LoginForm,UserAdminCreationForm,Userblog
from .models import User_blog,CustomUser
from django.views.generic.edit import DeleteView,UpdateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required


# Create your views here.

#home page
def home(request):
  return render(request,'blog/home.html')

#about page
def about(request):
  return render(request,'blog/about.html')

#contact page
def contact(request):
  form = Usercontact()
  return render(request,'blog/contact.html',{'form':form})

#signup page
def Usersignup(request):
  form = UserAdminCreationForm()
  if request.method == 'POST':
    form = UserAdminCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      group = Group.objects.get(name='author')
      user.groups.add(group)
      messages.success(request, 'Congratulation You Are Become A Author...!')
  return render(request, 'blog/signup.html', {'form': form})

#dashboard page
@login_required
def Userdashboard(request):
  data = request.user.get_username()
  user1 = CustomUser.objects.get(email=data)
  if user1.groups.filter(name='author'):
    blog = User_blog.objects.filter(email=data).values('id', 'title', 'des')
    grp = request.user.groups.all()
    return render(request,'blog/dashboard.html',{'data':data, 'blog':blog, 'grp':grp})
  else:
    logout(request)
    return HttpResponseRedirect('/login/')

# login page
def Userlogin(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      form = LoginForm(request=request, data=request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname,password=upass)
        if form is not None:
          login(request,user)
          messages.success(request,"Loged In Successfully...")
          return HttpResponseRedirect('/dashboard/')
    else:
      form = LoginForm()
    return render(request,'blog/login.html',{'form':form})
  else:
    return HttpResponseRedirect('/dashboard/')


#logout page
def Userlogout(request):
  logout(request)
  return HttpResponseRedirect('/')

#add blog
@login_required
def Addblog(request):
  if request.method == "POST":
    form = Userblog(request.POST, request.FILES)
    if form.is_valid():
      email = request.user.get_username()
      print(email)
      ttl = form.cleaned_data['title']
      des = form.cleaned_data['des']
      form = User_blog(title=ttl,email= email,des=des)
      form.save()
      messages.success(request,"Add Blog Successfully...")
      return HttpResponseRedirect('/addblog/')
  else:
    form = Userblog()
    return render(request,'blog/addblog.html',{'form':form})

#blog update
class BlogUpdateView(UpdateView):
  model = User_blog
  form_class = Userblog
  success_url = '/dashboard/'
  template_name = "blog/addblog.html"

#blog delete
class BlogDeleteView(DeleteView):
    model = User_blog
    template_name = "blog/delete.html"
    success_url = '/dashboard/'


