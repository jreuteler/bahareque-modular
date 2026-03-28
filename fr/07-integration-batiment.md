# Integration au batiment

![Integration au batiment](../svg/08-building-integration.svg)

## Deux configurations

Le systeme de panneaux a ete concu pour fonctionner **avec une ossature en acier** mais est structurellement capable de tenir seul. Chaque panneau peut supporter ~4 000 kg verticalement -- plus que suffisant pour un deuxieme etage et une toiture sans poteaux en acier.

| Configuration | Recommandee pour | Role structurel des panneaux |
|---------------|------------------|------------------------------|
| **Avec ossature en acier** | Plusieurs etages, zones hautement sismiques, commercial | Remplissage -- l'acier supporte les charges principales, les panneaux ajoutent le contreventement |
| **Sans ossature en acier** | Un etage + mezzanine, sismicite moderee, residentiel | Porteur -- les panneaux supportent directement la toiture et l'etage superieur, relies par une lisse haute |

Les sections ci-dessous decrivent la configuration avec ossature en acier en detail. Pour la configuration sans ossature, remplacer les poteaux en acier par une lisse haute en bois/bambou en tete du mur, et boulonner les panneaux a un seuil en beton a la base et entre eux sur les bords.

## Configuration avec ossature en acier

### Exigences de l'ossature

| Element | Specification |
|---------|--------------|
| Poteaux | HEA 150 ou equivalent (dimensionnes par calcul d'ingenierie) |
| Poutres | IPE 160-200 (portant entre poteaux) |
| Assemblages | Boulonnes sur site ; platines pre-soudees en atelier |
| Entraxe des poteaux | 2-4 m (par increments de 1 m = nombre exact de panneaux par travee) |
| Fondation | Beton arme selon la norme parasismique locale |

### Relation poteau-panneau

Le detail de conception cle : **les poteaux sont en retrait de l'epaisseur du panneau** par rapport aux poutres.

- La face exterieure de l'aile de la poutre = le plan du mur
- Les panneaux sont a fleur avec la face de la poutre
- Le poteau est en arriere des panneaux, entierement cache
- De l'exterieur : mur en enduit continu sans acier visible

Cela est realise en soudant des **pattes de boulonnage** sur les ailes des poteaux a la hauteur des panneaux. Les panneaux sont boulonnes a ces pattes depuis le cote interieur.

## Sequence d'installation des panneaux

1. **Ossature en acier erigee** -- poteaux, poutres, structure de toiture acheves
2. **Commencer par un angle** -- boulonner le premier panneau a la patte du poteau
3. **Panneau adjacent** -- boulonner a la patte suivante, pousser le bord contre le premier panneau (mortier contre mortier)
4. **Connexion electrique rapide** -- les connecteurs 12V et 120V s'enclenchent au joint des panneaux
5. **Continuer autour du batiment** -- les panneaux remplissent chaque travee entre les poteaux
6. **Ouvertures de fenetres/portes** -- sauter des panneaux, encadrer l'ouverture avec des linteaux en acier
7. **Tester tous les circuits** -- avant les finitions
8. **Enduit a la chaux** -- couvrir toutes les faces et joints des panneaux de maniere continue
9. **Badigeon de chaux** -- finition finale

## Detail panneau-poteau (vue de dessus)

```
EXTERIEUR                              INTERIEUR

|<- Enduit a la chaux (3-5mm)
|<- Mortier (15mm)
|<- Grillage a poule
|<- Lattes de bambou
|<- Ame du profile en T  +----------+
|<- Remplissage mortier   |  POTEAU  |  <- HEA 150
|<- Lattes de bambou      |  (cache) |    (en retrait)
|<- Grillage a poule      |          |
|<- Mortier (15mm)         +----------+
|<- Enduit a la chaux

Face exterieure du panneau = Face exterieure de la poutre = Plan du mur
```

## Joint panneau-panneau

Les panneaux adjacents se touchent **face de mortier contre face de mortier**. Le joint est :

1. Rempli de mortier (si un espace existe)
2. Couvert d'une bande de grillage a poule (pontant le joint)
3. Enduit a la chaux par-dessus -- completement invisible dans le mur fini

Les connecteurs electriques rapides sont sur la ligne de joint. Lorsque les panneaux sont pousses l'un contre l'autre, les connecteurs 2 broches (12V) et 3 broches (120V) s'engagent automatiquement.

## Ouvertures de fenetres et de portes

- Sauter les panneaux la ou des ouvertures sont necessaires
- Encadrer l'ouverture avec des linteaux en acier (soudes aux poteaux/poutres du batiment)
- Les bords des panneaux aux ouvertures restent exposes (bord de l'ossature en acier visible) -- couverts d'un habillage en teck, bois ou acier
- Pratique standard : ouvertures a des largeurs entieres de panneaux (1 m, 2 m, 3 m) pour des bords nets

## Cloisons interieures

Memes panneaux, installes entre poteaux interieurs ou equerres sol-plafond :

- Les deux faces visibles et finies a l'enduit a la chaux
- Separation acoustique et coupe-feu complete
- Circuits electriques independants des circuits de mur exterieur
- Peuvent etre retires et reconfigures (les panneaux se deboulonnent de l'ossature)

## Raccordement a la toiture

- Les panneaux s'arretent au niveau de la poutre (haut du mur)
- La charpente (pannes, chevrons) repose sur la poutre
- L'espace entre le haut du panneau et le dessous de la toiture est scelle avec du mortier ou un habillage
- Le debord de toiture protege le mur de la pluie -- minimum 1,5 m recommande en climat tropical

## Raccordement au sol

- Les panneaux reposent sur le dallage du rez-de-chaussee ou sur la poutre
- La base du panneau est a 30-50 mm au-dessus du niveau du sol fini (protection contre l'humidite)
- Une platine de base galvanisee ou un seuil en bois dur comble l'espace
- Scelle avec du mortier et de l'enduit a la chaux

## Integration du systeme electrique

Lorsque les panneaux sont installes sequentiellement, les connecteurs rapides creent des circuits continus :

- **Eclairage 12V :** Parcourt tous les panneaux. Connecte a un transformateur/alimentation 12V central. L'eclairage individuel des panneaux peut etre commande par des interrupteurs dans les panneaux de type S.
- **Secteur 120V :** Parcourt tous les panneaux. Connecte au tableau electrique principal du batiment. Disjoncteurs dimensionnes selon la norme electrique locale.
- **Eau (panneaux de type W) :** Les colonnes montantes se raccordent aux collecteurs de plomberie du batiment au niveau du sol. Les bouchons sont retires et raccordes aux appareils apres installation.

## Adaptabilite

Le systeme de panneaux s'adapte a differentes configurations de batiment :

| Configuration | Notes |
|---------------|-------|
| Un etage | Installation standard |
| Deux etages | Panneaux de l'etage superieur identiques, boulonnes a l'ossature de la poutre superieure |
| Plans en L ou en U | Panneaux d'angle : jonction a 90 deg avec poteau d'angle en acier |
| Murs courbes | Non supporte (les panneaux sont plats). Utiliser une approximation a facettes avec des poteaux inclines. |
| Construction mixte | Les panneaux peuvent remplir une partie du batiment, avec d'autres materiaux (verre, pierre, bois) ailleurs |
