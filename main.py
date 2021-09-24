print ('1. Listes')

print ('1.1 Modifier une liste')
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]

print('1.1.1 Supprimez les trois derniers éléments un par un, dans un premier temps')
print (annee)
del(annee[-1])
print (annee)
del(annee[-1])
print (annee)
del(annee[-1])
print (annee)

print("1.1.2 Puis rajoutez les mois 'Octobre', 'Novembre', 'Décembre' à la fin")
moisManquant = ['Octobre', 'Novembre', 'Decembre']
annee = annee + moisManquant
print (annee)

print('1.1.3 Supprimez les trois derniers éléments un par un, dans un premier temps')
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
annee[9] = 'Octobre'
annee[10] = 'Novembre'
annee[11] = 'Decembre'

print(annee)

print('1.1.4 Pour aller plus loin : la liste ‘en compréhension’')
x = [1, 2, 3, 4, 3, 5, 3, 1, 3, 2]
resultat = [y+1 for y in x]
print(resultat)

print('2. Tuples')
moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')

print('2.1 Accès aux éléments d’un tuple')
print(moisDeLannee[3])

print('2.2 Vérifier la présence d’un élément dans un tuple')
print('mars' in moisDeLannee)
print('Mars' in moisDeLannee)

print('3. Dictionnaires')
age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23}

print('3.1 Ajoutez des éléments au dictionnaire')
age['david'] = 35
age['veronique'] = 21
age['sylvie'] = 30
age['damien'] = 37
print(age)

print('3.2 Accéder à une valeur à partir d’une clé')
print(age['sylvie'])

print('3.3 Accéder à une valeur à partir d’une clé')
print('jean' in age)

print('3.4 Gérer des valeurs multiples')
#pierre durand, 1986, 1.72, 70 soit [‘pierre durand’]=(1986,1.72,70)
#victor dupont, 1987, 1.89, 57
#paul dupuis, 1989, 1.60, 92
#jean rieux, 1985, 1.88, 77
club ={}
club['pierre durand']=(1986,1.72,70)
club['victor dupont']=(1987,1.89,57)
club['paul dupuis']=(1989, 1.60, 92)
club['jean rieux']=(1985, 1.88, 77)
print(club)

print('3.5 Afficher les données d’un sportif')
#Accédez aux données de ‘paul dupuis’ et initialisez les variables dateNaissSportif, poidsSportif et tailleSportif avec les valeurs du tuple correspondant.
print(club['paul dupuis'])
dateNaissSportif = club['paul dupuis'][0]
tailleSportif = club['paul dupuis'][1]
poidsSportif = club['paul dupuis'][2]

#Créez ensuite une chaine de formatage formatDonnees qui permettra d’utiliser les variables pour afficher la chaine suivante avec un print() 

phrase = 'Le sportif nommé Paul Dupuis est né en {}, sa taille est de {} m et son poids est de {} Kg'

print(phrase.format(dateNaissSportif, tailleSportif,poidsSportif))

print('4. Entrées utilisateur')
print('4.1 Club sportif : variante')

nomSportif = input('Entrez le nom du sportif : ')

dateNaissSportif = club[nomSportif][0]
tailleSportif = club[nomSportif][1]
poidsSportif = club[nomSportif][2]
phrase = 'Le sportif nommé {} est né en {}, sa taille est de {} m et son poids est de {} Kg'

print(phrase.format(nomSportif, dateNaissSportif, tailleSportif,poidsSportif))