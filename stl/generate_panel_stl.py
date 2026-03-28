"""Generate STL files for the bahareque panel 3D print model.
Designed for Creality Ender 3 (220×220×250mm bed).
Scale: 7.33% (panel fits in 73×220mm footprint).

Thin parts are thickened for FDM printability (min ~0.8mm walls).
Proportions are representative, not exact engineering scale.

Print each file in a different color, glue together:
  01_frame.stl          → Black (steel T-bar frame)
  02_hdpe_blocks.stl    → Blue (HDPE spacer blocks)
  03_guadua_verticals.stl → Beige/Tan (vertical strips)
  04_guadua_diagonal_front.stl → Brown (front diagonal brace)
  05_guadua_diagonal_rear.stl  → Brown (rear diagonal brace)
  06_clamping_strips.stl → Silver/Grey (screw-down strips)
  07_conduit.stl        → White (PVC conduit)
  08_cable_12v.stl      → Red (12V cable)
  09_cable_120v.stl     → Yellow (120V cable)
"""

import struct
import math
import os

OUTPUT_DIR = "/home/reuteler/jardin/3d-panel-model"
SCALE = 0.0733  # 7.33%

# Real dimensions (mm) — these get scaled
PANEL_W = 1000
PANEL_H = 3000
WALL_THICK = 85

# Printable dimensions (already at print scale, NOT multiplied by SCALE again)
# These override the scaled-down values to ensure printability

# T-bar frame
FRAME_FLANGE_W = 30 * SCALE     # ~2.2mm
FRAME_FLANGE_T = 1.2            # thickened from 0.22mm
FRAME_WEB_T = 1.2               # thickened
FRAME_WEB_VERT = 30 * SCALE     # ~2.2mm
FRAME_WEB_HORIZ = WALL_THICK * SCALE  # ~6.2mm (full wall thickness)

# Panel print dimensions
PW = PANEL_W * SCALE   # ~73mm
PH = PANEL_H * SCALE   # ~220mm
PD = WALL_THICK * SCALE  # ~6.2mm

# HDPE blocks
BLOCK_H = max(30 * SCALE, 2.0)   # ~2.2mm
BLOCK_D = max(30 * SCALE, 2.0)   # ~2.2mm

# Guadua strips
GV_W = max(20 * SCALE, 1.2)     # ~1.5mm
GV_T = 1.0                       # thickened for handling
GV_GAP = max(15 * SCALE, 1.0)   # ~1.1mm

# Guadua diagonal
GD_W = max(60 * SCALE, 3.0)     # ~4.4mm
GD_T = max(20 * SCALE, 1.5)     # ~1.5mm

# Clamping strip
CL_W = max(20 * SCALE, 1.5)
CL_T = 0.8                       # thickened

# Conduit
COND_R = 1.0  # 2mm diameter

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


def rotated_box(x1, y1, x2, y2, z, width, thickness, axis='z'):
    """Box rotated along the line from (x1,y1) to (x2,y2) at height z.
    Width = perpendicular to line in XY plane. Thickness = Z dimension.
    Returns triangles for a properly rotated rectangular cross-section.
    """
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return []

    # Unit vectors
    ux, uy = dx/length, dy/length  # along the line
    nx, ny = -uy, ux  # perpendicular in XY

    hw = width / 2  # half width

    # 8 corners of the rotated box
    corners = []
    for (ex, ey) in [(x1, y1), (x2, y2)]:
        for ndir in [-1, 1]:
            for zoff in [0, thickness]:
                cx = ex + ndir * hw * nx
                cy = ey + ndir * hw * ny
                cz = z + zoff
                corners.append((cx, cy, cz))

    # Order: [start-left-bottom, start-right-bottom, end-left-bottom, end-right-bottom,
    #          start-left-top, start-right-top, end-left-top, end-right-top]
    # Reorder for our box convention
    v = [
        (x1 - hw*nx, y1 - hw*ny, z),           # 0: start, left, bottom
        (x1 + hw*nx, y1 + hw*ny, z),           # 1: start, right, bottom
        (x2 + hw*nx, y2 + hw*ny, z),           # 2: end, right, bottom
        (x2 - hw*nx, y2 - hw*ny, z),           # 3: end, left, bottom
        (x1 - hw*nx, y1 - hw*ny, z+thickness), # 4: start, left, top
        (x1 + hw*nx, y1 + hw*ny, z+thickness), # 5: start, right, top
        (x2 + hw*nx, y2 + hw*ny, z+thickness), # 6: end, right, top
        (x2 - hw*nx, y2 - hw*ny, z+thickness), # 7: end, left, top
    ]

    nz_down = (0, 0, -1)
    nz_up = (0, 0, 1)
    n_left = (-nx, -ny, 0)
    n_right = (nx, ny, 0)
    n_start = (-ux, -uy, 0)
    n_end = (ux, uy, 0)

    return [
        # Bottom
        ((v[0], v[2], v[1]), nz_down), ((v[0], v[3], v[2]), nz_down),
        # Top
        ((v[4], v[5], v[6]), nz_up), ((v[4], v[6], v[7]), nz_up),
        # Left side
        ((v[0], v[4], v[7]), n_left), ((v[0], v[7], v[3]), n_left),
        # Right side
        ((v[1], v[2], v[6]), n_right), ((v[1], v[6], v[5]), n_right),
        # Start cap
        ((v[0], v[1], v[5]), n_start), ((v[0], v[5], v[4]), n_start),
        # End cap
        ((v[3], v[7], v[6]), n_end), ((v[3], v[6], v[2]), n_end),
    ]


