# BaharequeModular

### Open-Source Prefabricated Panel Construction System

**Community-built, 80–100 year housing from local materials.**

> *This project is in active development. This initial publication is a work in progress — documentation will be refined, technical drawings improved, and the system built and tested in Colombia (Eje Cafetero region). All findings, test results, and design iterations will be published here as they happen. Feedback, suggestions, and contributions are welcome — file an issue or submit a pull request.*

---

## Related Techniques

This system builds on a worldwide family of traditional frame-and-infill construction: **bahareque** (Colombia), **quincha** (Peru/Chile), **wattle-and-daub** (global), **Fachwerk/colombage** (Europe), **dhajji-dewari** (Kashmir), **gaiola pombalina** (Portugal), **bajareque** (Honduras), **taquezal** (Nicaragua), **tabique** (Mexico/Philippines), **tsuchikabe** (Japan), **pau-a-pique** (Brazil). See [Philosophy](en/01-philosophy.md) for how each tradition informs this design.

## Why This Exists

Billions of people live in housing that fails — in earthquakes, floods, or simply from age. Most "affordable housing" lasts 15–20 years, trapping families in endless rebuild cycles.

**Bioconstruction** (bamboo, earth, lime) gives beautiful, breathable buildings with millennia of proven performance in tropical climates — but often lacks structural safety for seismic zones.

**Modern construction** (steel, concrete) gives safety and permits — but is expensive, requires specialized skills, and has no soul.

This system bridges both:

- **Traditional where it's seen** — lime plaster, guadua bamboo, natural textures
- **Modern where it matters** — galvanized steel L-angle frame carries seismic loads
- **80–100 year lifespan** — you build once, not every generation
- **Community-producible** — screw-clamping needs no welding, no specialized tools
- **Permaculture-integrated** — uses local bamboo, turns invasive grass into fiber reinforcement
- **Open source** — because the knowledge to build safe, beautiful, affordable housing should not be locked behind patents or consulting fees

## Quick Specs

| | |
|---|---|
| **Panel size** | 1.0 m × 2.5 m (vertical, scalable to any height) |
| **Dry-assembly weight** | ~75 kg (2 people — shipped to site before in-situ mortar pour) |
| **Finished weight (baseline mix)** | ~440 kg (≈ 176 kg/m²) |
| **Finished weight (optimized bahareque mix)** | ~360 kg (≈ 144 kg/m²) |
| **Frame** | L 40×40×4 mm, hot-dip galvanized steel (ASTM A36 / ICONTEC NTC 2542) |
| **Infill** | Structural bamboo strips, screw-clamped (30 % cavity density at baseline spec) |
| **Bracing** | Diagonal bamboo strips (3–5× seismic improvement) |
| **Mortar (baseline)** | 1:4 cement:sand + pozzolanic admixture |
| **Mortar (optimized)** | Pozzolanic lime + fly ash/RHA + pasto estrella fiber |
| **Pour method** | In-situ vertical pour (preferred) or workshop vibration-table pour |
| **Finish** | Lime plaster + lime wash |
| **Wall thickness** | ~85 mm |
| **Variants** | P (pass-through), O (outlet), S (switch), W (water) |
| **Integrated electrical** | 12V lighting + 120V mains, snap-connect between panels |

> _Combined-profile diagram pending — the previous SVG (`svg/11-combined-profile-face.svg`) shows T-bar geometry and is not representative of the current L 40×40×4 angle frame. See [`SVG-STATUS.md`](SVG-STATUS.md) for the full SVG regeneration task list._

## Repository Structure

```
bahareque-modular/
├── README.md              ← You are here
├── LICENSE-CERN-OHL-S-v2.txt
├── LICENSE-CC-BY-SA-4.0.txt
├── en/                    ← English documentation
│   ├── 01-philosophy.md
│   ├── 02-panel-anatomy.md
│   ├── 03-materials.md
│   ├── 04-construction-process.md
│   ├── 05-structural-performance.md
│   ├── 06-corrosion-prevention.md
│   ├── 08-contributing.md
│   ├── 09-cost-estimate.md
│   ├── 10-environmental-impact.md
│   ├── 11-transport-handling.md
│   ├── 12-climate-adaptation.md
│   ├── 13-bamboo-treatment.md
│   └── 14-acoustic-upgrade.md
├── de/                    ← Deutsche Dokumentation
├── es/                    ← Documentación en español
├── pt/                    ← Documentação em português
├── it/                    ← Documentazione in italiano
├── fr/                    ← Documentation en français
├── svg/                   ← Technical diagrams (language-neutral)
└── stl/                   ← 3D printable panel model
```

