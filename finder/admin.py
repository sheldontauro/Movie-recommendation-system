# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from finder.models import Customer, Movie, UserMovies, watchtime, Director, Direcmovies

class CustomerAdmin(admin.ModelAdmin) :
	list_display = ["__unicode__"]
	class Meta:
		model = Customer

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Movie)
admin.site.register(UserMovies)

admin.site.register(watchtime)
admin.site.register(Director)
admin.site.register(Direcmovies)