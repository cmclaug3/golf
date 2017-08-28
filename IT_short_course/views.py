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



def holes(request):

	all_rounds = Round.objects.all()
	corey_rounds = Player.objects.get(name='Corey').round_set.all()
	tyler_rounds = Player.objects.get(name='Tyler').round_set.all()

	cm_ones = []
	cm_twos = []
	cm_threes = []
	cm_fours = []
	cm_fives = []
	cm_sixes = []
	cm_sevens = []
	cm_eights = []
	cm_nines = []

	td_ones = []
	td_twos = []
	td_threes = []
	td_fours = []
	td_fives = []
	td_sixes = []
	td_sevens = []
	td_eights = []
	td_nines = []

	for one in corey_rounds:
		cm_ones.append(one.one)
	for one1 in tyler_rounds:
		td_ones.append(one1.one)
	for two in corey_rounds:
		cm_twos.append(two.two)
	for two1 in tyler_rounds:
		td_twos.append(two1.two)
	for three in corey_rounds:
		cm_threes.append(three.three)
	for three1 in tyler_rounds:
		td_threes.append(three1.three)
	for four in corey_rounds:
		cm_fours.append(four.four)
	for four1 in tyler_rounds:
		td_fours.append(four1.four)
	for five in corey_rounds:
		cm_fives.append(five.five)
	for five1 in tyler_rounds:
		td_fives.append(five1.five)
	for six in corey_rounds:
		cm_sixes.append(six.six)
	for six1 in tyler_rounds:
		td_sixes.append(six1.six)
	for seven in corey_rounds:
		cm_sevens.append(seven.seven)
	for seven1 in tyler_rounds:
		td_sevens.append(seven1.seven)
	for eight in corey_rounds:
		cm_eights.append(eight.eight)
	for eight1 in tyler_rounds:
		td_eights.append(eight1.eight)
	for nine in corey_rounds:
		cm_nines.append(nine.nine)
	for nine1 in tyler_rounds:
		td_nines.append(nine1.nine)

# FIRST
	cm_one_aces = []
	cm_one_birdies = []
	cm_one_pars = []
	cm_one_bogies = []
	cm_one_doubles = []
	cm_one_trips = []

	for a in cm_ones:
		if a == 1:
			cm_one_aces.append(a)
		elif a == 2:
			cm_one_birdies.append(a)
		elif a == 3:
			cm_one_pars.append(a)
		elif a == 4:
			cm_one_bogies.append(a)
		elif a == 5:
			cm_one_doubles.append(a)
		elif a >= 6:
			cm_one_trips.append(a)

	td_one_aces = []
	td_one_birdies = []
	td_one_pars = []
	td_one_bogies = []
	td_one_doubles = []
	td_one_trips = []

	for b in td_ones:
		if b == 1:
			td_one_aces.append(b)
		elif b == 2:
			td_one_birdies.append(b)
		elif b == 3:
			td_one_pars.append(b)
		elif b == 4:
			td_one_bogies.append(b)
		elif b == 5:
			td_one_doubles.append(b)
		elif b >= 6:
			td_one_trips.append(b)

# SECOND
	cm_two_aces = []
	cm_two_birdies = []
	cm_two_pars = []
	cm_two_bogies = []
	cm_two_doubles = []
	cm_two_trips = []

	for c in cm_twos:
		if c == 1:
			cm_two_aces.append(c)
		elif c == 2:
			cm_two_birdies.append(c)
		elif c == 3:
			cm_two_pars.append(c)
		elif c == 4:
			cm_two_bogies.append(c)
		elif c == 5:
			cm_two_doubles.append(c)
		elif c >= 6:
			cm_two_trips.append(c)

	td_two_aces = []
	td_two_birdies = []
	td_two_pars = []
	td_two_bogies = []
	td_two_doubles = []
	td_two_trips = []

	for d in td_twos:
		if d == 1:
			td_two_aces.append(d)
		elif d == 2:
			td_two_birdies.append(d)
		elif d == 3:
			td_two_pars.append(d)
		elif d == 4:
			td_two_bogies.append(d)
		elif d == 5:
			td_two_doubles.append(d)
		elif d >= 6:
			td_two_trips.append(d)