## Licensing

| Content | License |
|---|---|
| Hardware designs (SVGs, STLs, construction specs) | [CERN-OHL-S v2](LICENSE-CERN-OHL-S-v2.txt) |
| Documentation (text, educational content) | [CC BY-SA 4.0](LICENSE-CC-BY-SA-4.0.txt) |

**What this means:** You can freely use, modify, and distribute everything. But modifications must remain open source under the same licenses. No one can close this — not even us.

### License FAQ — Plain Language

**Can I build a house with this system?**
Yes. Free. No permission needed. No fees. No registration.

**Can I build panels and sell them?**
Yes. But you must share any design modifications you make under the same open licenses. You cannot patent your modifications.

**Can I teach a course using these documents?**
Yes. Credit the project and share any new materials you create under CC BY-SA 4.0.

**Can I patent a variation of this system?**
No. The CERN-OHL-S v2 license requires that anyone who distributes the design or products based on it grants a royalty-free patent license. This prevents anyone — including us — from patenting the system or its derivatives.

**Can a company use this commercially?**
Yes. Companies can manufacture and sell panels built with this system. They must share any design modifications under CERN-OHL-S v2. They cannot add patent restrictions.

**Why two licenses?**
CERN-OHL-S v2 is designed for physical hardware — it protects the panel design, construction method, and STL files, and includes patent defense. CC BY-SA 4.0 is designed for written works — it protects the documentation, diagrams, and educational content, and is recognized worldwide in 40+ languages. Together they cover everything.

**What if someone ignores the license?**
The same thing that happens with any open-source license violation: the community notices, the violation is documented, and legal action can follow. CC BY-SA has been upheld in courts worldwide. CERN-OHL-S is backed by CERN's legal framework.

**Can someone take this project private / close the source?**
No. Both licenses are copyleft / share-alike. Every derivative must remain open under the same terms. This is permanent and irrevocable.

## Contributing

This is a living project. We need:

- **Builders** — try it, document your experience, share what worked and what didn't
- **Engineers** — structural testing, seismic analysis, code compliance research
- **Bamboo experts** — adaptation notes for species beyond Guadua angustifolia
- **Translators** — help bring the documentation to more languages
- **Designers** — improve the SVGs, create assembly animations, render visualizations

File an issue. Submit a PR. All contributions inherit the same open licenses.

## Origin & Contact

Designed by **Jan Reuteler** (janreuteler@icloud.com), Switzerland.

Developed for the Colombian Andes (Eje Cafetero, ~2,000 m altitude) using locally available *Guadua angustifolia* — the strongest structural bamboo in the Americas. The principles apply to any tropical or subtropical region with access to structural bamboo, cement, and basic steel fabrication.

---

# BaharequeModular

### Offenes vorgefertigtes Paneel-Bausystem

**Gemeinschaftlich gebaut, 80–100 Jahre Lebensdauer, aus lokalen Materialien.**

> *Dieses Projekt befindet sich in aktiver Entwicklung. Diese erste Veröffentlichung ist ein Zwischenstand — die Dokumentation wird laufend verbessert, technische Zeichnungen verfeinert und das System in Kolumbien (Region Eje Cafetero) gebaut und getestet. Alle Erkenntnisse, Testergebnisse und Designänderungen werden hier veröffentlicht. Feedback, Vorschläge und Beiträge sind willkommen — erstellen Sie ein Issue oder einen Pull Request.*

## Warum dieses Projekt existiert

Milliarden Menschen leben in Häusern, die versagen — bei Erdbeben, Überschwemmungen oder einfach durch Alterung. Die meisten «bezahlbaren» Häuser halten 15–20 Jahre und zwingen Familien in endlose Wiederaufbauzyklen.

**Biokonstruktion** (Bambus, Erde, Kalk) liefert schöne, atmungsaktive Gebäude mit jahrtausendealter Bewährung in tropischen Klimazonen — aber oft ohne ausreichende Erdbebensicherheit.

