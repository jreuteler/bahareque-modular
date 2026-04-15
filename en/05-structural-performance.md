# Structural Performance

## System Architecture

This panel system was designed to work **with a steel column-and-beam frame** — the configuration we recommend for multi-story buildings in seismic zones. In that configuration, the steel frame carries gravity and seismic loads while the panels provide lateral bracing, weather enclosure, thermal mass, and integrated services.

However, the panels are **structurally capable of working without a steel building frame**. With compression capacity far exceeding typical residential loads (two side L-angle posts at L 40×40×4), a row of panels can comfortably carry a second floor and roof without an independent steel structure. A simple timber or bamboo ring beam at the top connects the panels and distributes the roof load.

**Two configurations:**

| Configuration | Use case | Panel role |
|---------------|----------|-----------|
| **With steel frame** (recommended) | Multi-story, high seismic zones, commercial/institutional | Infill — panels bolt into frame, steel carries primary loads |
| **Without steel frame** (simpler, lower cost) | Single story + loft/mezzanine, moderate seismic zones, residential | Load-bearing — panels carry roof and upper floor directly |

The load capacity estimates below apply to both configurations. The steel frame adds redundancy and moment resistance, but is not required for the panels to perform structurally.

## Seismic Performance

### Diagonal Bracing

Each panel contains two diagonal bamboo strips (one per side, opposing corners), forming an X when viewed from the front. Under seismic loading:

1. **Shear → tension conversion:** When the building frame racks sideways, one diagonal goes into tension while the opposite goes into compression. The bamboo diagonal in tension resists the racking force efficiently — bamboo has excellent tensile strength (150–200 MPa for Guadua angustifolia).
2. **Pre-tension:** Diagonals are installed with slight pre-tension, eliminating slack and ensuring immediate engagement under load.
3. **Wire tie grid:** Galvanized wire ties at every diagonal-vertical crossing (~16–20 ties total) distribute the diagonal force across the full panel face, preventing localized failure.

**Estimated improvement: 3–5× racking resistance** compared to panels without diagonal bracing.

### The )( Profile and Diagonal Interference

![Profile and Interference](../svg/09-profile.svg)

