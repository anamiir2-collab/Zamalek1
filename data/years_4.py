# -*- coding: utf-8 -*-
# السجل السنوي 1971–1990

YEARS = [
dict(y=1971, tag="إدارة", cls="gray", ar_t="زامورة يسلّم ويخرج", en_t="Zamora Steps Aside",
 ar=["في يوليو ١٩٧١ أنهى <b>حلمي زامورة</b> فترته الأولى في الرئاسة، وتولى <b>توفيق الخشن</b> قيادة النادي. وفي خزانة اللعبة أضاف الفريق <b>كأس التلفزيون المصري / Egyptian Television Cup</b> لعام ١٩٧١ — لقب موسمي أضافه النادي إلى سجلاته في سنوات ما بعد الحرب."],
 en=["In July 1971 <b>Helmy Zamora</b> ended his first presidency and <b>Tawfik El-Khashana</b> took over. In the cabinet, the club added the <b>Egyptian Television Cup</b> (1971)."],
 ev=[("يوليو 1971","نهاية الفترة الأولى لحلمي زامورة وتولي توفيق الخشن"),("1971","كأس التلفزيون المصري")],
 src="٣، ٢٣"),

dict(y=1972, tag="سجلات محدودة", cls="gray", ar_t="سنوات ما قبل أكتوبر", en_t="Before October",
 ar=["لا تتوافر في مصادرنا المتاحة ألقاب موثقة للنادي هذا العام؛ مصر كانت في سنوات الاستنزاف بعد حرب ١٩٦٧ استعدادًا للحرب القادمة، والكرة كانت تعيش مواسم مضطربة الإيقاع."],
 en=["No documented trophies this year in our sources; Egypt was in its post-1967 war of attrition years and football lived through unsettled seasons."],
 src="٣"),

dict(y=1973, tag="إدارة", cls="gray", ar_t="زامورة يعود في سنة الحرب", en_t="Zamora Returns in a War Year",
 ar=["في فبراير ١٩٧٣ عاد <b>حلمي زامورة</b> إلى الرئاسة قبل أشهر من حرب أكتوبر، وسيتولى قيادة النادي — بفترتين متتابعتين — أحد عشر عامًا قادمة، وهي الفترة التي سيُسمى بعدها ملعب النادي باسمه. لا تتوافر في مصادرنا المتاحة ألقاب موثقة للنادي هذا العام بسبب اضطراب الحرب."],
 en=["In February 1973 <b>Helmy Zamora</b> returned to the presidency months before the October War, beginning the tenure that would see the club ground bear his name. No documented trophies this year in our sources."],
 ev=[("فبراير 1973","عودة حلمي زامورة إلى الرئاسة")],
 src="٢٣"),

dict(y=1974, tag="بطولة", cls="gold", ar_t="كأس أكتوبر", en_t="The October League Cup",
 ar=["بعد انتصار أكتوبر ١٩٧٣ نظمت الكرة المصرية <b>كأس أكتوبر / October League Cup</b>، وفاز بها النادي عام ١٩٧٤ — أول أبطال في تاريخ هذه المسابقة الاحتفالية — في رمزية جميلة: أول لقب للقلعة البيضاء في عصر الانتصار."],
 en=["After the October 1973 victory, Egyptian football organised the <b>October League Cup</b>, which the club won in 1974 — the first winners in the competition’s history."],
 ev=[("1974","كأس أكتوبر — أول أبطال المسابقة")],
 src="٣"),

dict(y=1975, tag="بطولة", cls="gold", ar_t="كأس مصر في منتصف السبعينيات", en_t="An Egypt Cup Mid-Decade",
 ar=["في موسم ١٩٧٤-٧٥ رفع النادي <b>كأس مصر</b> — لقبه الأول في العقد الجديد وفتح بابه لموجة ألقاب السبعينيات التي ستتوّج بأول مشاركة إفريقية وحملة دوري ١٩٧٧-٧٨."],
 en=["In 1974-75 the club lifted the <b>Egypt Cup</b> — its first of the decade, opening the run of 1970s titles that would lead to the first African campaign."],
 ev=[("موسم 1974-75","كأس مصر")],
 src="٣"),

dict(y=1976, tag="إفريقيا", cls="red", ar_t="أول مشاركة قارية", en_t="The First African Campaign",
 ar=["بعد فوزه بكأس مصر، شارك النادي لأول مرة في مسابقات إفريقيا عبر <b>كأس الكؤوس الإفريقية / African Cup Winners’ Cup</b> عام ١٩٧٦، وسلك الطريق حتى نصف النهائي قبل أن يسقط أمام شوتنج ستارز النيجيري بركلات الترجيح بعد تعادل ٢-٢ في المجموع — أول عبرة إفريقية لفريق سيصبح لاحقًا ملك القارة."],
 en=["As cup holders, the club made its African debut in the 1976 <b>African Cup Winners’ Cup</b>, reaching the semi-finals before falling to Nigeria’s Shooting Stars on penalties after a 2–2 aggregate tie."],
 ev=[("1976","أول مشاركة إفريقية: كأس الكؤوس — نصف النهائي")],
 src="٤"),

dict(y=1977, tag="بطولة", cls="gold", ar_t="كأس مصر ثم بدء العصر الذهبي", en_t="A Cup, Then the Golden Run",
 ar=["في موسم ١٩٧٦-٧٧ رفع النادي <b>كأس مصر</b>، وفي الموسم نفسه بدأ مشوار الدوري الذي سيُتويج في فصل السنة التالية بلقب الدوري الرابع — بداية حقبة الثمانينيات الذهبية التي ستعرف القلعة إفريقيًّا لأول مرة."],
 en=["In 1976-77 the club lifted the <b>Egypt Cup</b>, while the league campaign that would bring the 1977-78 title was underway."],
 ev=[("موسم 1976-77","كأس مصر")],
 src="٣"),

dict(y=1978, tag="بطولة", cls="red", ar_t="اللقب الرابع في الدوري", en_t="League No. 4",
 ar=["في موسم ١٩٧٧-٧٨ فاز النادي بـ<b>الدوري المصري الممتاز</b> للسنة الرابعة في تاريخه — أول لقب دوري بعد خمس عشرة سنة من صمت المحصلة (منذ ١٩٦٤-٦٥)، وأول إشارة على جيل الثمانينيات الذي سيصنع تاريخ القلعة القاري."],
 en=["In 1977-78 the club won its <b>fourth Egyptian Premier League</b> title — the first in fifteen years (since 1964-65) and the first sign of the 1980s generation that would make continental history."],
 ev=[("موسم 1977-78","الدوري المصري الممتاز — الرابع")],
 src="٣"),

dict(y=1979, tag="إفريقيا", cls="red", ar_t="أول دخول لدوري الأبطال", en_t="First Champions’ Cup Entry",
 ar=["بطل الدوري لأول مرة في دوري أبطال إفريقيا عام ١٩٧٩ (كأس الأندية الأبطلة)، وسلك طريقه حتى ربع النهائي بفضل تجاوز سيمبا الأوغندي وأوغادين أنباسا الإثيوبي وCS إيمانا الزائري قبل الخروج — أول تجربة قارية في المسابقة الكبرى بعد أول تجربة في كأس الكؤوس عام ١٩٧٦."],
 en=["As league champions, the club entered the African Champions’ Cup for the first time in 1979, reaching the quarter-finals before exiting — its first taste of the continent’s main competition."],
 ev=[("1979","أول مشاركة في كأس الأندية الأبطلة — ربع النهائي")],
 src="٤"),

dict(y=1980, tag="سجلات محدودة", cls="gray", ar_t="سنوات ما قبل الانفجار", en_t="The Years Before the Explosion",
 ar=["لا تتوافر في مصادرنا المتاحة ألقاب موثقة للنادي هذا العام؛ العقد الجديد كان يبدأ، وفريق الثمانينيات الذي سيكتب تاريخ إفريقيا كان يتشكل في صمت: جمال عبد الحميد وفاروق جعفر ومجدي طلبة وإبراهيم يوسف وحسام يكن — الأسماء التي ستظهر في نهائي ١٩٨٤ كانت في طريقها إلى القمة."],
 en=["No documented trophies this year in our sources; the new decade began and the 1980s side that would write African history was quietly forming — the names that would appear in the 1984 final were on their way to the summit."],
 src="٣"),

dict(y=1981, tag="سجلات محدودة", cls="gray", ar_t="عقد الثمانينيات يفتح بهدوء", en_t="The ’80s Open Quietly",
 ar=["لا تتوافر في مصادرنا المتاحة ألقاب موثقة للنادي هذا العام؛ سنوات ١٩٨٠-١٩٨٣ كانت سنوات بناء جيل الثمانينيات قبل انفجار الألقاب عام ١٩٨٤، وهي سنوات تشتهر سجلاتها بغياب التوثيق المستقل المفصل."],
 en=["No documented trophies this year in our sources; 1980-1983 were the building years of the golden 1980s generation before the 1984 explosion."],
 src="٣"),

dict(y=1982, tag="بطولة", cls="gold", ar_t="كأس التلفزيون والإسكندرية الصيفية", en_t="TV Cup and Summer League",
 ar=["أضاف النادي إلى خزانته <b>كأس التلفزيون المصري</b> و<b>دوري الإسكندرية الصيفي / Alexandria Summer League</b> — لقبا موسميين يوثقان نشاط الفريق الكثيف في صيف ١٩٨٢ قبل سنة الانفجار الأول."],
 en=["The club added the <b>Egyptian Television Cup</b> and the <b>Alexandria Summer League</b> — seasonal titles documenting the team’s busy 1982 summer, one year before the first explosion."],
 ev=[("1982","كأس التلفزيون + دوري الإسكندرية الصيفي")],
 src="٣"),

dict(y=1983, tag="سجلات محدودة", cls="gray", ar_t="قبل عام الأربع ألقاب", en_t="The Year Before 1984",
 ar=["لا تتوافر في مصادرنا المتاحة ألقاب موثقة للنادي هذا العام؛ موسم ١٩٨٣-٨٤ كان يبدأ وهو الموسم الذي سيصنع التاريخ: لقب الدوري الخامس وأول تاج إفريقي معًا في سنة واحدة، وهو ما يجعل ١٩٨٣ من سنوات الانتظار المثيرة في ذاكرة الجمهور."],
 en=["No documented trophies this year in our sources; the 1983-84 season — which would deliver both the fifth league title and the first African crown — was beginning."],
 src="٣"),

dict(y=1984, tag="تاج إفريقي", cls="red", ar_t="أول تاج إفريقي: القاهرة تصمت من الفرح", en_t="The First African Crown",
 ar=["سنة تاريخية بالمعنى الكامل: فاز النادي بـ<b>الدوري المصري الممتاز</b> (١٩٨٣-٨٤) بلقبه الخامس، ثم كتب أول تاج إفريقي في تاريخه في <b>كأس الأندية الأبطلة</b> تحت قيادة المدرب <b>محمود أبو رجيلة</b>. في نهائي الذهاب بالقاهرة يوم ٢٣ نوفمبر فاز ٢-٠ بثنائية <b>جمال عبد الحميد</b> (٦٠′ و٧٠′ — أحدهما بركلات جزاء وفق توثيق النهائي)، وفي لاغوس يوم ٨ ديسمبر أمام ٩٠ ألف متفرج فاز ١-٠ ليكمل المجموع ٣-٠ — ولقبه الأول أمام نادٍ ضم نجومًا مثل سيغون أوديجبامي وراشيدي يكيني. وفي اليوم التالي للعودة قامت الحكومة النيجيرية بحل فريق شوتنج ستارز احتجاجًا على «العار» — لقطة تبقى في ذاكرة القارة، وأضاف الفريق في الموسم نفسه كأس التلفزيون ودوري الإسكندرية الصيفي."],
 en=["A fully historic year: the club won its <b>fifth Egyptian Premier League</b> (1983-84) and its <b>first African Champions’ Cup</b> under coach <b>Mahmoud Abou-Regaila</b>. In the Cairo first leg (23 November) it won 2–0 with a brace from <b>Gamal Abdel Hamid</b> (60’, 70’, one a penalty), and in Lagos (8 December, 90,000 fans) 1–0 sealed a 3–0 aggregate win over a Shooting Stars side featuring Odegbami and Yekini. Nigeria’s government disbanded the losing side the next day; the club also added the TV Cup and Alexandria Summer League."],
 ev=[("موسم 1983-84","الدوري المصري — اللقب الخامس"),("23 نوفمبر 1984","نهائي الأبطال ذهابًا: الزمالك ٢-٠ شوتنج ستارز (ثنائية جمال عبد الحميد)"),("8 ديسمبر 1984","نهائي الأبطال عودةً: ١-٠ في لاغوس — التاج الإفريقي الأول (٣-٠ إجماليًا)"),("1984","كأس التلفزيون + دوري الإسكندرية الصيفي")],
 src="٣، ٤، ١٠، ٣١"),

dict(y=1985, tag="إفريقيا", cls="red", ar_t="دفاع عن التاج يتوقف عند FAR", en_t="Title Defence Falls Short",
 ar=["حاول النادي الدفاع عن تاجه الإفريقي عام ١٩٨٥ ووصل إلى نصف النهائي قبل أن يسقط أمام FAR الرباط المغربي بركلات الترجيح (٣-٤) بعد تعادل ١-١ في المجموع — محطة مؤلمة أظهرت أن طريق إفريقيا يتطلب جيلًا كاملًا لا موسمًا واحدًا."],
 en=["The club attempted to defend its African crown in 1985, reaching the semi-finals before falling to Morocco’s FAR Rabat on penalties (3–4) after a 1–1 aggregate tie."],
 ev=[("1985","كأس الأبطال — نصف النهائي (خسارة بركلات الترجيح أمام FAR الرباط)")],
 src="٤"),

dict(y=1986, tag="تاج إفريقي", cls="red", ar_t="التاج الإفريقي الثاني", en_t="The Second African Crown",
 ar=["في نوفمبر وديسمبر ١٩٨٦ رفع النادي <b>كأس الأندية الأبطلة</b> للمرة الثانية على حساب أفريقيا سبورت الإيفواري: فاز ذهابًا في القاهرة يوم ٢٨ نوفمبر ٢-٠، وخسر عودةً في أبيدجان يوم ٢١ ديسمبر بنفس النتيجة، ثم حسم التعادل ٢-٢ بركلات الترجيح ٤-٢ في ملعب فيليكس هوفويه بواني. وفي الموسم نفسه أضاف <b>كأس الصداقة المصرية</b> و<b>دورة الأردن الدولية</b> (١٩٨٥-٨٦)."],
 en=["In November-December 1986 the club lifted the African Champions’ Cup for the second time against Ivory Coast’s Africa Sports: 2–0 in Cairo, 2–0 defeat in Abidjan, then a 4–2 penalty win after a 2–2 aggregate tie. The season also brought the Egyptian Friendship Cup and the Jordan International Cup."],
 ev=[("28 نوفمبر 1986","نهائي الأبطال ذهابًا: الزمالك ٢-٠ أفريقيا سبورت"),("21 ديسمبر 1986","العودة في أبيدجان: ٢-٢ إجمالًا و٤-٢ ركلات الترجيح — التاج الثاني"),("1986","كأس الصداقة المصرية + دورة الأردن الدولية")],
 src="٣، ٤، ٩"),

dict(y=1987, tag="بطولة قارية", cls="red", ar_t="إفروآسيوية أولى ثم مباراة كوتوكو", en_t="First Afro-Asian Crown",
 ar=["بعد فوزه بكأس الأبطال، واجه النادي بطل آسيا في <b>كأس إفروآسيوية للأندية / Afro-Asian Club Championship</b> وفاز بها عام ١٩٨٧ — أول لقب إفروآسيوي في تاريخه. وفي المشوار الإفريقي الجديد سقط في ربع النهائي أمام أشانتي كوتوكو الغاني بفارق ٣-٥ في المجموع بعد فوزه ذهابًا ٢-٠ وخسارته عودةً ١-٥ — إشارة مبكرة إلى الخصم الذي سيواجهه في نهائيات لاحقة. وفي المحلية أضاف <b>دورة الأردن الدولية</b> للموسم الثاني تواليًا (١٩٨٦-٨٧)."],
 en=["Following its Champions’ Cup win, the club faced Asia’s champion in the <b>Afro-Asian Club Championship</b> and won it in 1987 — its first Afro-Asian title. In the new African campaign it fell to Ghana’s Asante Kotoko in the quarter-finals (3–5 agg.). The Jordan International Cup was retained (1986-87)."],
 ev=[("1987","كأس إفروآسيوية للأندية — أول لقب"),("1987","دورة الأردن الدولية (١٩٨٦-٨٧)")],
 src="٣، ٤"),

dict(y=1988, tag="ثنائية", cls="red", ar_t="دوري وكأس معًا", en_t="League and Cup Together",
 ar=["موسم ثنائي كامل: فاز النادي بـ<b>الدوري المصري الممتاز</b> (١٩٨٧-٨٨) للسنة السادسة وبـ<b>كأس مصر</b> (١٩٨٧-٨٨) في الموسم نفسه، وأضاف <b>كأس الاستقلال</b> و<b>كأس التحدي الدولي</b> (١٩٨٨) إلى خزانته — عام ألقاب كثيف يمهد لحملة التاج الثالث."],
 en=["A full double season: the <b>League</b> (1987-88, sixth title) and the <b>Egypt Cup</b> (1987-88) together, plus the Independence Cup and Friendship International Cup (1988) — a dense trophy year."],
 ev=[("موسم 1987-88","الدوري المصري — السادس + كأس مصر"),("1988","كأس الاستقلال + كأس التحدي الدولي")],
 src="٣"),

dict(y=1989, tag="سجلات محدودة", cls="gray", ar_t="دخول مبكر للأبطال", en_t="An Early Champions’ Exit",
 ar=["في دفاعه عن اللقب الدوري، خاض النادي كأس الأبطال ١٩٨٩ وخرج من الدور الأول بعد تعادل ٢-٢ في المجموع أمام الموردة السودانية (بحكم الأهداف خارج الأرض) — محطة قصيرة في سنوات انتقالية قبل جيل التسعينيات. لا تتوافر في مصادرنا المتاحة ألقاب موثقة أخرى لهذا العام."],
 en=["Defending its league title, the club entered the 1989 Champions’ Cup and exited in the first round against Sudan’s Al Mourada on the away-goals rule (2–2 agg.) — a brief stop in transitional years before the 1990s generation. No other documented trophies this year in our sources."],
 ev=[("1989","كأس الأبطال — الخروج من الدور الأول")],
 src="٤"),

dict(y=1990, tag="إدارة", cls="gray", ar_t="تقلب رئاسي وجيل جديد", en_t="Presidential Shifts",
 ar=["شهد النادي سلسلة تقلبات إدارية: نهاية رئاسة حسن أبو الفتوح في مايو وتولي جلال إبراهيم مؤقتًا ثم <b>نور الدالي</b> في سبتمبر ١٩٩٠. لا تتوافر في مصادرنا المتاحة ألقاب موثقة للنادي هذا العام؛ الجيل الذي سيصنع التسعينيات الذهبية كان يتشكل داخل الفريق."],
 en=["The club saw administrative shifts: Hassan Abu El-Fotouh’s presidency ended in May, Jalal Ibrahim led briefly, and <b>Nour El-Dali</b> took office in September 1990. No documented trophies this year in our sources."],
 ev=[("سبتمبر 1990","نور الدالي يتولى الرئاسة")],
 src="٢٣"),
]