**Moderne Bauweise** (Stahl, Beton) liefert Sicherheit und Baugenehmigungen — ist aber teuer, erfordert Fachkräfte und hat keine Seele.

Dieses System vereint beides:

- **Traditionell, wo man es sieht** — Kalkputz, Guadua-Bambus, natürliche Texturen
- **Modern, wo es zählt** — verzinkter Stahl-T-Profilrahmen trägt Erdbebenlasten
- **80–100 Jahre Lebensdauer** — einmal bauen, nicht jede Generation
- **Gemeinschaftlich herstellbar** — Schraubklemmsystem braucht kein Schweissen, kein Spezialwerkzeug
- **Permakultur-integriert** — nutzt lokalen Bambus, verwandelt invasive Gräser in Faserverstärkung
- **Open Source** — weil das Wissen, sicheres, schönes, bezahlbares Wohnen zu bauen, nicht hinter Patenten oder Beraterhonoraren eingesperrt sein darf

## Kurzspezifikationen

| | |
|---|---|
| **Paneelgrösse** | 1,0 m × 2,5 m (vertikal, skalierbar auf jede Höhe) |
| **Gewicht — Trockenmontage** | ~75 kg (2 Personen, vor Ort-Mörtelguss) |
| **Gewicht — fertig (Standardmischung)** | ~440 kg (≈ 176 kg/m²) |
| **Gewicht — fertig (optimierte Bahareque-Mischung)** | ~360 kg (≈ 144 kg/m²) |
| **Rahmen** | L-Winkel 40×40×4 mm, feuerverzinkter Stahl (ASTM A36) |
| **Füllung** | Bambus-Strukturstreifen, schraubgeklemmt (30 % Hohlraumdichte) |
| **Aussteifung** | Diagonale Bambus-Aussteifung (3–5× Erdbebenverbesserung) |
| **Mörtel** | 1:4 Zement:Sand + puzzolanisches Zusatzmittel (Standard), oder hydraulischer Kalk + Flugasche/RHA + Pasto-Estrella-Fasern (optimiert) |
| **Gussverfahren** | Vor-Ort-Vertikalguss (bevorzugt) oder Werkstatt-Rütteltisch |
| **Oberfläche** | Kalkputz + Kalkanstrich |
| **Wandstärke** | ~85 mm |

> _Hinweis: Die Übersetzungen (DE/ES/FR/IT/PT) außerhalb dieser Schnellspezifikation spiegeln noch die vorherige T-Profil-Spezifikation wider und werden in einem nachfolgenden Update angeglichen._

## Lizenzierung

| Inhalt | Lizenz |
|---|---|
| Hardware-Designs (SVGs, STLs, Bauspezifikationen) | CERN-OHL-S v2 |
| Dokumentation (Texte, Bildungsinhalte) | CC BY-SA 4.0 |

Sie dürfen alles frei nutzen, verändern und verbreiten. Änderungen müssen unter denselben Lizenzen offen bleiben.

### Lizenz-FAQ

**Kann ich ein Haus mit diesem System bauen?**
Ja. Kostenlos. Ohne Genehmigung. Ohne Gebühren. Ohne Registrierung.

**Kann ich Paneele herstellen und verkaufen?**
Ja. Aber Sie müssen alle Designänderungen unter denselben offenen Lizenzen teilen. Sie können Ihre Änderungen nicht patentieren.

**Kann ich einen Kurs mit diesen Dokumenten geben?**
Ja. Nennen Sie das Projekt und teilen Sie neues Material unter CC BY-SA 4.0.

**Kann jemand eine Variante dieses Systems patentieren?**
Nein. Die CERN-OHL-S v2 Lizenz verlangt, dass jeder, der das Design oder darauf basierende Produkte verbreitet, eine gebührenfreie Patentlizenz erteilt.

**Kann ein Unternehmen dies kommerziell nutzen?**
Ja. Unternehmen können Paneele herstellen und verkaufen. Designänderungen müssen unter CERN-OHL-S v2 geteilt werden. Patentbeschränkungen dürfen nicht hinzugefügt werden.

**Kann jemand dieses Projekt schliessen?**
Nein. Beide Lizenzen sind Copyleft / Share-Alike. Jedes Derivat muss offen bleiben. Dies ist dauerhaft und unwiderruflich.

## Ursprung & Kontakt

Entworfen von **Jan Reuteler** (janreuteler@icloud.com), Schweiz.

