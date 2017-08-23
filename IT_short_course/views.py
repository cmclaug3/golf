# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from IT_short_course.models import Round, Player, Match


def home(request):

	# total average score
	yea = []
	test = Round.objects.all()
	for score in test:
		yea.append(score.to_par)
	total_average_score = round((sum(yea)) / float(test.count()), 3)

	# total average hole
	holding = []
	all_rounds = Round.objects.all()
	for avg_hole in all_rounds:
		holding.append(avg_hole.average_hole_score())
	total_average_hole = round((sum(holding)) / float(all_rounds.count()), 3)

	# total aces 
	aces = []
	for ace in all_rounds:
		aces.append(ace.ace_count())
	total_aces = sum(aces)

	# total birdies 
	birdies = []
	for birdie in all_rounds:
		birdies.append(birdie.birdie_count())
	total_birdies = sum(birdies)

	# total pars 
	pars = []
	for par in all_rounds:
		pars.append(par.par_count())
	total_pars = sum(pars)

	# total bogies 
	bogies = []
	for bogie in all_rounds:
		bogies.append(bogie.bogie_count())
	total_bogies = sum(bogies)

	# total doubles 
	doubles = []
	for double in all_rounds:
		doubles.append(double.double_count())
	total_doubles = sum(doubles)

	# total trips and over 
	trips = []
	for trip in all_rounds:
		trips.append(trip.trip_and_over_count())
	total_trips_and_above = sum(trips)


	# average score by hole
	first = []
	second = []
	third = []
	fourth = []
	fifth = []
	sixth = []
	seventh = []
	eighth = []
	ninth = []

	for one_score in all_rounds:
		first.append(one_score.one)
	one_avg = sum(first) / float(len(first))

	for two_score in all_rounds:
		second.append(two_score.two)
	two_avg = sum(second) / float(len(second))

	for three_score in all_rounds:
		third.append(three_score.three)
	three_avg = sum(third) / float(len(third))

	for four_score in all_rounds:
		fourth.append(four_score.four)
	four_avg = sum(fourth) / float(len(fourth))

	for five_score in all_rounds:
		fifth.append(five_score.five)
	five_avg = sum(fifth) / float(len(fifth))

	for six_score in all_rounds:
		sixth.append(six_score.six)
	six_avg = sum(sixth) / float(len(sixth))

	for seven_score in all_rounds:
		seventh.append(seven_score.seven)
	seven_avg = sum(seventh) / float(len(seventh))

	for eight_score in all_rounds:
		eighth.append(eight_score.eight)
	eight_avg = sum(eighth) / float(len(eighth))

	for nine_score in all_rounds:
		ninth.append(nine_score.nine)
	nine_avg = sum(ninth) / float(len(ninth))


	# hardest to easiest holes
	


	context = {
		'all_rounds': all_rounds,
		'all_players': Player.objects.all(),
		'all_matches': Match.objects.all(),
		'total_average_score': total_average_score,
		'total_average_hole': total_average_hole,
		'total_aces': total_aces,
		'total_birdies': total_birdies,
		'total_pars': total_pars,
		'total_bogies': total_bogies,
		'total_doubles': total_doubles,
		'total_trips_and_above': total_trips_and_above,
		'one_avg': one_avg,
		'two_avg': two_avg,
		'three_avg': three_avg,
		'four_avg': four_avg,
		'five_avg': five_avg,
		'six_avg': six_avg,
		'seven_avg': seven_avg,
		'eight_avg': eight_avg,
		'nine_avg': nine_avg
	}
	return render(request, 'home.html', context)


