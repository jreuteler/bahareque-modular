# Performance structurelle

## Architecture du systeme

Ce systeme de panneaux a ete concu pour fonctionner **avec une ossature en acier poteaux-poutres** -- la configuration que nous recommandons pour les batiments a plusieurs etages en zones sismiques. Dans cette configuration, l'ossature en acier supporte les charges gravitaires et sismiques tandis que les panneaux assurent le contreventement lateral, l'enveloppe climatique, la masse thermique et les equipements integres.

Cependant, les panneaux sont **structurellement capables de fonctionner sans ossature en acier**. Avec une capacite de compression depassant largement les charges residentielles typiques (deux montants lateraux en corniere L L 40x40x4), une rangee de panneaux peut aisement porter un deuxieme etage et une toiture sans structure en acier independante. Une simple lisse haute en bois ou en bambou relie les panneaux en tete et repartit la charge de toiture.

**Deux configurations :**

| Configuration | Cas d'usage | Role du panneau |
|---------------|-------------|-----------------|
| **Avec ossature en acier** (recommande) | Plusieurs etages, zones hautement sismiques, commercial/institutionnel | Remplissage -- les panneaux sont boulonnes dans l'ossature, l'acier supporte les charges principales |
| **Sans ossature en acier** (plus simple, moins couteux) | Un etage + mezzanine, zones sismiques moderees, residentiel | Porteur -- les panneaux supportent directement la toiture et l'etage superieur |

Les estimations de capacite portante ci-dessous s'appliquent aux deux configurations. L'ossature en acier ajoute de la redondance et de la resistance en flexion, mais n'est pas necessaire pour que les panneaux fonctionnent structurellement.

## Performance sismique

### Contreventement diagonal

Chaque panneau contient deux lattes diagonales en bambou (une par face, coins opposes), formant un X vu de face. Sous charge sismique :

1. **Conversion cisaillement vers traction :** Lorsque l'ossature du batiment se deforme lateralement, une diagonale passe en traction tandis que l'opposee passe en compression. La diagonale en bambou en traction resiste efficacement a l'effort de contreventement -- le bambou possede une excellente resistance en traction (150-200 MPa pour la Guadua angustifolia).
2. **Pre-tension :** Les diagonales sont installees avec une legere pre-tension, eliminant le jeu et assurant une mise en charge immediate.
3. **Grille de ligatures :** Les ligatures en fil galvanise a chaque croisement diagonale-verticale (~16-20 ligatures au total) repartissent l'effort diagonal sur toute la surface du panneau, empechant la rupture localisee.

**Amelioration estimee : 3 a 5 fois la resistance au contreventement** par rapport aux panneaux sans contreventement diagonal.

### Le profil )(

Les blocs en PEHD maintiennent les lattes de bambou a 30 mm de l'ame en haut et en bas. A mi-hauteur, les lattes flechissent vers l'interieur en direction de l'ame. Le mortier remplit cet espace variable, creant une section transversale en arc naturel :

- **Resistance hors plan :** L'arc de mortier agit comme une voute surbaissee, repartissant efficacement les charges de vent ou d'impact vers les bords rigides du cadre.
- **Verrouillage mecanique :** Le mortier d'epaisseur variable bloque les lattes de bambou en place -- elles ne peuvent etre retirees sans casser le mortier.

### Mode de rupture ductile

La combinaison de lattes de bambou, de ligatures en fil metallique et de mortier cree un composite qui rompt progressivement :

1. D'abord : le mortier se fissure (avertissement visible)
2. Puis : les ligatures s'etirent (absorption d'energie)
3. Puis : les lattes de bambou se deforment (haute ductilite)
4. L'ossature en acier reste intacte tout au long -- le batiment ne s'effondre pas

Cela differe fondamentalement de la maconnerie non armee, qui rompt de maniere fragile (effondrement soudain sans avertissement).

## Resistance au feu