Entwickelt für die kolumbianischen Anden (Eje Cafetero, ~2.000 m Höhe) mit lokal verfügbarer *Guadua angustifolia* — dem stärksten Strukturbambus der Amerikas. Die Prinzipien sind auf jede tropische oder subtropische Region mit Zugang zu Strukturbambus, Zement und einfacher Stahlverarbeitung anwendbar.

---

# BaharequeModular

### Sistema Abierto de Paneles Prefabricados

**Construido por la comunidad, 80–100 años de vida útil, con materiales locales.**

> *Este proyecto está en desarrollo activo. Esta publicación inicial es un trabajo en progreso — la documentación se irá refinando, los dibujos técnicos mejorados, y el sistema será construido y probado en Colombia (región del Eje Cafetero). Todos los hallazgos, resultados de pruebas e iteraciones de diseño se publicarán aquí. Comentarios, sugerencias y contribuciones son bienvenidos — abra un issue o envíe un pull request.*

## Por qué existe este proyecto

Miles de millones de personas viven en viviendas que fallan — en terremotos, inundaciones o simplemente por el paso del tiempo. La mayoría de la «vivienda asequible» dura 15–20 años, atrapando a las familias en ciclos interminables de reconstrucción.

**Bioconstrucción** (guadua, tierra, cal) ofrece edificios hermosos y transpirables con milenios de rendimiento comprobado en climas tropicales — pero frecuentemente sin suficiente seguridad sísmica.

**Construcción moderna** (acero, concreto) ofrece seguridad y permisos — pero es costosa, requiere mano de obra especializada y carece de alma.

Este sistema une ambos mundos:

- **Tradicional donde se ve** — pañete de cal, guadua, texturas naturales
- **Moderno donde importa** — marco de acero galvanizado en T soporta cargas sísmicas
- **80–100 años de vida útil** — se construye una sola vez, no cada generación
- **Producible por la comunidad** — el sistema de sujeción por tornillo no requiere soldadura ni herramientas especializadas
- **Integrado con permacultura** — usa guadua local, convierte pastos invasivos en refuerzo de fibra
- **Código abierto** — porque el conocimiento para construir vivienda segura, bella y asequible no debe estar encerrado detrás de patentes ni honorarios de consultoría

## Especificaciones rápidas

| | |
|---|---|
| **Tamaño del panel** | 1,0 m × 2,5 m (vertical, escalable a cualquier altura) |
| **Peso — ensamble en seco** | ~75 kg (2 personas, antes del vertido in-situ del mortero) |
| **Peso — terminado (mezcla base)** | ~440 kg (≈ 176 kg/m²) |
| **Peso — terminado (mezcla bahareque optimizada)** | ~360 kg (≈ 144 kg/m²) |
| **Marco** | Ángulo L 40×40×4 mm, acero galvanizado en caliente (ASTM A36 / ICONTEC NTC 2542) |
| **Relleno** | Tiras de bambú estructural, sujetadas con tornillos (30 % de densidad de cavidad) |
| **Arriostramiento** | Tiras diagonales de bambú (mejora sísmica 3–5×) |
| **Mortero** | 1:4 cemento:arena + adición puzolánica (base), o cal hidráulica + ceniza volante/RHA + fibras de pasto estrella (optimizado) |
| **Método de vertido** | Vertido vertical in-situ (preferido) o mesa vibratoria en taller |
| **Acabado** | Pañete de cal + lechada de cal |

> _Nota: Las traducciones (DE/ES/FR/IT/PT) fuera de esta especificación rápida aún reflejan la especificación anterior de perfil T y se actualizarán en una revisión posterior._
| **Espesor de muro** | ~85 mm |

## Licenciamiento

| Contenido | Licencia |
|---|---|
| Diseños de hardware (SVGs, STLs, especificaciones constructivas) | CERN-OHL-S v2 |
| Documentación (textos, contenido educativo) | CC BY-SA 4.0 |

Puede usar, modificar y distribuir todo libremente. Las modificaciones deben permanecer abiertas bajo las mismas licencias. Nadie puede cerrar esto — ni siquiera nosotros.

### Preguntas Frecuentes sobre la Licencia

**¿Puedo construir una casa con este sistema?**
Sí. Gratis. Sin permiso. Sin tarifas. Sin registro.

