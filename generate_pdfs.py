#!/usr/bin/env python3
"""Generate PDF documents for BaharequeModular in all languages."""

import os
import re
import glob
import markdown
from weasyprint import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE_DIR, "svg")

LANGUAGES = {
    "en": "English",
    "de": "Deutsch",
    "es": "Español",
    "pt": "Português",
    "it": "Italiano",
    "fr": "Français",
}

CSS = """
@page {
    margin: 2cm;
    size: A4;
    @bottom-center {
        content: "BaharequeModular — " counter(page);
        font-size: 9px;
        color: #999;
    }
}
body {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 11px;
    line-height: 1.6;
    color: #222;
    max-width: 170mm;
    margin: 0 auto;
}
h1 {
    font-size: 22px;
    color: #2d5a27;
    border-bottom: 3px solid #2d5a27;
    padding-bottom: 8px;
    page-break-after: avoid;
    margin-top: 40px;
}
h1:first-child { margin-top: 0; }
h2 {
    font-size: 16px;
    color: #3a7d32;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
    margin-top: 28px;
    page-break-after: avoid;
}
h3 {
    font-size: 13px;
    color: #555;
    margin-top: 20px;
    page-break-after: avoid;
}
h4 {
    font-size: 11px;
    color: #666;
    margin-top: 14px;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 8px 0 14px 0;
    font-size: 10px;
}
th, td {
    border: 1px solid #ccc;
    padding: 4px 6px;
    text-align: left;
}
th {
    background: #f0f5ef;
    color: #2d5a27;
    font-weight: 600;
}
tr:nth-child(even) { background: #fafafa; }
blockquote {
    background: #f0f5ef;
    border-left: 4px solid #2d5a27;
    padding: 10px 14px;
    margin: 14px 0;
    font-style: italic;
    color: #555;
    font-size: 10px;
}
code {
    background: #f4f4f4;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 10px;
}
pre {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 4px;
    font-size: 9px;
    overflow-x: auto;
}
pre code {
    background: none;
    padding: 0;
}
a { color: #2d5a27; }
img, svg {
    max-width: 100%;
    height: auto;
    margin: 10px 0;
}
.cover {
    text-align: center;
    padding-top: 200px;
    page-break-after: always;
}
.cover h1 {
    font-size: 36px;
    border: none;
    color: #2d5a27;
}
.cover .subtitle {
    font-size: 16px;
    color: #666;
    margin-top: 10px;
}
.cover .meta {
    font-size: 11px;
    color: #999;
    margin-top: 40px;
}
.chapter-break {
    page-break-before: always;
}
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 20px 0;
}
ul, ol { margin: 4px 0; padding-left: 20px; }
li { margin: 2px 0; }
strong { color: #333; }
"""

SUBTITLES = {
    "en": "Open-Source Prefabricated Panel System",
    "de": "Offenes Paneelsystem aus vorgefertigten Modulen",
    "es": "Sistema Abierto de Paneles Prefabricados",
    "pt": "Sistema Aberto de Painéis Pré-fabricados",
    "it": "Sistema Aperto di Pannelli Prefabbricati",
    "fr": "Système Ouvert de Panneaux Préfabriqués",
}

DESIGNER = {
    "en": "Designed by Jan Reuteler",
    "de": "Entworfen von Jan Reuteler",
    "es": "Diseñado por Jan Reuteler",
    "pt": "Projetado por Jan Reuteler",
    "it": "Progettato da Jan Reuteler",
    "fr": "Conçu par Jan Reuteler",
}

VERSION_NOTE = {
    "en": "First Publication — March 2026",
    "de": "Erstveröffentlichung — März 2026",
    "es": "Primera publicación — Marzo 2026",
    "pt": "Primeira publicação — Março 2026",
    "it": "Prima pubblicazione — Marzo 2026",
    "fr": "Première publication — Mars 2026",
}


TOC_TITLE = {
    "en": "Contents",
    "de": "Inhalt",
    "es": "Contenido",
    "pt": "Conteúdo",
    "it": "Indice",
    "fr": "Sommaire",
}