The HDPE blocks hold bamboo strips 30 mm from the web at top and bottom. Without the diagonal, strips would flex inward to ~5 mm from the web at mid-height, creating a smooth )( curve.

**In practice, the diagonal modifies this profile.** The diagonal strip (20 mm thick) runs at web level behind the vertical strips. At each of the ~22 crossing points in the middle 77% of the panel, the diagonal holds the vertical strip at 20 mm from the web — preventing full flex. Between crossings, strips flex slightly more. The result is a **ribbed )( profile**: a series of rigid nodes (at wire-tied crossings) with slight flex between them.

This interference is **by design and beneficial:**

- **Out-of-plane resistance:** The mortar between the strip layers still forms an arch, but with more pronounced ribs at each crossing — creating more mechanical interlock points than a smooth curve.
- **Mechanical interlock:** The varying mortar thickness at and between crossings locks the bamboo strips more securely than a uniform gap would.
- **Buckling resistance:** Strips held at 20 mm from the web (vs 5 mm with natural flex) contribute **7× more** to the wall's moment of inertia. This increases the critical buckling load by ~10% — meaning the diagonal improves not just racking resistance but also vertical load capacity.

| Zone | Panel height | Gap to web | Behavior |
|------|-------------|-----------|----------|
| HDPE block zone (top/bottom) | 0–12% and 88–100% | 30 mm | Free flex, no interference |
| Interference zone (middle) | 12–88% | 20 mm (held by diagonal) | Diagonal acts as spacer, wire ties lock crossings |

**For builders:** The diagonal strip is installed first (threaded through HDPE notches at web level), then the vertical strips are placed against it. At crossing points, the vertical strip rests on the diagonal — they touch, and the wire tie locks them together. No notching, cutting, or special treatment is needed. The mortar fills all gaps during the vibration table pour.

### Ductile Failure Mode

The combination of bamboo strips, wire ties, and mortar creates a composite that fails gradually:

1. First: mortar cracks (visible warning)
2. Then: wire ties stretch (energy absorption)
3. Then: bamboo strips deform (high ductility)
4. The steel frame remains intact throughout — the building does not collapse

This is fundamentally different from unreinforced masonry, which fails brittlely (sudden collapse with no warning).

## Fire Resistance

- **Mortar encasement:** The bamboo strips are fully encased in mortar (~85 mm wall thickness). Mortar is non-combustible and acts as thermal insulation for the bamboo.
- **Bamboo charring:** Even if fire penetrates the mortar, bamboo chars slowly and predictably (similar to timber construction). The steel frame behind maintains structural integrity.
- **Lime plaster finish:** Non-combustible. Provides additional fire protection.
- **No exposed bamboo:** Once installed and finished, no bamboo is visible or accessible to flame.

## Thermal Performance

- **Thermal mass:** ~85 mm of mortar provides significant thermal mass — absorbs heat during the day, releases at night. Reduces temperature swings in tropical climates.
- **Breathability:** Lime plaster is vapor-permeable. Moisture passes through the wall rather than getting trapped, preventing condensation and mold.
- **No insulation gap:** The system does not include a thermal insulation layer. In tropical climates (the primary target), thermal mass is more valuable than insulation. For temperate climates, an external insulation layer can be added outside the lime plaster.

## Acoustic Performance

The dense mortar core provides good sound attenuation:

- **Estimated STC (Sound Transmission Class):** 40–45 for a single panel wall
- **With lime plaster on both sides:** STC 42–48
- **Comparison:** Standard concrete block wall: STC 40–45. The panel system is comparable.

## Load Capacity

> **Disclaimer:** The values below are conservative analytical estimates based on material properties and geometry. They are NOT based on laboratory testing. Do not use these values for structural engineering without independent verification. Actual performance depends on material quality, workmanship, and connection details. See [Testing Needed](#testing-needed) below.

### Panel Self-Weight

| Component | Weight |
|-----------|--------|
| Steel L-angle frame (L 40×40×4, 7 m at 2.42 kg/m + clamping strips + gussets) | ~22 kg |
| Mortar, cement-sand, baseline (0.147 m³ net × ~2 000 kg/m³) | ~294 kg |
| Bamboo strips + diagonals (30 % cavity density) | ~42 kg |
| Lime plaster (10 mm each face × 1 800 kg/m³) | ~90 kg |
| HDPE blocks, wire, mesh, conduit, cables, lime wash, misc | ~12 kg |
| **Total panel weight, baseline mix** | **~460 kg** |
| **Weight per m² of wall, baseline** | **~184 kg/m²** |
| Total panel weight, optimized bahareque mix (pozzolanic lime + pasto estrella + 5 mm plaster) | ~380 kg |
| Weight per m² of wall, optimized | ~152 kg/m² |

For comparison: 150 mm concrete block wall ≈ 180 kg/m². The panel system at baseline is roughly equivalent to conventional masonry in weight per unit area; the optimized bahareque mix is ~15 % lighter. Both specs are dramatically lighter than reinforced concrete (~300 kg/m² for a 125 mm poured wall) and carry far lower embodied CO₂ per unit area.

### Axial (Vertical) Load

Each panel has two vertical L-angle side posts that can carry significant compressive loads:

| Element | Cross-section | Conservative axial capacity |
|---------|--------------|---------------------------|
| Side L-angle post (L 40×40×4 mm) | A ≈ 304 mm² | ~36 kN per post (at σ = 120 MPa, ~50 % of A36 yield) |
| Two side L-angle posts per panel | 2 × 304 mm² | ~72 kN per panel |

**What this means in practice:**

A typical single-story house with a loft/mezzanine and terracotta tile roof imposes roughly 200–400 kg of load per linear meter of wall (roof + ceiling + mezzanine floor + live load), i.e. ~2–4 kN/m. A single 1 m panel with ~72 kN of steel-alone axial capacity provides **roughly 18–36× the typical residential demand** — and the mortar and bamboo contribute additional capacity that has not yet been quantified through testing.

**The panels carry a second floor and roof comfortably.** The analytical estimate of steel-alone capacity is already many times above typical residential loads, but exact composite capacity requires lab validation.

When used **with a separate steel building frame** (steel columns between panels), this panel axial capacity is pure reserve margin — the columns carry the gravity loads. When used **without a separate building frame**, the panels are the load-bearing structure. In that case, a timber or bamboo ring beam at the top of the wall distributes the roof load evenly across all panels and ties them together.

Buckling is not a concern at these load levels **when the L-angle is embedded in the panel composite**: the 85 mm mortar wall thickness provides continuous lateral stiffness to the angle frame, and the panel height-to-thickness ratio (~2,500/85 ≈ 29) is well within accepted slenderness limits for reinforced walls. The diagonal bamboo bracing adds racking and out-of-plane stiffness to the composite.

**Important: open-profile weak-axis limitation.** Open structural profiles — L-angles, T-bars, C-channels — have minimal stiffness about their weak axis. A freestanding L 40×40×4 post without panel bracing (I_min ≈ 3.8 × 10⁴ mm⁴ about the weak axis through the heel) would buckle under modest load. The 36 kN per L-angle capacity stated above is the **axial yield capacity** and is ONLY achievable when the angle is continuously braced by the panel infill (mortar + guadua). This distinction is critical for construction sequencing — the L-angle frame must not be axially loaded before panels are poured, cured, and carrying composite load. For freestanding columns in multi-story buildings, open profiles are not appropriate — use square hollow section (SHS) instead.

### Lateral (In-Plane / Racking) Load

This is the panel's primary structural contribution — resisting horizontal forces from wind and earthquakes.

**Without diagonal bracing (mortar + vertical strips only):**

Conservative estimate based on mortar shear strength (τ ≈ 0.3 MPa for 1:4 cement:sand mortar) across the panel cross-section:

- Shear area: ~85 mm × 1,000 mm = 85,000 mm²
- Conservative shear capacity: 85,000 × 0.3 = ~25 kN per panel
- With safety factor 3: **~8 kN working load per panel**

**With diagonal bracing (the designed configuration):**

The diagonal bamboo strip (60 × 20 mm, Guadua angustifolia) in tension:

- Cross-section: 1,200 mm²
- Conservative tensile strength: 80 MPa (using ~50% of published 150–200 MPa)
- Diagonal tension capacity: 1,200 × 80 = ~96 kN
- Horizontal component (cos 69°): ~96 × 0.36 = ~34 kN per diagonal
- Two diagonals (one per side, one in tension): ~34 kN
- Wire ties and mortar interlock add additional resistance
- With safety factor 3: **~12–15 kN working racking load per panel**

**For context:** A 3 m wide wall section (3 panels) provides ~36–45 kN of racking resistance. A single-story residential building in a moderate seismic zone (PGA 0.2g) with 30 kN of seismic mass above the wall needs roughly 6 kN of base shear resistance per linear meter of wall. Three panels per meter provide 4–5× this requirement.

These are very conservative numbers. The mortar matrix, wire tie grid, and )( profile all contribute additional resistance not accounted for above.

### Out-of-Plane (Wind / Impact) Load

The panel resists pressure perpendicular to the wall face (wind suction/pressure, impact):

- The mortar arch created by the )( profile acts as a shallow vault between the rigid top and bottom L-angle members
- Conservative estimate for uniform wind pressure, treating the panel as a simply supported slab:

| Parameter | Value |
|-----------|-------|
| Panel span (between top/bottom L-angles) | 2.5 m |
| Panel width | 1.0 m |
| Mortar thickness (minimum, at center) | ~55 mm |
| Mortar flexural strength (conservative) | 1.0 MPa |
| Estimated uniform pressure capacity | ~0.7 kPa |
| With safety factor 2 | **~0.35 kPa working load** |

**For context:** 0.35 kPa ≈ wind speed ~25 m/s (90 km/h). For higher wind zones, the steel frame (not the panel) carries the wind load through the beam-to-column connections. The panel only needs to resist local pressure between its own frame members.

The bamboo strip grid and wire ties provide significant additional out-of-plane resistance not captured in the simple slab model — the panel is a composite, not a plain mortar slab.

### Point Loads (Fixtures, Shelves, Cabinets)

| Fixture type | Anchor method | Conservative capacity |
|-------------|--------------|----------------------|
| Light items (pictures, clocks, towel hooks) | Masonry nail or screw into mortar | 5–10 kg per anchor |
| Medium items (shelves, mirrors, small cabinets) | Plastic expansion anchor in mortar (6–8 mm) | 15–25 kg per anchor |
| Heavy items (kitchen cabinets, water heater, TV mount) | Through-bolt to steel L-angle web | 50–100 kg per anchor |
| Very heavy items (bookshelf, full pantry) | Multiple through-bolts to L-angle + distribution plate | 200+ kg per mounting point |

**Tip:** The L-angle frame runs along the panel perimeter at a known position (flush with the panel face, web extending inward). A stud-finder or magnet locates the vertical posts easily. Through-bolting to the angle web provides reliable, high-capacity anchorage comparable to steel stud framing.

### Summary — Conservative Capacity in kg per Panel

For builders and non-engineers, here are the same numbers expressed in kilograms. These are **very conservative working loads** (already divided by safety factors of 2–3). Actual failure loads are 2–3× higher.

| Load type | Direction | Conservative working capacity | What this means in practice |
|-----------|-----------|-------------------------------|---------------------------|
| **Racking (seismic/wind)** | Horizontal, in the wall plane | **~1,200–1,500 kg per panel** | A typical single-story house needs ~600 kg of racking resistance per meter of wall — one panel provides 2× that. |
| **Out-of-plane (wind pressure)** | Perpendicular to wall face | **~90 kg spread over the panel face** | Equivalent to ~36 kg/m² uniform pressure. A person leaning hard against the wall (~80 kg on ~0.3 m²) is well within capacity. |
| **Axial (vertical)** | Downward, through the panel | **Far exceeds residential loads** | The two side L-angle posts alone carry many times a typical roof + upper floor per meter of wall. Panels can carry a second story and roof without a separate steel building frame. Exact capacity to be validated through testing. |
| **Point load to mortar** | Pull-out / shear at anchor | **~15–25 kg per anchor** | A shelf bracket with 2 anchors holds 30–50 kg safely. |
| **Point load to L-angle** | Through-bolt | **~50–100 kg per bolt** | A kitchen cabinet with 4 through-bolts holds 200–400 kg safely. |

> **Important:** These are estimates, not tested values. They will be validated through physical testing. Do not use for structural engineering without independent verification. When in doubt, attach heavy items to the steel building frame, not to the panel.

## Durability (80–100 Year Design Life)

| Component | Degradation mechanism | Prevention | Expected life |
|-----------|----------------------|-----------|---------------|
| Steel frame | Corrosion | Hot-dip galvanizing (85 μm+) | 80–100 years (non-coastal) |
| Bamboo strips | Insect attack, fungal decay | Borate treatment + mortar encasement (alkaline, anaerobic) | 80+ years |
| Mortar | Carbonation, weathering | Protected by lime plaster (sacrificial layer) | 100+ years |
| Lime plaster | Surface erosion, micro-cracking | Self-healing (carbonation fills cracks), renewable lime wash | Indefinite with maintenance |
| Lime wash | UV degradation, rain erosion | Reapply every 5–10 years | 5–10 years per coat |
| Electrical | Insulation degradation | PVC conduit allows cable replacement without opening wall | Cables: 30–50 years, replaceable |
| HDPE blocks | None significant | UV-protected (inside wall) | 100+ years |

### Maintenance Schedule

| Interval | Action | Estimated cost |
|----------|--------|---------------|
| Every 5–10 years | Lime wash renewal | $50–100 per building |
| Every 15–20 years | Inspect lime plaster, patch cracks | $100–300 per building |
| Every 30–40 years | Inspect electrical, replace cables if needed | $200–500 per building |
| At 40 years | Inspect steel frame at accessible points (spot re-galvanize if needed) | $200–400 |
| **Lifetime total** | | **$1,400–2,000** |

## Testing Needed

**All load capacity values above are analytical estimates.** They will be validated through physical testing as part of this project's development. The first panels will be built and tested before any building is occupied.

Planned testing program:

- [ ] **Racking shear tests** (ASTM E564 or equivalent) — panels with and without diagonals, to validate the 3–5× improvement estimate
- [ ] **Out-of-plane load tests** — uniform pressure and point impact, to validate the )( profile benefit
- [ ] **Fire resistance tests** (ASTM E119 or equivalent) — time to structural failure
- [ ] **Cyclic seismic tests** — full-scale shake table or quasi-static cyclic loading, to verify ductile failure mode
- [ ] **Connection tests** — panel-to-column bolt tab capacity, snap connector durability
- [ ] **Long-term weathering tests** — accelerated aging of mortar-encased bamboo samples
- [ ] **Acoustic transmission tests** (ASTM E90) — STC measurement
- [ ] **Point load pull-out tests** — masonry anchor and through-bolt capacity in mortar + L-angle frame

Test results will be published in this repository as they become available. If you have access to testing facilities and want to contribute, please get in touch — collaborative testing across different bamboo species and mortar mixes will make this system stronger for everyone.
