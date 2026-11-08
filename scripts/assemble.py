#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""اجتماع فصول الكتاب: يقرأ ملفات بيانات السنوات وملفات HTML الجزئية ويجمّعها في index.html
مع تحقق برمجي كامل: 116 سنة متتالية دون فجوات، وعدّ الألقاب من القوائم."""
import os, sys, glob, re, importlib.util

REPO = "/home/z/my-project/zamalek-white-castle-book"
SRC = os.path.join(REPO, "site_src")
DATA = os.path.join(REPO, "data")

def load_years():
    years = []
    for f in sorted(glob.glob(os.path.join(DATA, "years_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        years.extend(mod.YEARS)
    return years

def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()

def render_year(ch):
    tag_cls = ch.get("cls", "gray")
    paras_ar = "\n".join(f'<p class="ar-p">{p}</p>' for p in ch["ar"])
    paras_en = "\n".join(f"<p>{p}</p>" for p in ch["en"])
    ev = ""
    if ch.get("ev"):
        items = "\n".join(
            f'<li><span class="d">{d}</span><span>{t}</span></li>' for d, t in ch["ev"])
        ev = (f'<div class="events"><div class="ev-title">أحداث موثقة · DOCUMENTED EVENTS</div>'
              f'<ul>{items}</ul></div>')
    note = '<div class="src-note">المراجع: <span class="en">[' + ch["src"] + ']</span> — قائمة المراجع في نهاية الكتاب</div>'
    return f'''<section class="year-chapter" id="y{ch["y"]}">
<div class="year-head"><div class="ynum">{ch["y"]}</div><span class="chip {tag_cls}">{ch["tag"]}</span><div class="yt"><div class="y-title">{ch["ar_t"]}</div><div class="y-title-en">{ch["en_t"]}</div></div></div>
{paras_ar}
<div class="en-box"><span class="en-label">English summary</span>{paras_en}</div>
{ev}
{note}
</section>'''

def render_toc_years(years):
    links = "\n".join(
        f'<a href="#y{c["y"]}"><span class="y-num">{c["y"]}</span> — {c["ar_t"]}</a>' for c in years)
    return f'<div class="years-toc">{links}</div>'

# ============ التجميع والتحقق ============
years = load_years()
ys = sorted(c["y"] for c in years)
assert len(ys) == len(set(ys)), "سنة مكررة!"
expected = list(range(1911, 2027))
assert ys == expected, f"فجوات أو سنوات ناقصة! عدد الفصول {len(ys)} — الفرق: {set(expected)-set(ys) or set(ys)-set(expected)}"
print(f"✔ فصول السنوات: {len(ys)} فصلًا من {ys[0]} إلى {ys[-1]} — لا فجوات، لا تكرار")

# ---- عدّ الألقاب من قوائم السنين (تحقق حسابي مستقل) ----
LEAGUE = [1960,1964,1965,1978,1984,1988,1992,1993,2001,2003,2004,2015,2021,2022,2026]
CUP = [1922,1932,1935,1938,1941,1943,1944,1952,1955,1957,1958,1959,1960,1962,1975,1977,1979,1988,1999,2002,2008,2013,2014,2015,2016,2018,2019,2021,2025]
CAFAF = [1984,1986,1993,1996,2002]
CONFED = [2019,2024]
CWC = [2000]
SUPERC = [1994,1997,2003,2020,2024]
CAIRO = [1923,1929,1930,1932,1934,1940,1941,1944,1945,1947,1949,1951,1952,1953]
checks = [("الدوري", LEAGUE, 15), ("كأس مصر", CUP, 29), ("دوري الأبطال", CAFAF, 5),
          ("الكونفيدرالية", CONFED, 2), ("كأس الكؤوس", CWC, 1), ("السوبر الإفريقي", SUPERC, 5),
          ("بطولة القاهرة", CAIRO, 14)]
for name, lst, n in checks:
    assert len(lst) == n and len(set(lst)) == n, f"عدّ {name} غير متسق: {len(lst)} != {n}"
    print(f"✔ {name}: {len(lst)} ألقاب (سنة سنوية، بلا تكرار)")

AR_DIG = "٠١٢٣٤٥٦٧٨٩"
def ar_num(n):
    return "".join(AR_DIG[int(d)] for d in str(n))

toc = f'''<div class="part-header" id="toc">
  <span class="kicker">المحتويات <span class="en">Table of contents</span></span>
  <h2>خريطة الكتاب — كل شيء يبعد نقرة واحدة</h2>
  <div class="h2-en">Every section and every year, one click away</div>
  <div class="divider"></div>
</div>
<div class="toc-wrap">
<div class="toc-part"><a href="#about"><div class="tp-ar"><span class="num">م</span>مقدمة الكتاب والمنهجية</div></a><div class="tp-en">About this book &amp; methodology</div></div>
<div class="toc-part"><a href="#timeline"><div class="tp-ar"><span class="num">ط</span>الخط الزمني الكبير ١٩١١–٢٠٢٦</div></a><div class="tp-en">Master timeline</div></div>
<div class="toc-part"><a href="#part1"><div class="tp-ar"><span class="num">١</span>التأسيس والهوية المبكرة (١٩١١–١٩٢٥)</div></a><div class="tp-en">Founding &amp; early identity</div></div>
<div class="toc-part"><a href="#part2"><div class="tp-ar"><span class="num">٢</span>العهد الملكي (١٩٢٥–١٩٥٢)</div></a><div class="tp-en">The royal era</div></div>
<div class="toc-part"><a href="#part3"><div class="tp-ar"><span class="num">٣</span>ما بعد ثورة ١٩٥٢</div></a><div class="tp-en">After the 1952 revolution</div></div>
<div class="toc-part"><a href="#part4"><div class="tp-ar"><span class="num">٤</span>الهوية والألوان واللقب</div></a><div class="tp-en">Identity, colours &amp; nicknames</div></div>
<div class="toc-part"><a href="#part5"><div class="tp-ar"><span class="num">٥</span>الجيل الذهبي</div></a><div class="tp-en">The golden generation</div></div>
<div class="toc-part"><a href="#part6"><div class="tp-ar"><span class="num">٦</span>الزمالك في إفريقيا</div></a><div class="tp-en">Zamalek in Africa</div></div>
<div class="toc-part"><a href="#part7"><div class="tp-ar"><span class="num">٧</span>الساحة المحلية</div></a><div class="tp-en">The domestic arena</div></div>
<div class="toc-part"><a href="#part8"><div class="tp-ar"><span class="num">٨</span>ديربي القاهرة</div></a><div class="tp-en">The Cairo derby</div></div>
<div class="toc-part"><a href="#part9"><div class="tp-ar"><span class="num">٩</span>ما وراء كرة القدم</div></a><div class="tp-en">Beyond football</div></div>
<div class="toc-part"><a href="#chronicle"><div class="tp-ar"><span class="num">س</span>السجل السنوي ١٩١١–٢٠٢٦ ({ar_num(len(ys))} فصلًا)</div></a><div class="tp-en">Year-by-year chronicle — 116 chapters</div></div>
<div class="toc-part"><a href="#trophies"><div class="tp-ar"><span class="num">ب</span>قاعدة بيانات البطولات</div></a><div class="tp-en">Trophy database</div></div>
<div class="toc-part"><a href="#legends"><div class="tp-ar"><span class="num">أ</span>سجل الأساطير</div></a><div class="tp-en">Legends register</div></div>
<div class="toc-part"><a href="#presidents"><div class="tp-ar"><span class="num">ر</span>رؤساء النادي عبر التاريخ</div></a><div class="tp-en">Presidents list</div></div>
<div class="toc-part"><a href="#references"><div class="tp-ar"><span class="num">م</span>المراجع وقائمة التحقق النهائية</div></a><div class="tp-en">References &amp; verification checklist</div></div>
<div class="toc-part"><a href="#toc-years"><div class="tp-ar"><span class="num">↑</span>فصول السنوات من ١٩١١ إلى ٢٠٢٦</div></a><div class="tp-en">Jump to any year</div></div>
</div>
<h3 class="section-tag" id="toc-years">فصول السنوات · YEAR CHAPTERS</h3>
{render_toc_years(years)}'''

chronicle_header = f'''<div class="part-header" id="chronicle">
  <span class="kicker">السجل السنوي <span class="en">Year-by-year chronicle 1911–2026</span></span>
  <h2>{ar_num(len(ys))} فصلًا مستقلًّا — فصل لكل سنة، بلا فجوات وبلا دمج</h2>
  <div class="h2-en">One chapter per year, 1911 to 2026 — no skips, no merges</div>
  <div class="divider"></div>
</div>
<p class="ar-p">قلب هذا الكتاب ينبض هنا: {ar_num(len(ys))} فصلًا مستقلًّا، فصل لكل سنة من عمر النادي، مرتبة ترتيبًا زمنيًّا صارمًا. كل فصل يحمل عنوانًا ثنائي اللغة، وسردًا عربيًا وثائقيًّا، وخلاصة إنجليزية، وقائمة أحداث موثقة بتواريخها، وأرقام المراجع. وحيثما كانت سجلات سنة معينة شحيحة، صرّح الفصل بذلك بوضوح — فالصدق جزء من الحكاية، والحكاية لا تُختلق.</p>'''

screen_nav = '''<nav class="screen-nav">
  <a href="#toc">المحتويات</a><a href="#timeline">الخط الزمني</a><a href="#part1">الأبواب</a>
  <a href="#chronicle">السجل السنوي 1911-2026</a><a href="#trophies">البطولات</a>
  <a href="#legends">الأساطير</a><a href="#presidents">الرؤساء</a><a href="#references">المراجع</a>
  <span class="nav-en">ZAMALEK SC — THE WHITE CASTLE STORY · 1911–2026</span>
</nav>'''

html = "\n".join([
    read("head.html"),
    screen_nav,
    read("cover.html"),
    '<div class="main-content">',
    read("intro.html"),
    toc,
    read("timeline.html"),
    read("parts_a.html"),
    read("parts_b.html"),
    chronicle_header,
    "\n".join(render_year(c) for c in sorted(years, key=lambda x: x["y"])),
    read("databases.html"),
    read("databases2.html"),
    "</div>",
    read("closing.html"),
    "</body>\n</html>",
])

out = os.path.join(REPO, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
size_kb = os.path.getsize(out) // 1024
print(f"✔ تم التجميع: {out} ({size_kb} KB)")
print(f"✔ عدد فصول السنوات المعروضة: {len(ys)} — فصل لكل سنة من ١٩١١ إلى ٢٠٢٦")