# THIRD
	cm_three_aces = []
	cm_three_birdies = []
	cm_three_pars = []
	cm_three_bogies = []
	cm_three_doubles = []
	cm_three_trips = []

	for e in cm_threes:
		if e == 1:
			cm_three_aces.append(e)
		elif e == 2:
			cm_three_birdies.append(e)
		elif e == 3:
			cm_three_pars.append(e)
		elif e == 4:
			cm_three_bogies.append(e)
		elif e == 5:
			cm_three_doubles.append(e)
		elif e >= 6:
			cm_three_trips.append(e)

	td_three_aces = []
	td_three_birdies = []
	td_three_pars = []
	td_three_bogies = []
	td_three_doubles = []
	td_three_trips = []

	for f in td_threes:
		if f == 1:
			td_three_aces.append(f)
		elif f == 2:
			td_three_birdies.append(f)
		elif f == 3:
			td_three_pars.append(f)
		elif f == 4:
			td_three_bogies.append(f)
		elif f == 5:
			td_three_doubles.append(f)
		elif f >= 6:
			td_three_trips.append(f)

# FOURTH
	cm_four_aces = []
	cm_four_birdies = []
	cm_four_pars = []
	cm_four_bogies = []
	cm_four_doubles = []
	cm_four_trips = []

	for g in cm_fours:
		if g == 1:
			cm_four_aces.append(g)
		elif g == 2:
			cm_four_birdies.append(g)
		elif g == 3:
			cm_four_pars.append(g)
		elif g == 4:
			cm_four_bogies.append(g)
		elif g == 5:
			cm_four_doubles.append(g)
		elif g >= 6:
			cm_four_trips.append(g)

	td_four_aces = []
	td_four_birdies = []
	td_four_pars = []
	td_four_bogies = []
	td_four_doubles = []
	td_four_trips = []

	for h in td_fours:
		if h == 1:
			td_four_aces.append(h)
		elif h == 2:
			td_four_birdies.append(h)
		elif h == 3:
			td_four_pars.append(h)
		elif h == 4:
			td_four_bogies.append(h)
		elif h == 5:
			td_four_doubles.append(h)
		elif h >= 6:
			td_four_trips.append(h)

# FIFTH
	cm_five_aces = []
	cm_five_birdies = []
	cm_five_pars = []
	cm_five_bogies = []
	cm_five_doubles = []
	cm_five_trips = []

	for i in cm_fives:
		if i == 1:
			cm_five_aces.append(i)
		elif i == 2:
			cm_five_birdies.append(i)
		elif i == 3:
			cm_five_pars.append(i)
		elif i == 4:
			cm_five_bogies.append(i)
		elif i == 5:
			cm_five_doubles.append(i)
		elif i >= 6:
			cm_five_trips.append(i)

	td_five_aces = []
	td_five_birdies = []
	td_five_pars = []
	td_five_bogies = []
	td_five_doubles = []
	td_five_trips = []

	for j in td_fives:
		if j == 1:
			td_five_aces.append(j)
		elif j == 2:
			td_five_birdies.append(j)
		elif j == 3:
			td_five_pars.append(j)
		elif j == 4:
			td_five_bogies.append(j)
		elif j == 5:
			td_five_doubles.append(j)
		elif j >= 6:
			td_five_trips.append(j)

