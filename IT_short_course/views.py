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
		'one_avg': round(one_avg, 3),
		'two_avg': round(two_avg, 3),
		'three_avg': round(three_avg, 3),
		'four_avg': round(four_avg, 3),
		'five_avg': round(five_avg, 3),
		'six_avg': round(six_avg, 3),
		'seven_avg': round(seven_avg, 3),
		'eight_avg': round(eight_avg, 3),
		'nine_avg': round(nine_avg, 3),
		'total_holes': round(total_holes, 3),
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
		'one_avg': round(one_avg, 3),
		'two_avg': round(two_avg, 3),
		'three_avg': round(three_avg, 3),
		'four_avg': round(four_avg, 3),
		'five_avg': round(five_avg, 3),
		'six_avg': round(six_avg, 3),
		'seven_avg': round(seven_avg, 3),
		'eight_avg': round(eight_avg, 3),
		'nine_avg': round(nine_avg, 3),
	}

	return render(request, 'single_player.html', context)



def matches(request):

	matches = Match.objects.all()


	context = {
		'matches': matches
	}
	return render(request, 'matches.html', context)



def match(request, match_id):

	rounds_in_match = Round.objects.filter(match=match_id)
	real_match = Match.objects.get(id=match_id)


	context = {
		'rounds_in_match': rounds_in_match,
		'real_match': real_match,
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

	# corey aces 
	aces = []
	player_rounds = corey_rounds
	for ace in player_rounds:
		aces.append(ace.ace_count())
	corey_aces = sum(aces)

	# tyler aces 
	spaces = []
	player_rounds = tyler_rounds
	for space in player_rounds:
		spaces.append(space.ace_count())
	tyler_aces = sum(spaces)

	# corey birdies 
	birdies = []
	player_rounds = corey_rounds
	for birdie in player_rounds:
		birdies.append(birdie.birdie_count())
	corey_birdies = sum(birdies)

	# tyler birdies 
	birdies2 = []
	player_rounds = tyler_rounds
	for birdie2 in player_rounds:
		birdies2.append(birdie2.birdie_count())
	tyler_birdies = sum(birdies2)

	# corey pars 
	pars = []
	all_rounds = corey_rounds
	for par in all_rounds:
		pars.append(par.par_count())
	corey_pars = sum(pars)

	# tyler pars 
	pars = []
	all_rounds = tyler_rounds
	for par in all_rounds:
		pars.append(par.par_count())
	tyler_pars = sum(pars)

	# corey bogies 
	bogies = []
	all_rounds = corey_rounds
	for bogie in all_rounds:
		bogies.append(bogie.bogie_count())
	corey_bogies = sum(bogies)

	# tyler bogies 
	bogies = []
	all_rounds = tyler_rounds
	for bogie in all_rounds:
		bogies.append(bogie.bogie_count())
	tyler_bogies = sum(bogies)

	# corey doubles 
	doubles = []
	all_rounds = corey_rounds
	for double in all_rounds:
		doubles.append(double.double_count())
	corey_doubles = sum(doubles)

	# tyler doubles 
	doubles = []
	all_rounds = tyler_rounds
	for double in all_rounds:
		doubles.append(double.double_count())
	tyler_doubles = sum(doubles)

	# corey trips and over 
	trips = []
	all_rounds = corey_rounds
	for trip in all_rounds:
		trips.append(trip.trip_and_over_count())
	corey_trips_and_above = sum(trips)

	# tyler trips and over 
	trips = []
	all_rounds = tyler_rounds
	for trip in all_rounds:
		trips.append(trip.trip_and_over_count())
	tyler_trips_and_above = sum(trips)

# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!
# I feel like I am repeating myself way too much! Not the DRY way to go!!

# COREY

	first = []
	second = []
	third = []
	fourth = []
	fifth = []
	sixth = []
	seventh = []
	eighth = []
	ninth = []

	player_rounds = corey_rounds

	for one_score in player_rounds:
		first.append(one_score.one)
	corey_one_avg = sum(first) / float(len(first))

	for two_score in player_rounds:
		second.append(two_score.two)
	corey_two_avg = sum(second) / float(len(second))

	for three_score in player_rounds:
		third.append(three_score.three)
	corey_three_avg = sum(third) / float(len(third))

	for four_score in player_rounds:
		fourth.append(four_score.four)
	corey_four_avg = sum(fourth) / float(len(fourth))

	for five_score in player_rounds:
		fifth.append(five_score.five)
	corey_five_avg = sum(fifth) / float(len(fifth))

	for six_score in player_rounds:
		sixth.append(six_score.six)
	corey_six_avg = sum(sixth) / float(len(sixth))

	for seven_score in player_rounds:
		seventh.append(seven_score.seven)
	corey_seven_avg = sum(seventh) / float(len(seventh))

	for eight_score in player_rounds:
		eighth.append(eight_score.eight)
	corey_eight_avg = sum(eighth) / float(len(eighth))

	for nine_score in player_rounds:
		ninth.append(nine_score.nine)
	corey_nine_avg = sum(ninth) / float(len(ninth))

# TYLER

	first = []
	second = []
	third = []
	fourth = []
	fifth = []
	sixth = []
	seventh = []
	eighth = []
	ninth = []

	player_rounds = tyler_rounds

	for one_score in player_rounds:
		first.append(one_score.one)
	tyler_one_avg = sum(first) / float(len(first))

	for two_score in player_rounds:
		second.append(two_score.two)
	tyler_two_avg = sum(second) / float(len(second))

	for three_score in player_rounds:
		third.append(three_score.three)
	tyler_three_avg = sum(third) / float(len(third))

	for four_score in player_rounds:
		fourth.append(four_score.four)
	tyler_four_avg = sum(fourth) / float(len(fourth))

	for five_score in player_rounds:
		fifth.append(five_score.five)
	tyler_five_avg = sum(fifth) / float(len(fifth))

	for six_score in player_rounds:
		sixth.append(six_score.six)
	tyler_six_avg = sum(sixth) / float(len(sixth))

	for seven_score in player_rounds:
		seventh.append(seven_score.seven)
	tyler_seven_avg = sum(seventh) / float(len(seventh))

	for eight_score in player_rounds:
		eighth.append(eight_score.eight)
	tyler_eight_avg = sum(eighth) / float(len(eighth))

	for nine_score in player_rounds:
		ninth.append(nine_score.nine)
	tyler_nine_avg = sum(ninth) / float(len(ninth))

	# total holes

	corey_rounds = Player.objects.get(name='Corey').round_set.all()
	tyler_rounds = Player.objects.get(name='Tyler').round_set.all()

	corey_holes = len(corey_rounds) * 9
	tyler_holes = len(tyler_rounds) * 9




	context = {

		'corey': corey,
		'tyler': tyler,
		'corey_average_score': corey_average_score,
		'tyler_average_score': tyler_average_score,
		'corey_average_hole': corey_average_hole,
		'tyler_average_hole': tyler_average_hole,
		'corey_aces': corey_aces,
		'tyler_aces': tyler_aces,
		'corey_birdies': corey_birdies,
		'tyler_birdies': tyler_birdies,
		'corey_pars': corey_pars,
		'tyler_pars': tyler_pars,
		'corey_bogies': corey_bogies,
		'tyler_bogies': tyler_bogies,
		'corey_doubles': corey_doubles,
		'tyler_doubles': tyler_doubles,
		'corey_trips_and_above': corey_trips_and_above,
		'tyler_trips_and_above': tyler_trips_and_above,

		# Corey individual holes
		'corey_one_avg': round(corey_one_avg, 3),
		'corey_two_avg': round(corey_two_avg, 3),
		'corey_three_avg': round(corey_three_avg, 3),
		'corey_four_avg': round(corey_four_avg, 3),
		'corey_five_avg': round(corey_five_avg, 3),
		'corey_six_avg': round(corey_six_avg, 3),
		'corey_seven_avg': round(corey_seven_avg, 3),
		'corey_eight_avg': round(corey_eight_avg, 3),
		'corey_nine_avg': round(corey_nine_avg, 3),

		# Tyler individual holes
		'tyler_one_avg': round(tyler_one_avg, 3),
		'tyler_two_avg': round(tyler_two_avg, 3),
		'tyler_three_avg': round(tyler_three_avg, 3),
		'tyler_four_avg': round(tyler_four_avg, 3),
		'tyler_five_avg': round(tyler_five_avg, 3),
		'tyler_six_avg': round(tyler_six_avg, 3),
		'tyler_seven_avg': round(tyler_seven_avg, 3),
		'tyler_eight_avg': round(tyler_eight_avg, 3),
		'tyler_nine_avg': round(tyler_nine_avg, 3),
		# total holes
		'corey_holes': corey_holes,
		'tyler_holes': tyler_holes



	}
	return render(request, 'all_player_stats.html', context)















