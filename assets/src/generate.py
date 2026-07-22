#!/usr/bin/env python3
"""Regenerate ../header.svg and ../footer.svg from art.txt.

Usage:  python3 generate.py
The ASCII art (Braille) lives in art.txt — one row per line, all equal width.
Animations use SMIL so they run inside GitHub's <img>-embedded SVG.
"""
import os

D = os.path.dirname(os.path.abspath(__file__))
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

art = [l for l in open(os.path.join(D, 'art.txt'), encoding='utf-8').read().split('\n') if l != '']
FS, LS, AX, AY0 = 11, 11, 48, 104
ARTH = len(art) * LS
IDY   = AY0 + ARTH + 34
METAY = IDY + 28
H     = METAY + 22
SCANY = AY0 - LS + 2
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

rows = "\n".join(
    '    <text x="%d" y="%d" opacity="0" xml:space="preserve">%s'
    '<animate attributeName="opacity" values="0;1" begin="%.2fs" dur="0.4s" fill="freeze"/></text>'
    % (AX, AY0 + i*LS, esc(ln), 0.35 + i*0.028)
    for i, ln in enumerate(art))

header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {H}" width="900" height="{H}" role="img" aria-label="Kevin Darrell — software engineer · ASCII art of a Porsche 911 · I build systems that think.">
  <defs>
    <style>
      text{{font-family:{MONO};}}
    </style>
  </defs>

  <rect width="900" height="{H}" fill="#0b0e14"/>
  <text x="44" y="40" font-size="12.5" fill="#4c5561" letter-spacing="2">~/kevin-darrell</text>

  <!-- prompt -->
  <text x="44" y="82" font-size="19" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="0.05s" dur="0.4s" fill="freeze"/>
    <tspan fill="#7ee787">❯</tspan><tspan fill="#e6edf3" dx="12">whoami</tspan>
  </text>

  <!-- ascii art (prints row by row) -->
  <g fill="#e6edf3" font-size="{FS}">
{rows}
  </g>

  <!-- scan line -->
  <rect x="{AX}" y="{SCANY}" width="470" height="{LS+2}" fill="#e6edf3" opacity="0">
    <animate attributeName="opacity" values="0;0.13;0.13;0" keyTimes="0;0.12;0.88;1" dur="4.6s" begin="1.1s" repeatCount="indefinite"/>
    <animateTransform attributeName="transform" type="translate" from="0 0" to="0 {ARTH}" dur="4.6s" begin="1.1s" repeatCount="indefinite"/>
  </rect>

  <!-- identity -->
  <text x="44" y="{IDY}" font-size="20" font-weight="700" fill="#e6edf3" letter-spacing=".3" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="0.9s" dur="0.5s" fill="freeze"/>
    kevin darrell<tspan font-weight="400" font-size="16" fill="#9aa4b0" letter-spacing="1"> — software engineer · systems that think</tspan><tspan dx="8" fill="#7ee787">█<animate attributeName="fill-opacity" values="1;1;0;0" dur="1.1s" begin="1.5s" repeatCount="indefinite"/></tspan>
  </text>

  <!-- meta -->
  <text x="44" y="{METAY}" font-size="11.5" fill="#5a636f" letter-spacing="2" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="1.1s" dur="0.5s" fill="freeze"/>
    UTC+7  ·  OPEN TO COLLABORATE  ·  CLEAN CODE &amp; SYSTEMS
  </text>
