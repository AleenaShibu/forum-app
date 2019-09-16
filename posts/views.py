
from django.views.generic import DetailView ,ListView
from .models import Post

	
		
class DetailPostsView(DetailView):
	model = Post 
	template_name = 'detail.html'
	
class HomePostView(ListView):
	model = Post 
	template_name = 'index.html'
	context_object_name = 'article'