- **Enrobage de mortier :** Les lattes de bambou sont entierement enrobees de mortier (~85 mm d'epaisseur de mur). Le mortier est incombustible et agit comme isolant thermique pour le bambou.
- **Carbonisation du bambou :** Meme si le feu penetre le mortier, le bambou se carbonise lentement et de maniere previsible (similaire a la construction en bois). L'ossature en acier derriere maintient l'integrite structurelle.
- **Enduit a la chaux :** Incombustible. Fournit une protection supplementaire contre le feu.
- **Pas de bambou expose :** Une fois installe et fini, aucun bambou n'est visible ni accessible a la flamme.

## Performance thermique

- **Masse thermique :** ~85 mm de mortier fournissent une masse thermique significative -- absorbe la chaleur le jour, la restitue la nuit. Reduit les variations de temperature dans les climats tropicaux.
- **Respirabilite :** L'enduit a la chaux est permeable a la vapeur d'eau. L'humidite traverse le mur plutot que d'etre piegee, empechant la condensation et les moisissures.
- **Pas de lame d'air isolante :** Le systeme n'inclut pas de couche d'isolation thermique. Dans les climats tropicaux (la cible principale), la masse thermique a plus de valeur que l'isolation. Pour les climats temperes, une couche d'isolation externe peut etre ajoutee par-dessus l'enduit a la chaux.

## Performance acoustique

Le noyau dense en mortier offre une bonne attenuation sonore :

- **STC estime (Sound Transmission Class) :** 40-45 pour un mur a panneau simple
- **Avec enduit a la chaux sur les deux faces :** STC 42-48
- **Comparaison :** Mur en bloc de beton standard : STC 40-45. Le systeme de panneaux est comparable.

## Capacite portante

> **Avertissement :** Les valeurs ci-dessous sont des estimations analytiques prudentes basees sur les proprietes des materiaux et la geometrie. Elles ne sont PAS basees sur des essais en laboratoire. Ne pas utiliser ces valeurs pour l'ingenierie structurelle sans verification independante. La performance reelle depend de la qualite des materiaux, de la mise en oeuvre et des details d'assemblage. Voir [Essais necessaires](#essais-necessaires) ci-dessous.

### Poids propre du panneau

| Composant | Poids |
|-----------|-------|
| Cadre en corniere L en acier (L 40x40x4, 7 m a 2,42 kg/m + bandes de serrage + goussets) | ~22 kg |
| Mortier de noyau (de base : ciment-sable, ~0,147 m3, densite durcie ~2 000 kg/m3) | ~294 kg |
| Lattes de bambou + diagonales (~30 % densite de cavite) | ~38 kg |
| Blocs PEHD, fil, grillage, gaine, cables | ~6 kg |
| Enduit a la chaux (10 mm les deux faces) | ~100 kg |
| **Poids total du panneau, melange de base** | **~460 kg** |
| **Poids par m2 de mur, base** | **~184 kg/m2** |
| Poids total du panneau, melange bahareque optimise (chaux pouzzolanique + pasto estrella + enduit 5 mm) | ~380 kg |
| Poids par m2 de mur, optimise | ~152 kg/m2 |
| Poids d'expedition de l'assemblage a sec (cadre + bambou + grillage + equipements, avant coulage) | ~75 kg |

Pour comparaison : un mur en bloc de beton de 150 mm pese environ 180 kg/m2. Le systeme de panneaux (melange de base) pese a peu pres autant que la maconnerie conventionnelle par unite de surface ; le melange bahareque optimise est ~15 % plus leger. Critique pour la logistique : le **poids d'expedition de l'assemblage a sec (~75 kg)** est la forme sous laquelle le panneau est transporte de l'atelier au chantier (le mortier est coule sur place).

### Charge axiale (verticale)

Chaque panneau possede deux montants lateraux verticaux en corniere L capables de supporter des charges de compression significatives :

| Element | Section | Capacite axiale prudente |
|---------|---------|--------------------------|
| Montant lateral en corniere L (L 40x40x4 mm) | A = 304 mm2 | ~36 kN par montant (a sigma = 120 MPa, ~50 % de la limite elastique A36) |
| Deux montants lateraux par panneau | 2 x 304 mm2 | ~72 kN par panneau (~7 200 kg) |

**Ce que cela signifie en pratique :**

Une maison typique a un etage avec mezzanine et toiture en tuiles terre cuite impose environ 200-400 kg de charge par metre lineaire de mur (toiture + plafond + plancher de mezzanine + charge d'exploitation). Un seul panneau de 1 m peut supporter **18 a 36 fois cette exigence**. **Les panneaux n'ont pas besoin d'une ossature en acier separee pour porter un deuxieme etage et une toiture.**

Utilises **avec une ossature en acier**, cette capacite axiale est une pure marge de reserve -- l'acier supporte les charges gravitaires. Utilises **sans ossature en acier**, les panneaux sont la structure porteuse. Dans ce cas, une lisse haute en bois ou en bambou en tete du mur repartit la charge de toiture uniformement sur tous les panneaux et les relie entre eux.

Le flambage n'est pas une preoccupation a ces niveaux de charge **lorsque la corniere L est noyee dans le composite du panneau** : l'epaisseur de mur en mortier de 85 mm fournit au cadre angulaire une rigidite laterale continue, et le rapport hauteur/epaisseur du panneau (~2 500/85 = 29) est bien en deca des limites d'elancement acceptees pour les murs armes.

**Important : limitation des profiles ouverts sur l'axe faible.** Les profiles structurels ouverts -- cornieres L, profiles T, profiles C -- ont une rigidite minimale autour de leur axe faible. Un montant L 40x40x4 autoportant sans contreventement par le panneau (I_min = 3,8 x 10⁴ mm⁴ autour de l'axe faible passant par le talon) flamberait sous une charge modeste. La capacite de 36 kN par corniere L indiquee ci-dessus est la **capacite de limite elastique axiale** et n'est atteignable QUE lorsque la corniere est continument contreventee par le remplissage du panneau (mortier + guadua). Cette distinction est cruciale pour le sequencage de la construction -- le cadre en corniere L ne doit pas etre charge axialement avant que les panneaux soient coules, durcis et travaillent en composite. Pour les colonnes autoportantes dans les batiments a plusieurs etages, les profiles ouverts ne conviennent pas -- utiliser un tube carre (SHS) a la place.

### Charge laterale (dans le plan / contreventement)

C'est la contribution structurelle principale du panneau -- resister aux forces horizontales du vent et des seismes.

**Sans contreventement diagonal (mortier + lattes verticales uniquement) :**

Estimation prudente basee sur la resistance au cisaillement du mortier (tau = 0,3 MPa pour un mortier 1:4 ciment:sable) sur la section du panneau :

- Surface de cisaillement : ~85 mm x 1 000 mm = 85 000 mm2
- Capacite de cisaillement prudente : 85 000 x 0,3 = ~25 kN par panneau
- Avec coefficient de securite 3 : **~8 kN en charge de service par panneau**

**Avec contreventement diagonal (la configuration concue) :**

La latte diagonale en bambou (60 x 20 mm, Guadua angustifolia) en traction :

- Section : 1 200 mm2
- Resistance en traction prudente : 80 MPa (utilisant ~50% des 150-200 MPa publies)
- Capacite de traction diagonale : 1 200 x 80 = ~96 kN
- Composante horizontale (cos 69 deg) : ~96 x 0,36 = ~34 kN par diagonale
- Deux diagonales (une par face, une en traction) : ~34 kN
- Les ligatures et le verrouillage du mortier ajoutent une resistance supplementaire
- Avec coefficient de securite 3 : **~12-15 kN en charge de service de contreventement par panneau**

**En contexte :** Une section de mur de 3 m de large (3 panneaux) fournit ~36-45 kN de resistance au contreventement. Un batiment residentiel a un etage en zone sismique moderee (PGA 0,2g) avec 30 kN de masse sismique au-dessus du mur necessite environ 6 kN de resistance a l'effort tranchant a la base par metre lineaire de mur. Trois panneaux par metre fournissent 4 a 5 fois cette exigence.

Ce sont des chiffres tres prudents. La matrice de mortier, la grille de ligatures et le profil )( contribuent tous a une resistance supplementaire non comptabilisee ci-dessus.

### Charge hors plan (vent / impact)

Le panneau resiste a la pression perpendiculaire a la face du mur (succion/pression du vent, impact) :

- L'arc de mortier cree par le profil )( agit comme une voute surbaissee entre les profiles en T superieur et inferieur rigides
- Estimation prudente pour une pression de vent uniforme, en traitant le panneau comme une dalle simplement appuyee :

| Parametre | Valeur |
|-----------|--------|
| Portee du panneau (entre profiles en T haut/bas) | 2,5 m |
| Largeur du panneau | 1,0 m |
| Epaisseur du mortier (minimum, au centre) | ~55 mm |
| Resistance en flexion du mortier (prudente) | 1,0 MPa |
| Capacite estimee en pression uniforme | ~0,7 kPa |
| Avec coefficient de securite 2 | **~0,35 kPa en charge de service** |

**En contexte :** 0,35 kPa correspond a une vitesse de vent de ~25 m/s (90 km/h). Pour les zones de vent plus fort, l'ossature en acier (pas le panneau) supporte la charge de vent via les assemblages poutre-poteau. Le panneau doit seulement resister a la pression locale entre ses propres elements de cadre.

La grille de lattes de bambou et les ligatures fournissent une resistance hors plan supplementaire significative non captee dans le modele de dalle simple -- le panneau est un composite, pas une simple dalle de mortier.

### Charges ponctuelles (fixations, etageres, placards)

| Type de fixation | Methode d'ancrage | Capacite prudente |
|-----------------|-------------------|-------------------|
| Elements legers (cadres, horloges, pateres) | Clou de maconnerie ou vis dans le mortier | 5-10 kg par ancrage |
| Elements moyens (etageres, miroirs, petits placards) | Cheville a expansion plastique dans le mortier (6-8 mm) | 15-25 kg par ancrage |
| Elements lourds (placards de cuisine, chauffe-eau, support TV) | Boulon traversant vers l'ame de la corniere L | 50-100 kg par ancrage |
| Elements tres lourds (bibliotheque, garde-manger plein) | Boulons traversants multiples vers la corniere L + plaque de repartition | 200+ kg par point de fixation |

**Conseil :** L'ame de la corniere L se trouve a une position connue (centre de l'epaisseur du mur). Un detecteur de montant ou un aimant la localise facilement. Le boulonnage traversant vers l'ame fournit un ancrage fiable et de haute capacite comparable a une ossature a montants metalliques.

### Resume -- Capacite prudente en kg par panneau

Pour les constructeurs et non-ingenieurs, voici les memes chiffres exprimes en kilogrammes. Ce sont des **charges de service tres prudentes** (deja divisees par des coefficients de securite de 2-3). Les charges de rupture reelles sont 2-3 fois plus elevees.

| Type de charge | Direction | Capacite de service prudente | Ce que cela signifie en pratique |
|----------------|-----------|------------------------------|----------------------------------|
| **Contreventement (sismique/vent)** | Horizontale, dans le plan du mur | **~1 200-1 500 kg par panneau** | Une force horizontale de 1,2-1,5 tonnes appliquee en tete d'un seul panneau avant qu'il atteigne sa limite de service. Une maison typique a un etage necessite ~600 kg de resistance au contreventement par metre de mur -- un panneau en fournit le double. |
| **Hors plan (pression du vent)** | Perpendiculaire a la face du mur | **~90 kg repartis sur la surface du panneau** | Equivalent a ~36 kg/m2 de pression uniforme. Une personne s'appuyant fortement contre le mur (~80 kg sur ~0,3 m2) est bien en deca de la capacite. |
| **Axiale (verticale)** | Vers le bas, a travers le panneau | **Depasse largement les charges residentielles (~7 200 kg de limite elastique axiale par panneau en composite)** | Les deux montants en corniere L supportent bien plus que la charge typique d'une toiture + etage superieur par metre de mur. Les panneaux peuvent porter un deuxieme etage et une toiture sans ossature en acier separee. |
| **Charge ponctuelle dans le mortier** | Arrachement / cisaillement a l'ancrage | **~15-25 kg par ancrage** | Une equerre d'etagere avec 2 ancrages supporte 30-50 kg en toute securite. |
| **Charge ponctuelle sur la corniere L** | Boulon traversant | **~50-100 kg par boulon** | Un placard de cuisine avec 4 boulons traversants supporte 200-400 kg en toute securite. |

> **Important :** Ce sont des estimations, pas des valeurs testees. Elles seront validees par des essais physiques. Ne pas utiliser pour l'ingenierie structurelle sans verification independante. En cas de doute, fixer les elements lourds a l'ossature metallique du batiment, pas au panneau.

## Durabilite (duree de vie de conception de 80-100 ans)

| Composant | Mecanisme de degradation | Prevention | Duree de vie attendue |
|-----------|--------------------------|------------|----------------------|
| Ossature en acier | Corrosion | Galvanisation a chaud (85 um+) | 80-100 ans (non cotier) |
| Lattes de bambou | Attaque d'insectes, degradation fongique | Traitement au borate + enrobage de mortier (alcalin, anaerobie) | 80+ ans |
| Mortier | Carbonatation, erosion | Protege par l'enduit a la chaux (couche sacrificielle) | 100+ ans |
| Enduit a la chaux | Erosion de surface, microfissuration | Auto-cicatrisant (la carbonatation comble les fissures), badigeon de chaux renouvelable | Indefinie avec entretien |
| Badigeon de chaux | Degradation UV, erosion par la pluie | Renouveler tous les 5-10 ans | 5-10 ans par couche |
| Electricite | Degradation de l'isolant | La gaine PVC permet le remplacement des cables sans ouvrir le mur | Cables : 30-50 ans, remplacables |
| Blocs en PEHD | Aucune significative | Proteges des UV (a l'interieur du mur) | 100+ ans |

### Calendrier de maintenance

| Intervalle | Action | Cout estime |
|------------|--------|-------------|
| Tous les 5-10 ans | Renouvellement du badigeon de chaux | 50-100 $ par batiment |
| Tous les 15-20 ans | Inspection de l'enduit a la chaux, colmatage des fissures | 100-300 $ par batiment |
| Tous les 30-40 ans | Inspection electrique, remplacement des cables si necessaire | 200-500 $ par batiment |
| A 40 ans | Inspection de l'ossature en acier aux points accessibles (re-galvanisation ponctuelle si necessaire) | 200-400 $ |
| **Total sur la duree de vie** | | **1 400-2 000 $** |

## Essais necessaires

**Toutes les valeurs de capacite portante ci-dessus sont des estimations analytiques.** Elles seront validees par des essais physiques dans le cadre du developpement de ce projet. Les premiers panneaux seront construits et testes avant qu'un batiment ne soit occupe.

Programme d'essais prevu :

- [ ] **Essais de cisaillement par contreventement** (ASTM E564 ou equivalent) -- panneaux avec et sans diagonales, pour valider l'estimation d'amelioration de 3-5x
- [ ] **Essais de charge hors plan** -- pression uniforme et impact ponctuel, pour valider le benefice du profil )(
- [ ] **Essais de resistance au feu** (ASTM E119 ou equivalent) -- temps jusqu'a la rupture structurelle
- [ ] **Essais sismiques cycliques** -- table vibrante en grandeur reelle ou chargement cyclique quasi-statique, pour verifier le mode de rupture ductile
- [ ] **Essais d'assemblage** -- capacite des pattes de boulonnage panneau-poteau, durabilite des connecteurs rapides
- [ ] **Essais de vieillissement accelere** -- vieillissement accelere d'echantillons de bambou enrobe de mortier
- [ ] **Essais de transmission acoustique** (ASTM E90) -- mesure du STC
- [ ] **Essais d'arrachement de charges ponctuelles** -- capacite des chevilles de maconnerie et des boulons traversants dans le mortier + corniere L

Les resultats des essais seront publies dans ce depot au fur et a mesure de leur disponibilite. Si vous avez acces a des installations d'essai et souhaitez contribuer, contactez-nous -- des essais collaboratifs sur differentes especes de bambou et differents dosages de mortier rendront ce systeme plus robuste pour tous.
