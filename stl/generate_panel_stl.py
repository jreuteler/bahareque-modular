"""Generate STL files for the bahareque panel 3D print model.
Designed for Creality Ender 3 (220x220x250mm bed).
Max print length: 200mm (reserve for bed clips/adhesion).
Scale: 6.44% (total height 3106mm → 200mm).

Frame geometry (April 2026 unified panel):
  - Side T-bars: vertical, flange OUTWARD, web INWARD, flush top/bottom
  - Short T-bars: horizontal, flange inside panel, web protrudes OUTWARD
    (top web UP, bottom web DOWN). Width = panel width (1000mm), no wider.
  - Bolt holes: 4 per protrusion (2 pairs near side edges), horizontally spaced

Thin parts are thickened for FDM printability (min ~0.8mm walls).
Proportions are representative, not exact engineering scale.

Two frame halves — print flat, glue back-to-back with components sandwiched:
  01a_frame_front.stl         → Black (front half of steel frame)
  01b_frame_rear.stl          → Black (rear half of steel frame)
  02a_hdpe_front.stl          → Blue (front HDPE blocks)
  02b_hdpe_rear.stl           → Blue (rear HDPE blocks)
  03a_guadua_vert_front.stl   → Beige/Tan (front vertical strips)
  03b_guadua_vert_rear.stl    → Beige/Tan (rear vertical strips)
  04_guadua_diagonal_front.stl → Brown (front diagonal brace)
  05_guadua_diagonal_rear.stl  → Brown (rear diagonal brace)
  06a_clamps_front.stl        → Silver/Grey (front V-clamp strips)
  06b_clamps_rear.stl         → Silver/Grey (rear V-clamp strips)
  07_conduit.stl              → White (PVC conduit)
  08_cable_12v.stl            → Red (12V cable)
  09_cable_120v.stl           → Yellow (120V cable)
"""

import struct
import math
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Real dimensions (mm)
PANEL_W = 1000
PANEL_H = 3000
WALL_THICK = 86  # finished wall thickness: 60mm frame + 2×13mm mortar+lime
FLANGE = 60        # flange width
FLANGE_T = 7       # flange thickness
WEB_H = 53         # web height (protrusion height)
WEB_T = 7          # web thickness

# Total real height including top/bottom web protrusions
TOTAL_H = PANEL_H + 2 * WEB_H  # 3106mm

# Scale: fit 200mm max print length
MAX_PRINT = 200.0
SCALE = MAX_PRINT / TOTAL_H  # ~0.0644

# Print dimensions
PW = PANEL_W * SCALE          # ~64.4mm
PH = PANEL_H * SCALE          # ~193.1mm
PD = WALL_THICK * SCALE       # ~5.5mm
PROT_H = WEB_H * SCALE        # ~3.4mm (web protrusion height, scaled OK)

# Printable overrides (thickened where scaled value < FDM minimum)
P_FLANGE_W = FLANGE * SCALE           # ~3.9mm — OK
P_FLANGE_T = max(FLANGE_T * SCALE, 1.2)  # 0.45→1.2mm
P_WEB_H = max(WEB_H * SCALE, 2.5)    # 3.4mm — OK, but ensure visible
P_WEB_T = max(WEB_T * SCALE, 1.2)    # 0.45→1.2mm

# HDPE blocks
BLOCK_H = max(30 * SCALE, 2.0)   # ~1.9→2.0mm
BLOCK_D = max(30 * SCALE, 2.0)   # ~1.9→2.0mm

# Guadua vertical strips
GV_W = max(20 * SCALE, 1.2)      # ~1.3mm
GV_T = 1.0                        # thickened for handling
GV_GAP = max(20 * SCALE, 1.0)    # ~1.3mm

# Guadua diagonal braces (60x20mm real)
GD_W = max(60 * SCALE, 3.0)      # ~3.9mm
GD_T = max(20 * SCALE, 1.5)      # ~1.3→1.5mm

# Clamping strip
CL_W = max(20 * SCALE, 1.5)
CL_T = 0.8                        # thickened from 0.2mm

# Bolt holes (M12, 14mm hole)
BOLT_HOLE_R = max(14 * SCALE / 2, 0.5)  # ~0.45→0.5mm radius
BOLT_EDGE = 18 * SCALE                   # ~1.16mm from side edge
BOLT_SPACING = 36 * SCALE                # ~2.32mm between pair

