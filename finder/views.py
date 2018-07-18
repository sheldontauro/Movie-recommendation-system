# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from models import Customer,Movie, UserMovies, watchtime, Director, Direcmovies
from django.views.generic import View
from forms import CustomerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
# from forms import CustomerForm

# Create your views here.

def login(request):
	all_customers = Customer.objects.all()
	return render(request,'login.html',{'all_customers' : all_customers})
def index(request) :
	form = CustomerForm(request.POST)
	if(request.method=='POST'):
		if(form.is_valid()):
			form.save()
			stu = Customer.objects.all()
			UserList = User.objects.all()
			for tm in stu:
				f = 0
				for che in UserList:
					if (tm.name == che.username):
						f = 1
						break
				if f==0:
					user = User.objects.create_user(username = tm.name,
													password = tm.Password,
													email = 'tm@gmail.com'
													)


			#print form.cleaned_data[Customer.name]
			#user = User.objects.create_user(username = {{form.name}}, 
			#								password = {{form.RollNo}},
			#								email = 'tm@gmail.com'
			#								)
			message = 'Successfully Registered'
			#return render(request,'success.html',{'message': message})
			return redirect("/success/", {'message' : message})

		else :
			form_error = "(Registration Failed. Username Exists!)"
			return render(request,'index.html',{'form': form,'form_error': form_error})
	else :
		form = CustomerForm(request.POST)
	return render(request,'index.html',{'form': form})



	
def search(request):
	tm = request.user.username
	alb = Customer.objects.all()
	all_movies1 = Movie.objects.all()
	query = request.GET.get("q")
	if query:
		all_movies1 = all_movies1.filter(m_title__icontains=query)
	paginator = Paginator(all_movies1,40)
	page = request.GET.get('page')
	try:
		all_movies = paginator.page(page)
	except PageNotAnInteger:
		all_movies = paginator.page(1)
	except EmptyPage:
		all_movies = paginator.page(paginator.num_pages)
	bad1 = 60
	bad2 = 40
	return render(request , 'search.html' , {'bad1' : bad1,'bad2' : bad2,'alb' : alb , 'all_movies' : all_movies , 'tm' : tm })
	
def home(request):
	tm = request.user.username
	alb = Customer.objects.all()
	all_movies1 = Movie.objects.all().order_by('-m_rrating')
	paginator = Paginator(all_movies1,40)
	page = request.GET.get('page')
	try:
		all_movies = paginator.page(page)
	except PageNotAnInteger:
		all_movies = paginator.page(1)
	except EmptyPage:
		all_movies = paginator.page(paginator.num_pages)
	bad1 = 60
	bad2 = 40
	return render(request , 'home.html' , {'bad1' : bad1,'bad2' : bad2,'alb' : alb , 'all_movies' : all_movies , 'tm' : tm })

def directors(request):
	tm = request.user.username
	all_directors1 = Director.objects.all()
	paginator = Paginator(all_directors1,20)
	page = request.GET.get('page')
	try:
		all_directors = paginator.page(page)
	except PageNotAnInteger:
		all_directors = paginator.page(1)
	except EmptyPage:
		all_directors = paginator.page(paginator.num_pages)
	return render(request , 'directorlist.html',{'all_directors' : all_directors , 'tm' : tm})


def homeaction(request,home_action):
	tm = request.user.username
	alb = Customer.objects.all()
	all_movies1 = Movie.objects.filter(m_genre = home_action)
	paginator = Paginator(all_movies1,10)
	page = request.GET.get('page')
	try:
		all_movies = paginator.page(page)
	except PageNotAnInteger:
		all_movies = paginator.page(1)
	except EmptyPage:
		all_movies = paginator.page(paginator.num_pages)
	bad1 = 60
	bad2 = 40
	return render(request , 'home.html' , {'bad1' : bad1,'bad2' : bad2,'alb' : alb , 'all_movies' : all_movies , 'tm' : tm })

def direcaction(request,direc_action):
	direc_movies = Direcmovies.objects.filter(direc_name = direc_action)
	tm = request.user.username
	for mv in direc_movies:
		print mv.direc_title
	director1 = get_object_or_404(Director, d_name = direc_action)
	return render(request , 'director.html' , {'tm' : tm, 'direc_movies' : direc_movies ,'director1' : director1})


def success(request):
	return render(request,'success.html')

def about(request):
	return render(request,'about.html')

