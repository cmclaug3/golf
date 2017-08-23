# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse

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


	# total holes
	total_holes = len(all_rounds) * 9

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
		'nine_avg': nine_avg,
		'total_holes': total_holes
	}
	return render(request, 'home.html', context)




def single_player(request, player_id):

	player = Player.objects.get(id=player_id)
	player_rounds = player.round_set.all()

	# player average score
	yea = []
	test = player_rounds
	for score in test:
		yea.append(score.to_par)
	player_average_score = round((sum(yea)) / float(test.count()), 3)

	# player average hole
	holes = []
	big = player_rounds
	for hole_score in big:
		holes.append(hole_score.average_hole_score())
	player_average_hole = round((sum(holes)) / float(big.count()), 3)

	# player aces 
	aces = []
	for ace in player_rounds:
		aces.append(ace.ace_count())
	player_aces = sum(aces)

	# player birdies 
	birdies = []
	for birdie in player_rounds:
		birdies.append(birdie.birdie_count())
	player_birdies = sum(birdies)

	# player pars 
	pars = []
	for par in player_rounds:
		pars.append(par.par_count())
	player_pars = sum(pars)

	# player bogies 
	bogies = []
	for bogie in player_rounds:
		bogies.append(bogie.bogie_count())
	player_bogies = sum(bogies)

	# player doubles 
	doubles = []
	for double in player_rounds:
		doubles.append(double.double_count())
	player_doubles = sum(doubles)

	# player trips and over 
	trips = []
	for trip in player_rounds:
		trips.append(trip.trip_and_over_count())
	player_trips_and_above = sum(trips)

	# player average score by hole
	first = []
	second = []
	third = []
	fourth = []
	fifth = []
	sixth = []
	seventh = []
	eighth = []
	ninth = []

	for one_score in player_rounds:
		first.append(one_score.one)
	one_avg = sum(first) / float(len(first))

	for two_score in player_rounds:
		second.append(two_score.two)
	two_avg = sum(second) / float(len(second))

	for three_score in player_rounds:
		third.append(three_score.three)
	three_avg = sum(third) / float(len(third))

	for four_score in player_rounds:
		fourth.append(four_score.four)
	four_avg = sum(fourth) / float(len(fourth))

	for five_score in player_rounds:
		fifth.append(five_score.five)
	five_avg = sum(fifth) / float(len(fifth))

	for six_score in player_rounds:
		sixth.append(six_score.six)
	six_avg = sum(sixth) / float(len(sixth))

	for seven_score in player_rounds:
		seventh.append(seven_score.seven)
	seven_avg = sum(seventh) / float(len(seventh))

	for eight_score in player_rounds:
		eighth.append(eight_score.eight)
	eight_avg = sum(eighth) / float(len(eighth))

	for nine_score in player_rounds:
		ninth.append(nine_score.nine)
	nine_avg = sum(ninth) / float(len(ninth))

	# player match record
	

	context = {
		'player_name': player.name,
		'player_rounds_amount': len(player_rounds),
		'player_average_score': player_average_score,
		'round_total': len(player_rounds) * 9,
		'player_average_hole': player_average_hole,
		'player_aces': player_aces,
		'player_birdies': player_birdies,
		'player_pars': player_pars,
		'player_bogies': player_bogies,
		'player_doubles': player_doubles,
		'player_trips_and_above': player_trips_and_above,
		# player
		'one_avg': one_avg,
		'two_avg': two_avg,
		'three_avg': three_avg,
		'four_avg': four_avg,
		'five_avg': five_avg,
		'six_avg': six_avg,
		'seven_avg': seven_avg,
		'eight_avg': eight_avg,
		'nine_avg': nine_avg,
	}

	return render(request, 'single_player.html', context)



def matches(request):
	context = {
		'matches': Match.objects.all()
	}
	return render(request, 'matches.html', context)



def match(request, match_id):
	match = Round.objects.filter(match=match_id)
	context = {
		'match': match
	}
	return render(request, 'match.html', context)



def all_player_stats(request):

	corey = Player.objects.get(name='Corey')
	tyler = Player.objects.get(name='Tyler')

	corey_rounds = corey.round_set.all()
	tyler_rounds = tyler.round_set.all()


	# corey average score
	yea = []
	for score in corey_rounds:
		yea.append(score.to_par)
	corey_average_score = round((sum(yea)) / float(corey_rounds.count()), 3)

	# tyler average score
	scores = []
	for par in tyler_rounds:
		scores.append(par.to_par)
	tyler_average_score = round((sum(scores)) / float(tyler_rounds.count()), 3)

	# corey average hole
	holes = []
	big = corey_rounds
	for hole_score in big:
		holes.append(hole_score.average_hole_score())
	corey_average_hole = round((sum(holes)) / float(big.count()), 3)

	# tyler average hole
	tees = []
	small = tyler_rounds
	for tee_score in small:
		tees.append(tee_score.average_hole_score())
	tyler_average_hole = round((sum(tees)) / float(small.count()), 3)

# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!

	context = {

		'corey': corey,
		'tyler': tyler,
		'corey_average_score': corey_average_score,
		'tyler_average_score': tyler_average_score,
		'corey_average_hole': corey_average_hole,
		'tyler_average_hole': tyler_average_hole

	}
	return render(request, 'all_player_stats.html', context)