# Chapter descriptions per language: {lang: {chapter_number: (title, description)}}
CHAPTERS = {
    "en": {
        "01": ("Design Philosophy", "Origin in Colombian permaculture, traditional techniques worldwide, the hybrid approach, beauty, 80–100 year lifespan, community production, prior art, open source"),
        "02": ("Panel Anatomy", "Complete technical spec: T-bar frame, HDPE blocks, bamboo strips, )( profile, diagonal bracing, wire ties, electrical, mortar, finish layers, weight breakdown"),
        "03": ("Materials", "Bill of materials per panel, bamboo species alternatives, steel specs, HDPE alternatives, mortar mix, lime plaster, chicken wire, aluminum mesh"),
        "04": ("Construction Process", "Step-by-step production: frame fabrication, clamping, diagonal bracing, mesh, vibration table mortar pour, curing, installation, finishing, quality checklist"),
        "05": ("Structural Performance", "Two configurations (with/without steel frame), seismic, fire, thermal, acoustic performance, conservative load estimates in kg, testing plan"),
        "06": ("Corrosion Prevention", "Galvanic analysis of every material interface, environmental factors, maintenance schedule, coastal adaptations"),
        "07": ("Building Integration", "Steel frame and frameless configurations, column-panel detail, panel-to-panel joints, windows, doors, interior partitions, electrical system, adaptability"),
        "08": ("Contributing", "Project status, how to contribute, structural testing, bamboo species adaptation, translation, photography, licensing, code of conduct"),
        "09": ("Cost Estimate", "Material cost per panel (~$65–70), cost per m² (~$26–28), comparison with conventional construction, full house estimate, cost reduction strategies, regional price variations"),
        "10": ("Environmental Impact", "Carbon footprint per panel (~6–10 kg CO₂/m²), comparison with conventional walls, carbon per year of service, path to carbon-neutral, water use, waste, end of life"),
        "11": ("Transport & Handling", "Carrying jig, workshop storage, truck loading, crane/hoist for upper floors, damage repair, pre-transport checklist"),
        "12": ("Climate Adaptation", "Tropical humid, highland, dry, subtropical, coastal — mortar mix, lime plaster, overhang, and bamboo species tables for each zone"),
        "13": ("Bamboo Treatment", "Borate solution preparation, tank soaking, modified Boucherie method, quality control (turmeric test), safety, treatment summary"),
        "14": ("Acoustic Upgrade", "Noise-facing wall upgrades: dense mortar, clay damping layer, double panel with fiber cavity. Apply only where needed. Retrofit-friendly."),
        "16": ("Floor Panel Concept", "Bamboo bowstring beam: compression arch + tension tie + mortar, zero steel in span, concept pending validation"),
    },
    "de": {
        "01": ("Designphilosophie", "Ursprung in kolumbianischer Permakultur, traditionelle Techniken weltweit, der hybride Ansatz, Schönheit, 80–100 Jahre Lebensdauer, Gemeinschaftsproduktion, Stand der Technik, Open Source"),
        "02": ("Paneel-Aufbau", "Vollständige technische Spezifikation: T-Profil-Rahmen, HDPE-Blöcke, Bambusstreifen, )(-Profil, diagonale Aussteifung, Drahtbindungen, Elektrik, Mörtel, Oberflächenschichten"),
        "03": ("Materialien", "Stückliste pro Paneel, alternative Bambusarten, Stahlspezifikationen, HDPE-Alternativen, Mörtelmischung, Kalkputz"),
        "04": ("Bauprozess", "Schritt-für-Schritt-Produktion: Rahmenfertigung, Klemmung, Diagonalaussteifung, Gitter, Rütteltisch-Mörtelverguss, Aushärtung, Montage, Qualitätscheckliste"),
        "05": ("Tragverhalten", "Zwei Konfigurationen, Erdbeben-, Brand-, Wärme-, Schallschutz, konservative Tragfähigkeitsschätzungen in kg, Prüfplan"),
        "06": ("Korrosionsschutz", "Galvanische Analyse aller Materialgrenzflächen, Umweltfaktoren, Wartungsplan"),
        "07": ("Gebäudeintegration", "Stahlrahmen- und rahmenlose Konfiguration, Anschlussdetails, Fenster, Türen, Trennwände"),
        "08": ("Mitwirken", "Projektstatus, Beiträge, Prüfungen, Übersetzung, Lizenzierung"),
        "09": ("Kostenschätzung", "Materialkosten pro Paneel, Vergleich mit konventionellem Bau, Gesamthausschätzung"),
        "10": ("Umweltbilanz", "CO₂-Fussabdruck, Vergleich, Weg zur Klimaneutralität, Wasser, Abfall"),
        "11": ("Transport & Handhabung", "Tragehilfe, Lagerung, LKW-Beladung, Kranoptionen, Schadensreparatur"),
        "12": ("Klimaanpassung", "Tropisch feucht, Hochland, trocken, subtropisch, Küste — Anpassungstabellen"),
        "13": ("Bambusbehandlung", "Boratlösung, Tauchbad, Boucherie-Methode, Qualitätskontrolle, Sicherheit"),
        "14": ("Akustik-Upgrade", "Schallschutz für lärmbelastete Wände: dichterer Mörtel, Lehmdämpfung, Doppelpaneel mit Faserfüllung"),
        "16": ("Bodenpaneel-Konzept", "Bambus-Bogenträger: Druckbogen + Zugband + Mörtel, Nullstahl in der Spannweite, Konzept zur Validierung"),
    },
    "es": {
        "01": ("Filosofía de Diseño", "Origen en permacultura colombiana, técnicas tradicionales, el enfoque híbrido, belleza, 80–100 años, producción comunitaria, estado del arte, código abierto"),
        "02": ("Anatomía del Panel", "Especificación técnica completa: marco en perfil T, bloques HDPE, tiras de bambú, perfil )(, arriostramiento diagonal, amarres, eléctrica, mortero"),
        "03": ("Materiales", "Lista de materiales por panel, especies alternativas de bambú, HDPE alternativas, mortero, pañete de cal"),
        "04": ("Proceso Constructivo", "Paso a paso: fabricación de marcos, sujeción, diagonales, malla, vertido en mesa vibratoria, curado, instalación, lista de verificación"),
        "05": ("Desempeño Estructural", "Dos configuraciones, resistencia sísmica, fuego, térmica, acústica, estimaciones conservadoras en kg, plan de pruebas"),
        "06": ("Prevención de Corrosión", "Análisis galvánico de cada interfaz, factores ambientales, mantenimiento"),
        "07": ("Integración en Edificio", "Configuración con y sin estructura de acero, detalles de conexión, ventanas, puertas, divisiones"),
        "08": ("Contribuir", "Estado del proyecto, cómo contribuir, pruebas, traducción, licencia"),
        "09": ("Estimación de Costos", "Costo por panel (~$65–70 USD), comparación con construcción convencional, estimación de casa completa"),
        "10": ("Impacto Ambiental", "Huella de carbono, comparación, camino a neutralidad, agua, residuos"),
        "11": ("Transporte y Manejo", "Estructura de carga, almacenamiento, carga en camión, grúa, reparación de daños"),
        "12": ("Adaptación Climática", "Tropical húmedo, altiplano, seco, subtropical, costero — tablas de adaptación"),
        "13": ("Tratamiento del Bambú", "Solución de borato, inmersión, método Boucherie, control de calidad, seguridad"),
        "14": ("Mejora Acústica", "Mejoras para muros expuestos al ruido: mortero denso, capa de arcilla, panel doble con fibra"),
        "16": ("Concepto Panel de Piso", "Viga arco de bambú: arco en compresión + tirante en tracción + mortero, cero acero en la luz, concepto por validar"),
    },
    "pt": {
        "01": ("Filosofia de Design", "Origem na permacultura colombiana, técnicas tradicionais, abordagem híbrida, beleza, 80–100 anos, produção comunitária, estado da arte, código aberto"),
        "02": ("Anatomia do Painel", "Especificação técnica: perfil T, blocos HDPE, tiras de bambu, perfil )(, contraventamento diagonal, amarrações, elétrica, argamassa"),
        "03": ("Materiais", "Lista de materiais, espécies de bambu, alternativas HDPE, argamassa, reboco de cal"),
        "04": ("Processo Construtivo", "Passo a passo: fabricação, fixação, diagonais, tela, mesa vibratória, cura, instalação"),
        "05": ("Desempenho Estrutural", "Duas configurações, resistência sísmica, fogo, térmica, acústica, estimativas em kg"),
        "06": ("Prevenção de Corrosão", "Análise galvânica, fatores ambientais, manutenção"),
        "07": ("Integração no Edifício", "Configuração com e sem estrutura de aço, conexões, janelas, portas"),
        "08": ("Contribuir", "Status do projeto, como contribuir, testes, tradução, licença"),
        "09": ("Estimativa de Custos", "Custo por painel, comparação com construção convencional, estimativa de casa"),
        "10": ("Impacto Ambiental", "Pegada de carbono, comparação, caminho para neutralidade, água, resíduos"),
        "11": ("Transporte e Manuseio", "Estrutura de transporte, armazenamento, carregamento, guindaste, reparo"),
        "12": ("Adaptação Climática", "Tropical úmido, planalto, seco, subtropical, costeiro — tabelas"),
        "13": ("Tratamento do Bambu", "Solução de borato, imersão, método Boucherie, controle de qualidade"),
        "14": ("Melhoria Acústica", "Melhorias para paredes expostas a ruído: argamassa densa, camada de argila, painel duplo"),
        "16": ("Conceito Painel de Piso", "Viga arco de bambu: arco em compressão + tirante em tração + argamassa, zero aço no vão"),
    },
    "it": {
        "01": ("Filosofia del Design", "Origine nella permacultura colombiana, tecniche tradizionali, approccio ibrido, bellezza, 80–100 anni, produzione comunitaria, stato dell'arte, open source"),
        "02": ("Anatomia del Pannello", "Specifica tecnica: profilo T, blocchi HDPE, listelli di bambù, profilo )(, controvento diagonale, legature, impianto elettrico, malta"),
        "03": ("Materiali", "Distinta materiali, specie di bambù, alternative HDPE, malta, intonaco di calce"),
        "04": ("Processo Costruttivo", "Passo dopo passo: fabbricazione, fissaggio, diagonali, rete, tavola vibrante, stagionatura, installazione"),
        "05": ("Prestazioni Strutturali", "Due configurazioni, resistenza sismica, fuoco, termica, acustica, stime conservative in kg"),
        "06": ("Prevenzione Corrosione", "Analisi galvanica, fattori ambientali, manutenzione"),
        "07": ("Integrazione nell'Edificio", "Configurazione con e senza telaio in acciaio, connessioni, finestre, porte"),
        "08": ("Contribuire", "Stato del progetto, come contribuire, test, traduzione, licenza"),
        "09": ("Stima Costi", "Costo per pannello, confronto con costruzione convenzionale, stima casa"),
        "10": ("Impatto Ambientale", "Impronta di carbonio, confronto, percorso verso neutralità, acqua, rifiuti"),
        "11": ("Trasporto e Movimentazione", "Struttura di trasporto, stoccaggio, caricamento, gru, riparazione"),
        "12": ("Adattamento Climatico", "Tropicale umido, altopiano, secco, subtropicale, costiero — tabelle"),
        "13": ("Trattamento Bambù", "Soluzione di borato, immersione, metodo Boucherie, controllo qualità"),
        "14": ("Miglioramento Acustico", "Miglioramenti per pareti esposte al rumore: malta densa, strato di argilla, pannello doppio"),
        "16": ("Concetto Pannello Pavimento", "Trave arco di bambù: arco in compressione + tirante in trazione + malta, zero acciaio nella campata"),
    },
    "fr": {
        "01": ("Philosophie de Conception", "Origine dans la permaculture colombienne, techniques traditionnelles, approche hybride, beauté, 80–100 ans, production communautaire, état de l'art, open source"),
        "02": ("Anatomie du Panneau", "Spécification technique : profilé T, blocs HDPE, lattes de bambou, profil )(, contreventement diagonal, ligatures, électricité, mortier"),
        "03": ("Matériaux", "Nomenclature par panneau, espèces de bambou, alternatives HDPE, mortier, enduit à la chaux"),
        "04": ("Processus de Construction", "Étape par étape : fabrication, serrage, diagonales, grillage, table vibrante, cure, installation"),
        "05": ("Performance Structurelle", "Deux configurations, résistance sismique, feu, thermique, acoustique, estimations conservatives en kg"),
        "06": ("Prévention de la Corrosion", "Analyse galvanique, facteurs environnementaux, maintenance"),
        "07": ("Intégration au Bâtiment", "Configuration avec et sans ossature acier, connexions, fenêtres, portes"),
        "08": ("Contribuer", "État du projet, comment contribuer, tests, traduction, licence"),
        "09": ("Estimation des Coûts", "Coût par panneau, comparaison avec construction conventionnelle, estimation maison"),
        "10": ("Impact Environnemental", "Empreinte carbone, comparaison, chemin vers neutralité, eau, déchets"),
        "11": ("Transport et Manutention", "Structure de portage, stockage, chargement, grue, réparation"),
        "12": ("Adaptation Climatique", "Tropical humide, altitude, sec, subtropical, côtier — tableaux"),
        "13": ("Traitement du Bambou", "Solution de borate, trempage, méthode Boucherie, contrôle qualité"),
        "14": ("Amélioration Acoustique", "Améliorations pour murs exposés au bruit : mortier dense, couche d'argile, double panneau"),
        "16": ("Concept Panneau de Sol", "Poutre arc en bambou : arc en compression + tirant en traction + mortier, zéro acier dans la portée"),
    },
}


