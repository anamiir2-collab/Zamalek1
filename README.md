# الزمالك.. حكاية وطن أبيض 🏹
# ZAMALEK SC — The White Castle Story (1911–2026)

مرجع تاريخي وثائقي **ثنائي اللغة (عربي/إنجليزي)** لنادي الزمالك المصري، من تأسيسه في ٥ يناير ١٩١١ باسم «نادي قصر النيل» حتى ٢ نوفمبر ٢٠٢٦ — **١١٦ فصلًا سنويًّا مستقلًّا، فصل لكل سنة بلا فجوات ولا دمج**، مع تسعة أبواب موضوعية، وقاعدة بيانات بطولات مصنفة، وسجل أساطير وقائمة رؤساء كاملة، ومراجع مرقمة وقائمة تحقق نهائية من الدقة التاريخية.

A bilingual Arabic/English documentary history of Zamalek SC — **116 independent year-by-year chapters (1911–2026)**, nine thematic parts, a classified trophy database, a legends register, the complete presidents list, numbered references and a final verification checklist.

---

## 🌐 شاهد الكتاب أونلاين / Read it online

بعد رفع المشروع إلى GitHub، فعّل خدمة **GitHub Pages**:

1. افتح تبويب **Settings → Pages** في المستودع.
2. في **Source** اختر **GitHub Actions**.
3. يعمل ملف `pages.yml` تلقائيًا وينشر الكتاب على:
   `https://<اسم-حسابك>.github.io/<اسم-المستودع>/`

Once pushed to GitHub, enable **Settings → Pages → Source: GitHub Actions** and the included workflow deploys the book automatically.

---

## 📄 تنزيل نسخة PDF / Download the PDF

**الطريقة ١ — تلقائيًا عبر GitHub Actions (الأفضل):**
1. بعد أول `push` يعمل ملف `.github/workflows/build-pdf.yml` تلقائيًا.
2. افتح تبويب **Actions** → آخر تشغيل لـ *Build PDF book* → **Artifacts** → نزّل `ZAMALEK_SC_COMPLETE_HISTORY_1911_2026.pdf`.
3. عند نشر أي **Tag** (مثل `v1.0`) يُرفق ملف PDF تلقائيًا في **Releases** ويبقى رابط تنزيل دائم.

**الطريقة ٢ — محليًا:**
```bash
pip install playwright
playwright install chromium
python scripts/build_pdf.py
# الناتج: ZAMALEK_SC_COMPLETE_HISTORY_1911_2026.pdf
```

**الطريقة ٣ — من المتصفح مباشرة:**
افتح `index.html` ثم اضغط **Ctrl+P** (طباعة) → «حفظ كـ PDF» → مقاس الصفحة كما هو (`794×1123px`) وفعّل خلفيات الطباعة. تنسيق الطباعة مضبوط بالكامل داخل الكتاب.

---

## 📂 بنية المشروع / Repository layout

```
├── index.html                    # الكتاب كاملًا — ملف واحد جاهز للنشر
├── fonts/                        # خطوط Google Fonts محلية (OFL) + fonts.css
├── site_src/                     # ملفات المصدر الجزئية (الغلاف، الأبواب، CSS…)
├── data/                         # بيانات الفصول السنوية 1911–2026 (Python)
├── scripts/
│   ├── assemble.py               # تجميع index.html + تحقق برمجي (116 سنة، عدّ الألقاب)
│   └── build_pdf.py              # بناء PDF عبر Playwright/Chromium
└── .github/workflows/
    ├── pages.yml                 # نشر الكتاب على GitHub Pages
    └── build-pdf.yml             # بناء PDF + Artifact/Release تلقائيًا
```

## 🛠 تعديل المحتوى / Editing the content

عدّل ملفات `data/years_*.py` (فصول السنوات) أو ملفات `site_src/*.html` (الأبواب والقوائم)، ثم أعد التجميع:

```bash
python scripts/assemble.py      # يتحقق تلقائيًا: 116 سنة متتالية + اتساق أعداد الألقاب
```

الأداة ترفض التجميع لو وُجدت سنة ناقصة أو مكررة أو إذا لم تتطابق أعداد الألقاب مع القوائم — حماية برمجية من أخطاء التوثيق.

## ✅ ضمانات الدقة / Accuracy guarantees

- **لا اختلاق:** لا أحداث ولا نتائج ولا تواريخ ولا اقتباسات مُختلقة؛ كل حدث كبير موثق بمصدر مرقّم (٣٨ مرجعًا بتاريخ وصول ٨ نوفمبر ٢٠٢٦).
- **تعارضات معلنة:** خلاف المصادر (سنة تسمية «فاروق» ١٩٤١/١٩٤٢، أول رئيس كرامر/مرزباخ، عدّ كأس مصر ٢٨/٢٩) معروض للقارئ كما هو.
- **أرقام محسوبة:** أعداد الألقاب (١٥ دوريًّا، ٢٩ كأسًا، ٥ دوري أبطال، ٥ سوبر إفريقي، ١٤ بطولة قاهرة…) مُعدّة برمجيًّا من قوائم السنين لا من الأرقام المجملة.
- **إحصاءات منسوبة:** أرقام الديربي (٢٣٣ مباراة وفق ويكيبيديا) وأرقام الألعاب الأخرى نُسبت إلى مصادرها صراحةً.
- **لا صور مولّدة:** لا صور AI ولا صور بأرشفة مشكوك فيها؛ العناصر البصرية طباعية وإحصائية بالكامل.
- **حد زمني:** الكتاب يغطي حتى ٢ نوفمبر ٢٠٢٦ حصرًا، بلا أي تنبؤات مستقبلية.

## 🔤 الخطوط والتراخيص / Fonts & licenses

سبع عائلات خطوط من Google Fonts مضمّنة محليًّا (تعمل دون إنترنت وتُضمَّن داخل PDF):

| العربية | الإنجليزية | الاستخدام |
|---|---|---|
| Amiri | Playfair Display | العناوين والغلاف |
| Noto Naskh Arabic | Lora | المتن |
| Tajawal | Montserrat | البطاقات والتوقيتات والعناوين الفرعية |
| Cairo | — | الجداول |

كلها بترخيص **SIL Open Font License** وفق شروط Google Fonts. محتوى الكتاب مُجمَّع من مصادر عامة موثقة في قسم المراجع (منها ويكيبيديا — CC BY-SA 4.0)؛ الأستخدام التعليمي والتوثيقي مقصود، والعلامات التجارية وأرص النادي ملك لأصحابها.

---

*من ١٩١١ إلى ٢٠٢٦.. الحكاية لم تنتهِ — From 1911 to 2026, the story continues.*