def movieprof(request , movie_prof):
	tm = request.user.username
	cus = Customer.objects.all()
	fl = -1
	for var in cus:
		if(var.name == tm):
			tm1 = var
			fl = 1
			break

	if(fl == -1):
		return render(request,'error.html')

	revrate = request.GET.get('dpurl')
	if revrate:
		movieobj = Movie.objects.get(m_title = movie_prof)
		update1 = UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).count()
		gettime = watchtime.objects.get(pk = 1)
		time1 = gettime.w_time
		time1 = time1 + 1

		if(update1 == 0):
			userobj = UserMovies(c_name = tm1, c_movie_title = movie_prof, c_time = time1)
			userobj.save()

		test1 = UserMovies.objects.get(c_movie_title = movie_prof,c_name = tm1)
		print(test1.c_rating)
		if(int(test1.c_rating) == -1):
			print(movieobj.m_rrating*movieobj.m_rvote + int(revrate))
			revrating = (movieobj.m_rrating*movieobj.m_rvote + int(revrate))/(movieobj.m_rvote + 1)
			nvotes = movieobj.m_rvote + 1
			revrating = round(revrating,0)
			print(revrating)
			Movie.objects.filter(m_title = movie_prof).update(m_rrating = revrating)
			Movie.objects.filter(m_title = movie_prof).update(m_rvote = nvotes)
		else:
			revrating = (movieobj.m_rrating*movieobj.m_rvote + int(revrate) - test1.c_rating)/(movieobj.m_rvote)
			revrating = round(revrating,0)
			Movie.objects.filter(m_title = movie_prof).update(m_rrating = revrating)

		UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).update(c_time = time1)
		UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).update(c_rating = revrate)
		watchtime.objects.filter(pk = 1).update(w_time = time1) 
	
	mov = Movie.objects.all()
	fl = -1
	for var in mov:
		if (var.m_title == movie_prof):
			alb = var
			fl = 1
			break
	all_movies = UserMovies.objects.filter(c_name = tm)
	update1 = UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm).count()
	cate1 = -1
	if(update1 == 1):
		ate = UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm)
		for aa in ate:
			cate1 = aa.c_rating
	if (fl == -1):
		return render(request,'error.html')


	isreviewer = tm1.reviewer
	return render(request , 'movieprof.html' ,{'update1' : update1, 'isreviewer' : isreviewer
		,'alb' : alb , 'tm' : tm , 'all_movies' : all_movies, 'cate1' : cate1})

def error(request):
	return render(request,'error.html')

def custprof(request , cust_prof):
	dpurl = request.GET.get('dpurl')
	if dpurl:
		myobject = Customer.objects.filter(name=request.user.username).update(im_link=dpurl)

	tm = request.user.username
	cus = Customer.objects.all()
	fl = -1
	for var in cus:
		if(var.name == cust_prof):
			tm1 = var
			fl = 1
			break
	if(tm != cust_prof):
		fl = -2
	if (fl == -1):
		return render(request,'error.html')

	all_movies = Movie.objects.all()


	if (fl == -2):
		return render(request,'home.html',{'all_movies' : all_movies ,'tm' : tm})

	all_movies = UserMovies.objects.filter(c_name = tm).order_by('-c_time')[:26]
	print(all_movies.count())
	a = {}
	a1 = {}
	a2 = {}
	for mov in all_movies:
		curmov = Movie.objects.get(m_title = mov.c_movie_title)
		if curmov.m_dir in a:
			a[curmov.m_dir] = a[curmov.m_dir] + 1
		else:
			a[curmov.m_dir] = 1
		if curmov.m_genre in a1:
			a1[curmov.m_genre] = a1[curmov.m_genre] + 1
		else:
			a1[curmov.m_genre] = 1
		usrwatch = UserMovies.objects.filter(c_movie_title = mov.c_movie_title)
		for usr in usrwatch:
			if usr.c_name == tm1.name:
				break
			if usr.c_name in a2:
				a2[usr.c_name] = a2[usr.c_name] + 1
			else:
				a2[usr.c_name] = 1
	b = max(a,key = a.get)
	b1 = max(a1,key = a1.get)
	b2 = max(a2,key = a2.get)
	print(b)
	print(b1)
	print(b2)
	moviewatch = UserMovies.objects.filter(c_name = b2)
	pusermovies = UserMovies.objects.filter(c_name = tm)
	# ng_movie = null 
	# for mv in moviewatch:
	# 	f = 1
	# 	for pmv in pusermovies:
	# 		if pmv.c_name == mv.c_name:
	# 			f = 0
	# 			break
	# 	if f == 1:
	# 		mv = Movie.objects.get(m_title = mv.c_movie_title)
	# 		ng_movie = ng_movie + mv

	# movie7 = ng_movie.objects.raw('select * from finder_movie where m_title not in (select c_movie_title from finder_customer)')

	all_movies1 = Movie.objects.all()[:20]
	cust1 = tm1.Genre2
	movie1 = Movie.objects.raw('select * from finder_movie where m_genre = %s and m_title not in (select c_movie_title from finder_customer,finder_usermovies where c_name = name) order by m_urating desc',[tm1.Genre1])[:3]
	movie2 = Movie.objects.raw('select * from finder_movie where m_genre = %s and m_title not in (select c_movie_title from finder_customer,finder_usermovies where c_name = name) order by m_urating desc',[tm1.Genre2])[:3]
	movie3 = Movie.objects.raw('select * from finder_movie where m_genre = %s and m_title not in (select c_movie_title from finder_customer,finder_usermovies where c_name = name) order by m_urating desc',[tm1.Genre3])[:2]
	movie4 = Movie.objects.raw('select * from finder_movie where m_genre <> %s and m_genre != %s and m_genre != %s  and m_title not in (select c_movie_title from finder_customer,finder_usermovies where c_name = name) order by m_rrating desc',[tm1.Genre3,tm1.Genre2,tm1.Genre1])[:8]
	movie5 = Movie.objects.raw('select * from finder_movie where m_dir = %s and m_title not in (select c_movie_title from finder_customer,finder_usermovies where c_name = name) order by m_urating desc',[b])[:2]
	movie6 = Movie.objects.raw('select * from finder_movie where m_genre = %s and m_title not in (select c_movie_title from finder_customer,finder_usermovies where c_name = name) order by m_urating desc',[b1])[:2]
	movie7 = UserMovies.objects.raw('select * from finder_usermovies where c_movie_title not in (select c_movie_title from finder_usermovies where c_name = %s) and c_movie_title in (select c_movie_title from finder_usermovies where c_name = %s)',[tm1.name,b2])
	a3 = {}
	result = [];
	for titi in movie7:
		addition1 = Movie.objects.get(m_title = titi.c_movie_title)
		a3[addition1.m_title] = 1;
	movie4 = movie1 + movie2 + movie3 + movie4 + movie5 + movie6
	for titi in movie4:
		addition = Movie.objects.get(m_title = titi.m_title)
		a3[addition.m_title] = 1;

	mov = Movie.objects.all().order_by('-m_rrating')
	for chk in mov:
		if (chk.m_title in a3):
			result.append(chk)
			print(chk.m_title)

	print(tm1.Genre3, tm1.Genre2, tm1.Genre1)
	result = result[:20]
	isreviewer = tm1.reviewer
	return render(request , 'custprof.html' ,{'tm' : tm, 'tm1' : tm1, 'result' : result, 'movie3' : movie3, 'isreviewer' : isreviewer,
		'all_movies' : all_movies,'movie4' : movie4, 'movie2' : movie2 ,  'all_movies1' : all_movies1})