def cylinder(x, y, z, radius, height, segments=12, axis='y'):
    """Cylinder along specified axis."""
    tris = []
    for i in range(segments):
        a1 = 2*math.pi*i/segments
        a2 = 2*math.pi*(i+1)/segments
        c1, s1 = math.cos(a1), math.sin(a1)
        c2, s2 = math.cos(a2), math.sin(a2)

        if axis == 'y':
            p1b = (x+radius*c1, y, z+radius*s1)
            p2b = (x+radius*c2, y, z+radius*s2)
            p1t = (x+radius*c1, y+height, z+radius*s1)
            p2t = (x+radius*c2, y+height, z+radius*s2)
            cb = (x, y, z)
            ct = (x, y+height, z)
            nb = (0,-1,0)
            nt = (0,1,0)
        else:
            return []

        nm = ((c1+c2)/2, 0, (s1+s2)/2)
        tris += [
            ((p1b, p2b, p2t), nm), ((p1b, p2t, p1t), nm),
            ((cb, p2b, p1b), nb), ((ct, p1t, p2t), nt),
        ]
    return tris


def gen_frame():
    t = []
    ft = FRAME_FLANGE_T
    fw = FRAME_FLANGE_W
    wt = FRAME_WEB_T
    wv = FRAME_WEB_VERT
    wh = FRAME_WEB_HORIZ
    wc = (fw - wt) / 2  # web centered on flange

    # Left vertical: flange + web
    t += box(0, 0, 0, fw, PH, ft)
    t += box(wc, 0, ft, wt, PH, max(wv - ft, 0.5))

    # Right vertical: flange + web
    rx = PW - fw
    t += box(rx, 0, 0, fw, PH, ft)
    t += box(rx + wc, 0, ft, wt, PH, max(wv - ft, 0.5))

    # Bottom horizontal: flange (along X, thin in Y) + deep web
    t += box(0, 0, 0, PW, ft, fw)
    t += box(0, 0, fw, PW, ft, max(wh - fw, 0.5))

    # Top horizontal
    ty = PH - ft
    t += box(0, ty, 0, PW, ft, fw)
    t += box(0, ty, fw, PW, ft, max(wh - fw, 0.5))

    write_binary_stl("01_frame.stl", t, "frame")


def gen_hdpe():
    t = []
    bx = fw = FRAME_FLANGE_W
    bw = PW - 2*fw
    bz = FRAME_FLANGE_T + 0.3

    # Bottom block
    by = FRAME_FLANGE_T + 0.3
    t += box(bx, by, bz, bw, BLOCK_H, BLOCK_D)

    # Top block
    by2 = PH - FRAME_FLANGE_T - BLOCK_H - 0.3
    t += box(bx, by2, bz, bw, BLOCK_H, BLOCK_D)

    write_binary_stl("02_hdpe_blocks.stl", t, "hdpe_blocks")


def gen_guadua_vert():
    t = []
    fw = FRAME_FLANGE_W
    pitch = GV_W + GV_GAP
    start_x = fw + 0.5
    start_y = FRAME_FLANGE_T + BLOCK_H + 1.0
    strip_h = PH - 2*(FRAME_FLANGE_T + BLOCK_H + 1.0)
    sz = FRAME_FLANGE_T + 0.5

    count = 0
    x = start_x
    while x + GV_W < PW - fw:
        t += box(x, start_y, sz, GV_W, strip_h, GV_T)
        x += pitch
        count += 1

    print(f"  {count} vertical strips")
    write_binary_stl("03_guadua_verticals.stl", t, "guadua_verticals")


