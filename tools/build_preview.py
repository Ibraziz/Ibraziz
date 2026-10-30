"""Render README.md as a local, GitHub-like preview. Never publishes content."""

from pathlib import Path

try:
    import markdown
except ImportError:
    raise SystemExit("Install the optional preview dependency: python -m pip install -r requirements-preview.txt")


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "preview"
CSS = """
:root {color-scheme:light;--bg:#f6f8fa;--panel:#fff;--ink:#1f2328;--muted:#59636e;--border:#d1d9e0;--link:#0969da;--code:#eff2f5;--row:#f6f8fa}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--bg:#010409;--panel:#0d1117;--ink:#e6edf3;--muted:#919eae;--border:#30363d;--link:#79c0ff;--code:#21262d;--row:#151b23}}
:root[data-theme=dark]{color-scheme:dark;--bg:#010409;--panel:#0d1117;--ink:#e6edf3;--muted:#919eae;--border:#30363d;--link:#79c0ff;--code:#21262d;--row:#151b23}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}
.toolbar{max-width:1000px;margin:28px auto 18px;padding:0 24px;display:flex;gap:16px;justify-content:space-between;align-items:center;color:var(--muted);font-size:13px}
.toolbar strong{color:var(--ink)}select{font:inherit;background:var(--panel);border:1px solid var(--border);color:var(--ink);padding:6px 10px;border-radius:7px}
.repository{max-width:1000px;margin:0 auto 40px;background:var(--panel);border:1px solid var(--border);border-radius:12px;overflow:hidden}
.filebar{font:13px ui-monospace,Consolas,monospace;padding:15px 32px;border-bottom:1px solid var(--border);color:var(--muted)}
.markdown-body{padding:36px 40px 40px;overflow-wrap:break-word}.markdown-body>:first-child{margin-top:0}.markdown-body>:last-child{margin-bottom:0}
p{margin:0 0 16px}a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}img{max-width:100%;height:auto;vertical-align:middle}picture{display:block;margin:0 0 18px}
h1,h2,h3{line-height:1.25;font-weight:600;margin:25px 0 16px}h1{font-size:2em}h2{font-size:1.5em;border-bottom:1px solid var(--border);padding-bottom:.3em;margin-top:30px}h3{font-size:1.25em;margin-top:26px}
ul{padding-left:2em;margin:0 0 16px}li+li{margin-top:5px}strong{font-weight:600}table{display:block;max-width:100%;overflow:auto;border-collapse:collapse;margin:0 0 16px;font-size:15px}
th,td{border:1px solid var(--border);padding:9px 13px;text-align:left}th{font-weight:600}tr:nth-child(2n){background:var(--row)}td:first-child{min-width:165px}
code{background:var(--code);border-radius:5px;padding:.2em .4em;font-size:85%}pre{background:var(--code);padding:16px;border-radius:8px;overflow:auto}
@media(max-width:650px){.toolbar{margin:18px auto 12px;padding:0 16px;gap:10px;font-size:12px}.repository{border-left:0;border-right:0;border-radius:0;margin:0}.filebar{padding:12px 20px}.markdown-body{padding:24px 20px;font-size:15px}h2{font-size:1.35em}h3{font-size:1.1em}table{font-size:13px}td:first-child{min-width:115px}}
"""
SCRIPT = r"""
const picker=document.querySelector('select');
const query=new URLSearchParams(location.search).get('theme');
function setTheme(theme){
  if(theme==='system')delete document.documentElement.dataset.theme;
  else document.documentElement.dataset.theme=theme;
  document.querySelectorAll('picture').forEach(p=>{
    p.querySelectorAll('source').forEach(s=>{
      if(!s.dataset.originalMedia)s.dataset.originalMedia=s.media;
      s.media=theme==='system'?s.dataset.originalMedia:(s.dataset.originalMedia.includes(theme)?s.dataset.originalMedia.replace(/\(prefers-color-scheme: (dark|light)\)/g,'(min-width: 0px)'):'not all');
    });
  });
}
picker.addEventListener('change',()=>setTheme(picker.value));
if(['dark','light','system'].includes(query)){picker.value=query;setTheme(query)}
"""


def main():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    body = markdown.markdown(readme, extensions=["tables", "fenced_code", "sane_lists"])
    body = body.replace('src="./assets/', 'src="../assets/').replace('srcset="./assets/', 'srcset="../assets/')
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ibraziz — GitHub profile preview</title><style>{CSS}</style></head><body>
<div class="toolbar"><div><strong>Ibraziz / profile</strong><br>Local preview · GitHub may render small details differently</div>
<label>Appearance <select aria-label="Preview appearance"><option value="system">System</option><option value="dark">Dark</option><option value="light">Light</option></select></label></div>
<main class="repository"><div class="filebar">README.md</div><article class="markdown-body">{body}</article></main>
<script>{SCRIPT}</script></body></html>
"""
    OUT.mkdir(exist_ok=True)
    target = OUT / "index.html"
    target.write_text(html, encoding="utf-8", newline="\n")
    print(target)


if __name__ == "__main__":
    main()