# Conduit
COND_R = 1.0

# Cable
CABLE_R_12V = 0.6
CABLE_R_120V = 0.6


def write_binary_stl(filename, triangles, name="object"):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'wb') as f:
        header = name.encode('ascii')[:80].ljust(80, b'\0')
        f.write(header)
        f.write(struct.pack('<I', len(triangles)))
        for (v1, v2, v3), normal in triangles:
            f.write(struct.pack('<fff', *normal))
            f.write(struct.pack('<fff', *v1))
            f.write(struct.pack('<fff', *v2))
            f.write(struct.pack('<fff', *v3))
            f.write(struct.pack('<H', 0))
    print(f"  {filename}: {len(triangles)} tris, {os.path.getsize(filepath)} bytes")


def box(x, y, z, w, h, d):
    """12 triangles for axis-aligned box. (x,y,z)=min corner, (w,h,d)=size."""
    if w <= 0 or h <= 0 or d <= 0:
        return []
    x2, y2, z2 = x+w, y+h, z+d
    v = [(x,y,z),(x2,y,z),(x2,y2,z),(x,y2,z),
         (x,y,z2),(x2,y,z2),(x2,y2,z2),(x,y2,z2)]
    return [
        ((v[0],v[2],v[1]),(0,0,-1)), ((v[0],v[3],v[2]),(0,0,-1)),
        ((v[4],v[5],v[6]),(0,0,1)),  ((v[4],v[6],v[7]),(0,0,1)),
        ((v[0],v[1],v[5]),(0,-1,0)), ((v[0],v[5],v[4]),(0,-1,0)),
        ((v[2],v[3],v[7]),(0,1,0)),  ((v[2],v[7],v[6]),(0,1,0)),
        ((v[0],v[4],v[7]),(-1,0,0)), ((v[0],v[7],v[3]),(-1,0,0)),
        ((v[1],v[2],v[6]),(1,0,0)),  ((v[1],v[6],v[5]),(1,0,0)),
    ]


def rotated_box(x1, y1, x2, y2, z, width, thickness):
    """Box rotated along the line from (x1,y1) to (x2,y2) at height z."""
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return []
    ux, uy = dx/length, dy/length
    nx, ny = -uy, ux
    hw = width / 2

    v = [
        (x1 - hw*nx, y1 - hw*ny, z),
        (x1 + hw*nx, y1 + hw*ny, z),
        (x2 + hw*nx, y2 + hw*ny, z),
        (x2 - hw*nx, y2 - hw*ny, z),
        (x1 - hw*nx, y1 - hw*ny, z+thickness),
        (x1 + hw*nx, y1 + hw*ny, z+thickness),
        (x2 + hw*nx, y2 + hw*ny, z+thickness),
        (x2 - hw*nx, y2 - hw*ny, z+thickness),
    ]

    nz_down = (0, 0, -1)
    nz_up = (0, 0, 1)
    n_left = (-nx, -ny, 0)
    n_right = (nx, ny, 0)
    n_start = (-ux, -uy, 0)
    n_end = (ux, uy, 0)

    return [
        ((v[0], v[2], v[1]), nz_down), ((v[0], v[3], v[2]), nz_down),
        ((v[4], v[5], v[6]), nz_up), ((v[4], v[6], v[7]), nz_up),
        ((v[0], v[4], v[7]), n_left), ((v[0], v[7], v[3]), n_left),
        ((v[1], v[2], v[6]), n_right), ((v[1], v[6], v[5]), n_right),
        ((v[0], v[1], v[5]), n_start), ((v[0], v[5], v[4]), n_start),
        ((v[3], v[7], v[6]), n_end), ((v[3], v[6], v[2]), n_end),
    ]


