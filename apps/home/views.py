from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

# Imports of contrib
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import TemplateView, ListView

from .. blog.models import Post
from .. blog.forms import PostForm

# Create your views here.

class HomeTemplateView(TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['var'] = 'Hello World'
		return context

# View of admin
@method_decorator(staff_member_required, name='dispatch')
class AdminListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'home/admin.html'


@method_decorator(staff_member_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home:admin')
    template_name = 'home/confirm.html'


@method_decorator(staff_member_required, name='dispatch')
class PostUpdateView(UpdateView):
	model=Post
	form_class=PostForm
	template_name='blog/post_form.html'
	success_url = reverse_lazy('home:admin')

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
