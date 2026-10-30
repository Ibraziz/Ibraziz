"""Generate self-contained GitHub profile artwork using the standard library."""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PALETTES = {
    "dark": {
        "bg": "#0b1423", "panel": "#111f32", "line": "#293e55",
        "ink": "#edf5ff", "muted": "#a4b7cb", "accent": "#5eead4",
        "blue": "#91baff", "violet": "#bc9cff", "tint": "#123b3b", "soft": "#1c304a",
    },
    "light": {
        "bg": "#f0f7f9", "panel": "#ffffff", "line": "#cbdde5",
        "ink": "#142b43", "muted": "#4c657b", "accent": "#087f73",
        "blue": "#386cc2", "violet": "#8154c8", "tint": "#d9f2ed", "soft": "#e3edf6",
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
        f'<path d="M54 51H98" stroke="url(#aurora)" stroke-width="4" stroke-linecap="round"/>',
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
        color = p["accent"] if i in (0, 4, 7) else p["violet"] if i in (1, 5, 6) else p["blue"]
        radius = 11 if i == 4 else 6
        body.extend([
            f'<circle cx="{x}" cy="{y}" r="{radius + 9}" fill="{color}" opacity=".08"/>',
            f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{p["bg"]}" stroke="{color}" stroke-width="2"/>',
        ])
    body.append(f'<circle class="pulse" cx="962" cy="181" r="22" fill="none" stroke="{p["accent"]}" stroke-width="1.5" opacity=".32"/>')
    defs = (
        f'<linearGradient id="wash"><stop stop-color="{p["bg"]}"/>'
        f'<stop offset=".55" stop-color="{p["blue"]}" stop-opacity=".12"/>'
        f'<stop offset="1" stop-color="{p["violet"]}" stop-opacity=".25"/></linearGradient>'
        f'<linearGradient id="aurora" gradientUnits="userSpaceOnUse" x1="54" y1="51" x2="98" y2="51"><stop stop-color="{p["accent"]}"/>'
        f'<stop offset=".5" stop-color="{p["blue"]}"/>'
        f'<stop offset="1" stop-color="{p["violet"]}"/></linearGradient>'
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



# Labels and colors for the profile's tools table. These are not skill ratings.
BADGE_ROWS = [
    ('Programming', [
        ('python', 'Python', '#3776ab', '#ffffff'),
        ('sql', 'SQL', '#ba5a12', '#ffffff'),
        ('dotnet', '.NET', '#7436c4', '#ffffff'),
    ]),
    ('AI & NLP', [
        ('pytorch', 'PyTorch', '#cf4128', '#ffffff'),
        ('hugging-face', 'Hugging Face', '#e9c637', '#202531'),
        ('transformers', 'Transformers', '#dfb81a', '#202531'),
        ('vllm', 'vLLM', '#7343bd', '#ffffff'),
        ('dspy', 'DSPy', '#18795d', '#ffffff'),
    ]),
    ('LLMs & agents', [
        ('langchain', 'LangChain', '#216a59', '#ffffff'),
        ('langgraph', 'LangGraph', '#177c73', '#ffffff'),
        ('rag', 'RAG', '#4268bf', '#ffffff'),
    ]),
    ('APIs & applications', [
        ('fastapi', 'FastAPI', '#078474', '#ffffff'),
        ('flask', 'Flask', '#4c586a', '#ffffff'),
        ('streamlit', 'Streamlit', '#c73855', '#ffffff'),
        ('pydantic', 'Pydantic', '#b92b5b', '#ffffff'),
        ('sqlalchemy', 'SQLAlchemy', '#a63740', '#ffffff'),
    ]),
    ('Data & databases', [
        ('oracle-sql', 'Oracle SQL', '#c72b2b', '#ffffff'),
        ('postgresql', 'PostgreSQL', '#336791', '#ffffff'),
        ('duckdb', 'DuckDB', '#e2c526', '#202531'),
        ('sqlite', 'SQLite', '#167ba5', '#ffffff'),
        ('parquet', 'Parquet', '#25783b', '#ffffff'),
        ('pyspark', 'PySpark', '#b75b17', '#ffffff'),
    ]),
    ('Vector search', [
        ('chroma', 'Chroma', '#bf572b', '#ffffff'),
        ('faiss', 'FAISS', '#3c64ab', '#ffffff'),
    ]),
    ('HPC & containers', [
        ('slurm', 'Slurm', '#237eab', '#ffffff'),
        ('docker', 'Docker', '#1678cf', '#ffffff'),
        ('apptainer', 'Apptainer', '#5554b5', '#ffffff'),
        ('cuda', 'CUDA', '#5a7b16', '#ffffff'),
        ('rocm', 'ROCm', '#ba3048', '#ffffff'),
    ]),
    ('Knowledge graphs', [
        ('rdf', 'RDF', '#ac511b', '#ffffff'),
        ('sparql', 'SPARQL', '#7552ae', '#ffffff'),
        ('ontologies', 'Ontologies', '#94389d', '#ffffff'),
    ]),
    ('Cloud & dev tools', [
        ('aws-fundamentals', 'AWS Fundamentals', '#8e5512', '#ffffff'),
        ('git', 'Git', '#c24c32', '#ffffff'),
        ('github', 'GitHub', '#3e4a5d', '#ffffff'),
        ('jupyter', 'Jupyter', '#af5818', '#ffffff'),
    ]),
]


def shade(color, amount):
    channels = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
    target = 255 if amount >= 0 else 0
    return '#' + ''.join(f'{round(c + (target - c) * abs(amount)):02x}' for c in channels)


def badge(label, color, ink):
    widths = (4 if c in "il., '|" else 11 if c in 'MW@' else 8 if c.isupper() else 7 for c in label)
    width = max(45, sum(widths) + 24)
    body = [
        f'<rect x=".5" y=".5" width="{width - 1}" height="25" rx="4" fill="url(#paint)" stroke="{shade(color, -.18)}"/>',
        f'<path d="M5 1h{width - 10}q4 0 4 4v7H1V5q0-4 4-4Z" fill="#ffffff" opacity=".07"/>',
    ]
    if ink == '#ffffff':
        body.append(text(width / 2, 18, label, 13, '#000000', 500, "Verdana,Arial,sans-serif", 'text-anchor="middle" opacity=".3"'))
    body.append(text(width / 2, 17, label, 13, ink, 500, "Verdana,Arial,sans-serif", 'text-anchor="middle"'))
    defs = (f'<linearGradient id="paint" x2="0" y2="1">'
            f'<stop stop-color="{shade(color, .15)}"/>'
            f'<stop offset=".5" stop-color="{color}"/>'
            f'<stop offset="1" stop-color="{shade(color, -.12)}"/></linearGradient>')
    return svg(width, 26, label, f'Tool or framework: {label}.', '\n'.join(body), defs)


def update_readme():
    lines = ['<!-- tools:start -->', '', '| Area | Tools & frameworks |', '| :--- | :--- |']
    for category, tools in BADGE_ROWS:
        images = ' '.join(f'<img src="./assets/badges/{slug}.svg" alt="{escape(label, quote=True)}" height="26">' for slug, label, _, _ in tools)
        lines.append(f'| **{category}** | {images} |')
    lines.extend(['', '<!-- tools:end -->'])
    path = ROOT / 'README.md'
    content, count = re.subn(r'<!-- tools:start -->.*?<!-- tools:end -->', '\n'.join(lines), path.read_text(encoding='utf-8'), flags=re.S)
    if count != 1:
        raise ValueError('README.md must contain one tools:start / tools:end block')
    path.write_text(content, encoding='utf-8', newline='\n')


def main():
    ASSETS.mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        for name, artwork in [('hero', hero(palette)), ('hero-mobile', hero_mobile(palette))]:
            (ASSETS / f'{name}-{theme}.svg').write_text(artwork, encoding='utf-8', newline='\n')
    badge_dir = ASSETS / 'badges'
    badge_dir.mkdir(exist_ok=True)
    for _, tools in BADGE_ROWS:
        for slug, label, color, ink in tools:
            (badge_dir / f'{slug}.svg').write_text(badge(label, color, ink), encoding='utf-8', newline='\n')
    update_readme()
    print(f'Updated banners, {sum(len(tools) for _, tools in BADGE_ROWS)} badges, and the README tool table.')


if __name__ == '__main__':
    main()