def gen_diagonals():
    fw = FRAME_FLANGE_W
    margin = 1.0

    # Front diagonal: bottom-left to top-right
    x1 = fw + margin
    y1 = FRAME_FLANGE_T + margin
    x2 = PW - fw - margin
    y2 = PH - FRAME_FLANGE_T - margin
    dz = FRAME_FLANGE_T + 0.3

    t1 = rotated_box(x1, y1, x2, y2, dz, GD_W, GD_T)
    write_binary_stl("04_guadua_diagonal_front.stl", t1, "diagonal_front")

    # Rear diagonal: top-left to bottom-right (other side of wall)
    dz2 = PD - FRAME_FLANGE_T - GD_T - 0.3
    t2 = rotated_box(x1, y2, x2, y1, dz2, GD_W, GD_T)
    write_binary_stl("05_guadua_diagonal_rear.stl", t2, "diagonal_rear")


def gen_clamps():
    t = []
    fw = FRAME_FLANGE_W
    cx = fw + 0.3
    cw = PW - 2*fw - 0.6
    cz = FRAME_FLANGE_T + 0.2

    # Bottom clamp
    cy = FRAME_FLANGE_T + 0.5
    t += box(cx, cy, cz, cw, CL_W, CL_T)

    # Top clamp
    cy2 = PH - FRAME_FLANGE_T - CL_W - 0.5
    t += box(cx, cy2, cz, cw, CL_W, CL_T)

    write_binary_stl("06_clamping_strips.stl", t, "clamping_strips")


def gen_conduit():
    cx = PW / 3
    cz = PD / 2
    cy = FRAME_FLANGE_T + BLOCK_H + 2
    ch = PH - 2*(FRAME_FLANGE_T + BLOCK_H + 2)
    t = cylinder(cx, cy, cz, COND_R, ch, segments=12)
    write_binary_stl("07_conduit.stl", t, "conduit")


def gen_cables():
    cy = FRAME_FLANGE_T + BLOCK_H + 3
    ch = PH - 2*(FRAME_FLANGE_T + BLOCK_H + 3)

    # 12V
    t1 = cylinder(PW*0.25, cy, PD*0.3, CABLE_R_12V, ch, segments=8)
    write_binary_stl("08_cable_12v.stl", t1, "cable_12v")

    # 120V
    t2 = cylinder(PW*0.75, cy, PD*0.7, CABLE_R_120V, ch, segments=8)
    write_binary_stl("09_cable_120v.stl", t2, "cable_120v")


if __name__ == "__main__":
    print(f"Panel model for 3D printing")
    print(f"Real: {PANEL_W}×{PANEL_H}×{WALL_THICK}mm")
    print(f"Print: {PW:.1f}×{PH:.1f}×{PD:.1f}mm (scale {SCALE*100:.1f}%)")
    print(f"Fits Creality Ender 3 bed (220×220mm)")
    print()
    print("Printable dimensions:")
    print(f"  T-bar flange: {FRAME_FLANGE_W:.1f}mm wide × {FRAME_FLANGE_T}mm thick")
    print(f"  T-bar web: {FRAME_WEB_T}mm thick × {FRAME_WEB_VERT:.1f}mm (vert) / {FRAME_WEB_HORIZ:.1f}mm (horiz)")
    print(f"  Guadua strip: {GV_W:.1f}mm wide × {GV_T}mm thick, gap {GV_GAP:.1f}mm")
    print(f"  Diagonal: {GD_W:.1f}mm wide × {GD_T}mm thick")
    print(f"  Clamping strip: {CL_W:.1f}mm × {CL_T}mm")
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
    print("  01_frame          → Black")
    print("  02_hdpe_blocks    → Blue")
    print("  03_guadua_vert    → Beige/Tan")
    print("  04_diagonal_front → Brown")
    print("  05_diagonal_rear  → Brown")
    print("  06_clamps         → Silver/Grey")
    print("  07_conduit        → White")
    print("  08_cable_12v      → Red")
    print("  09_cable_120v     → Yellow")
    print()
    print("Tip: Print frame lying flat (73mm × 220mm footprint, 6.2mm tall)")
    print("     Diagonals are properly rotated — no stepping artifacts")