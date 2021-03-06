from django.shortcuts import render, HttpResponse, get_object_or_404
from eventManager.models import event as event_model
from teachers.models import teacher
from briStudents.models import students
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from noticeboard.models import notice
from .models import blog, contact_information
from study_materials.models import free_materials
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

def home(request):
	p = event_model.objects.filter().order_by('-id')[:3]
	selected_event = []

	for this_event in p:
		temp_dict = {}
		temp_dict['pk'] = this_event.id
		temp_dict['title'] = this_event.title
		temp_dict['date'] = this_event.date
		temp_dict['location'] = this_event.location
		#temp_dict['title_image'] = str(this_event.title_image)
		temp_dict['title_image'] = this_event.title_image.url
		selected_event.append(temp_dict)
		
	context = {}
	context['selected_event'] = selected_event

	p = teacher.objects.filter()[:4]

	teacher_list = []

	for t in p:
		temp_dict = {}
		temp_dict['name'] = t.name
		temp_dict['subject'] = t.subject
		temp_dict['photo'] = str(t.teacher_photo.url)
		teacher_list.append(temp_dict)

	context['teacher_list'] = teacher_list

	p = students.objects.filter()[:4]

	student_list = []

	for s in p:
		temp_dict = {}
		temp_dict['name'] = s.name
		temp_dict['subject'] = s.subject
		temp_dict['university'] = s.university
		temp_dict['batch'] = s.batch
		temp_dict['photo'] = str(s.student_photo.url)
		student_list.append(temp_dict)

	context['student_list'] = student_list	

	
	return render(request, 'home/index.html', context)


def course_view_science(request):
	p = free_materials.objects.filter(Q(belongs_to='Science') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_science.html', { 'selected_materials' : selected_materials})

def course_view_commerce(request):
	p = free_materials.objects.filter(Q(belongs_to='Commerce') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_commerce.html', { 'selected_materials': selected_materials})

def course_view_arts(request):
	p = free_materials.objects.filter(Q(belongs_to='Arts') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_arts.html', {'selected_materials' : selected_materials})

def course_view_english(request):
	p = free_materials.objects.filter(Q(belongs_to='English') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_english.html', {'selected_materials' : selected_materials})

def events(request):
	p = event_model.objects.filter().order_by('-id')[0]
	selected_event = {}
	selected_event['pk'] = p.id
	selected_event['title'] = p.title
	selected_event['date'] = p.date
	selected_event['location'] = p.location
	selected_event['title_image'] = p.title_image.url
	selected_event['short_description'] = p.short_description

	q = event_model.objects.filter().order_by('-id')[1:]
	all_event = []

	for event in q:
		temp_dict = {}
		temp_dict['pk'] = event.id
		temp_dict['title'] = event.title
		temp_dict['date'] = event.date
		temp_dict['location'] = event.location
		temp_dict['title_image'] = event.title_image.url
		temp_dict['short_description'] = event.short_description
		
		all_event.append(temp_dict)

	context = {}
	context['selected_event'] = selected_event
	context['all_event'] = all_event

	return render(request, 'home/events.html', context)

def events_param(request, pk=None):
	p = event_model.objects.get(pk=pk)
	selected_event = {}
	selected_event['pk'] = p.id
	selected_event['title'] = p.title
	selected_event['date'] = p.date
	selected_event['location'] = p.location
	selected_event['title_image'] = p.title_image.url
	selected_event['short_description'] = p.short_description
	
	
	q = event_model.objects.filter().order_by('-id').exclude(id=pk)

	all_event = []

	for event in q:
		temp_dict = {}
		temp_dict['pk'] = event.id
		temp_dict['title'] = event.title
		temp_dict['date'] = event.date
		temp_dict['location'] = event.location
		temp_dict['title_image'] = event.title_image.url
		temp_dict['short_description'] = event.short_description
		all_event.append(temp_dict)

	context = {}
	context['selected_event'] = selected_event
	context['all_event'] = all_event

	return render(request, 'home/events.html', context)



def teachers(request):
	p = teacher.objects.all().order_by('name')
	teacher_list = []

	for t in p:
		temp_dict = {}
		temp_dict['name'] = t.name
		temp_dict['subject'] = t.subject
		temp_dict['photo'] = str(t.teacher_photo.url)
		teacher_list.append(temp_dict)

	context = {}
	context['teacher_list'] = teacher_list
	
	return render(request, 'home/teachers.html', context)


def stu(request):
	p = students.objects.all().order_by('name')
	student_list = []

	for s in p:
		temp_dict = {}
		temp_dict['name'] = s.name
		temp_dict['subject'] = s.subject
		temp_dict['university'] = s.university
		temp_dict['batch'] = s.batch
		temp_dict['photo'] = str(s.student_photo.url)
		student_list.append(temp_dict)
	context = {}
	context['student_list'] = student_list
	return render(request, 'home/students.html', context)

def contact(request):
	if request.method == 'POST':
		try:
			name = request.POST['name']
			email = request.POST['email']
			phone = request.POST['phone']
			institution = request.POST['institution']
			subject = request.POST['subject']
			message = request.POST['name']
			
			cinfo = contact_information(name=name, email=email, phone=phone, institution=institution, subject=subject, message=message)
			print(cinfo)
			cinfo.save()

			context = {}
			context['success'] = True
			return render(request, 'home/contact.html', context)
		except:
			context = {}
			print("Hello")
			context['success'] = False
			return render(request, 'home/contact.html', context)
	return render(request, 'home/contact.html')

def test(request, pk=None):
	return render(request, 'home/events.html')

def noticeView(request):
	notice_list = notice.objects.all().order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(notice_list, 5)

	try:
		selected_notice = paginator.page(page)
	except PageNotAnInteger:
		selected_notice = paginator.page(1)
	except EmptyPage:
		selected_notice = paginator.page(paginator.num_pages)

	return render(request, 'home/notice.html', {'selected_notice': selected_notice} )

def blogList(request):
	blog_list = blog.objects.all().order_by('-date')
	paginator = Paginator(blog_list, 5)
	page = request.GET.get('page')



	try:
		selected_blog = paginator.page(page)
	except PageNotAnInteger:
		selected_blog = paginator.page(1)
	except EmptyPage:
		selected_blog = paginator.page(paginator.num_pages)
	
	

	


	return render(request, 'home/bloglist.html', {'selected_blog' : selected_blog} )

def searchResult(request):
	val = request.GET["s"]

	selected_blog = blog.objects.filter(Q(content__contains=val) | Q(title__contains=val) | Q(name__contains=val) | Q(university__contains=val))
	
	blog_list = []

	for s in selected_blog:
		temp_dict = {}
		temp_dict['id'] = s.id
		temp_dict['title'] = s.title
		temp_dict['name'] = s.name
		temp_dict['university'] = s.university
		temp_dict['content'] = s.content
		temp_dict['date'] = s.date
		temp_dict['photo'] = str(s.photo.url)
		blog_list.append(temp_dict)

	return render(request, 'home/bloglist.html', {'selected_blog' : blog_list} )

def blogView(request, pk=None):
	query = get_object_or_404(blog, pk=pk)

	return render(request, 'home/blog_view.html', {'selected_blog' : query })