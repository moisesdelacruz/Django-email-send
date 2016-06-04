from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	var = 'Hello World'
	template = 'home/index.html'
	return render(request, template)

# View of admin
@staff_member_required
def admin(request):
	template = 'home/admin.html'
	return render(request, template)

# View of Login
def login_view(request):
	message = None
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has identificado de forma correcta"
					url_next = request.GET.get('next')
					if url_next is not None:
						return redirect(url_next)
					else:
						return redirect('/')
				else:
					message = "Tu usuario esta incorrecto"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = AuthenticationForm()
	return render(request, 'home/login.html', {'message': message, 'form': form})

# View of new user
def newUser(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreationForm()
		return render(request, 'home/register.html', locals())

# View of Logout
@login_required
def log_out(request):
	logout(request)
	return redirect('/login')