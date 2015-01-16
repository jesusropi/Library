#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

@python_2_unicode_compatible
class Author(models.Model):
	"""
		Author of the book
	"""
	name = models.CharField('name', max_length=200)
	surname = models.CharField('surname', max_length=200)
	birth = models.DateField('birth')
	
	class Meta:
		verbose_name = _('author')
		verbose_name_plural = _('authors')

	def __str__(self):
		return self.name + self.surname

@python_2_unicode_compatible
class Book(models.Model):
	"""
		Book
	"""
	title = models.CharField('título', max_length=200)
	isbn = models.CharField('isbn', max_length=13)
	GENRE = (('E', 'Epica'), 
			('L', 'Lirica'),
			)
	t_genre = models.CharField(max_length=1, choices=GENRE, default='L')
	authors = models.ManyToManyField(Author)
	
	class Meta:
		verbose_name = _('book')
		verbose_name_plural = _('books')
	
	def __str__(self):
		return self.title + self.isbn