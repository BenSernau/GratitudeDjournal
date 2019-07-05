from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DayForm
from .models import Day

def day_create_view(request):
	form = DayForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DayForm()
		return redirect('../')

	context = { "form": form }
	return render(request, "days/day_create.html", context)

def day_delete_view(request, id):
	obj = get_object_or_404(Day, id = id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "days/day_delete.html", context)

def day_list_view(request):
	queryset = Day.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "days/day_list.html", context)