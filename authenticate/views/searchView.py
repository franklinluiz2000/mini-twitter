from authenticate.views import *

# @login_required
def SearchView(request):
    if request.method == 'POST':
        searchNow = request.POST.get('search')
        print(searchNow)
        results = User.objects.filter(username__contains=searchNow)
        
        context = {
            'results':results
        }
        return render(request, 'users/search.html', context)
    
    
    return render(request, 'users/search.html')
    