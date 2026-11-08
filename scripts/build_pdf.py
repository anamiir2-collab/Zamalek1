#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""بناء نسخة PDF من الكتاب عبر Playwright/Chromium (نفس محرك المتصفح).
يُستخدم محليًا وعلى GitHub Actions. الناتج: ZAMALEK_SC_COMPLETE_HISTORY_1911_2026.pdf"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "ZAMALEK_SC_COMPLETE_HISTORY_1911_2026.pdf")

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--force-color-profile=srgb"])
    page = browser.new_page(viewport={"width": 794, "height": 1123})
    page.goto("file://" + SRC)
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready.then(() => true)")
    page.wait_for_timeout(2500)
    page.emulate_media(media="print")
    page.pdf(
        path=OUT,
        width="794px",
        height="1123px",
        print_background=True,
        prefer_css_page_size=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
    )
    browser.close()

size_mb = os.path.getsize(OUT) / 1024 / 1024
print(f"PDF written: {OUT} ({size_mb:.1f} MB)")
