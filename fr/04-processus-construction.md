# Processus de construction

## Installation de l'atelier

Tous les panneaux sont fabriques dans un atelier couvert -- independant de la meteo, avec controle qualite et efficacite de chaine de montage. Exigences minimales de l'atelier :

- Surface couverte : ~6 x 4 m (toit, cotes ouverts acceptables)
- Poste de soudure (fabrication des cadres uniquement)
- Perceuse a colonne ou perceuse portative
- 2x tables vibrantes (~1,2 x 2,7 m chacune)
- Approvisionnement en sable pour le lit
- Malaxeur a mortier (electrique ou manuel)
- Outils a main de base : tournevis, pinces coupantes, pinces, agrafeuse

![Sequence d'assemblage](../svg/07-assembly-sequence.svg)

## Etapes de production

### Etape 1 : Fabrication du cadre

1. Couper le profile en T aux longueurs : 2x 1,0 m (haut/bas, ame de 85 mm) + 2x 2,5 m (cotes, ame de 30 mm)
2. Souder les angles dans un gabarit -- tous les cadres sont identiques
3. Percer les trous de serrage tous les 100 mm le long des ames superieures et inferieures (10 trous par barre, 20 au total)
4. Galvaniser a chaud les cadres finis (processus par lot -- envoyer 20-50 cadres a la fois)

**Tous les cadres sont identiques quelle que soit la variante de panneau.** Le gabarit garantit des dimensions constantes. Un gabarit, un cadre, pour toujours.

### Etape 2 : Blocs en PEHD

1. Couper le stock PEHD a 30 x 30 mm x 1 000 mm (2 par panneau)
2. Couper les encoches d'angle : 10 x 10 mm a chaque extremite (4 encoches par bloc, 8 par panneau)
3. Monter les blocs sur les ames des profiles en T haut et bas avec des vis ou de l'adhesif

### Etape 3 : Electricite

1. Passer le cable 12V dans la gaine PVC
2. Passer le cable 120V dans une gaine PVC separee
3. Monter les douilles E10 (3 pres du haut, chaque face)
4. Pour le type O/S : monter le boitier de prise, relier le pigtail au cable principal
5. Pour le type S : monter le boitier d'interrupteur a 120 cm de hauteur
6. Pour le type W : monter les colonnes montantes d'eau (alimentation CPVC/PEX, evacuation PVC) avec des bouchons
7. Fixer les connecteurs rapides aux deux bords verticaux (2 broches pour 12V, 3 broches pour 120V)

### Etape 4 : Lattes de bambou (face 1)

1. Poser le cadre du panneau a plat sur la table de travail, face 1 vers le haut
2. Disposer les lattes verticales de bambou contre l'ame, entre les blocs en PEHD
3. Laisser des espaces de ~20 mm entre les lattes pour la penetration du mortier
4. Placer la gaine PVC avec les cables entre les lattes, contre l'ame
5. Passer la latte diagonale a travers l'encoche inferieure gauche du bloc PEHD, en travers jusqu'a l'encoche superieure droite (au niveau de l'ame)
6. Pre-tendre la diagonale et la fixer aux deux extremites

![Systeme de serrage par vis](../svg/04-screw-clamping.svg)

### Etape 5 : Serrage par vis (face 1)

1. Placer la bande de serrage en acier (2 mm x 30 mm x 1 000 mm) sur les lattes de bambou au niveau du profile en T superieur
2. Aligner les trous de la bande de serrage avec ceux de l'ame du profile en T
3. Visser les vis en acier inoxydable a travers : bande de serrage, lattes de bambou, trous de l'ame
4. La bande de serrage se flexe pour s'adapter aux variations naturelles d'epaisseur -- auto-ajustable
5. Repeter au profile en T inferieur
6. Ligaturer la diagonale a chaque latte verticale aux croisements (~8-10 ligatures)

**Temps : ~5 minutes par face pour le serrage, ~3 minutes pour les ligatures**

### Etape 6 : Retourner et repeter (face 2)

1. Retourner le panneau
2. Repeter les etapes 4-5 de l'autre cote
3. La diagonale de la face 2 va du coin superieur gauche au coin inferieur droit (oppose a la diagonale de la face 1 -- ensemble elles forment un X)

### Etape 7 : Grillage

1. Poser le grillage a poule sur la face 1, depassant de 20 mm les bords du cadre (pour le recouvrement avec les panneaux adjacents)
2. Agrafer ou ligaturer au cadre et aux lattes de bambou
3. Si utilisation d'un grillage anti-insectes en aluminium : le placer sous le grillage a poule
4. Retourner et repeter sur la face 2

### Etape 8 : Coulage du mortier