def cylinder_z(cx, cy, z, radius, height, segments=12):
    """Cylinder along Z axis centered at (cx,cy), from z to z+height."""
    tris = []
    for i in range(segments):
        a1 = 2*math.pi*i/segments
        a2 = 2*math.pi*(i+1)/segments
        c1, s1 = math.cos(a1), math.sin(a1)
        c2, s2 = math.cos(a2), math.sin(a2)

        p1b = (cx+radius*c1, cy+radius*s1, z)
        p2b = (cx+radius*c2, cy+radius*s2, z)
        p1t = (cx+radius*c1, cy+radius*s1, z+height)
        p2t = (cx+radius*c2, cy+radius*s2, z+height)
        cb = (cx, cy, z)
        ct = (cx, cy, z+height)

        nm = ((c1+c2)/2, (s1+s2)/2, 0)
        tris += [
            ((p1b, p2b, p2t), nm), ((p1b, p2t, p1t), nm),
            ((cb, p2b, p1b), (0,0,-1)), ((ct, p1t, p2t), (0,0,1)),
        ]
    return tris


def cylinder_y(cx, z, y_start, radius, height, segments=12):
    """Cylinder along Y axis at (cx, z), from y_start to y_start+height."""
    tris = []
    for i in range(segments):
        a1 = 2*math.pi*i/segments
        a2 = 2*math.pi*(i+1)/segments
        c1, s1 = math.cos(a1), math.sin(a1)
        c2, s2 = math.cos(a2), math.sin(a2)

        p1b = (cx+radius*c1, y_start, z+radius*s1)
        p2b = (cx+radius*c2, y_start, z+radius*s2)
        p1t = (cx+radius*c1, y_start+height, z+radius*s1)
        p2t = (cx+radius*c2, y_start+height, z+radius*s2)
        cb = (cx, y_start, z)
        ct = (cx, y_start+height, z)

        nm = ((c1+c2)/2, 0, (s1+s2)/2)
        tris += [
            ((p1b, p2b, p2t), nm), ((p1b, p2t, p1t), nm),
            ((cb, p2b, p1b), (0,-1,0)), ((ct, p1t, p2t), (0,1,0)),
        ]
    return tris


# ============================================================
# Y-axis layout (print coordinate system):
#   y=0                          : bottom web protrusion base
#   y=P_WEB_H                   : bottom flange bottom
#   y=P_WEB_H + P_FLANGE_T      : bottom flange top (panel interior starts)
#   y=P_WEB_H + P_FLANGE_T + PH : top flange bottom (panel interior ends)
#                       ... + P_FLANGE_T : top flange top
#                       ... + P_WEB_H    : top web protrusion top = 200mm
# ============================================================

# Y offsets for clarity
Y_BOT_WEB = 0
Y_BOT_FLANGE = P_WEB_H
Y_PANEL_BOT = P_WEB_H + P_FLANGE_T
Y_PANEL_TOP = Y_PANEL_BOT + PH - 2 * P_FLANGE_T  # inner panel height
Y_TOP_FLANGE = Y_PANEL_BOT + PH - 2 * P_FLANGE_T
Y_TOP_WEB = Y_TOP_FLANGE + P_FLANGE_T

# Recalc: panel interior from Y_PANEL_BOT to Y_PANEL_TOP
# Actually let's be precise:
# Bottom web:    y = 0 to P_WEB_H
# Bottom flange: y = P_WEB_H to P_WEB_H + P_FLANGE_T
# Panel inside:  y = P_WEB_H + P_FLANGE_T to P_WEB_H + P_FLANGE_T + (PH - 2*P_FLANGE_T)
# Top flange:    y = P_WEB_H + PH - P_FLANGE_T to P_WEB_H + PH
# Top web:       y = P_WEB_H + PH to P_WEB_H + PH + P_WEB_H

Y_BOT_WEB_START = 0
Y_BOT_WEB_END = P_WEB_H
Y_BOT_FL_START = P_WEB_H
Y_BOT_FL_END = P_WEB_H + P_FLANGE_T
Y_INNER_START = Y_BOT_FL_END
Y_INNER_END = P_WEB_H + PH - P_FLANGE_T
Y_TOP_FL_START = Y_INNER_END
Y_TOP_FL_END = P_WEB_H + PH
Y_TOP_WEB_START = Y_TOP_FL_END
Y_TOP_WEB_END = Y_TOP_WEB_START + P_WEB_H
INNER_H = Y_INNER_END - Y_INNER_START

# Z center
ZC = PD / 2
FLANGE_Z = ZC - P_FLANGE_W / 2  # flange centered on wall depth


