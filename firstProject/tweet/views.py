from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm , UserRegisrationForm ,SearchForm
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def tweet_view(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'view_tweet.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet-view')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet-view')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})
@login_required
def tweetDelete(request, tweet_id):
    try:
        tweet = Tweet.objects.get(id=tweet_id, user=request.user)
        tweet.delete()
        return redirect('tweet-view')
    except Tweet.DoesNotExist:
        raise Http404("No Tweet matches the given query.")
    
def register(request):
    if request.method == 'POST':
      form = UserRegisrationForm(request.POST)
      if form.is_valid():
          user =form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request, user)
          return redirect('tweet-view')
    else:
      form = UserRegisrationForm()
    return render(request, 'registration/register.html', {'form': form})   

def search_view(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Tweet.objects.filter(text__icontains=query)  # Filtering based on the 'text' field
    return render(request, 'search_results.html', {'form': form, 'results': results})

