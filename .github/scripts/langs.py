"""Gera assets/langs-light.svg e assets/langs-dark.svg com as linguagens mais usadas
nos repositorios do dono (publicos e privados). Texto convertido em paths (Jost, OFL).
Env: STATS_TOKEN (PAT com leitura de repos), OWNER, EXCLUDE (csv), LANG_DATA_JSON (teste)."""
import json, os, urllib.request, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OWNER = os.environ.get("OWNER", "JonasaAugusto")
TOKEN = os.environ.get("STATS_TOKEN", "")
EXCLUDE = {x.strip() for x in os.environ.get("EXCLUDE", "").split(",") if x.strip()}
HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(os.environ.get("OUT_DIR", HERE.parent.parent / "assets"))


def api(url):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json", "User-Agent": "langs-card"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect():
    if os.environ.get("LANG_DATA_JSON"):
        return json.loads(os.environ["LANG_DATA_JSON"]), 0
    repos, page = [], 1
    while True:
        batch = api(f"https://api.github.com/user/repos?affiliation=owner&visibility=all&per_page=100&page={page}")
        if not batch:
            break
        repos += batch
        page += 1
    repos = [r for r in repos if r["owner"]["login"] == OWNER and not r["fork"] and not r["archived"]]
    totals = {}
    for r in repos:
        for k, v in api(r["languages_url"]).items():
            totals[k] = totals.get(k, 0) + v
    return totals, len(repos)


font = TTFont(HERE / "jost-400.woff")
gs = font.getGlyphSet()
cmap = font.getBestCmap()
upm = font["head"].unitsPerEm
hm = font["hmtx"]


def width(t, s, tr=0):
    return sum(hm[cmap.get(ord(c), cmap[63])][0] * s / upm + tr * s for c in t) - tr * s


def text(t, s, x, y, tr=0):
    sc = s / upm
    cur = x
    d = []
    for ch in t:
        gn = cmap.get(ord(ch), cmap[63])
        if ch != " ":
            pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}")
            gs[gn].draw(TransformPen(pen, (sc, 0, 0, -sc, cur, y)))
            d.append(pen.getCommands())
        cur += hm[gn][0] * sc + tr * s
    return "".join(d)


THEMES = {
    "light": dict(txt="#0F1E2E", sub="#5B6773", track="#E6E9E7", ramp=["#1E7A55", "#2E9C73", "#4FB894", "#7ACBB2", "#A6DCC9"], other="#B8C0C6"),
    "dark": dict(txt="#FFFFFF", sub="#7A8896", track="#1B2E41", ramp=["#50C878", "#3FAE86", "#2F9475", "#237A65", "#1B5F52"], other="#4B5B6B"),
}


def render(totals, nrepos):
    items = sorted(((k, v) for k, v in totals.items() if k not in EXCLUDE), key=lambda kv: -kv[1])
    total = sum(v for _, v in items) or 1
    top = items[:5]
    rest = sum(v for _, v in items[5:])
    if rest:
        top.append(("Outros", rest))
    W, BAR_Y, BAR_H, cols, rowh = 880, 34, 12, 3, 28
    rows = (len(top) + cols - 1) // cols
    H = BAR_Y + BAR_H + 26 + rows * rowh
    for name, t in THEMES.items():
        colors = [t["other"] if top[i][0] == "Outros" else t["ramp"][i] for i in range(len(top))]
        title = "Linguagens mais usadas: " + ", ".join(f"{k} {v*100/total:.1f}%" for k, v in top)
        s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{title}</title>']
        sub = f"{nrepos} repositórios, públicos e privados" if nrepos else "repositórios públicos e privados"
        s.append(f'<path fill="{t["sub"]}" d="{text("LINGUAGENS MAIS USADAS", 12, 0, 12, 0.2)}"/>')
        s.append(f'<path fill="{t["sub"]}" d="{text(sub, 12, W - width(sub, 12), 12)}"/>')
        s.append(f'<clipPath id="c"><rect x="0" y="{BAR_Y}" width="{W}" height="{BAR_H}" rx="6"/></clipPath>')
        s.append(f'<rect x="0" y="{BAR_Y}" width="{W}" height="{BAR_H}" rx="6" fill="{t["track"]}"/><g clip-path="url(#c)">')
        x = 0.0
        for (k, v), c in zip(top, colors):
            w = W * v / total
            s.append(f'<rect x="{x:.2f}" y="{BAR_Y}" width="{max(w-2, 0.5):.2f}" height="{BAR_H}" fill="{c}"/>')
            x += w
        s.append("</g>")
        colw = W / cols
        for i, ((k, v), c) in enumerate(zip(top, colors)):
            cx = (i % cols) * colw
            cy = BAR_Y + BAR_H + 26 + (i // cols) * rowh
            s.append(f'<circle cx="{cx+5:.1f}" cy="{cy-5}" r="5" fill="{c}"/><path fill="{t["txt"]}" d="{text(k, 15, cx+18, cy)}"/>')
            pct = f"{v*100/total:.1f}%".replace(".", ",")
            s.append(f'<path fill="{t["sub"]}" d="{text(pct, 15, cx+18+width(k, 15)+10, cy)}"/>')
        s.append("</svg>")
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"langs-{name}.svg").write_text("".join(s), encoding="utf-8")


if __name__ == "__main__":
    totals, n = collect()
    render(totals, n)
    print("ok", n)
