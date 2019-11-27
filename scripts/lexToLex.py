#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Ouverture d'un flux vers la ressource
with open('lexique381.txt', 'r') as src:
	ligne = fichier = ""
	# Tant que la condition se vérifie (c-à-d toujours !)
	while True:
		# La ligne courante dans la variable "txt"
		ligne = src.readline()
		# Si "txt" ne contient rien du tout
		if ligne == "":
			# Alors, on met un terme à la boucle (ouf !)
			break
		else:
			fichier += ligne

# lexique = liste de mots avec différentes infos
# lemmes = liste de lemmes
lexique, lemmes = [], []
# Pour chaque ligne du fichier
for ligne in fichier.split('\n')[1:-1]:
	# Récupération des seules infos opportunes
	mot = ligne.split('\t')[0]
	phonemes = ligne.split('\t')[1]
	lemme = ligne.split('\t')[2]
	# màj du lexique
	lexique.append([mot, phonemes, lemme])
	# màj des lemmes
	lemmes.append(lemme)
# éliminer les doublons grâce à un set
lemmes = set(lemmes)

# Création d'un dictionnaire
dico = {}

# Pour chaque lemme
for lemme in lemmes:
	# Parcourir le lexique
	for ligne in lexique:
		# [0] : mot ; [1] : phonétique ; [2] : lemme
		if lemme == ligne[0]:
			dico.update({lemme: ligne[1]})

lex = ''
for mot in dico:
	lex += '{}\t{}\n'.format(mot, dico[mot])

with open('lexique.txt', 'w') as dest:
	dest.write(lex)