def movierate(request, movie_prof, movie_rate):
	gettime = watchtime.objects.get(pk = 1)
	time1 = gettime.w_time

	backq = 1
	rate1 = int(movie_rate)
	tm1 = request.user.username
	tm = Customer.objects.get(pk = tm1)
	mov = Movie.objects.all()
	if(rate1 >= 100 and rate1 < 111):
		backq = 2
		rate1 = rate1 - 100
	fl = -1
	for var in mov:
		if (var.m_title == movie_prof):
			alb = var
			fl = 1
			break

	if (fl == -1):
		return render(request,'error.html')
	print(tm1)
	if(rate1 == 0):
		update1 = UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).count()
		if(update1 == 0):
			userobj = UserMovies(c_name = tm1, c_movie_title = movie_prof,c_time = time1)
			time1 = time1 + 1 
			watchtime.objects.filter(pk = 1).update(w_time = time1)
			update1 = update1 + 1;
			userobj.save()
		time1 = time1 + 1 
		UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).update(c_time = time1)
		watchtime.objects.filter(pk = 1).update(w_time = time1) 
		return render(request, 'movierate.html', {'alb' : alb, 'update1' : update1,'backq' : backq, 'tm' : tm, 'rate1' : rate1})


	movieobj = Movie.objects.get(m_title = movie_prof)
	
	update1 = UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).count()
	#print(update1)
	time1 = time1 + 1

	if(update1 == 0):
		userobj = UserMovies(c_name = tm1, c_movie_title = movie_prof, c_time = time1)
		userobj.save()

	test1 = UserMovies.objects.get(c_movie_title = movie_prof,c_name = tm1)
	print(test1.c_rating)
	if(int(test1.c_rating) == -1):
		print(movieobj.m_urating*movieobj.m_uvote + int(rate1))
		userrating = (movieobj.m_urating*movieobj.m_uvote + int(rate1))/(movieobj.m_uvote + 1)
		nvotes = movieobj.m_uvote + 1
		userrating = round(userrating,3)
		print(userrating)
		Movie.objects.filter(m_title = movie_prof).update(m_urating = userrating)
		Movie.objects.filter(m_title = movie_prof).update(m_uvote = nvotes)
	else:
		userrating = (movieobj.m_urating*movieobj.m_uvote + int(rate1) - test1.c_rating)/(movieobj.m_uvote)
		userrating = round(userrating,3)
		Movie.objects.filter(m_title = movie_prof).update(m_urating = userrating)

	UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).update(c_time = time1)
	UserMovies.objects.filter(c_movie_title = movie_prof,c_name = tm1).update(c_rating = rate1)
	watchtime.objects.filter(pk = 1).update(w_time = time1) 
	

	return render(request, 'movierate.html', {'backq' : backq, 'tm' : tm, 'alb' : alb, 'rate1' : rate1})
