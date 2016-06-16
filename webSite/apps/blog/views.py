# Imports of shortcuts
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
# Imports of http
from django.http import HttpResponse
# Imports of utils
from django.utils.decorators import method_decorator
# Imports of template
from django.template import RequestContext
# Imports of conf
from django.conf import settings
# Imports of template
from django.template.loader import render_to_string
# Imports of core
from django.core.mail import send_mail
# Imports of contrib
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Imports from views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Imports from app
from .models import Post, Email
from .forms import PostForm, EmailForm


# Create your views here.

# View of blogs
@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
	template_name = 'blog/index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['posts'] = Post.objects.all()
		return context


# Detail of a post
@method_decorator(login_required, name='dispatch')
class PostView(DetailView):
	model = Post


# New post
@method_decorator(staff_member_required, name='dispatch')
class NewPostView(CreateView):
	template_name = 'blog/post_form.html'
	form_class = PostForm
	success_url = '/blog/'

	def form_valid(self, form):
		sendEmail(self.request)
		return super(NewPostView, self).form_valid(form)


# Subscribe emails
def subscribe(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']

		Email.objects.create(
			name = name,
			email = email
		)
		message = "Gracias por suscribirte en Email.com, ahora podras recibir una notificacion cada vez que se publique un nuevo post"

	else:
		message = "It supports only method post"
	return HttpResponse(message, content_type = 'text/html')


# metodo of send emails
def sendEmail(request):
	emails = Email.objects.all()
	emailsList = []
	for email in emails:
		emailsList.append(email.email)

	msg_html = render_to_string('plantilla.html', {'title': request.POST['title'], 'description': request.POST['description']})
	send_mail(
		'Se a publicado un nuevo post en EmailSend',
		'Se a publicado un nuevo en EmailSend',
		settings.EMAIL_HOST_USER,
		emailsList,
		html_message=msg_html,
		fail_silently=True
	)
