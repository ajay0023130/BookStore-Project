from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from Books.models import Book,Review
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
# Create your views here.

#class based view
class BookListView(ListView):
    model = Book
    template_name = 'Books/HomePage.html'
    context_object_name = 'books'
    paginate_by = 3 

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(subtitle__icontains=query) |
                Q(publisher__icontains=query) |
                Q(author__icontains=query)
            )
        return Book.objects.all().order_by('-id')






class BookDetailView(DetailView):
    model = Book
    template_name = 'Books/BookDetails.html'
    context_object_name = 'singleBook'

    def post(self, request, *args, **kwargs):
        book_id = kwargs['pk']
        review_content = request.POST.get('review')
        new_review = Review.objects.create(review=review_content, book_id=book_id)
        reviews_for_book = Review.objects.filter(book_id=book_id)
        return self.render_to_response({'singleBook': self.get_object(), 'reviews_for_book': reviews_for_book})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews_for_book = Review.objects.filter(book_id=self.object.id).order_by('-id')
        context['reviews_for_book'] = reviews_for_book
        return context












# all function based view
# def index(request):
#     query = request.GET.get('q')  # Get the search query from the URL parameters
    
#     if query:
#         # Perform the search if a query exists
#         AllBooks = Book.objects.filter(
#             Q(title__icontains=query) |
#             Q(subtitle__icontains=query) |
#             Q(publisher__icontains=query) |
#             Q(author__icontains=query)
#         )
#     else:
#         # If no search query, retrieve all books
#         AllBooks = Book.objects.all()
    
#      # Pagination 
#     paginator = Paginator(AllBooks, 3)  # Display 6 books per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     # context = {'Books': AllBooks, 'query': query,'page_obj':page_obj}
#     context = {'books': page_obj, 'query': query}
#     # return render(request,'Books/index.html',context)
#     return render(request,'Books/HomePage.html',context)






# def show(request,book_id):
#     if request.method == "POST":
#         review_content = request.POST['review']
#         print("review_data",review_content)
#         new_review=Review(review=review_content,book_id=book_id)
#         new_review.save()
        
#         reviews_for_book = Review.objects.filter(book_id=book_id)
#         singleBook = get_object_or_404(Book,id=book_id)
#         context = {'singleBook': singleBook,'reviews_for_book':reviews_for_book}
#         return render(request,'Books/BookDetails.html',context)
#     # try:
#     #     singleBook = Book.objects.get(id = id)
#     #     context = {'singleBook': singleBook}
#     # except Book.DoesNotExist:
#     #     raise Http404("Book does not exist")
#     # return render(request,'Books/BookDetails.html',context)
    
#     #shortcut code
#     else:
#         reviews_for_book = Review.objects.filter(book_id=book_id)
#         singleBook = get_object_or_404(Book,id=book_id)
#         context = {'singleBook': singleBook,'reviews_for_book':reviews_for_book}
#         return render(request,'Books/BookDetails.html',context)
    


    

def aboutPage(request):
    return render(request,'Books/About.html')

def contactPage(request):
    return render(request,'Books/Contact.html')

        
    
    
    

