from django.shortcuts import render

def post_list(request):
    return render(request, 'infpoolsite/post_list.html', {})