# SIXTH
	cm_six_aces = []
	cm_six_birdies = []
	cm_six_pars = []
	cm_six_bogies = []
	cm_six_doubles = []
	cm_six_trips = []

	for k in cm_sixes:
		if k == 1:
			cm_six_aces.append(k)
		elif k == 2:
			cm_six_birdies.append(k)
		elif k == 3:
			cm_six_pars.append(k)
		elif k == 4:
			cm_six_bogies.append(k)
		elif k == 5:
			cm_six_doubles.append(k)
		elif k >= 6:
			cm_six_trips.append(k)

	td_six_aces = []
	td_six_birdies = []
	td_six_pars = []
	td_six_bogies = []
	td_six_doubles = []
	td_six_trips = []

	for l in td_sixes:
		if l == 1:
			td_six_aces.append(l)
		elif l == 2:
			td_six_birdies.append(l)
		elif l == 3:
			td_six_pars.append(l)
		elif l == 4:
			td_six_bogies.append(l)
		elif l == 5:
			td_six_doubles.append(l)
		elif l >= 6:
			td_six_trips.append(l)



	context = {
		'all_rounds': all_rounds,
# first
		'cm_one_aces': len(cm_one_aces),
		'cm_one_birdies': len(cm_one_birdies),
		'cm_one_pars': len(cm_one_pars),
		'cm_one_bogies': len(cm_one_bogies),
		'cm_one_doubles': len(cm_one_doubles),
		'cm_one_trips': len(cm_one_trips),

		'td_one_aces': len(td_one_aces),
		'td_one_birdies': len(td_one_birdies),
		'td_one_pars': len(td_one_pars),
		'td_one_bogies': len(td_one_bogies),
		'td_one_doubles': len(td_one_doubles),
		'td_one_trips': len(td_one_trips),
# second
		'cm_two_aces': len(cm_two_aces),
		'cm_two_birdies': len(cm_two_birdies),
		'cm_two_pars': len(cm_two_pars),
		'cm_two_bogies': len(cm_two_bogies),
		'cm_two_doubles': len(cm_two_doubles),
		'cm_two_trips': len(cm_two_trips),

		'td_two_aces': len(td_two_aces),
		'td_two_birdies': len(td_two_birdies),
		'td_two_pars': len(td_two_pars),
		'td_two_bogies': len(td_two_bogies),
		'td_two_doubles': len(td_two_doubles),
		'td_two_trips': len(td_two_trips),
# third
		'cm_three_aces': len(cm_three_aces),
		'cm_three_birdies': len(cm_three_birdies),
		'cm_three_pars': len(cm_three_pars),
		'cm_three_bogies': len(cm_three_bogies),
		'cm_three_doubles': len(cm_three_doubles),
		'cm_three_trips': len(cm_three_trips),

		'td_three_aces': len(td_three_aces),
		'td_three_birdies': len(td_three_birdies),
		'td_three_pars': len(td_three_pars),
		'td_three_bogies': len(td_three_bogies),
		'td_three_doubles': len(td_three_doubles),
		'td_three_trips': len(td_three_trips),
# fourth
		'cm_four_aces': len(cm_four_aces),
		'cm_four_birdies': len(cm_four_birdies),
		'cm_four_pars': len(cm_four_pars),
		'cm_four_bogies': len(cm_four_bogies),
		'cm_four_doubles': len(cm_four_doubles),
		'cm_four_trips': len(cm_four_trips),

		'td_four_aces': len(td_four_aces),
		'td_four_birdies': len(td_four_birdies),
		'td_four_pars': len(td_four_pars),
		'td_four_bogies': len(td_four_bogies),
		'td_four_doubles': len(td_four_doubles),
		'td_four_trips': len(td_four_trips),

# fifth
		'cm_five_aces': len(cm_five_aces),
		'cm_five_birdies': len(cm_five_birdies),
		'cm_five_pars': len(cm_five_pars),
		'cm_five_bogies': len(cm_five_bogies),
		'cm_five_doubles': len(cm_five_doubles),
		'cm_five_trips': len(cm_five_trips),

		'td_five_aces': len(td_five_aces),
		'td_five_birdies': len(td_five_birdies),
		'td_five_pars': len(td_five_pars),
		'td_five_bogies': len(td_five_bogies),
		'td_five_doubles': len(td_five_doubles),
		'td_five_trips': len(td_five_trips),

# sixth
		'cm_six_aces': len(cm_six_aces),
		'cm_six_birdies': len(cm_six_birdies),
		'cm_six_pars': len(cm_six_pars),
		'cm_six_bogies': len(cm_six_bogies),
		'cm_six_doubles': len(cm_six_doubles),
		'cm_six_trips': len(cm_six_trips),

		'td_six_aces': len(td_six_aces),
		'td_six_birdies': len(td_six_birdies),
		'td_six_pars': len(td_six_pars),
		'td_six_bogies': len(td_six_bogies),
		'td_six_doubles': len(td_six_doubles),
		'td_six_trips': len(td_six_trips),

		# this cannot be the way to do it...


	}
	return render(request, 'holes.html', context)


# def hole(request, hole_id):

	

# 	context = {
# 		'hole': hole
# 	}
# 	return render(request, 'hole.html', context)



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















