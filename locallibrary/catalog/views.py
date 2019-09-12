from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Book,Author,BookInstance,Genre

def index(request):
    num_books=Book.objects.all().count()
    num_instances= BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    num_visits=request.session.get("num_visits",0)
    request.session["num_visits"] = num_visits+1

    return render(
        request,
        "index.html",
        context={'num_books':num_books,'num_instance':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                 "num_visits":num_visits},
    )
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/book_detail.html',
            context={'book': book_id, }
        )

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, pk):
        try:
            author_id = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404("Author does not exist")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/author_detail.html',
            context={'author': author_id, }
        )
