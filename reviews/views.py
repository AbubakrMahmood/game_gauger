from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from reviews.models import Game, Review, UserProfile
from reviews.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    game_list = Game.objects.all()
    context_dict = {'games': game_list}
    return render(request, 'reviews/index.html', context=context_dict)

def about(request):
    return render(request, 'reviews/about.html')

def featured(request):
    return render(request, 'reviews/featured.html')

def FAQs(request):
    return render(request, 'reviews/FAQ.html')

def categories(request):
    return render(request, 'reviews/categories.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'reviews/signup.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'reviews/signin.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def addgame(request):
    return render(request, 'reviews/addgame.html')

def detail(request, UID):
    game = Game.objects.get(pk=UID)
    reviews = Review.objects.all()
    context_dict = {'game':game, 'reviews': reviews}
    return render(request, 'reviews/detail.html', context=context_dict)