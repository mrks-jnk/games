from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# create index Views


#@login_required
def index(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)
