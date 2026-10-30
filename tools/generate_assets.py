"""Generate self-contained GitHub profile artwork using the standard library."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PALETTES = {
    "dark": {
        "bg": "#0b1423", "panel": "#111f32", "line": "#293e55",
        "ink": "#edf5ff", "muted": "#a4b7cb", "accent": "#5eead4",
        "blue": "#91baff", "tint": "#123b3b", "soft": "#1c304a",
    },
    "light": {
        "bg": "#f0f7f9", "panel": "#ffffff", "line": "#cbdde5",
        "ink": "#142b43", "muted": "#4c657b", "accent": "#087f73",
        "blue": "#386cc2", "tint": "#d9f2ed", "soft": "#e3edf6",
    },
}
FONT = "'Segoe UI', Inter, Arial, sans-serif"
MONO = "'Cascadia Code', Consolas, monospace"


def text(x, y, value, size, color, weight=400, family=FONT, extra=""):
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" '
        f'font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'
    )


def svg(width, height, title, description, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
        f'  <title id="title">{escape(title)}</title>\n'
        f'  <desc id="desc">{escape(description)}</desc>\n'
        f'  <defs>{defs}</defs>\n{body}\n</svg>\n'
    )


def hero(p):
    # The graph is a decorative illustration, not a claim about a model topology.
    links = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4),
             (3, 6), (4, 5), (4, 7), (5, 8), (6, 7), (7, 8), (2, 4), (4, 6)]
    nodes = [(862, 113), (970, 73), (1071, 116), (820, 204), (962, 181),
             (1120, 211), (866, 279), (992, 291), (1082, 279)]
    body = [
        f'<rect x="1" y="1" width="1198" height="348" rx="24" fill="{p["bg"]}" stroke="{p["line"]}"/>',
        f'<path d="M790 1h385a24 24 0 0 1 24 24v300a24 24 0 0 1-24 24H790Z" fill="url(#wash)"/>',
        f'<path d="M54 51H98" stroke="{p["accent"]}" stroke-width="4" stroke-linecap="round"/>',
        text(115, 57, "@IBRAZIZ", 18, p["muted"], 500, MONO, 'letter-spacing="3"'),
        text(52, 141, "Abdelaziz Ibrahim", 61, p["ink"], 700, extra='letter-spacing="-2.2"'),
        text(55, 191, "AI engineer · NLP researcher", 29, p["accent"], 600),
        text(55, 239, "Language models. Useful tools. Reliable data.", 23, p["muted"]),
        f'<circle cx="62" cy="302" r="4" fill="{p["accent"]}"/>',
        text(78, 308, "Jyväskylä, Finland", 18, p["muted"]),
        f'<path d="M55 269H691" stroke="{p["line"]}"/>',
        f'<circle cx="970" cy="182" r="128" fill="none" stroke="{p["line"]}" stroke-dasharray="3 10"/>',
    ]
    for a, b in links:
        x1, y1 = nodes[a]
        x2, y2 = nodes[b]
        body.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{p["line"]}" stroke-width="1.5"/>')
    body.append(f'<path d="M862 113L970 73L1071 116L962 181L866 279L992 291" fill="none" stroke="{p["accent"]}" stroke-opacity=".5" stroke-width="2"/>')
    for i, (x, y) in enumerate(nodes):
        color = p["accent"] if i in (0, 4, 7) else p["blue"]
        radius = 11 if i == 4 else 6
        body.extend([
            f'<circle cx="{x}" cy="{y}" r="{radius + 9}" fill="{color}" opacity=".08"/>',
            f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{p["bg"]}" stroke="{color}" stroke-width="2"/>',
        ])
    body.append(f'<circle class="pulse" cx="962" cy="181" r="22" fill="none" stroke="{p["accent"]}" stroke-width="1.5" opacity=".32"/>')
    defs = (
        f'<linearGradient id="wash"><stop stop-color="{p["bg"]}"/>'
        f'<stop offset="1" stop-color="{p["tint"]}" stop-opacity=".7"/></linearGradient>'
        '<style>.pulse{transform-origin:962px 181px;animation:breathe 5s ease-in-out infinite}'
        '@keyframes breathe{0%,100%{transform:scale(.9);opacity:.18}50%{transform:scale(1.35);opacity:.48}}'
        '@media(prefers-reduced-motion:reduce){.pulse{animation:none}}</style>'
    )
    return svg(1200, 350, "Abdelaziz Ibrahim | AI engineer and NLP researcher",
               "Language models, useful tools, and reliable data. Based in Jyväskylä, Finland.",
               "\n".join(body), defs)


def hero_mobile(p):
    body = [
        f'<rect x="1" y="1" width="598" height="308" rx="22" fill="{p["bg"]}" stroke="{p["line"]}"/>',
        f'<path d="M32 40H67" stroke="{p["accent"]}" stroke-width="4" stroke-linecap="round"/>',
        text(82, 46, "@IBRAZIZ", 19, p["muted"], 500, MONO, 'letter-spacing="2"'),
        text(30, 114, "Abdelaziz Ibrahim", 49, p["ink"], 700, extra='letter-spacing="-1.8"'),
        text(32, 160, "AI engineer · NLP researcher", 26, p["accent"], 600),
        text(32, 204, "Language models. Useful tools.", 23, p["muted"]),
        text(32, 235, "Reliable data.", 23, p["muted"]),
        f'<circle cx="38" cy="276" r="4" fill="{p["accent"]}"/>',
        text(53, 282, "Jyväskylä, Finland", 20, p["muted"]),
    ]
    return svg(600, 310, "Abdelaziz Ibrahim | AI engineer and NLP researcher",
               "Language models, useful tools, and reliable data. Based in Jyväskylä, Finland.",
               "\n".join(body))


def research(p, mobile=False):
    if mobile:
        body = [f'<rect x="1" y="1" width="598" height="304" rx="18" fill="{p["bg"]}" stroke="{p["line"]}"/>']
        rows = [
            ("09", "evaluators benchmarked", "Reference-free quality estimation"),
            ("41,412", "translation directions", "Evaluator benchmark coverage"),
            ("1.14B", "translation pairs scored", "421-direction scoring subset"),
        ]
        for i, (value, label, note) in enumerate(rows):
            y = 100 * i
            body.extend([
                text(24, y + 61, value, 38, p["accent"], 700, extra='letter-spacing="-1.5"'),
                text(210, y + 44, label, 23, p["ink"], 600),
                text(210, y + 75, note, 19, p["muted"]),
            ])
            if i < 2:
                body.append(f'<path d="M24 {y + 101}H576" stroke="{p["line"]}"/>')
        return svg(600, 306, "FineOPUS quality-estimation work",
                   "Nine evaluators benchmarked across 41,412 directions; 1.14 billion translation pairs scored in a 421-direction subset.",
                   "\n".join(body))
    body = [f'<rect x="1" y="1" width="1198" height="160" rx="16" fill="{p["bg"]}" stroke="{p["line"]}"/>']
    metrics = [
        (35, "09", "evaluators benchmarked", "Reference-free quality estimation"),
        (435, "41,412", "translation directions", "Evaluator benchmark coverage"),
        (835, "1.14B", "translation pairs scored", "421-direction scoring subset"),
    ]
    for x, value, label, note in metrics:
        body.extend([
            text(x, 63, value, 45, p["accent"], 700, extra='letter-spacing="-1.5"'),
            text(x, 100, label, 22, p["ink"], 600),
            text(x, 130, note, 16, p["muted"]),
        ])
    for x in (400, 800):
        body.append(f'<path d="M{x} 28v106" stroke="{p["line"]}"/>')
    return svg(1200, 162, "FineOPUS quality-estimation work",
               "Nine evaluators benchmarked across 41,412 directions; 1.14 billion translation pairs scored in a 421-direction subset.",
               "\n".join(body))


def tool_grid(p, mobile=False):
    tools = [
        ("Py", "Python"), ("SQL", "SQL"), ("Pt", "PyTorch"),
        ("Tf", "Transformers"), ("vL", "vLLM"), ("LG", "LangGraph"),
        ("LC", "LangChain"), ("FA", "FastAPI"), ("Fl", "Flask"),
        ("Db", "DuckDB"), ("Dk", "Docker"), ("Sl", "Slurm"),
    ]
    body = []
    for i, (mark, name) in enumerate(tools):
        columns = 3 if mobile else 6
        x, y = (i % columns) * 202, (i // columns) * 78
        body.extend([
            f'<rect x="{x + 1}" y="{y + 1}" width="188" height="64" rx="12" fill="{p["bg"]}" stroke="{p["line"]}"/>',
            f'<rect x="{x + 12}" y="{y + 14}" width="38" height="38" rx="9" fill="{p["tint"]}"/>',
            text(x + 31, y + 39, mark, 16 if len(mark) == 3 else 18, p["accent"], 700, MONO, 'text-anchor="middle"'),
            text(x + 61, y + 40, name, 18 if len(name) > 9 else 20, p["ink"], 600),
        ])
    return svg(600 if mobile else 1200, 300 if mobile else 144, "Languages and tools",
               ", ".join(name for _, name in tools) + ". Text badges, not vendor logos or skill ratings.",
               "\n".join(body))


def main():
    ASSETS.mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        for name, renderer in (("hero", hero), ("research", research), ("tools", tool_grid)):
            path = ASSETS / f"{name}-{theme}.svg"
            path.write_text(renderer(palette), encoding="utf-8", newline="\n")
            print(path.relative_to(ROOT))
        for name, artwork in (("hero", hero_mobile(palette)),
                              ("research", research(palette, mobile=True)),
                              ("tools", tool_grid(palette, mobile=True))):
            path = ASSETS / f"{name}-mobile-{theme}.svg"
            path.write_text(artwork, encoding="utf-8", newline="\n")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