def gen_frame():
    """Generate frame as two halves split at the web centerline.
    Each half prints flat (face down), no supports needed.
    Glue back-to-back with components sandwiched between.
    """
    wc = ZC - P_WEB_T / 2  # web z-start (centered)
    side_web_len = min(P_WEB_H, PD/2 - P_WEB_T/2)

    # Bolt hole positions
    bolt_xs = [BOLT_EDGE, BOLT_EDGE + BOLT_SPACING,
               PW - BOLT_EDGE - BOLT_SPACING, PW - BOLT_EDGE]

    # --- FRONT HALF (z = 0 to ZC) ---
    # Prints face-down on bed. Flat bottom = clean exterior face.
    tf = []

    # Left side T-bar: flange (exterior face) + web to centerline
    tf += box(-P_FLANGE_T, Y_BOT_FL_START, FLANGE_Z, P_FLANGE_T, PH, P_FLANGE_W / 2)
    tf += box(0, Y_BOT_FL_START, wc, side_web_len, PH, P_WEB_T / 2)

    # Right side T-bar: flange + web to centerline
    tf += box(PW, Y_BOT_FL_START, FLANGE_Z, P_FLANGE_T, PH, P_FLANGE_W / 2)
    tf += box(PW - side_web_len, Y_BOT_FL_START, wc, side_web_len, PH, P_WEB_T / 2)

    # Bottom short T-bar: flange (front half) + web (front half)
    tf += box(0, Y_BOT_FL_START, FLANGE_Z, PW, P_FLANGE_T, P_FLANGE_W / 2)
    tf += box(0, Y_BOT_WEB_START, wc, PW, P_WEB_H, P_WEB_T / 2)

    # Top short T-bar: flange (front half) + web (front half)
    tf += box(0, Y_TOP_FL_START, FLANGE_Z, PW, P_FLANGE_T, P_FLANGE_W / 2)
    tf += box(0, Y_TOP_WEB_START, wc, PW, P_WEB_H, P_WEB_T / 2)

    # Bolt hole marks (front face of web protrusions)
    for bx in bolt_xs:
        by_bot = Y_BOT_WEB_START + P_WEB_H / 2
        tf += cylinder_z(bx, by_bot, wc - 0.3, BOLT_HOLE_R, P_WEB_T / 2 + 0.3, segments=8)
        by_top = Y_TOP_WEB_START + P_WEB_H / 2
        tf += cylinder_z(bx, by_top, wc - 0.3, BOLT_HOLE_R, P_WEB_T / 2 + 0.3, segments=8)

    write_binary_stl("01a_frame_front.stl", tf, "frame_front")

    # --- REAR HALF (z = ZC to PD) ---
    # Mirror of front half, shifted to rear
    tr = []
    rear_fl_z = ZC  # flanges from center to back

    # Left side T-bar
    tr += box(-P_FLANGE_T, Y_BOT_FL_START, ZC, P_FLANGE_T, PH, P_FLANGE_W / 2)
    tr += box(0, Y_BOT_FL_START, ZC, side_web_len, PH, P_WEB_T / 2)

    # Right side T-bar
    tr += box(PW, Y_BOT_FL_START, ZC, P_FLANGE_T, PH, P_FLANGE_W / 2)
    tr += box(PW - side_web_len, Y_BOT_FL_START, ZC, side_web_len, PH, P_WEB_T / 2)

    # Bottom short T-bar
    tr += box(0, Y_BOT_FL_START, ZC, PW, P_FLANGE_T, P_FLANGE_W / 2)
    tr += box(0, Y_BOT_WEB_START, ZC, PW, P_WEB_H, P_WEB_T / 2)

    # Top short T-bar
    tr += box(0, Y_TOP_FL_START, ZC, PW, P_FLANGE_T, P_FLANGE_W / 2)
    tr += box(0, Y_TOP_WEB_START, ZC, PW, P_WEB_H, P_WEB_T / 2)

    # Bolt hole marks (rear face)
    for bx in bolt_xs:
        by_bot = Y_BOT_WEB_START + P_WEB_H / 2
        tr += cylinder_z(bx, by_bot, ZC, BOLT_HOLE_R, P_WEB_T / 2 + 0.3, segments=8)
        by_top = Y_TOP_WEB_START + P_WEB_H / 2
        tr += cylinder_z(bx, by_top, ZC, BOLT_HOLE_R, P_WEB_T / 2 + 0.3, segments=8)

    write_binary_stl("01b_frame_rear.stl", tr, "frame_rear")