![Processus de coulage du mortier](../svg/06-mortar-pour.svg)

C'est l'innovation cle en matiere de methode d'application :

1. **Preparer la table vibrante :** Surface de niveau, moteur monte en dessous
2. **Etaler le lit de sable :** ~30 mm de sable propre et sec sur la surface de la table. Le sable s'adapte a toute irregularite de la face du panneau et empeche l'adherence du mortier a la table.
3. **Placer le panneau face vers le bas** sur le lit de sable (le cote grillage a poule touche le sable)
4. **Preparer le mortier :** 1:4 ciment:sable + fibre PP + adjuvant pouzzolanique, E/C ~0,45-0,50 (coulable mais pas liquide)
5. **Couler le mortier** sur le dos expose du panneau, en remplissant entre les lattes et en couvrant le grillage
6. **Demarrer la vibration :** Faire fonctionner la table pendant 30-60 secondes. La vibration :
   - Fait penetrer le mortier a travers les espaces entre les lattes
   - Remplit completement la cavite centrale
   - Elimine les vides et les poches d'air
   - Le mortier penetre jusqu'au grillage de la face avant (reposant sur le sable)
7. **Araser** l'exces de mortier au niveau des bords du cadre
8. **Lisser a la truelle** (cela devient la face interieure)

> **Guide de construction de la table vibrante :** Un plan de table vibrante DIY (moteur, plateforme, ressorts) sera publie dans ce depot une fois la conception testee et jugee sure en pratique. En attendant, toute plateforme plate avec un vibrateur a beton fixe au bord fonctionnera pour les premieres experimentations.

**Pourquoi une table vibrante sur lit de sable ?**
- Gravite + vibration = remplissage complet, zero vide
- Lit de sable = pas de moule necessaire, le sable s'adapte a la forme du panneau
- Pas d'equipement de projection necessaire (moins couteux que le mortier projete)
- Un coulage d'un seul cote remplit les deux faces -- le mortier s'ecoule a travers les espaces entre les lattes
- Qualite constante -- la vibration elimine l'erreur humaine

### Etape 9 : Durcissement

1. Couvrir le panneau avec une bache plastique pour retenir l'humidite
2. Maintenir humide pendant minimum 7 jours (brumisation ou toile de jute humide)
3. Resistance maximale a 28 jours
4. Les panneaux peuvent etre empiles verticalement (sur chant) apres 7 jours pour economiser de l'espace
5. Marquer chaque panneau avec le type de variante et la date de production

**Cadence de production : 3-4 panneaux par jour** avec 2 tables vibrantes fonctionnant en parallele, equipe de 4-6 personnes. Travail actif par panneau : ~15-20 minutes. Durcissement passif : 7-28 jours (les panneaux durcissent pendant que de nouveaux sont produits).

### Etape 10 : Transport et installation

1. Transporter les panneaux sur le chantier en utilisant un simple chariot a cadre en A ou un camion
2. Boulonner les panneaux dans l'ossature metallique du batiment aux emplacements des poteaux (pattes de fixation pre-soudees sur les poteaux)
3. Les panneaux adjacents se touchent mortier contre mortier
4. Connecter l'electricite entre panneaux adjacents par connexion rapide (12V + 120V)
5. Tester les circuits avant les finitions

### Etape 11 : Finitions sur site

1. Combler les joints entre panneaux avec du mortier
2. Appliquer le grillage a poule sur les joints (si le recouvrement depuis les bords des panneaux n'est pas suffisant)
3. Appliquer l'enduit a la chaux : 3-5 mm, a la truelle, les deux faces
4. Laisser durcir (maintenir humide pendant 3-5 jours)
5. Appliquer le badigeon de chaux : 2-3 couches fines au pinceau

Le mur fini est sans couture -- pas de joints visibles, pas d'acier visible, pas de vis visibles. Juste un enduit a la chaux lisse avec la texture d'un mur fait main.

## Liste de controle qualite

- [ ] Dimensions du cadre dans une tolerance de +/-2 mm
- [ ] Tous les trous de serrage perces et alignes
- [ ] Lattes de bambou traitees au borate (teinte verte/bleue visible)
- [ ] Diagonale pre-tendue (doit sonner lorsqu'on la tapote)
- [ ] Toutes les ligatures serrees
- [ ] Circuits electriques testes avant le mortier (12V et 120V)
- [ ] Consistance du mortier correcte (essai d'affaissement)
- [ ] Vibration effectuee pendant 30-60 secondes completes
- [ ] Aucun vide visible sur la face de coulage apres vibration
- [ ] Panneau marque avec le type et la date
- [ ] Durcissement minimum de 7 jours avant manipulation
