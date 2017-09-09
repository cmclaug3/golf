# TODO


# Individual Match View

# 	Matplotlib graphing itegration
# 	watch scores of the round as it happens



# the unDRY problem
	
# 	what you need to do is write model methods/views that recycle the calculation 
# 	either in loop or in function argument



# ANNOTATE EX
# for i in Player.objects.annotate(avg_three=Avg('round__three')):
#     print('{} averages {} on three'.format(i.name, i.avg_three))



# COURSE MODEL ADD ON SCREW UPS
# 	Home = GOOD
# 	Matches = GOOD
# 	Holes = Just showing Indian Tree, (7-9) shows list of all hole scores
# 	All Stats: Total = GOOD, Hole by Hole = Just showing Indian three


# PARS OR BETTER / TOTAL HOLES
# corey_rounds = Player.objects.get(name='Corey').round_set.all()
# new = [i.score_list() for i in corey_rounds]
# holes_par_or_better = []
# for x in new:
#     for y in x:
#         if y <= 3:
#             holes_par_or_better.append(y)
# pars_or_better_ratio = len(holes_par_or_better) / (len(corey_rounds)*9)

		# ALSO COULD DO BOGIES OR BETTER

# master_ratio = concept of calculating an average round in terms on aces, birdies, pars, etc...
# last five round scores and average



# tyler_rounds = Round.objects.filter(player__name='Tyler')
# big_list = [i.score_list() for i in tyler_rounds]
# par_under = []
# for x in big_list:
#     for y in x:
#         if y <= 3:
#             par_under.append(y)
# par_ratio = len(par_under) / 180.0