def gen_hdpe():
    """HDPE blocks — front side only (glue into front frame half).
    Rear side blocks are mirrored and glue into rear half.
    """
    wc = ZC - P_WEB_T / 2
    bx = side_web_x()
    bw = PW - 2 * bx

    # Front blocks (exterior side, z < center)
    tf = []
    by = Y_INNER_START + 0.3
    by2 = Y_INNER_END - BLOCK_H - 0.3
    tf += box(bx, by, wc - BLOCK_D, bw, BLOCK_H, BLOCK_D)
    tf += box(bx, by2, wc - BLOCK_D, bw, BLOCK_H, BLOCK_D)
    write_binary_stl("02a_hdpe_front.stl", tf, "hdpe_front")

    # Rear blocks (interior side, z > center)
    tr = []
    tr += box(bx, by, ZC + P_WEB_T / 2, bw, BLOCK_H, BLOCK_D)
    tr += box(bx, by2, ZC + P_WEB_T / 2, bw, BLOCK_H, BLOCK_D)
    write_binary_stl("02b_hdpe_rear.stl", tr, "hdpe_rear")


def side_web_x():
    """X extent of side web (how far it reaches inward)."""
    return min(P_WEB_H, PD/2 - P_WEB_T/2)


def gen_guadua_vert():
    """Vertical bamboo strips — front and rear sets."""
    wc = ZC - P_WEB_T / 2
    swx = side_web_x()
    pitch = GV_W + GV_GAP
    start_x = swx + 0.3
    start_y = Y_INNER_START + BLOCK_H + 0.8
    strip_h = INNER_H - 2 * (BLOCK_H + 0.8)

    sz_ext = wc - BLOCK_D - GV_T
    sz_int = ZC + P_WEB_T / 2 + BLOCK_D

    tf = []
    tr = []
    count = 0
    x = start_x
    while x + GV_W < PW - swx:
        tf += box(x, start_y, sz_ext, GV_W, strip_h, GV_T)
        tr += box(x, start_y, sz_int, GV_W, strip_h, GV_T)
        x += pitch
        count += 1

    print(f"  {count} vertical strips (×2 sides)")
    write_binary_stl("03a_guadua_vert_front.stl", tf, "guadua_vert_front")
    write_binary_stl("03b_guadua_vert_rear.stl", tr, "guadua_vert_rear")


def gen_diagonals():
    swx = side_web_x()
    wc = ZC - P_WEB_T / 2
    margin = 1.0

    # Inner frame corners
    x1 = swx + margin
    y1 = Y_INNER_START + margin
    x2 = PW - swx - margin
    y2 = Y_INNER_END - margin

    # Shorten for 60mm width (scaled) to stay inside corners
    inner_w = x2 - x1
    inner_h = y2 - y1
    angle = math.atan2(inner_h, inner_w)
    corner_trim = GD_W / 2 / math.sin(angle)
    diag_full = math.sqrt(inner_w**2 + inner_h**2)
    diag_len = diag_full - 2 * corner_trim

    # Adjust start/end points inward along the diagonal
    ux = (x2 - x1) / diag_full
    uy = (y2 - y1) / diag_full
    trim_dx = corner_trim * ux
    trim_dy = corner_trim * uy

    # Front diagonal: bottom-left → top-right (exterior side of web)
    dz_ext = wc - GD_T
    t1 = rotated_box(x1 + trim_dx, y1 + trim_dy,
                      x2 - trim_dx, y2 - trim_dy,
                      dz_ext, GD_W, GD_T)
    write_binary_stl("04_guadua_diagonal_front.stl", t1, "diagonal_front")

    # Rear diagonal: top-left → bottom-right (interior side of web)
    dz_int = wc + P_WEB_T
    t2 = rotated_box(x1 + trim_dx, y2 - trim_dy,
                      x2 - trim_dx, y1 + trim_dy,
                      dz_int, GD_W, GD_T)
    write_binary_stl("05_guadua_diagonal_rear.stl", t2, "diagonal_rear")


