# SVG Regeneration — Status & Pending Tasks

The bahareque-modular documentation has shifted from a **T 60×60×7 mm T-bar** panel frame to an **L 40×40×4 mm equal-leg angle** panel frame. The text has been updated across all English chapters (see `en/02-panel-anatomy.md`, `en/03-materials.md`, `en/04-construction-process.md`, `en/05-structural-performance.md`, `en/10-environmental-impact.md`, `en/11-transport-handling.md`, `en/14-acoustic-upgrade.md`). The SVG diagrams have **not** been updated yet.

> **Chapter 07 (building integration) temporarily removed.** The panel-to-connector / ring-beam interface needs a full structural re-resolution for the L-angle panel side (the connector ring beam profile choice itself is open). The chapter has been moved out of the published docs to `../bahareque-modular-inprogress/` (sibling of this repo, not pushed to GitHub) until that decision is settled and the body text + SVGs can be revised together. The four SVGs that were chapter-07-only (`08-building-integration`, `14-floor-connection-detail`, `15-corner-piece-detail`, `16-foundation-channel`) are no longer referenced from any published chapter.

This file tracks which SVGs are **currently linked** in the documentation (representative of the L-angle spec or structurally neutral enough to reuse), and which are **pending regeneration** (still show T-bar geometry and have been unlinked from the docs pending revision).

## SVGs currently linked in docs (representative for L-angle spec)

These nine SVGs are retained in the documentation because they either do not show the panel frame profile specifically, or they show geometric elements that remain valid under the L-angle spec:

| File | Used in chapter | Notes |
|---|---|---|
| `svg/01-panel-exploded.svg` | 02-panel-anatomy | Exploded view — to be regenerated with L-angle frame in a future revision; retained provisionally |
| `svg/05-diagonal-bracing.svg` | (referenced conceptually in 02 and 05) | Diagonal bracing geometry — independent of frame profile choice |
| `svg/06-mortar-pour.svg` | 04-construction-process | Mortar pour process — independent of frame profile |
| `svg/07-assembly-sequence.svg` | 04-construction-process | High-level assembly sequence — retained provisionally pending L-angle regeneration |
| `svg/08-building-integration.svg` | 07-building-integration | Building-level integration diagram — largely independent of panel-frame detail |
| `svg/09-profile.svg` | 02-panel-anatomy, 05-structural-performance | Panel side profile (the )( profile) — geometry stays the same with L-angle |
| `svg/10-panel-face-view.svg` | 02-panel-anatomy | Panel face view — face layout independent of frame profile |
| `svg/12-floor-panel-side.svg` | 16-floor-panel-concept | Floor panel side view — separate element from wall panels |
| `svg/13-floor-panel-top.svg` | 16-floor-panel-concept | Floor panel top view — separate element |

## SVGs unlinked from docs (pending L-angle regeneration)

These SVGs show T-bar-specific geometry and have been **unlinked from the English chapters** until regenerated for the L 40×40×4 angle frame. The files themselves remain in `svg/` for reference but are no longer rendered into the published documentation:

| File | Was linked in | Issue | Pending action |
|---|---|---|---|
| `svg/02-tbar-profile.svg` | 02-panel-anatomy | Shows T 60×60×7 cross-section | **Regenerate as L 40×40×4 angle profile** |
| `svg/03-panel-cross-section.svg` | 02-panel-anatomy | Shows T-bar web in center of panel cross-section | **Regenerate with L-angle frame asymmetric about panel centerline** |
| `svg/04-screw-clamping.svg` | 04-construction-process | Shows clamping strip screwing through T-bar web | **Regenerate with clamping strip screwing through L-angle vertical web** |
| `svg/15-corner-piece-detail.svg` | 07-building-integration | Shows T-bar corner piece geometry | **Regenerate for L-angle corner detail** |
| `svg/16-foundation-channel.svg` | 07-building-integration | Shows T-bar bottom engaging foundation brick channel | **Regenerate for L-angle foundation interface** |
| `svg/17-wall-panel-frame.svg` | 04-construction-process | Shows rectangular T-bar frame | **Regenerate for L-angle rectangular frame** |
| `svg/14-floor-connection-detail.svg` | 07-building-integration | Shows T-bar panel connecting to T-bar ring beam / floor connector | **Regenerate with L-angle panel side + T 60×60 ring beam (ring beam T-bar is unchanged; panel-side interface geometry changes)** |
| `svg/11-combined-profile-face.svg` | (not currently linked) | Shows T-bar + panel face combined | **Regenerate or retire** |
| `svg/panel-2500mm.svg` | (not currently linked) | T-bar based | **Regenerate or retire** |
| `svg/panel-T60-150mm.svg` | (not currently linked) | T-bar based | **Regenerate or retire** |
| `svg/panel-T150-200mm.svg` | (not currently linked) | T-bar based | **Regenerate or retire** |
| `svg/panel-universal-cross-section.svg` | (not currently linked) | T-bar based | **Regenerate or retire** |

## Tasks — pending

1. **Regenerate core cross-section SVGs** for L 40×40×4 frame: `02-tbar-profile.svg` (rename to `02-angle-profile.svg`), `03-panel-cross-section.svg`, `17-wall-panel-frame.svg`
2. **Regenerate interface detail SVGs**: `04-screw-clamping.svg`, `15-corner-piece-detail.svg`, `16-foundation-channel.svg`, `14-floor-connection-detail.svg`
3. **Review & regenerate assembly / exploded SVGs** for L-angle: `01-panel-exploded.svg`, `07-assembly-sequence.svg`
4. **Retire or update** the panel size/thickness variant SVGs (`panel-2500mm.svg`, `panel-T60-150mm.svg`, `panel-T150-200mm.svg`, `panel-universal-cross-section.svg`, `11-combined-profile-face.svg`)
5. **Re-link updated SVGs** in the chapters once regenerated, replacing the inline `> _… pending …_` notes
6. **Cascade SVG updates to language translations** (`de/svg/`, `es/svg/`, `fr/svg/`, `it/svg/`, `pt/svg/`) — each language folder has its own `svg/` subfolder that mirrors the English set
7. **Regenerate PDFs** (`BaharequeModular-*.pdf`) via `generate_pdfs.py` after all text + SVG updates are complete

## Translations

The English chapters have been updated to reflect the L-angle spec and corrected weight figures. **The 5 translation folders (de, es, fr, it, pt) have NOT been updated** — they still reflect the T-bar spec and the old weight figures (155 kg total). When the English text is finalized, the translations need to be cascaded with the same changes, and the language-specific `svg/` folders need to sync with the regenerated English diagrams.

## Source of truth

If a diagram and the text disagree, **the text is the source of truth** until SVG regeneration catches up. The L 40×40×4 spec is definitive; any SVG still showing T-bar geometry is out of date and should not be used for fabrication or structural reference.
