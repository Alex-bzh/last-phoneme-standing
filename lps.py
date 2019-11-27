#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
	Jeu où chaque mot donné par un utilisateur doit débuter par les phonèmes
	qui terminent le mot précédent.
'''
# =======================
#        MODULES
# =======================
import tools

# =======================
#   PROGRAMME PRINCIPAL
# =======================
 
# Programme principal
if __name__ == "__main__":

	# Affichage du message de bienvenue
	print '###############'
	print '# Phon Game ! #'
	print '###############'

	# Affichage du menu
	while 1:
		try:
			# Choix de l'utilisateur
			choix = int(tools.main_menu())
			# Soit il joue, soit il quitte
			if choix in [0,1]:
				# Si l'option 0 est choisie
				if choix == 0:
					# On le remercie d'avoir joué
					print tools.msg_erreurs('err_03')
					# On ferme le programme
					exit()
				# Sinon, on sort de la boucle et on se met à jouer
				else:
					break
			# Soit il veut un peu d'aide pour apprendre à jouer
			elif choix == 9:
				print tools.aide()
			# Soit, enfin, il a entré une option qui n'existe pas
			else:
				print tools.msg_erreurs('err_00')
		# On lève une exception s'il a saisi des caractères alphabétiques
		except ValueError:
			# Affichage d'un message d'erreur
			print tools.msg_erreurs('err_01')

	lexique = tools.getLex()			# Acquisition du lexique
	dico = tools.getDicoLex(lexique)	# Constitution d'un dictionnaire de référence

	motsJoues = []						# Liste des mots joués pendant la partie
	mot = ''							# Mot à comparer
	nbRounds = 1						# Nombre de rounds
	nbTours = 1							# Nombre de tours

	while 1:
		if nbRounds % 2:
			print '###########{}'.format('#' * len(str(nbTours)))
			print "# Tour n°{} #".format(nbTours)
			print '###########{}'.format('#' * len(str(nbTours)))
			if mot != '': print "Le mot en cours est : {}\nPour arrêter le jeu, appuyez sur la touche 0".format(mot)
			nbTours += 1
		# Saisie utilisateur
		ih = raw_input("Choisissez un mot ?\n>> ").lower()
		# S'il appuie sur le zéro
		if ih == '0':
			# On le remercie d'avoir joué
			print tools.msg_erreurs('err_03')
			# On ferme le programme
			exit()
		elif ih == '9':
			print tools.aide()
		else:
			# Si l'entrée n'est pas dans le dictionnaire
			if not tools.existeMot(ih, dico):
				# Renvoyer un message d'erreur
				print tools.msg_erreurs('err_02', ih)
			# Et si elle ne figure pas déjà dans la liste des mots joués
			elif ih in motsJoues:
				print tools.msg_erreurs('err_04', ih)
			# L'entrée figure bien dans le dictionnaire
			else:
				# On la rajoute à la liste des mots joués
				motsJoues.append(ih)
				# S'il existe un mot à comparer
				if mot != '':
					# Récupérer ses trois derniers phonèmes
					motLastPhon = dico[mot][-3:]
					# Ainsi que les trois premiers de la saisie utilisateur
					ihFirstPhon = dico[ih][:3]
					# Comparer !
					print "Comparaison de {} et {}…".format(dico[mot], dico[ih])
					if ihFirstPhon == motLastPhon:
						print "Matching complet des phonèmes ({}) !".format(motLastPhon)
					elif ihFirstPhon[:2] in motLastPhon:
						print "2 phonèmes correspondent ({}), c'est bien !".format(ihFirstPhon[:2])
					elif ihFirstPhon[:1] in motLastPhon:
						print "un seul phonème en commun ({}), continuez !".format(ihFirstPhon[:1])
					else:
						print "Désolé, on ne peut valider le point"
						# On retire le mot proposé de la liste des mots joués (c'est le dernier)

						ih = mot
				mot = ih
				nbRounds += 1