def build_toc(lang):
    """Build a table of contents page."""
    title = TOC_TITLE.get(lang, "Contents")
    chapters = CHAPTERS.get(lang, CHAPTERS["en"])

    rows = ""
    for num in sorted(chapters.keys()):
        ch_title, ch_desc = chapters[num]
        rows += f"""
        <tr>
            <td style="width:30px; font-weight:bold; color:#2d5a27; vertical-align:top; border:none; padding:6px 8px;">{num}</td>
            <td style="vertical-align:top; border:none; padding:6px 8px;"><strong>{ch_title}</strong><br>
            <span style="font-size:8px; color:#888;">{ch_desc}</span></td>
        </tr>"""

    return f"""
    <div class="chapter-break" style="padding-top: 40px;">
        <h1 style="border-bottom: 3px solid #2d5a27; padding-bottom: 8px;">{title}</h1>
        <table style="border:none; width:100%; margin-top:20px; border-collapse:collapse;">
            <tbody style="border:none;">{rows}</tbody>
        </table>
    </div>
    """


def read_svg(filename, lang="en"):
    """Read an SVG file and return its content for inline embedding.
    Tries language-specific SVG first, falls back to English master."""
    if lang != "en":
        lang_path = os.path.join(BASE_DIR, lang, "svg", filename)
        if os.path.exists(lang_path):
            with open(lang_path, "r") as f:
                content = f.read()
            content = re.sub(r'<\?xml[^?]*\?>\s*', '', content)
            return content
    # Fallback to English master
    path = os.path.join(SVG_DIR, filename)
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
        content = re.sub(r'<\?xml[^?]*\?>\s*', '', content)
        return content
    return f"<!-- SVG not found: {filename} -->"


