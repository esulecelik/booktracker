from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Book,Category,Writer

def index(request):

    books = Book.objects.all()
    categories = Category.objects.all()
    print(categories)
    return render(request,'library/index.html',{
        'books' : books,
        'categories' : categories
    })



def get(request, slug):

    book = Book.objects.get(slug=slug)
    return render(request, 'library/book-detail.html',{
        'book': book
    })

def update(request, id):
    pass

def delete(request, id):
    pass

def getall(request):
    pass

def add(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        writer = request.POST.get('writer')
        page_number = request.POST.get('pagenumber')
        start_date_included  = request.POST.get('optstartdate')
        started_on = request.POST.get('startdate')
        current_date_included = request.POST.get('optcurrentpage')
        current_page = request.POST.get('currentpage')
        finish_date_included = request.POST.get('optfinishdate')
        finished_on = request.POST.get('finishdate')
        cover = request.FILES['bookcover']
        category_id = request.POST.get('categoryid')


        if not start_date_included:
            started_on = None

        if not finish_date_included:
            finished_on = None

        if not current_date_included:
            current_page = None

        book = Book( name=name,
                     page_number=page_number,
                     started_on=started_on,
                     finished_on = finished_on,
                     current_page= current_page,
                     cover = cover,
                     writer = Writer.objects.get_or_create(name=writer)[0],
                     category = Category.objects.get(id=category_id)
                    )
        book.save()

        books =  Book.objects.all()
        return HttpResponseRedirect(redirect_to=reverse('index'))
    
        
