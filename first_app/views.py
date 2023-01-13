from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from first_app.forms import UserProfileInfoForm, UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context_dict = {'text': 'hello world!', 'number': 100}
    return render(request, 'first_app/index.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))



def other(request):
    return render(request, 'first_app/other.html')

@login_required
def relative(request):
    return render(request, 'first_app/relative_url_templates.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            registered = True
            print("in userform else:")
            print(registered)

            if 'portfolio' in request.FILES:
                profile.portfolio = request.FILES['portfolio']

                profile.save()

                print(registered)
        else:
            print(user_form.errors, profile_form.errors)
            print("in first else:")
            print(registered)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        print("in second else:")
        print(registered)

    return render(request, 'first_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active!!")
        else:
            print("Someone tried to login and failed!")
            print("Username{} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'first_app/login.html', {})
