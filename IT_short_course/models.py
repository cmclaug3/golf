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


class Match(models.Model):
	date = models.DateField()
	time = models.TimeField()
	condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)

	def __str__(self):
		return '{} {}'.format(self.date, self.time)


class Round(models.Model):
	player = models.ForeignKey(Player)
	match = models.ForeignKey(Match)
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

		


	

