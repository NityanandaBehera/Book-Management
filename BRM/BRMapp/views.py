from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from BRMapp import models
from BRMapp.forms import NewBookForm,SearchForm

def newBook(request):
    form=NewBookForm()
    res=(request,'BRMapp/new_book.html',{"form":form})
    return res
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record stored<br><a href='/BRMapp/view-books'>view all Books</a>"
    return HttpResponse(s) 
def viewBooks(request):
    books=models.Book.objects.all()
    username=request.session['username']
    res=render(request,'BRMapp/view_book.html',{'books':books,'username':username}) 
    return res 
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMapp/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
         form=NewBookForm(request.POST)
         book=models.Book()
         book.id=request.POST['bookid']
         book.title=request.POST['title']
         book.price=request.POST['price']
         book.author=request.POST['author']
         book.publisher=request.POST['publisher']
         book.save()
    return HttpResponseRedirect('BRMapp/view-books')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('/BRMapp/view-books')
def searchBook(request):
    form=SearchForm(request.POST)
    res=render(request,'BRMapp/search_book.html',{'form':form})
    return res
