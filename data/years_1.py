# -*- coding: utf-8 -*-
# السجل السنوي 1911–1930 — بيانات فصول السنوات
# كل فصل: y=السنة، tag=الشارة، cls=لون الشارة (dark/gold/red/gray)، ar_t/en_t=العنوانان،
# ar=فقرات عربية، en=فقرات إنجليزية، ev=[(التاريخ، الحدث)]، src=أرقام المراجع

YEARS = [
dict(y=1911, tag="التأسيس", cls="dark", ar_t="بداية الحكاية", en_t="The Beginning of a Legend",
 ar=["في صباح الخامس من يناير عام ١٩١١، وضع المستشار القضائي البلجيكي <b>جورج مرزباخ / George Merzbach</b> — رجل القانون الذي أصبح لاحقًا أستاذًا في كلية الحقوق — حجر أول نادٍ رياضي جديد في القاهرة تحت اسم <b>«نادي قصر النيل» / Qasr El-Nil Club</b>. اتخذ النادى مقره على ضفة النيل في مواجهة نادي الجزيرة، وبدأ حياته نادٍ اجتماعي رياضي متعدد الأنشطة قبل أن تصبح كرة القدم لغته الأشهر. في تلك السنة نفسها كان <b>حسين هجازي / Hussein Hegazi</b> — الذي سيُعرف لاحقًا بـ«أب الكرة المصرية» — يبدأ مشواره الدراسي والكروي في لندن مع دالويتش هامليت، مشيرًا إلى مسار الكرة المصرية الذي يتشكل من الجهتين معًا."],
 en=["On 5 January 1911 the Belgian lawyer <b>George Merzbach</b> founded a new sports club in Cairo under the name <b>Qasr El-Nil Club</b>, headquartered on the Nile bank opposite the Gezira Club. In the same year, <b>Hussein Hegazi</b> — later called the “father of Egyptian football” — was starting his football adventure with Dulwich Hamlet in London."],
 ev=[("5 يناير 1911","تأسيس «نادي قصر النيل» برئاسة جورج مرزباخ")],
 src="١، ٤، ٨، ٩"),

dict(y=1912, tag="إدارة", cls="gray", ar_t="خطوات النادي الأولى", en_t="The First Steps",
 ar=["سجلات هذا العام إدارية أكثر منها كروية: وفق قائمة الرؤساء الموثقة، انتهت رئاسة هنري كرامر في ٢٨ أبريل ١٩١٢ وتولى <b>أنطوان بيانكي / Antoine Bianchi</b> القيادة، في فترة تمهيدية للتحولات الكبرى القادمة. المصادر الكروية المفصلة عن هذا العام شحيحة، ولذلك نكتفي بالتوثيق الإداري ولا نضيف حدثًا كرويًا لا مصدر له — هذا تحديدًا ما يفعله الكتاب في كل سنة صامتة عبر تاريخ النادي."],
 en=["Records for 1912 are administrative rather than footballing: per the documented presidents list, Henry Kramer’s presidency ended on 28 April and <b>Antoine Bianchi</b> took over. Detailed footballing records for this year are scarce, so the book documents the administration and nothing else — our policy for every silent year."],
 src="١، ٢٣"),

dict(y=1913, tag="هوية", cls="dark", ar_t="هوية جديدة وأول كأس", en_t="A New Identity and the First Trophy",
 ar=["عامان بعد التأسيس، تغيّر اسم النادي إلى <b>«النادي المختلط» / El Mokhtalat Club</b> — الاسم الذي يعكس طبيعة عضويته المختلطة بين المصريين والأجانب — وانتقل إلى مقر جديد حصل عليه مرزباخ عند تقاطع شارعي ٢٦ يوليو ورمسيس. وفي نفس السنة رفع الفريق أول كأس في تاريخ النادي: <b>كأس التحدي «بولانكي» / Bolanchi Challenge Cup</b>، أول سطر في سجل الخزائن الذي سيحتاج أكثر من قرن ليمتلئ."],
 en=["Two years after its birth the club was renamed <b>El Mokhtalat Club</b> — reflecting its mixed Egyptian-foreign membership — and moved to a new site at the junction of 26 July and Ramses streets. In the same year the club won its first-ever trophy: the <b>Bolanchi Challenge Cup</b>."],
 ev=[("1913","تغيير الاسم إلى «المختلط» والانتقال إلى شارع ٢٦ يوليو"),("1913","أول كأس في تاريخ النادي: كأس التحدي بولانكي")],
 src="١، ٢، ٤"),

dict(y=1914, tag="سجلات محدودة", cls="gray", ar_t="العالم يحترب والنادي يصبر", en_t="The World at War",
 ar=["اندلاع الحرب العالمية الأولى في أغسطس ١٩١٤ غيّرت حياة القاهرة كلها، وتشوشت السجلات الرياضية المفصلة عن تلك الفترة. لا تتوافر في مصادرنا المتاحة توثيق مستقل لبطولات أو مباريات محددة للنادي هذا العام، فنصارح القارئ بذلك بدلًا من ملء الصفحة بأحداث غير موثقة. المهم أن المؤسسة — ناد قصر النيل الذي صار «المختلط» — استمرت في قلبه الحربي للقاهرة."],
 en=["With the outbreak of the First World War in August 1914, life in Cairo changed and detailed sports records from the period are sparse. No independent documentation of specific matches or trophies for the club this year exists in our sources — and we say so honestly rather than fill the page with unverified events."],
 src="٢"),

dict(y=1915, tag="مفصل", cls="dark", ar_t="النواة الكروية الأولى", en_t="The Football Nucleus",
 ar=["في هذا العام وقع المفصل الذي صنع مستقبل النادي الكروي: انتقل <b>إبراهيم علام «جهينة»</b> إلى النادي ومعه فريق كامل من نادي السكة الحديد، فوجد «المختلط» أخيرًا نواة فريق كرة قدم حقيقية قادرة على المنافسة. هذه اللقطة — نقل فريق لا لاعب واحد — تشرح لماذا صار النادي خلال سنوات قليلة منافسًا للأندية الإنجليزية والإيطالية التي كانت تهيمن على الكرة المصرية آنذاك."],
 en=["The decisive moment of the club’s footballing future arrived: <b>Ibrahim Allam “Juhaina”</b> moved to the club with an entire team from Sekka El-Hadid SC, finally giving El Mokhtalat a genuine football nucleus. This explains why, within a few years, the club could challenge the foreign sides that dominated Egyptian football."],
 ev=[("1915","انتقال فريق إبراهيم علام «جهينة» من السكة الحديد إلى المختلط")],
 src="٢"),

dict(y=1916, tag="سجلات محدودة", cls="gray", ar_t="سنة صامتة في زمن الحرب", en_t="A Silent Wartime Year",
 ar=["استمرار الحرب العالمية الأولى جعل عام ١٩١٦ من أكثر سنوات الكرة المصرية صمتًا في السجلات؛ لا تتوافر في مصادرنا المتاحة تفاصيل موثقة عن نشاط النادي في هذه السنة تحديدًا، ونعيد القارئ إلى سياق الفترة: نادٍ في منتصف العقد الأول من عمره، ينمو بصمت في ظل اقتصاد الحرب، وبعض الإدارة العربية المستقلة ما زالت هدفًا قيد التفاوض داخل النادى."],
 en=["1916 remains one of the quietest years in the records; no independently documented matches or trophies for the club exist in our sources for this year. What we know is context: a club in its mid-teens, growing silently under a war economy."],
 src="٢"),

dict(y=1917, tag="ديربي", cls="red", ar_t="أول ديربي وأول صراع مصري داخل النادي", en_t="The First Derby",
 ar=["هذا العام يُسجل في تاريخ النادي مرتين: الأولى في الميدان، حين سُمح للمختلط — أول فريق مصري — بالمشاركة في <b>كأس السلطان حسين / Sultan Hussein Cup</b> التي كانت حكرًا على فرق الأجانب والعسكريين؛ والثانية في ٩ فبراير حين التقى لأول مرة بالأهلي في مباراة ودية فاز فيها الأهلي ١-٠ — ولادة <b>ديربي القاهرة / Cairo derby</b> الأشهر في إفريقيا. وداخليًا، شهد النادي معركة «التمصير»: محاولة أعضاء مصريين تشكيل مجلس إدارة مصري بقيادة محمد بدر استمرت عشرين يومًا فقط (١٧ مايو – ٦ يونيو ١٩١٧) قبل أن تتفكك بفعل ضغط الإدارة الأجنبية."],
 en=["1917 is recorded twice: El Mokhtalat became the first Egyptian club admitted to the <b>Sultan Hussein Cup</b>, and on 9 February the club met Al Ahly for the first time — a friendly lost 1–0 that marked the birth of the <b>Cairo derby</b>. Internally, the Egyptian members’ struggle produced the first Egyptian council under Mohamed Badr, which lasted just twenty days (17 May – 6 June 1917)."],
 ev=[("9 فبراير 1917","أول لقاء في تاريخ الديربي: الأهلي ١-٠ (ودي)"),("1917","أول نادٍ مصري يشارك في كأس السلطان حسين"),("مايو–يونيو 1917","أول مجلس مصري بقيادة محمد بدر يدوم ٢٠ يومًا")],
 src="٢، ٥، ٧، ٢٣"),

dict(y=1918, tag="سجلات محدودة", cls="gray", ar_t="حرب تنتهي وكرة تتعافى", en_t="War Ends, Football Recovers",
 ar=["انتهت الحرب العالمية الأولى في نوفمبر ١٩١٨، لكن كرة القدم المصرية احتاجت سنوات لتستعيد إيقاعها قبل الحرب. سجلات النادي المفصلة عن هذا العام محدودة في المصادر المتاحة؛ نكتفي بذلك القول المهم: النادي خرج من سنوات الحرب موجودًا ومنظمًا، وهو ما كان شرطًا لانفجار الألقاب القادم بعد ثلاث سنوات فقط."],
 en=["The First World War ended in November 1918, but Egyptian football needed time to recover its rhythm. Detailed records for the club this year are scarce in our sources; what matters is that the club emerged from the war years organised — the precondition for the trophy explosion that followed within three years."],
 src="٢"),

dict(y=1919, tag="سجلات محدودة", cls="gray", ar_t="ثورة ١٩١٩ وكرة تنتظر", en_t="The 1919 Revolution",
 ar=["ثورة ١٩١٩ اهتزت بها مصر كلها، وكرة القدم لم تكن استثناء من قلق البلد. لا تتوافر تفاصيل موثقة مستقلة عن موسم النادي هذا العام في المصادر المتاحة، لكن السياق مهم: النادي الذي كانت إدارته «مختلطة» بين أجانب ومصريين كان يعيش نفس الأسئلة الوطنية التي أثارها عام الثورة، وسنوات قليلة تفصله عن لقبه الأول الذي سيجعله بطلًا للمصريين جميعًا."],
 en=["The 1919 Revolution shook all of Egypt, and football was no exception. No independently documented records of the club’s season this year exist in our sources; the context matters: a club with mixed foreign-Egyptian administration living through the same national questions, three years away from its first great title."],
 src="٢"),

dict(y=1920, tag="سجلات محدودة", cls="gray", ar_t="الاستعداد للاختراق الأول", en_t="Preparing for the Breakthrough",
 ar=["عام ١٩٢٠ سنة استعداد صامتة قبل اللحظة التاريخية: كأس السلطان حسين — المسابقة الأولى الكبرى في مصر — كانت ما زالت ميدانًا للفرق الأجنبية، لكن المختلط أصبح قوة حقيقية بعد سنوات بناء فريق جهينة. السجلات المفصلة عن مباريات هذا العام محدودة في المصادر المتاحة، والقارئ سيقرأ في فصل ١٩٢١ ما جعل هذه السنوات من الاستعداد ذات معنى."],
 en=["1920 was a quiet year of preparation before the historic moment: the Sultan Hussein Cup was still a foreign-teams affair, but El Mokhtalat had become a real force after years of building. Detailed match records for this year are scarce; the meaning of these years of preparation becomes clear in the 1921 chapter."],
 src="٢"),

dict(y=1921, tag="لقب تاريخي", cls="gold", ar_t="أول فريق مصري يرفع كأسًا", en_t="The First Egyptian Champions",
 ar=["في موسم ١٩٢٠-٢١ كتب النادي واحدة من أهم صفحات الكرة المصرية كلها: فاز <b>المختلط</b> بـ<b>كأس السلطان حسين / Sultan Hussein Cup</b>، ليصبح <b>أول فريق مصري في التاريخ يفوز بلقب رسمي</b> في مسابقة كانت حكرًا على الأجانب. لم يكن اللقب مجرد كأس؛ كان إعلانًا بأن الكرة المصرية انقطعت عن التبعية، وأن النادي صار صوت الأمل الرياضي للجمهور المصري الذي كان يضيق بذات فرق الجاليات."],
 en=["In 1920-21 El Mokhtalat wrote one of the most important pages in all of Egyptian football: it won the <b>Sultan Hussein Cup</b>, becoming <b>the first Egyptian team in history to win an official title</b> in a competition previously monopolised by foreign sides."],
 ev=[("موسم 1920-21","أول لقب في تاريخ الكرة المصرية لفريق مصري: كأس السلطان حسين")],
 src="١، ٢، ٤"),

dict(y=1922, tag="لقب تاريخي", cls="gold", ar_t="أول كأس مصر في التاريخ", en_t="The First Ever Egypt Cup",
 ar=["عام ١٩٢٢ سنة التاج المزدوج: النادي فاز بـ<b>كأس مصر / Egypt Cup</b> في أول نسخة من المسابقة على الإطلاق (موسم ١٩٢١-٢٢)، وكرر الفوز بـ<b>كأس السلطان حسين</b> للمرة الثانية، ثم بدأ موسم ١٩٢٢-٢٣ الذي سيمنه أول بطولة لمنطقة القاهرة. بهذه الألقاب المتتالية تحول «المختلط» من مفاجأة صاعدة إلى رأس الهرم الكروي في مصر، وبدأت ثنائية الأهلي والزمالك التي ستسيطر على جداول الأبطال قرنًا كاملًا."],
 en=["1922 was a year of double crowns: the club lifted the very first <b>Egypt Cup</b> in history (1921-22) and won the Sultan Hussein Cup again, before the 1922-23 season brought its first Cairo League title. El Mokhtalat had turned from rising surprise into Egyptian football’s summit — the Ahly-Zamalek duopoly had begun."],
 ev=[("موسم 1921-22","أول كأس مصر في تاريخ المسابقة"),("موسم 1921-22","كأس السلطان حسين للمرة الثانية")],
 src="٣، ٤"),

dict(y=1923, tag="سجلات محدودة", cls="gray", ar_t="استقرار بعد التاج", en_t="After the Crown",
 ar=["بعد عامين من التتويج المتتالي، عاد ١٩٢٣ إلى الصمت النسبي في السجلات المتاحة — عدا تفصيلة من تاريخ الديربي: أول هاتريك موثق في مواجهات الناديين سجله <b>صادق فهمي / Sadek Fahmy</b> في مباراة ودية بتاريخ ٥ يناير ١٩٢٣ (بحسب توثيق صفحة الديربي). أما بطولات الموسم الرسمية فلا تتضمن اسم المختلط هذا العام، والقارئ يعرف الآن أن صمت سجلاتنا لا يعني صمت الميدان."],
 en=["After two consecutive crowns, 1923 returns to relative silence in the available records — except one derby detail: the first documented hat-trick in the clubs’ meetings was scored by <b>Sadek Fahmy</b> in a friendly on 5 January 1923. No official trophies this season; our silence in the records is not silence on the pitch."],
 ev=[("5 يناير 1923","أول هاتريك موثق في تاريخ الديربي: صادق فهمي (ودي)")],
 src="٥، ٧"),

dict(y=1924, tag="لقب شعبي", cls="dark", ar_t="«قاهر الأجانب»", en_t="The Conqueror of Foreigners",
 ar=["في هذا العام حصل النادي على أشهر ألقابه غير الرسمية: بعد سلسلة انتصارات على فرق الجاليات الأجنبية، أهدى الجمهور المختلط لقب <b>«قاهر الأجانب»</b>. وفي السياق نفسه انتقل النادى إلى مقره الثالث قرب كوبري الزمالك في الموقع الذي يشغله اليوم مسرح البالون — آخر محطات في مسار النادي داخل الجزيرة قبل نزوله إلى ميت عقبة بعد ثلاثة عقود."],
 en=["In 1924 the club earned its most famous unofficial title: after a string of victories over foreign community teams, fans hailed El Mokhtalat as <b>“Qahir al-Aganib” — the Conqueror of Foreigners</b>. The same period brought a third headquarters move, near the Zamalek bridge at today’s Balloon Theatre site."],
 ev=[("1924","لقبه الجديد: «قاهر الأجانب» بعد انتصاراته على فرق الأجانب"),("1924","الانتقال إلى المقر الثالث قرب كوبري الزمالك")],
 src="١، ٢"),

dict(y=1925, tag="بطولة", cls="gold", ar_t="كأس الملك فؤاد الأولى", en_t="First King Fouad Cup",
 ar=["افتتح النادي عصرًا جديدًا من البطولات الملكية بفوزه بأول <b>كأس الملك فؤاد / King Fouad Cup</b> عام ١٩٢٥ — المسابقة التي ستكرر اسمه في خزانة النادي مرتين أخريين (١٩٣٤ و١٩٤١). السجلات المفصلة عن مسار البطولة ومبارياته محدودة في مصادرنا المتاحة، لكن حصوله على اللقب موثق في قوائم الألقاب، وهو أول لقب للنادي يحمل اسم ملك مصر."],
 en=["The club opened a new era of royal-era trophies by winning the first <b>King Fouad Cup</b> in 1925 — a competition it would win twice more (1934 and 1941). Detailed match records are limited, but the title itself is documented in the honours registers."],
 ev=[("1925","كأس الملك فؤاد للمرة الأولى")],
 src="٣"),

dict(y=1926, tag="سجلات محدودة", cls="gray", ar_t="سنوات بين البطولات", en_t="Between Trophies",
 ar=["لا تتوافر في مصادرنا المتاحة ألقاب أو أحداث موثقة مستقلة للنادي في هذا العام؛ سنوات العشرينيات كانت تنقل القاهرة بين مواسم بطولة القاهرة وكأس مصر ودورات الملك، والنادي كان يعيش فترة استقرار بين موجات التتويج. نصارح بحدود السجلات كما هي، ونجمع في فصل ١٩٢٧ التغيير الإداري الكبير."],
 en=["No independently documented trophies or events for the club this year exist in our sources; the 1920s alternated between Cairo League seasons, Egypt Cups and King Fouad tournaments, and the club lived a period of consolidation between waves of titles."],
 src="٣"),

dict(y=1927, tag="إدارة", cls="gray", ar_t="بداية عصر حيدر باشا", en_t="The Haidar Pasha Era Begins",
 ar=["تشكّل في هذا العام مجلس إدارة جديد برئاسة الجنرال <b>محمد حيدر باشا / Mohamed Haidar Pasha</b> — وزير الحربية سابقًا — الذي سيصبح في نهاية المطاف أطول رؤساء النادي خدمة على الإطلاق. تختلف المصادر في تأريخ بداية رئاسته الفعلية (١٩٢٣ أو ١٩٢٧)، لكن التشكيل الموثق لمجلسه هذا العام يجعل ١٩٢٧ نقطة البدء المثبتة في قائمة الرؤساء."],
 en=["A new council formed under General <b>Mohamed Haidar Pasha</b>, former minister of war — destined to become the longest-serving president in the club’s history. Sources differ on when his effective presidency began (1923 or 1927); the documented 1927 council is the fixed start point in the presidents list."],
 ev=[("1927","تشكيل مجلس جديد برئاسة محمد حيدر باشا")],
 src="٢٣"),

dict(y=1928, tag="بطولة", cls="gold", ar_t="رحيل المؤسس ولقب القاهرة", en_t="Farewell to the Founder",
 ar=["سنة متضاربة المشاعر: في ١٧ فبراير رحل <b>جورج مرزباخ</b> — المؤسس الذي عاد لرئاسة النادي عام ١٩٢١ — عن القاهرة بعمر ٥٣ عامًا، تاركًا مؤسسته تستمر بعد وفاته قرنًا ونصفًا. وفي الميدان فاز النادي بـ<b>بطولة منطقة القاهرة</b> موسم ١٩٢٨-٢٩، أول ألقاب بطولة القاهرة بعد لقب ١٩٢٢-٢٣، وبداية سلسلة الثلاثينيات التي ستحكم بها القلعة كرة القاهرة."],
 en=["A bittersweet year: on 17 February <b>George Merzbach</b> died in Cairo at 53, leaving behind an institution that would outlive him by more than a century. On the pitch, the club won the <b>Cairo League</b> (1928-29) — its first since 1922-23 and the start of a title-rich late 1920s."],
 ev=[("17 فبراير 1928","وفاة المؤسس جورج مرزباخ في القاهرة"),("موسم 1928-29","بطولة منطقة القاهرة")],
 src="٦، ٨، ٣"),

dict(y=1929, tag="بطولة", cls="gold", ar_t="ثنائية القاهرة", en_t="Back-to-Back in Cairo",
 ar=["كرر النادي الفوز بـ<b>بطولة منطقة القاهرة</b> في موسم ١٩٢٩-٣٠ مباشرة بعد لقب ١٩٢٨-٢٩، ليؤكد أن سيادة القلعة البيضاء على كرة القاهرة لم تكن صدفة سنة واحدة. السجلات المفصلة عن مباريات هذا الموسم محدودة في المصادر المتاحة، لكن التتويج الموثق يكفي ليؤكد أن الثلاثينيات ستفتح على قلعة مطمئنة في عهد حيدر باشا."],
 en=["The club retained the <b>Cairo League</b> title in 1929-30, confirming its rule over Cairo football was no one-season accident. Detailed match records are limited, but the documented back-to-back crowns speak clearly."],
 ev=[("موسم 1929-30","بطولة منطقة القاهرة للمرة الثانية تواليًا")],
 src="٣"),

dict(y=1930, tag="إدارة", cls="gray", ar_t="حيدر باشا يعود", en_t="Haidar Pasha Returns",
 ar=["في يوليو ١٩٣٠ عاد <b>محمد حيدر باشا</b> إلى رئاسة النادي بعد سلسلة رئاسات متقلبة قصيرة (عمر إبراهيم حليم، عباس حليم، عمر حليم)، لتبدأ من هنا الفترة الطويلة التي ستمتد — بلا انقطاع جوهري — حتى ١٨ سبتمبر ١٩٥٢. السجلات الكروية المفصلة عن هذا الموسم محدودة في المصادر المتاحة؛ المهم أن القيادة أصبحت مستقرة تاريخيًّا."],
 en=["In July 1930 <b>Mohamed Haidar Pasha</b> returned to the presidency after a run of short-lived leaders, beginning the long tenure that would last — without essential interruption — until 18 September 1952. Detailed footballing records for the season are limited; what matters is that leadership had become historically stable."],
 ev=[("يوليو 1930","عودة حيدر باشا إلى الرئاسة")],
 src="٢٣"),
]