</svg>
'''

footer = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 96" width="900" height="96" role="img" aria-label="Let's build something that thinks.">
  <defs>
    <style>text{{font-family:{MONO};}}</style>
  </defs>
  <rect width="900" height="96" fill="#0b0e14"/>
  <rect x="0" y="0" width="900" height="2" fill="#21262d"/>

  <text x="44" y="46" font-size="17" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="0.1s" dur="0.5s" fill="freeze"/>
    <tspan fill="#7ee787">❯</tspan><tspan fill="#e6edf3" dx="12">exit</tspan>
  </text>
  <text x="44" y="74" font-size="14" fill="#9aa4b0" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="0.4s" dur="0.5s" fill="freeze"/>
    // let's build something that thinks.<tspan dx="6" fill="#7ee787">█<animate attributeName="fill-opacity" values="1;1;0;0" dur="1.1s" begin="1s" repeatCount="indefinite"/></tspan>
  </text>

  <text x="856" y="46" text-anchor="end" font-size="12.5" fill="#e6edf3" letter-spacing="2" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="0.6s" dur="0.5s" fill="freeze"/>KEVIN DARRELL</text>
  <text x="856" y="72" text-anchor="end" font-size="11" fill="#5a636f" letter-spacing="2" opacity="0">
    <animate attributeName="opacity" values="0;1" begin="0.75s" dur="0.5s" fill="freeze"/>SOFTWARE ENGINEER</text>
</svg>
'''

# ---- stack card (SVG so the green labels actually render on GitHub) ----
STACK = [
    ("lang",  ["typescript", "javascript", "python", "go"]),
    ("back",  ["node", "express", "nestjs", "graphql"]),
    ("front", ["react", "next", "tailwind"]),
    ("infra", ["postgres", "mongo", "redis", "docker", "aws", "linux"]),
]
def _val(items):
    out = []
    for i, it in enumerate(items):
        if i: out.append('<tspan fill="#5a636f"> · </tspan>')
        out.append('<tspan fill="#e6edf3">%s</tspan>' % it)
    return ''.join(out)

SY0, SSTEP, SFS = 56, 33, "15.5"
SH = SY0 + (len(STACK)-1)*SSTEP + 30
srows = "\n".join(
    '  <g opacity="0"><animate attributeName="opacity" values="0;1" begin="%.2fs" dur="0.5s" fill="freeze"/>'
    '<text x="44" y="%d" font-size="%s"><tspan fill="#7ee787">%s</tspan></text>'
    '<text x="150" y="%d" font-size="%s">%s</text></g>'
    % (0.15 + i*0.12, SY0 + i*SSTEP, SFS, lbl, SY0 + i*SSTEP, SFS, _val(items))
    for i, (lbl, items) in enumerate(STACK))

stack = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {SH}" width="900" height="{SH}" role="img" aria-label="Tech stack — lang: typescript javascript python go; back: node express nestjs graphql; front: react next tailwind; infra: postgres mongo redis docker aws linux">
  <defs><style>text{{font-family:{MONO};}}</style></defs>
  <rect x="1" y="1" width="898" height="{SH-2}" rx="10" fill="#0b0e14" stroke="#21262d" stroke-width="1"/>
{srows}
</svg>
'''

# ---- connect badges (dark terminal pills; clickable via link-wrap in README) ----
BADGES = [
    ("linkedin", "linkedin",
     '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'),
    ("email", "email",
     '<path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/>'),
    ("github", "github",
     '<path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.52 11.52 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222 0 1.606-.014 2.898-.014 3.293 0 .321.216.694.825.576C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>'),
]
for name, label, icon in BADGES:
    W = 44 + int(len(label) * 8.4) + 16
    badge = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 40" width="{W}" height="40" role="img" aria-label="{label}">
  <defs><style>text{{font-family:{MONO};}}</style></defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="39" rx="8" fill="#0b0e14" stroke="#30363d"/>
  <g transform="translate(15,11) scale(0.75)" fill="#e6edf3">{icon}</g>
  <text x="44" y="26" font-size="14" fill="#e6edf3">{label}</text>
</svg>
'''
    open(os.path.join(D, '..', name + '.svg'), 'w', encoding='utf-8').write(badge)

open(os.path.join(D, '..', 'header.svg'), 'w', encoding='utf-8').write(header)
open(os.path.join(D, '..', 'footer.svg'), 'w', encoding='utf-8').write(footer)
open(os.path.join(D, '..', 'stack.svg'), 'w', encoding='utf-8').write(stack)
print("regenerated header.svg (%d rows), footer.svg, stack.svg, + linkedin/email/github badge svgs" % len(art))
