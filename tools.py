#!/usr/bin/env python
#-*- coding: utf-8 -*-
# =======================
#       FONCTIONS
# =======================
def getLex():
	'''
		Lecture séquentielle du fichier "lexique.txt"
		où figurent lemmes et représentations phonétiques.
	'''
	# Ouverture d'un flux vers la ressource
	with open('lexique.txt', 'r') as src:
		ligne = lexique = ""
		# Tant que la condition se vérifie (c-à-d toujours !)
		while True:
			# La ligne courante dans la variable "txt"
			ligne = src.readline()
			# Si "txt" ne contient rien du tout
			if ligne == "":
				# Alors, on met un terme à la boucle (ouf !)
				break
			else:
				lexique += ligne
	# Formatage d'une liste d'entrées
	return lexique.split('\n')[:-1]

def getDicoLex(lexique):
	'''
		À partir du lexique, création d'un dictionnaire sous la forme :
		{ lemme: phonétique }
	'''
	dico = {}

	for ligne in lexique:
		lem = ligne.split('\t')[0]
		phon = ligne.split('\t')[1]
		dico.update({lem: phon})

	# On retourne le dictionnaire
	return dico

def getMot(lexique):
	'''
		Tirage d'un mot au hasard dans le lexique
	'''
	# Importation du module random
	from random import choice
	# Tirage au sort d'une entrée dans le lexique
	mot = choice(lexique)
	# Récupération du lemme et de la représentation phonétique
	lemme = mot.split('\t')[0]
	phonetique = ia.split('\t')[1]
	return (lemme, phonetique)

def existeMot(mot, dico):
	'''
		Teste si un mot saisi par l'utilisateur existe bien dans le dictionnaire
	'''
	try:
		if mot in dico.keys(): return 1
	except KeyError:
		return 0


# Menu principal
def main_menu():
	'''
		Affichage du menu
	'''
	print('Merci de sélectionner une option :')
	print('1. Jouer !')
	#print '2. 2 joueurs humains'
	print('9. Aide')
	print('0. Quitter')
	return int(input(">>  "))

def aide():
	'''
		Affichage de l'aide du jeu
	'''
	msg = '###############\n'
	msg += '# Aide de jeu #\n'
	msg += '###############\n'
	msg += '\n'
	msg += 'Phon Game est un jeu de langage ultra-simple :\n'
	msg += 'Tout mot proposé par un joueur doit reprendre l’un des trois derniers phonèmes du mot précédent !\n'
	msg += '# Règles\n'
	msg += '- Un mot ne peut être proposé qu’une seule fois\n'
	msg += '- Seuls l’infinitif ou le masculin singulier sont acceptés\n'
	msg += '# Fonctionnalités :\n'
	msg += '- Pour sortir du programme, appuyez sur la touche "0"\n'
	msg += '- Pour obtenir le message d’aide, appuyez sur la touche "9"\n'
	msg += '# Base de données\n'
	msg += 'Phon Game repose sur une exploitation de LEXIQUE v3.81 :\n'
	msg += 'New B., Pallier C., Ferrand L., Matos R. (2001). – Une base de données lexicales du français contemporain sur internet : LEXIQUE. – "L’Année Psychologique", 101, 447-462. http://www.lexique.org'
	return msg

# =======================
#         LISTES
# =======================
def msg_erreurs(code, mot = ''):
	'''
		Retourne le message d'erreur approprié
	'''
	erreurs = {
		'err_00' : '\n/!\\ Saisissez l’une des valeurs autorisées (1, 9 ou 0)/!\\\n',
		'err_01' : '\n/!\\ Veuillez saisir une valeur numérique parmi celles autorisées (1, 2, 9 ou 0) /!\\\n',
		'err_02' : '\n/!\\ Le mot "{}" ne figure pas dans le dictionnaire. Merci d’en saisir un autre ! /!\\\n'.format(mot),
		'err_03' : '\nÀ bientôt sur Phon Game !\n',
		'err_04' : '\n/!\ Le mot "{}" a déjà été proposé /!\\n'.format(mot)
	}
	return erreurs[code]