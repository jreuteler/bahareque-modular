# Prevention de la corrosion

## Philosophie de conception

Le systeme de panneaux utilise plusieurs materiaux en contact intime. Chaque interface entre materiaux represente un risque potentiel de corrosion. Ce chapitre documente l'analyse galvanique de chaque interface et la strategie de prevention.

**Objectif de conception : 80-100 ans sans defaillance structurelle par corrosion.**

## Serie galvanique (metaux concernes)

De l'anodique (se corrode en premier) au cathodique (protege) :

1. Zinc (revetement de galvanisation)
2. Aluminium (grillage anti-insectes)
3. Acier doux (ossature, bandes de serrage)
4. Acier inoxydable (vis)

Lorsque deux metaux sont en contact electrique en presence d'un electrolyte (humidite), le metal le plus anodique se corrode preferentiellement. C'est le principe de la corrosion galvanique.

## Analyse des interfaces

### 1. Ossature en acier ↔ Mortier

- **Contact :** Direct -- le mortier est coule sur et autour de l'ossature en acier galvanise
- **Niveau de risque :** FAIBLE
- **Analyse :** L'environnement alcalin du mortier de ciment (pH 12-13) passive le revetement de zinc, formant une couche stable d'oxyde de zinc. C'est en fait une combinaison *benefique* -- le mortier protege le zinc, et le zinc protege l'acier. Meme principe que les armatures dans le beton arme.
- **L'adjuvant pouzzolanique** reduit progressivement le pH du mortier a 10-11 au fil des decennies. Cela reste bien dans la plage de passivation du zinc.
- **Prevention :** Galvanisation a chaud selon ISO 1461 (minimum 85 μm). Aucune mesure supplementaire necessaire.

### 2. Vis en acier inoxydable ↔ Cadre galvanise

- **Contact :** Direct -- les vis traversent l'ame galvanisee
- **Niveau de risque :** FAIBLE-MOYEN
- **Analyse :** L'acier inoxydable est cathodique par rapport au zinc. En theorie, cela accelere la corrosion du zinc au point de contact. En pratique, l'enrobage de mortier elimine l'humidite continue (l'electrolyte), et le revetement de zinc au niveau du trou de vis est une zone sacrificielle -- le zinc environnant le protege cathodiquement.
- **Prevention :** Utiliser des vis en acier inoxydable A2 (304). La tete de vis est recouverte par la bande de serrage et le mortier. Aucun chemin d'humidite.

### 3. Grillage a poule ↔ Ossature en acier

- **Contact :** Indirect -- le grillage a poule est agrafe sur la face de mortier, separe de l'ossature par 30+ mm de mortier
- **Niveau de risque :** NUL
- **Analyse :** Les deux sont en acier galvanise. Aucune difference de potentiel galvanique. Separes par une couche de mortier. Aucun probleme.

### 4. Grillage aluminium ↔ Ossature en acier

- **Contact :** Indirect -- le grillage aluminium se situe entre le grillage a poule et le mortier, separe de l'ossature par 30+ mm
- **Niveau de risque :** NUL
- **Analyse :** L'aluminium est anodique par rapport a l'acier (il se corroderait en premier en contact direct). Mais il n'y a aucun contact metal-metal direct -- la couche de mortier assure une isolation electrique complete.
- **Prevention :** S'assurer que le grillage aluminium ne touche pas directement l'ossature en acier lors de l'installation. La couche de mortier gere cela naturellement.

### 5. Grillage aluminium ↔ Grillage a poule (acier galvanise)

- **Contact :** Direct -- les couches de grillage se touchent lors de l'installation
- **Niveau de risque :** FAIBLE
- **Analyse :** Un certain potentiel galvanique existe. Mais les deux sont enrobes dans le mortier apres installation, eliminant le chemin d'humidite. Le grillage aluminium est une couche sacrificielle mince -- meme si une certaine corrosion se produit aux points de contact, le grillage a poule structurel reste intact.
- **Prevention :** Aucune action necessaire. L'enrobage de mortier est suffisant.

### 6. Bande de serrage ↔ Ame du cadre

- **Contact :** Direct -- la bande de serrage est boulonnee contre l'ame a travers les lattes de bambou
- **Niveau de risque :** NUL
- **Analyse :** Les deux sont en acier doux galvanise a chaud. Meme materiau, meme revetement. Aucun potentiel galvanique.

### 7. Ossature en acier ↔ Lattes de bambou

- **Contact :** Direct -- les lattes de bambou reposent contre l'ame galvanisee
- **Niveau de risque :** FAIBLE
- **Analyse :** Le bambou n'est pas un metal -- aucune corrosion galvanique possible. Le risque concerne l'humidite qui migre par capillarite a travers le bambou, creant une zone humide persistante sur l'acier. L'enrobage de mortier elimine ce risque en scellant l'interface. Le traitement au borate reduit egalement l'absorption d'humidite.

## Facteurs environnementaux

### Environnements cotiers (< 1 km de la mer)

L'air charge de sel accelere considerablement la consommation du zinc. En environnement cotier :
- Augmenter l'epaisseur de galvanisation a 120+ μm
- Utiliser des vis en acier inoxydable 316L (au lieu de 304)
- Envisager un revetement epoxy supplementaire sur l'ossature avant galvanisation
- Duree de vie prevue de l'ossature en zone cotiere : 40-60 ans (contre 80-100 a l'interieur des terres)

### Precipitations elevees (> 2 000 mm/an)

- Assurer un debord de toiture adequat (minimum 1,5 m) pour proteger les surfaces murales de la pluie
- L'enduit a la chaux agit comme couche sacrificielle -- a renouveler tous les 10-15 ans en zones de fortes precipitations
- L'interieur du mur (enrobe de mortier) n'est pas affecte par les precipitations

### Humidite tropicale

- La respirabilite de l'enduit a la chaux est essentielle -- il permet a l'humidite de traverser plutot que de la pieger
- NE PAS sceller le mur avec de la peinture ou un revetement hydrofuge -- cela piege l'humidite et accelere la degradation
- Le mur doit respirer : badigeon de chaux uniquement

## Resume

| Interface | Risque | Prevention | Entretien |
|-----------|--------|-----------|-----------|
| Ossature en acier dans le mortier | Faible | Galvanisation a chaud | Aucun (inspecter a 40 ans) |
| Vis inox dans cadre galv. | Faible-Moyen | Inox A2, enrobage mortier | Aucun |
| Grillage a poule vers ossature | Nul | Meme materiau, separation par mortier | Aucun |
| Grillage alu vers ossature | Nul | Isolation par mortier | Aucun |
| Grillage alu vers grillage a poule | Faible | Enrobage mortier | Aucun |
| Bande de serrage vers cadre | Nul | Meme materiau | Aucun |
| Acier vers bambou | Faible | Traitement au borate, enrobage mortier | Aucun |

**La protection anticorrosion du systeme repose sur trois couches : la galvanisation (primaire), l'enrobage de mortier (secondaire) et l'enduit a la chaux (tertiaire/sacrificiel). La defaillance d'une seule couche ne compromet pas le systeme.**
