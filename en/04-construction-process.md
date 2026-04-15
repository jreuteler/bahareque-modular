# Construction Process

> **SVG update pending**: some diagrams in this chapter were generated for the previous T-bar frame spec and have been temporarily unlinked until regenerated for the current **L 40×40×4 mm angle** spec. See [`SVG-STATUS.md`](../SVG-STATUS.md) at the repo root.

## Workshop Setup

All panels are built in a covered workshop — weather-independent, quality-controlled, assembly-line efficient. Minimum workshop requirements:

- Covered area: ~6 × 4 m (roof, open sides acceptable)
- Welding station (frame fabrication only)
- Drill press or hand drill
- 2× vibration tables (~1.2 × 2.7 m each) for workshop-pour production model, **or** formwork + in-situ mortar pump for the preferred in-situ pour model (see [Panel Anatomy § Weight Breakdown](02-panel-anatomy.md))
- Sand supply for bed
- Mortar mixer (electric or hand)
- Basic hand tools: screwdrivers, wire cutters, pliers, staple gun

![Assembly Sequence](../svg/07-assembly-sequence.svg)

## Production Steps

### Step 1: Frame Fabrication

> _Wall-panel-frame diagram pending — the previous frame SVG shows T-bar geometry and is not representative of the L-angle frame. See `SVG-STATUS.md`._

1. Cut L 40×40×4 angle to length: 2× 1.0 m (top/bottom) + 2× 2.5 m (sides). Commodity stock from Gerdau Diaco / Acesco / Ferrasa, 6 m sticks
2. Mitre-cut the corners at 45° (or straight-cut with one leg lapped over the other — either produces a clean rectangular frame)
3. Weld corners in a jig — all frames identical. Optional small corner gussets (60×60×3 plate) can be welded across each inside corner for rigidity during handling
4. Drill clamping holes every ~70 mm along the top and bottom angle webs (one per two bamboo strips, ~14 holes per bar, ~28 total)
5. Hot-dip galvanize the completed frame (batch process — send 20–50 frames at once)

**All frames are identical regardless of panel variant.** The jig ensures consistent dimensions. One jig, one frame, forever.

### Step 2: HDPE Blocks

1. Cut HDPE stock to 30 × 30 mm × 1,000 mm (2 per panel)
2. Cut corner notches: 10 × 10 mm at each end (4 notches per block, 8 per panel)
3. Mount blocks on top and bottom angle webs using screws or adhesive

### Step 3: Electrical

1. Route 12V cable through PVC conduit
2. Route 120V cable through separate PVC conduit
3. Mount E10 sockets (3 near top, each side)
4. For Type O/S: mount outlet box, wire pigtail to main cable
5. For Type S: mount switch box at 120 cm height
6. For Type W: mount water risers (CPVC/PEX supply, PVC drain) with capped stub-outs
7. Attach snap connectors at both vertical edges (2-pin for 12V, 3-pin for 120V)

### Step 4: Bamboo Strips (Side 1)

1. Place panel frame flat on work table, side 1 up
2. Lay vertical bamboo strips against the web, between the HDPE blocks
3. Leave ~20 mm gaps between strips for mortar penetration
4. Place PVC conduit with cables between strips, against web
5. Thread diagonal strip through bottom-left HDPE notch, across to top-right notch (at web level)
6. Pre-tension diagonal and secure at both ends

> _Screw-clamping diagram pending — the previous clamping SVG shows T-bar web geometry; the L-angle clamping detail is similar in principle (clamping strip → bamboo → screw through web) but geometrically different. See `SVG-STATUS.md`._

### Step 5: Screw-Clamping (Side 1)

1. Place steel clamping strip (flat bar, 3 mm × 40 mm × 1,000 mm) over the bamboo strips at the top angle web
2. Align holes in clamping strip with holes in the L-angle web
3. Drive stainless steel screws through: clamping strip → bamboo strips → web holes
4. The clamping strip flexes to accommodate natural thickness variation — self-adjusting
5. Repeat at bottom angle
6. Wire-tie diagonal to each vertical strip at crossings (~8–10 ties)

**Time: ~5 minutes per side for clamping, ~3 minutes for wire ties**

### Step 6: Flip and Repeat (Side 2)

1. Flip panel
2. Repeat steps 4–5 on the other side
3. Diagonal on side 2 runs from top-left to bottom-right (opposing the side 1 diagonal — together they form an X)

### Step 7: Mesh

1. Lay chicken wire over side 1, extending 20 mm past frame edges (for overlap with adjacent panels)
2. Staple or wire-tie to frame and bamboo strips
3. If using aluminum insect mesh: place under chicken wire
4. Flip and repeat on side 2

### Step 8: Mortar Pour

![Mortar Pour Process](../svg/06-mortar-pour.svg)

This is the key innovation in application method:

