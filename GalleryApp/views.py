import datetime as dt
from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location, Category


# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to Gallery App')

def welcome(request):
    return render(request, 'welcome.html')    

# def GalleryApp_of_day(request):
#     date = dt.date.today()
#     day = convert_dates(date)
#     images = Image.objects.all()
#     location = Location.objects.all()
#    category = Category.objects.all()

#     return render(request, 'index.html',{'images':images})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day  
     




def index(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
    title = 'Gallery App'

    return render(request, 'index.html', {'title':title, 'images':images, 'location':location})


def unique(request,category_name,image_id):
    # images = Image.get_image_by_id(image_id)
    title = 'Image'
    location = Location.objects.all()
    # category = Category.get_category_id(id = image_category)
    image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"unique.html",{'title':title,"image":image, "location":location, "image_category":image_category})

def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    location = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "location":location})
    else:
        message = 'You have not searched for any image'
        return render(request, 'search.html',{"message": message})


def location_filter(request, image_location):
    location = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'location':location, 'location':location})
     