**¿Puedo fabricar paneles y venderlos?**
Sí. Pero debe compartir cualquier modificación de diseño bajo las mismas licencias abiertas. No puede patentar sus modificaciones.

**¿Puedo dar un curso usando estos documentos?**
Sí. Cite el proyecto y comparta cualquier material nuevo bajo CC BY-SA 4.0.

**¿Se puede patentar una variación de este sistema?**
No. La licencia CERN-OHL-S v2 requiere que cualquier persona que distribuya el diseño o productos basados en él otorgue una licencia de patente libre de regalías.

**¿Puede una empresa usar esto comercialmente?**
Sí. Las empresas pueden fabricar y vender paneles. Deben compartir modificaciones de diseño bajo CERN-OHL-S v2. No pueden agregar restricciones de patente.

**¿Alguien puede cerrar el código fuente de este proyecto?**
No. Ambas licencias son copyleft / share-alike. Cada derivado debe permanecer abierto. Esto es permanente e irrevocable.

## Origen y contacto

Diseñado por **Jan Reuteler** (janreuteler@icloud.com), Suiza.

Desarrollado para los Andes colombianos (Eje Cafetero, ~2.000 m de altitud) usando *Guadua angustifolia* disponible localmente — el bambú estructural más fuerte de las Américas. Los principios son aplicables a cualquier región tropical o subtropical con acceso a bambú estructural, cemento y fabricación básica de acero.

---

# BaharequeModular

### Sistema Aberto de Painéis Pré-fabricados

**Construído pela comunidade, 80–100 anos de vida útil, com materiais locais.**

> *Este projeto está em desenvolvimento ativo. Esta publicação inicial é um trabalho em andamento — a documentação será refinada, os desenhos técnicos melhorados, e o sistema será construído e testado na Colômbia (região do Eje Cafetero). Todos os resultados e iterações de design serão publicados aqui. Comentários, sugestões e contribuições são bem-vindos.*

Documentação completa: [pt/](pt/)

**Licença:** Hardware: CERN-OHL-S v2 · Documentação: CC BY-SA 4.0

Pode construir, fabricar, vender, ensinar — tudo livre. Modificações devem permanecer abertas. Ninguém pode patentear variações. Ninguém pode fechar o código. Permanente e irrevogável.

Projetado por **Jan Reuteler** (janreuteler@icloud.com), Suíça.

---

# BaharequeModular

### Sistema Aperto di Pannelli Prefabbricati

**Costruito dalla comunità, 80–100 anni di vita utile, con materiali locali.**

> *Questo progetto è in sviluppo attivo. Questa pubblicazione iniziale è un lavoro in corso — la documentazione verrà perfezionata, i disegni tecnici migliorati, e il sistema sarà costruito e testato in Colombia (regione dell'Eje Cafetero). Tutti i risultati e le iterazioni di design saranno pubblicati qui. Commenti, suggerimenti e contributi sono benvenuti.*

Documentazione completa: [it/](it/)

**Licenza:** Hardware: CERN-OHL-S v2 · Documentazione: CC BY-SA 4.0

Si può costruire, fabbricare, vendere, insegnare — tutto libero. Le modifiche devono rimanere aperte. Nessuno può brevettare variazioni. Nessuno può chiudere il codice. Permanente e irrevocabile.

Progettato da **Jan Reuteler** (janreuteler@icloud.com), Svizzera.

---

# BaharequeModular

### Système Ouvert de Panneaux Préfabriqués

**Construit par la communauté, 80–100 ans de durée de vie, avec des matériaux locaux.**

> *Ce projet est en développement actif. Cette publication initiale est un travail en cours — la documentation sera affinée, les dessins techniques améliorés, et le système sera construit et testé en Colombie (région de l'Eje Cafetero). Tous les résultats et itérations de conception seront publiés ici. Commentaires, suggestions et contributions sont les bienvenus.*

Documentation complète : [fr/](fr/)

**Licence :** Hardware : CERN-OHL-S v2 · Documentation : CC BY-SA 4.0

Vous pouvez construire, fabriquer, vendre, enseigner — tout est libre. Les modifications doivent rester ouvertes. Personne ne peut breveter des variations. Personne ne peut fermer le code. Permanent et irrévocable.

Conçu par **Jan Reuteler** (janreuteler@icloud.com), Suisse.