def resolve_svg_references(html_content, lang="en"):
    """Replace markdown image references to SVGs with inline SVG content."""
    def replace_svg_img(match):
        src = match.group(1)
        if src.endswith(".svg") and ("svg/" in src):
            filename = os.path.basename(src)
            svg_content = read_svg(filename, lang)
            return f'<div style="margin: 12px 0;">{svg_content}</div>'
        return match.group(0)

    # Match <img> tags pointing to SVGs
    html_content = re.sub(
        r'<img[^>]*src="([^"]*\.svg)"[^>]*/?>',
        replace_svg_img,
        html_content
    )
    # Also match markdown-generated img tags
    html_content = re.sub(
        r'<img\s+alt="[^"]*"\s+src="([^"]*\.svg)"\s*/?>',
        replace_svg_img,
        html_content
    )
    return html_content


def generate_pdf(lang):
    """Generate a PDF for the given language."""
    lang_dir = os.path.join(BASE_DIR, lang)
    if not os.path.isdir(lang_dir):
        print(f"  Skipping {lang} — directory not found")
        return

    # Get all markdown files sorted by number
    md_files = sorted(glob.glob(os.path.join(lang_dir, "*.md")))
    if not md_files:
        print(f"  Skipping {lang} — no markdown files")
        return

    # Build cover page
    cover = f"""
    <div class="cover">
        <h1>BaharequeModular</h1>
        <div class="subtitle">{SUBTITLES.get(lang, SUBTITLES['en'])}</div>
        <div class="meta">
            {DESIGNER.get(lang, DESIGNER['en'])}<br>
            janreuteler@icloud.com<br><br>
            {VERSION_NOTE.get(lang, VERSION_NOTE['en'])}<br><br>
            Hardware: CERN-OHL-S v2 · Documentation: CC BY-SA 4.0
        </div>
    </div>
    """

    # Build content from all markdown files
    chapters = []
    for md_file in md_files:
        with open(md_file, "r") as f:
            md_content = f.read()

        # Convert markdown to HTML
        html = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code", "toc"]
        )

        # Add chapter break
        chapters.append(f'<div class="chapter-break">{html}</div>')

    # Insert table of contents between cover and chapters
    toc = build_toc(lang)
    body = cover + toc + "\n".join(chapters)

    # Resolve SVG references to inline SVGs
    body = resolve_svg_references(body, lang)

    # Full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""

    # Generate PDF
    output_path = os.path.join(BASE_DIR, f"BaharequeModular-{lang.upper()}.pdf")
    HTML(string=full_html, base_url=BASE_DIR).write_pdf(output_path)
    file_size = os.path.getsize(output_path)
    print(f"  {output_path} ({file_size // 1024} KB)")


if __name__ == "__main__":
    print("Generating BaharequeModular PDFs...\n")
    for lang, name in LANGUAGES.items():
        print(f"{name} ({lang}):")
        generate_pdf(lang)
    print("\nDone.")
