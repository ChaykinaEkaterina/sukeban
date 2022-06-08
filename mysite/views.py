#from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import logout
from website.models import Post
from website.models import Comment
from django.views import View
#from django.views.generic import TemplateView

# Create your views here.
def home(request):
  context = {
     'posts': Post.objects.all(),
     'comments': Comment.objects.all()
  }
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def rus(request):
  return render(request, 'rus.html')

def games(request):
  return render(request, 'games.html')

#def login(request):
#   return render(request, 'login.html')

def registration(request):
  return render(request, 'registration.html')

class PostCommentView(View):
    def dispatch(self, request, *args, **kwargs):
        post_id = request.GET.get("post_id")
        comment = request.GET.get("comment")
        if comment and post_id:
            post = Post.objects.get(pk=post_id)
            comment = Comment(text=comment, post=post, author=request.user)
            comment.save()
            return render(request, "comment.html", {'comment': comment})
        return HttpResponse(status=500, content="")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponse('Logged out')
  
'''
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("/")
    template_name = "registration.html"
   

class LoginView(TemplateView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            name = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, name=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Email или пароль неправильные"
        return render(request, self.template_name, context)
'''