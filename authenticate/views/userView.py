from django.shortcuts import render
from authenticate.models import Profile
from django.core.paginator import Paginator

def user_view(request):
    name = request.GET.get('name')
    address = request.GET.get('address')
    city = request.GET.get('city')
    state = request.GET.get('state')
    medics = Profile.objects.all()
    print(medics)

    if len(medics) > 0:
        paginator = Paginator(medics, 8)
        page = request.GET.get('page')
        medics = paginator.get_page(page)
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'medics': medics,
        'parameters': parameters
    }

    return render(request, template_name='user/users.html', context=context, status=200)