def gen_clamps():
    """Clamping strips — front and rear sets."""
    swx = side_web_x()
    wc = ZC - P_WEB_T / 2
    cx = swx + 0.3
    cw = PW - 2 * swx - 0.6

    cz_ext = wc - BLOCK_D - GV_T - CL_T
    cz_int = ZC + P_WEB_T / 2 + BLOCK_D + GV_T

    cy = Y_INNER_START + 0.5
    cy2 = Y_INNER_END - CL_W - 0.5

    tf = []
    tf += box(cx, cy, cz_ext, cw, CL_W, CL_T)
    tf += box(cx, cy2, cz_ext, cw, CL_W, CL_T)
    write_binary_stl("06a_clamps_front.stl", tf, "clamps_front")

    tr = []
    tr += box(cx, cy, cz_int, cw, CL_W, CL_T)
    tr += box(cx, cy2, cz_int, cw, CL_W, CL_T)
    write_binary_stl("06b_clamps_rear.stl", tr, "clamps_rear")


def gen_conduit():
    swx = side_web_x()
    cx = PW / 3
    cz = PD / 2
    cy = Y_INNER_START + BLOCK_H + 2
    ch = INNER_H - 2 * (BLOCK_H + 2)
    t = cylinder_y(cx, cz, cy, COND_R, ch, segments=12)
    write_binary_stl("07_conduit.stl", t, "conduit")


def gen_cables():
    cy = Y_INNER_START + BLOCK_H + 3
    ch = INNER_H - 2 * (BLOCK_H + 3)

    t1 = cylinder_y(PW * 0.25, PD * 0.3, cy, CABLE_R_12V, ch, segments=8)
    write_binary_stl("08_cable_12v.stl", t1, "cable_12v")

    t2 = cylinder_y(PW * 0.75, PD * 0.7, cy, CABLE_R_120V, ch, segments=8)
    write_binary_stl("09_cable_120v.stl", t2, "cable_120v")


if __name__ == "__main__":
    print(f"Panel model for 3D printing")
    print(f"Real: {PANEL_W}x{PANEL_H}x{WALL_THICK}mm (total height with protrusions: {TOTAL_H}mm)")
    print(f"Print: {PW:.1f}x{Y_TOP_WEB_END:.1f}x{PD:.1f}mm (scale {SCALE*100:.2f}%)")
    print(f"Max dimension: {Y_TOP_WEB_END:.1f}mm (≤200mm for Ender 3 with reserve)")
    print()
    print("Printable dimensions:")
    print(f"  Side T-bar flange: {P_FLANGE_W:.1f}mm wide x {P_FLANGE_T}mm thick")
    print(f"  Side T-bar web:    {P_WEB_T}mm thick x {side_web_x():.1f}mm deep (inward)")
    print(f"  Short T-bar web:   protrudes {P_WEB_H:.1f}mm outward (up/down)")
    print(f"  Bolt holes:        {BOLT_HOLE_R*2:.1f}mm dia, 4 per protrusion")
    print(f"  Guadua strip:      {GV_W:.1f}mm wide x {GV_T}mm thick, gap {GV_GAP:.1f}mm")
    print(f"  Diagonal brace:    {GD_W:.1f}mm wide x {GD_T}mm thick")
    print(f"  HDPE block:        {BLOCK_H:.1f}mm x {BLOCK_D:.1f}mm")
    print(f"  Clamping strip:    {CL_W:.1f}mm x {CL_T}mm")
    print()

    gen_frame()
    gen_hdpe()
    gen_guadua_vert()
    gen_diagonals()
    gen_clamps()
    gen_conduit()
    gen_cables()

    print()
    print("Print colors:")
    print("  01a/b_frame           -> Black (2 halves)")
    print("  02a/b_hdpe            -> Blue (2 halves)")
    print("  03a/b_guadua_vert     -> Beige/Tan (2 halves)")
    print("  04/05_diagonal        -> Brown (front + rear)")
    print("  06a/b_clamps          -> Silver/Grey (2 halves)")
    print("  07_conduit            -> White")
    print("  08_cable_12v          -> Red")
    print("  09_cable_120v         -> Yellow")
    print()
    print("Assembly:")
    print("  1. Print all halves flat (face down) — no supports needed")
    print("  2. Glue HDPE, strips, diagonal, clamps, conduit, cables onto front frame half")
    print("  3. Glue rear frame half on top, sandwiching components")
    print("  Bolt holes visible as cylindrical marks on top/bottom web protrusions.")
