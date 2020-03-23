from django.shortcuts import HttpResponse,render,redirect

from .forms import apply_form

from .models import db

# Create your views here.

def home_view(request):
	c1 = db.objects.filter(course='course_1').count()
	c2 = db.objects.filter(course='course_2').count()
	c3 = db.objects.filter(course='course_3').count()
	c4 = db.objects.filter(course='course_4').count()
	c5 = db.objects.filter(course='course_5').count()
	c6 = db.objects.filter(course='course_6').count()
	context={
		'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6
	}
	return render(request,'home.html',context)

def apply_view(request,num):
	# course list
	course_list = {
			1:'course_1',
			2:'course_2',
			3:'course_3',
			4:'course_4',
			5:'course_5',
			6:'course_6'
		}
	# Invalid entry in url
	if num in course_list.keys() :
		course_name=course_list[num]
		reg_count = db.objects.filter(course=course_list[num]).count()
		# when registrating is less than 60
		if reg_count<60:
			my_form = apply_form(request.POST or None)
			# For is valid
			if my_form.is_valid():
				form_obj = my_form.cleaned_data
				form_obj['course']=course_list[num]
				print(form_obj)
				reg_count = db.objects.filter(course=course_list[num]).count()
				# second step verification for registration 
				if reg_count<60:
					p = db.objects.create(**form_obj)
					return redirect('/success/')
				# registration is full
				else:
					return redirect('/failed/')
			context = {
				'form' : my_form,
				'course_name' : course_name
			}
			print('the num is ',num)
			return render(request,'apply.html',context)
		# Registration Full
		else:
			return redirect('/failed/')
	else:
		return render(request,'home.html')

def success_view(request):
	return render(request,'success.html')

def failed_view(request):
	return render(request,'failed.html')

def offline_view(request):
	return render(request,'offline.html')