1. **Prepare vibration table:** Level surface, motor mounted underneath
2. **Spread sand bed:** ~30 mm of clean dry sand on the table surface. The sand conforms to any panel face irregularities and prevents mortar adhesion to the table.
3. **Place panel face-down** on the sand bed (chicken wire side touching sand)
4. **Mix mortar:** 1:4 cement:sand + PP fiber + pozzolanic admixture, W/C ~0.45–0.50 (pourable but not liquid)
5. **Pour mortar** over the exposed back of the panel, filling between strips and covering the mesh
6. **Start vibration:** Run table for 30–60 seconds. The vibration:
   - Drives mortar through the gaps between strips
   - Fills the center cavity completely
   - Eliminates voids and air pockets
   - Mortar penetrates to the front face mesh (now resting on sand)
7. **Screed** excess mortar level with the frame edges
8. **Trowel** smooth (this becomes the interior face)

> **Vibration table build guide:** A DIY vibration table design (motor, platform, springs) will be published in this repository once the design has been tested and proven safe in practice. Until then, any flat platform with a concrete vibrator clamped to the edge will work for initial experiments.

**Why vibration table on sand bed?**
- Gravity + vibration = complete fill, no voids
- Sand bed = no mold needed, sand conforms to panel shape
- No spraying equipment needed (cheaper than spray mortar)
- One-sided pour fills both sides — mortar flows through strip gaps
- Consistent quality — vibration eliminates human error

### Step 9: Curing

1. Cover panel with plastic sheet to retain moisture
2. Keep moist for minimum 7 days (mist spray or damp burlap)
3. Full strength at 28 days
4. Panels can be stacked vertically (edge-on) after 7 days to save space
5. Mark each panel with variant type and production date

**Production rate: 3–4 panels per day** with 2 vibration tables running in parallel, team of 4–6 people. Active work per panel: ~15–20 minutes. Passive curing: 7–28 days (panels cure while new ones are produced).

### Step 10: Transport and Installation

1. Transport panels to building site using simple A-frame cart or truck
2. Bolt panels into steel building frame at column positions (pre-welded bolt tabs on columns)
3. Adjacent panels touch mortar-to-mortar
4. Snap-connect electrical between adjacent panels (12V + 120V)
5. Test circuits before finishing

### Step 11: On-Site Finishing

1. Fill any joints between panels with mortar
2. Apply chicken wire mesh over joints (if not already overlapping from panel edges)
3. Apply lime plaster: 3–5 mm, hand-troweled, both faces
4. Allow to cure (keep moist for 3–5 days)
5. Apply lime wash: 2–3 thin coats with brush

The finished wall is seamless — no visible joints, no visible steel, no visible screws. Just smooth lime plaster with the texture of a hand-made wall.

### Step 12: Bathroom Waterproofing

Bathroom and shower zones require waterproof treatment instead of lime plaster:

1. **Shower walls:** apply liquid waterproof membrane (Sika-1 or similar) directly to the mortar panel face — 2 coats, brush-on. Then flexible tile adhesive + ceramic/porcelain tiles. **No lime plaster in the shower zone.**
2. **Bathroom floor (entire):** waterproof membrane on the slab surface + ceramic tiles. The slab must have a 2% fall toward the floor drain (formed during the slab pour).
3. **Bathroom walls outside shower:** lime plaster is acceptable, or tiles for easy cleaning.
4. **Ceiling (under mezzanine):** lime plaster — not directly sprayed.

The mortar panel surface provides excellent adhesion for the liquid membrane — no additional prep needed. Just clean the panel face and apply.

### Drainage (planned in the slab)

All drainage must be installed BEFORE the foundation slab is poured:

- **Toilet drain:** 4" (100mm) PVC pipe to septic tank. Position is fixed — cannot be moved later.
- **Shower floor drain:** 2" (50mm) PVC with trap. Slab recessed ~20mm in shower area to contain water.
- **Sink drains:** 1.5" (40mm) PVC with trap. Kitchen sink through the slab; bathroom sink through the W-type water panel or slab.
- **Cleanout:** accessible fitting outside the building on the drain line.

The W-type panel provides supply risers (hot/cold CPVC). Drainage is always in the slab — gravity drainage needs slope that panels cannot provide.

## Quality Checklist

- [ ] Frame dimensions within ±2 mm
- [ ] All clamping holes drilled and aligned
- [ ] Bamboo strips borate-treated (green/blue tint visible)
- [ ] Diagonal pre-tensioned (should ring when tapped)
- [ ] All wire ties tight
- [ ] Electrical circuits tested before mortar (12V and 120V)
- [ ] Mortar consistency correct (slump test)
- [ ] Vibration run for full 30–60 seconds
- [ ] No visible voids on pour face after vibration
- [ ] Panel marked with type and date
- [ ] Cured minimum 7 days before handling
