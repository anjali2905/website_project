from django.shortcuts import render

def Business(request):
	return render(request, 'courses/Business.html')

def Kids(request):
	return render(request, 'courses/Kids.html')

def Corporate(request):
	return render(request, 'courses/Corporate.html')

def Courses(request):
	return render(request, 'courses/Courses.html')


