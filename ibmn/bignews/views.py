from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView, UpdateView, TemplateView, DeleteView
from ibmn.bignews.models import Bignews
from ibmn.bignews.forms import CreateBignewsForm, EditBigNewsForm
from ibmn.comments.forms import CommentForm
from ibmn.comments.models import Comment



# Create your views here.

class BignewsCreateView(View):
    template_name = 'manager_pages/bignews_add_news.html'
    form_class = CreateBignewsForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})


    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your news was successfully posted!')

        return render(request,self.template_name, {'form':form})

bignews_create_view  = BignewsCreateView.as_view()


class BignewsListPostView(LoginRequiredMixin, ListView):
    model = Bignews
    context_object_name = 'bignews_list'
    template_name = 'manager_pages/bignews_list_news.html'

bignews_list_view  =  BignewsListPostView.as_view()



class BignewsUpdateView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    form_class = EditBigNewsForm
    model = Bignews
    template_name = 'manager_pages/bignews_update.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return Bignews.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("news:manager_home")
   

bignews_update_view  = BignewsUpdateView.as_view()




class BignewsManagerDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = Bignews
    template_name = 'manager_pages/bignews_delete_news.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return Bignews.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("news:manager_home")
   

bignews_manager_delete_view = BignewsManagerDeleteView.as_view()






def big_news_details_view(request, slug):
    bignews=get_object_or_404(Bignews,slug=slug)

    similar_bignews =  bignews.tags.similar_objects()[:4]

    # List of active comments for this post
    bignews_comments = bignews.bignews_comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.bignews = bignews
            # Save the comment to the database
            new_comment.save()
            return redirect(bignews.get_absolute_url()+'#')
    else:
        comment_form = CommentForm()

    # List of similar posts
    
    return render(request, 'pages/bignews_details.html', {'bignews':bignews,'bignews_comments': bignews_comments,
                                                            'comment_form':comment_form, 'similar_bignews':similar_bignews
                                                        })


def big_news_reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            bignews_id = request.POST.get('bignews_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            bignews_url = request.POST.get('bignews_url')  # from hidden input
            reply = form.save(commit=False)
    
            reply.post = Bignews(id=bignews_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
            return redirect(bignews_url+'#')
    return redirect("/")