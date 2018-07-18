# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movie(models.Model):
	m_genre = models.CharField(max_length = 100, null = False, default = 'Action')
	m_title = models.CharField(max_length = 100 , default = None, null = False, primary_key = True)
	m_year = models.CharField(max_length = 200 , default = None, null = False)
	m_urating = models.FloatField(default = 10 , null = False)
	m_rrating = models.IntegerField(default = 100, null = False)
	m_uvote = models.IntegerField(default = 120)
	m_rvote = models.IntegerField(default = 20)
	m_dir = models.CharField(max_length = 200)
	m_url = models.CharField(max_length = 2000,default = None)
	m_description = models.CharField(max_length = 3000, default = "NICE")
	m_duration = models.CharField(default = None, null = False, max_length = 50)

	def __unicode__(self):
		return unicode(self.m_title)

class UserMovies(models.Model):
	c_name = models.CharField(null = False, max_length = 100, default = None)
	c_movie_title = models.CharField(null = False, max_length = 200, default = None)
	c_rating = models.FloatField(default = -1, null = False)
	c_time = models.IntegerField(default = 0, null = False)
	#def __unicode__(self):
	#	return unicode(self.u_movie_id)



class Customer(models.Model) :
	G_Choices = (
		('action','action') ,
		('animation','animation'),
		('crime' , 'crime'),
		('horror' , 'horror'),
		('sci-fi' , 'sci-fi'),
	)
	name = models.CharField(max_length=50,default=None,null=False, primary_key = True)
	reviewer = models.IntegerField(default = 0)
	Password = models.CharField(max_length=20,default=None,null=False)
	Genre1 = models.CharField(max_length = 20, default = 'Action' ,choices = G_Choices , null = False)
	Genre2 = models.CharField(max_length = 20, default = 'Romance' ,choices = G_Choices , null = False)
	Genre3 = models.CharField(max_length = 20, default = 'Thriller' ,choices = G_Choices , null = False)
	im_link = models.CharField(max_length = 1000, default = 'https://www.alaskapacific.edu/wp-content/uploads/2015/11/placeholder_profile_photo-200x200.png', null = False)
	def __unicode__(self):
		return unicode(self.name)

class Director(models.Model):
	d_name = models.CharField(max_length=100,default='Jane',primary_key = True,null = False)
	d_link = models.CharField(max_length=1000,default='https://www.alaskapacific.edu/wp-content/uploads/2015/11/placeholder_profile_photo-200x200.png')
	d_age = models.IntegerField(default = 40)
	d_bio = models.CharField(max_length=1000,default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
	def __unicode__(self):
		return unicode(self.d_name);

class Direcmovies(models.Model):
	direc_name = models.CharField(max_length= 100,null = False,default="Jane")
	direc_title = models.CharField(max_length = 100,null = False)

class watchtime(models.Model):
 	w_time = models.IntegerField(default = 1, null = False)