# BLACK_JACK-GAME
jeux de black_jack sur python


Python : Brief projet

Les jeux de cartes sont divers et variés mai tous utilisent les mêmes fonctionnalités de base
comme constituer des paquets, des mains, mélanger les cartes, les disposer d’une certaine
manière sur le tapis de jeu.
L’objectif de ce projet est d’utiliser les notions acquises en Python pour implémenter le plus
populaire des jeux de cartes : le Blackjack !
On considère la version simplifiée du Blackjack détaillée ci-dessous.
La partie oppose tous les joueurs contre le croupier (pour simplifier, il n'y aura ici qu'un seul
joueur). Le but est de faire plus de points que le croupier sans dépasser 21. Dès qu'un joueur
fait plus que 21, on dit qu'il « saute » et il perd sa mise initiale. La valeur des cartes est établie
comme suit :
- de 2 à 10 → valeur nominale de la carte
- une figure → 10 points
- un as → 1 ou 11 (au choix)
Un blackjack est composé d'un as et d'une « bûche » (carte ayant pour valeur 10, donc 10,
valet, dame ou roi). Cependant, si le joueur atteint le point 21 en 3 cartes ou plus on compte
le point 21 et non pas blackjack.
Au début de la partie le croupier distribue une carte face visible à chaque joueur et tire une
carte face visible également pour lui. Il tire ensuite pour chacun des joueurs une seconde carte
face visible et tire une seconde carte face cachée pour lui au blackjack américain. Au blackjack
européen, le croupier tire sa seconde carte après le tour de jeu des joueurs.
Puis il demande au premier joueur de la table (joueur situé à sa gauche) l'option qu'il désire
choisir.
Si le joueur veut une carte, il doit l'annoncer en disant « Carte ! ». Le joueur peut demander
autant de cartes qu'il le souhaite pour approcher 21 sans dépasser. Si après le tirage d'une
carte, il a dépassé 21, il perd sa mise et le croupier passe au joueur suivant.

Ecole Data/IA de Microsoft by Simplon
S'il décide de s'arrêter, en disant « Je reste », le croupier passe également au joueur suivant.
Le croupier répète cette opération jusqu'à ce que tous les joueurs soient servis.
Ensuite, il joue pour lui selon une règle simple et codifiée « la banque tire à 16, reste à 17 ».
Ainsi, le croupier tire des cartes jusqu'à atteindre un nombre compris entre 17 et 21 que l'on
appelle un point.
S'il fait plus de 21, tous les joueurs restants gagnent mais s'il fait son point, seuls gagnent ceux
ayant un point supérieur au sien (sans avoir sauté). Dans cette situation, le joueur remporte
l'équivalent de sa mise.
En cas d'égalité le joueur garde sa mise mais n'empoche rien en plus.
À noter que le blackjack (une bûche et un as en deux cartes) est plus fort que 21 fait en ayant
tiré plus de deux cartes.
Travail demandé :
1. Ecrire une fonction qui crée un jeu de cartes de 52.
2. Ecrire une fonction qui crée une main.
3. Ecrire une fonction qui calcule les points d’une main.
4. Ecrire une fonction qui permet de tirer une carte d’une main.
5. Ecrire une fonction qui affiche la main du croupier et du joueur avec les points
respectifs.
6. Ecrire une fonction qui affiche un message au joueur selon l’état du jeu.
Exemple : « Blackjack ! Félicitations ! »
7. Ecrire une fonction qui réinitialise le jeu.
8. Ecrire une fonction qui simule le jeu.
N.B : les fonctions proposées sont à titre indicatif. Une attention particulière sera apportée à
la qualité du code et à sa lisibilité. Il est fortement recommander de suivre les
