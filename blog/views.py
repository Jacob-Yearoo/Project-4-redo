from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Report, Comment
from .forms import CommentForm, ReportForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):


    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'comment_form': CommentForm(),
                'report_form': ReportForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        report_form = ReportForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        if report_form.is_valid():
            report_form.instance.email = request.user.email
            report_form.instance.name = request.user.username
            report = report_form.save(commit=False)
            report.reported_post = post
            report.save()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'comment_form': CommentForm(),
                'report_form': ReportForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class ReportView(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        report_form = ReportForm(data=request.POST)

        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.reported_post = post
            report.save()

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def report_post(request, slug):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            # Process the form data and save the report
            report = form.save(commit=False)
            report.reported_post = Post.objects.get(slug=slug)
            report.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
    else:
        form = ReportForm()
    return render(request, 'report.html', {'form': form})

def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=comment.post.slug)

    else:
        form = CommentForm(instance=comment)

    return render(request, 'update_comment.html', {'form': form, 'comment': comment})


# def delete_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)

#     if request.method == 'POST':
#         comment.delete()
#         return redirect('index', slug=comment.post.slug)

#     return render(request, 'delete_comment.html', {'comment': comment})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = comment.post.slug 

    if request.method == 'POST':
        comment.delete()
        return redirect('index') 

    return render(request, 'delete_comment.html', {'comment': comment})

