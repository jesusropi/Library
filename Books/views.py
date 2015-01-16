from django.shortcuts import render, HttpResponse
from models import Book
import simplejson as simplejson


def search(request):
	return render(request, 'Books/search.html', \
		{'error_message': "You didn't select a choice."})

def autocompleteModel(request):
	search_qs = Book.objects.filter(title__startswith=request.REQUEST['search'])
	results = []
	resp = None
	for r in search_qs:
		results.append(r.title)
		resp = request.REQUEST['callback'] + '(' + simplejson.dumps(results) + ');'
	return HttpResponse(resp, content_type='application/json')	