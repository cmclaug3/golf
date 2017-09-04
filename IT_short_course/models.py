# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


CONDITION_CHOICES = (
	('sunny', 'Sunny'),
	('overcast', 'Overcast'),
	('rainy', 'Rainy'),
)


class Player(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Match(models.Model):
	date = models.DateField()
	time = models.TimeField()
	condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)

	def __str__(self):
		return '{} {}'.format(self.date, self.time)


class Round(models.Model):
	player = models.ForeignKey(Player)
	match = models.ForeignKey(Match, null=True, blank=True)
	course = models.ForeignKey(Course, default="Indian Tree")
	one = models.IntegerField()
	two = models.IntegerField()
	three = models.IntegerField()
	four = models.IntegerField()
	five = models.IntegerField()
	six = models.IntegerField()
	seven = models.IntegerField()
	eight = models.IntegerField()
	nine = models.IntegerField()

	def __str__(self):
		return '{} {}'.format(self.player, self.match)

	def score_list(self):
		scores = [self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine]
		return scores

	def total_score(self):
		return sum(self.score_list())

	def ace_count(self):
		scores = self.score_list()
		count = 0
		for hole in scores:
			if hole == 1:
				count += 1
		return count		

	def birdie_count(self):
		scores = self.score_list()
		count = 0
		for hole in scores:
			if hole == 2:
				count += 1
		return count

	def par_count(self):
		scores = self.score_list()
		count = 0
		for hole in scores:
			if hole == 3:
				count += 1
		return count

	def bogie_count(self):
		scores = self.score_list()
		count = 0
		for hole in scores:
			if hole == 4:
				count += 1
		return count		

	def double_count(self):
		scores = self.score_list()
		count = 0
		for hole in scores:
			if hole == 5:
				count += 1
		return count

	def trip_and_over_count(self):
		scores = self.score_list()
		count = 0
		for hole in scores:
			if hole >= 6:
				count += 1
		return count

	@property
	def to_par(self):
		total = self.one+self.two+self.three+self.four+self.five+self.six+self.seven+self.eight+self.nine
		par = 27
		to_par = total - par
		return to_par

	def average_hole_score(self):
		average_hole = round(float((sum(self.score_list())) / 9.0), 2)
		return average_hole









	

