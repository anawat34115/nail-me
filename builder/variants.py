# web-dev/freelance/websites/nail-me/builder/variants.py
# สร้าง design2.html (โครงตาม seeunail.com) และ design3.html (โครงตาม nailgarden.com) จาก index.html
# เนื้อหา/i18n/JS ใช้ร่วมกัน ต่างกันที่โทนสี ฟอนต์ และเลย์เอาต์ของ hero / โปร / บริการ / ผลงาน / จองคิว
# ใช้: python builder/variants.py  (รันจากโฟลเดอร์ websites/nail-me)
import re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'index.html'

def section(html, n):
    """คืน (start, end) ของ section ที่ขึ้นต้นด้วย <!-- ===== n. """
    m = re.search(r'    <!-- ===== %d\. .*?=====\s*-->\n' % n, html)
    assert m, n
    end = html.index('    </section>\n', m.start()) + len('    </section>\n')
    return m.start(), end

def swap(html, n, new):
    a, b = section(html, n)
    return html[:a] + new + html[b:]

def sub_colors(html, colors, fonts, body_bg):
    # tailwind config
    html = re.sub(r"colors: \{.*?\n          \}", "colors: {\n            " + ", ".join(f"'{k}': '{v}'" for k, v in colors.items()) + "\n          }", html, flags=re.S)
    html = re.sub(r":root \{\n      --blush.*?--line:#[0-9A-Fa-f]{6};", ":root {\n      " + " ".join(f"--{k}:{v};" for k, v in colors.items()), html, flags=re.S)
    html = html.replace("display: ['\"Cormorant Garamond\"', '\"Noto Serif Thai\"', 'serif'],\n            body: ['\"IBM Plex Sans Thai\"', 'sans-serif']", fonts['tw'])
    html = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/css2\?[^"]+">', fonts['link'], html)
    html = html.replace('"Cormorant Garamond", serif', fonts['display_css']).replace('"IBM Plex Sans Thai", sans-serif', fonts['body_css'])
    html = html.replace('<body class="bg-blush text-ink font-body antialiased">', f'<body class="{body_bg} text-ink font-body antialiased">')
    return html

# ---------------------------------------------------------------- แบบ 2: "Private & Calm" (โครงตาม seeUnail.com: hero รูปเต็ม+tagline → โปรเป็นแบนเนอร์ → บริการการ์ดรูป+ราคา → เช็กลิสต์จุดเด่น → แกลเลอรีแน่น → รีวิวคะแนน → "กรุณาจองคิว" → SEO)
D2_COLORS = {
    'blush': '#F4EFE9',      # พื้นเบจอุ่น
    'cream': '#FFFDFA',
    'rose': '#E9DDD3',       # เบจชมพู (placeholder)
    'pink': '#B98C7A',       # น้ำตาลชมพู (hover)
    'pink-deep': '#6B4A3E',  # น้ำตาลโกโก้อ่อน = ปุ่มหลัก/ราคา
    'gold': '#C9A24B', 'gold-deep': '#8F6D22', 'gold-light': '#E9D7A5',
    'ink': '#2E2622', 'muted': '#6C5F58', 'cocoa': '#3A2A24', 'line': '#E2D8CF',
}
D2_FONTS = {
    'tw': "display: ['\"Cormorant Garamond\"', '\"Noto Serif Thai\"', 'serif'],\n            body: ['\"Noto Sans Thai\"', 'sans-serif']",
    'link': '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Noto+Serif+Thai:wght@500;600&family=Noto+Sans+Thai:wght@300;400;500&display=swap">',
    'display_css': '"Cormorant Garamond", serif', 'body_css': '"Noto Sans Thai", sans-serif',
}
PHO = lambda k: f'https://lh3.googleusercontent.com/d/{k}=w1200'
P_HAND = PHO('15XJ6vhagHu2wiS42nPKwGygAmkw32Ddo'); P_FEET = PHO('1PJcpMwC7X_qX3z4oiqHcDRZhIesSawyU'); P_CAT = PHO('1IL1Bl3lZf0EJge_MZ1uISRHAorFu3-7n')
P_PVC = PHO('1Oei9dUjojxuSW-H6natRzdzBWvKEZrLM'); P_FSPA = PHO('1L0eg8f7cFxLhymha1i9WO9aAN6N9W_Um'); P_HSPA = PHO('1bbEwPtwzzEIAQPlsJBp3Yin35wcx4Ipo')
P_ART = PHO('1pntTSKYGk-EFayT3rF-0HT8P55UZXQ5F'); P_GLIT = PHO('1YmKe5tEzvpZkWJGLssCTW6MaXt49mOmg')

D2_CSS = """
    /* แบบ 2: การ์ดบริการมีรูป + เช็กลิสต์ */
    .svc-card { background: var(--cream); border: 1px solid var(--line); border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
    .svc-card .ph { aspect-ratio: 4 / 3; overflow: hidden; }
    .svc-card .body { padding: 20px; display: flex; flex-direction: column; gap: 4px; flex: 1; }
    .svc-card .pr { font-family: "Cormorant Garamond", serif; font-weight: 600; font-size: 28px; color: var(--pink-deep); line-height: 1; }
    .check { display: flex; gap: 12px; padding: 10px 0; border-top: 1px solid var(--line); }
    .check i { color: var(--pink-deep); font-size: 20px; flex: none; margin-top: 4px; }
    .hero-dim { background: linear-gradient(180deg, rgba(46,38,34,.25) 0%, rgba(46,38,34,.55) 100%); }
"""

D2_HERO = f"""    <!-- ===== 1. Hero: รูปเต็มจอ ข้อความกลาง (โครงตาม seeUnail) ===== -->
    <section id="top" class="relative text-cream overflow-hidden min-h-[560px] md:min-h-[640px] flex items-center">
      <img src="{P_HAND}" alt="" class="absolute inset-0 w-full h-full object-cover" width="900" height="1200" fetchpriority="high" decoding="async">
      <div class="absolute inset-0 hero-dim" aria-hidden="true"></div>
      <div class="relative mx-auto max-w-[800px] px-4 md:px-8 py-20 md:py-28 text-center">
        <p class="label !text-gold-light" data-stagger style="--d:0ms" data-i18n="hero.eyebrow">ร้านทำเล็บ สุราษฎร์ธานี · ข้างตลาดศาลเจ้า</p>
        <h1 class="font-display font-semibold text-[clamp(44px,8vw,88px)] mt-4 leading-[1.05]" data-stagger style="--d:120ms">
          <span data-i18n="hero.title1">ร้านหรู</span> <span class="text-gold-light whitespace-nowrap" data-i18n="hero.title2">แต่ราคาน่ารัก</span>
        </h1>
        <p class="text-cream/90 mt-6 max-w-[30em] mx-auto text-[17px] md:text-[19px]" data-stagger style="--d:240ms" data-i18n="hero.sub">Nail Me ร้านทำเล็บ สปาเท้า สปามือ และสระไดร์ ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สีเจลให้เลือกกว่า 100 เฉด ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน</p>
        <div class="flex flex-wrap justify-center gap-4 mt-8" data-stagger style="--d:360ms">
          <a class="btn btn-lg bg-cream text-pink-deep hover:bg-gold-light" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
          <a class="btn btn-lg btn-on-dark" href="https://m.me/nailmesuratthani" target="_blank" rel="noopener" data-track="message"><i class="ph ph-messenger-logo" aria-hidden="true"></i><span data-i18n="cta.line">ทักเพจ</span></a>
        </div>
        <p class="mt-8 text-[15px] text-cream/80" data-stagger style="--d:480ms"><span data-i18n="hero.hours">เปิดทุกวัน 09:00–21:00</span> · <span data-i18n="hero.walkin">จองคิวหรือ walk-in</span> · <a href="tel:+66646542666" data-track="call" class="text-gold-light underline underline-offset-4">064-654-2666</a></p>
      </div>
    </section>
"""

D2_PROMO = f"""    <!-- ===== 2. โปรโมชั่น: แบนเนอร์ 2 ใบ (ตาม seeUnail ที่โปรเป็นรูปแบนเนอร์) ===== -->
    <section id="promo" class="py-14 md:py-20" aria-labelledby="promo-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="flex flex-wrap items-baseline justify-between gap-4 reveal">
          <div><p class="label" data-i18n="promo.label">โปรเดือนนี้</p><h2 id="promo-title" class="font-display font-semibold text-[28px] md:text-[36px] mt-1" data-i18n="promo.title">แคปโพสต์โปร ให้ช่างก่อนรับบริการ</h2></div>
          <a class="text-[15px] underline decoration-gold underline-offset-4 hover:text-pink-deep" href="https://www.facebook.com/profile.php?id=61580350351076" target="_blank" rel="noopener" data-track="facebook" data-i18n="promo.cta">ดูโพสต์โปรบนเพจ</a>
        </div>
        <div class="grid md:grid-cols-2 gap-6 mt-8 reveal">
          <div class="relative overflow-hidden rounded-lg aspect-[16/9] bg-pink-deep text-cream">
            <img src="{P_GLIT}" alt="" class="absolute inset-0 w-full h-full object-cover opacity-50" loading="lazy" decoding="async" width="900" height="1200">
            <div class="relative p-6 md:p-8 h-full flex flex-col justify-end"><p class="num text-[56px] md:text-[72px] leading-none">฿200</p><p class="mt-2 text-[15px]" data-i18n="promo.p0">ทาสีเจล ตัดแต่งหนังฟรี <span class="line-through opacity-70">250</span></p></div>
          </div>
          <div class="relative overflow-hidden rounded-lg aspect-[16/9] bg-cocoa text-cream">
            <img src="{P_FSPA}" alt="" class="absolute inset-0 w-full h-full object-cover opacity-50" loading="lazy" decoding="async" width="900" height="1200">
            <div class="relative p-6 md:p-8 h-full flex flex-col justify-end"><p class="num text-[56px] md:text-[72px] leading-none">฿450</p><p class="mt-2 text-[15px]" data-i18n="promo.p1">สปาเท้า 9 ขั้นตอน <span class="line-through opacity-70">499</span></p><p class="text-[14px] text-cream/80 mt-1"><span class="num text-[20px]">฿150</span> <span data-i18n="promo.p2">สระไดร์ ทุกความยาว</span></p></div>
          </div>
        </div>
      </div>
    </section>
"""

def d2_card(img, alt, key_t, t, key_d, d, price):
    return f"""          <article class="svc-card">
            <div class="ph"><img src="{img}" alt="{alt}" class="photo" loading="lazy" decoding="async" width="900" height="1200"></div>
            <div class="body"><h3 class="font-display font-semibold text-[22px]" data-i18n="{key_t}">{t}</h3><p class="text-[14px] text-muted" data-i18n="{key_d}">{d}</p><p class="pr mt-auto pt-3">{price}</p></div>
          </article>
"""

D2_SERVICES = f"""    <!-- ===== 3. บริการและราคา: การ์ดรูป+ราคา (ตาม seeUnail) + เมนูเต็มด้านล่าง ===== -->
    <section id="services" class="bg-cream border-y border-line py-14 md:py-20 lg:py-24" aria-labelledby="services-title">
      <div id="menu" class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="text-center max-w-[640px] mx-auto reveal">
          <p class="label">Our services</p>
          <h2 id="services-title" class="font-display font-semibold text-[clamp(36px,5vw,56px)] mt-2" data-i18n="services.title">บริการและราคา</h2>
          <p class="mt-4 text-muted" data-i18n="services.intro">ทาสีเจล ต่อเล็บ ดูแลเล็บมือ-เท้า และสปา ราคาปกติตามป้ายราคาในร้าน ช่วงโปรโมชั่นถูกกว่านี้ ดูที่โปรเดือนนี้</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-10 reveal">
{d2_card(P_HAND,'ทาสีเจลมือ ผลงาน Nail Me','s.gelh','ทาสีเจลมือ','s.gelh.d','สีเจลคุณภาพดี ติดทน 1–3 เดือน เลือกได้กว่า 100 เฉด','฿250')}{d2_card(P_FEET,'ทาสีเจลเท้า ผลงาน Nail Me','s.gelf','ทาสีเจลเท้า','s.gelf.d','สีสวย เงางาม แห้งไว ไม่ทำลายหน้าเล็บ','฿300')}{d2_card(P_CAT,'เล็บเจลปลายโครม ผลงาน Nail Me','s.cat','สีลูกแก้ว Cat Eye','s.cat.d','เจลแม่เหล็ก ประกายลึกเหมือนตาแมว','฿350')}{d2_card(P_PVC,'ต่อเล็บ PVC ผลงาน Nail Me','s.pvc','ต่อเล็บ PVC','s.pvc.d','ต่อเล็บยาวสวยเป็นธรรมชาติ เจลเว้นโคน','฿350')}{d2_card(P_FSPA,'สปาเท้า ผลงาน Nail Me','s.fspa','สปาเท้า 10&nbsp;<span class="whitespace-nowrap">ขั้นตอน</span>','s.fspa.d','ขัดถึงใต้เข่า แช่ ขัด มาร์ก นวด บำรุง <a href="#spa" class="underline decoration-gold underline-offset-4" data-i18n="s.steps">ดูขั้นตอน</a>','฿499')}{d2_card(P_HSPA,'สปามือ ผลงาน Nail Me','s.hspa','สปามือ 9&nbsp;<span class="whitespace-nowrap">ขั้นตอน</span>','s.hspa.d','บำรุงล้ำลึก ผ่อนคลายสุดมือ','฿399')}        </div>
        <div class="grid md:grid-cols-2 gap-x-12 gap-y-2 mt-12 max-w-[960px] mx-auto text-[15px] reveal">
          <div class="flex justify-between gap-4 py-3 border-t border-line"><span data-i18n="s.ov1">เสริมหน้าเล็บหลังทาสี</span><span class="num text-[20px] text-pink-deep">฿150</span></div>
          <div class="flex justify-between gap-4 py-3 border-t border-line"><span data-i18n="s.ov2">เสริมหน้าเล็บก่อนทาสี</span><span class="num text-[20px] text-pink-deep">฿450</span></div>
          <div class="flex justify-between gap-4 py-3 border-t border-line"><span data-i18n="s.mani">Manicure / Pedicure</span><span class="num text-[20px] text-pink-deep">฿200</span></div>
          <div class="flex justify-between gap-4 py-3 border-t border-line"><span data-i18n="s.rem.d">ถอดแล้วทำต่อที่ร้าน เจล 50 · PVC 100 · ถอดอย่างเดียว 100</span><span class="num text-[20px] text-pink-deep whitespace-nowrap"><small class="font-body text-[12px] font-normal text-muted mr-1" data-i18n="from">เริ่ม</small>฿50</span></div>
          <div class="md:col-span-2 flex justify-between gap-4 py-3 border-y border-line"><span><span data-i18n="s.art">งานเพ้นท์ คิดเพิ่มต่อนิ้ว</span> · <span class="text-muted" data-i18n="s.art.d">เพ้นท์ลาย +20 · เฟรนช์ปลาย +30 · ออมเบร +30 · ติดอะไหล่ +20 · ปั้นนูน +50</span></span><span class="num text-[20px] text-pink-deep whitespace-nowrap"><small class="font-body text-[12px] font-normal text-muted mr-1" data-i18n="from">เริ่ม</small>฿20</span></div>
        </div>
        <p class="mt-6 text-[14px] text-muted text-center" data-i18n="services.note">ราคาตามป้ายราคาในร้าน (ต.ค. 2569) · บริการผม ขนตา แว็กซ์ สอบถามทางโทรศัพท์หรือเพจ</p>
        <div class="text-center mt-8 reveal"><a class="btn btn-pink btn-lg" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a></div>
      </div>
    </section>
"""

D2_WHY = f"""    <!-- ===== 5. จุดเด่น: เช็กลิสต์ (ตาม seeUnail) ใช้เฉพาะข้อที่ร้านยืนยันจริง ===== -->
    <section id="why" class="py-14 md:py-20 lg:py-24" aria-labelledby="why-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8 grid lg:grid-cols-12 gap-10 lg:gap-16 items-center">
        <div class="lg:col-span-5 order-2 lg:order-1 reveal">
          <div class="aspect-[4/5] overflow-hidden rounded-lg"><img src="{P_ART}" alt="ผลงานเล็บเฟรนช์ปลายลายดอกไม้ จากร้าน Nail Me" class="photo" loading="lazy" decoding="async" width="900" height="1200"></div>
        </div>
        <div class="lg:col-span-7 order-1 lg:order-2 reveal">
          <h2 id="why-title" class="font-display font-semibold text-[clamp(32px,4.5vw,48px)]" data-i18n="why.title">เราจะดูแลคุณอย่างดี เพราะคุณคือคนพิเศษ</h2>
          <p class="mt-4 text-muted" data-i18n="why.sub">คำสัญญาที่เขียนไว้ท้ายป้ายราคาของร้าน และเป็นเหตุผลที่ลูกค้ากลับมา</p>
          <ul class="mt-8">
            <li class="check"><i class="ph-fill ph-check-circle" aria-hidden="true"></i><div><strong class="font-medium" data-i18n="w1">ดูแลให้หลังทำ ไม่ทิ้งงาน</strong><p class="text-[14px] text-muted" data-i18n="w1.d">ทำแล้วมีปัญหา กลับมาให้ช่างดูได้ ร้านดูแลต่อให้</p></div></li>
            <li class="check"><i class="ph-fill ph-check-circle" aria-hidden="true"></i><div><strong class="font-medium" data-i18n="w2">สีเจลกว่า 100 เฉด</strong><p class="text-[14px] text-muted" data-i18n="w2.d">สายหวาน มินิมอล แฟชั่น สีลูกแก้ว ช่างช่วยเลือกสีให้เข้ากับคุณ</p></div></li>
            <li class="check"><i class="ph-fill ph-check-circle" aria-hidden="true"></i><div><strong class="font-medium" data-i18n="w3">ราคาชัดตามป้าย ไม่มีบวกเพิ่ม</strong><p class="text-[14px] text-muted" data-i18n="w3.d">ราคาทุกบริการติดไว้หน้าร้าน งานเพ้นท์คิดเพิ่มต่อนิ้วตามป้าย</p></div></li>
            <li class="check"><i class="ph-fill ph-check-circle" aria-hidden="true"></i><div><strong class="font-medium" data-i18n="w4">ใจกลางเมือง มาง่าย</strong><p class="text-[14px] text-muted" data-i18n="w4.d">ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน เยื้อง Tops</p></div></li>
            <li class="check border-b border-line"><i class="ph-fill ph-check-circle" aria-hidden="true"></i><div><strong class="font-medium" data-i18n="w5">ยินดีต้อนรับนักท่องเที่ยว</strong><p class="text-[14px] text-muted" data-i18n="w5.d">We welcome both Thai customers and international travellers.</p></div></li>
          </ul>
          <!-- TODO: เช็กลิสต์ความสะอาด (ฆ่าเชื้ออุปกรณ์ ฯลฯ) ใส่ได้เมื่อร้านยืนยัน -->
          <a class="btn btn-pink btn-lg mt-8" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
        </div>
      </div>
    </section>
"""

D2_GALLERY = """    <!-- ===== 6. ผลงาน: กริดแน่น ขนาดเท่ากัน (ตาม seeUnail) ===== -->
    <section id="gallery" class="bg-cream border-y border-line py-14 md:py-20" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="text-center mb-8 reveal">
          <h2 id="gallery-title" class="font-display font-semibold text-[clamp(32px,4.5vw,48px)]" data-i18n="gallery.title">ผลงานจากร้าน</h2>
          <a class="inline-block mt-2 text-[15px] underline decoration-gold underline-offset-4 hover:text-pink-deep" href="https://www.facebook.com/nailmesuratthani" target="_blank" rel="noopener" data-track="facebook" data-i18n="gallery.more">ดูผลงานล่าสุดบนเพจ</a>
        </div>
        <div class="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-2 md:gap-3 reveal">
__PHOTOS__
        </div>
      </div>
    </section>
"""

D2_REVIEWS = """    <!-- ===== 7. รีวิว: คะแนนใหญ่ + รายการรีวิว (ตาม seeUnail) ===== -->
    <section id="reviews" class="py-14 md:py-20 lg:py-24" aria-labelledby="reviews-title">
      <div class="mx-auto max-w-[800px] px-4 md:px-8 text-center">
        <h2 id="reviews-title" class="label" data-i18n="reviews.title">รีวิวจากลูกค้า</h2>
        <p class="num text-[72px] md:text-[96px] leading-none text-pink-deep mt-4 reveal">100%</p>
        <p class="text-muted reveal" data-i18n="stat.0">แนะนำ จาก 6 รีวิวบนเพจ</p>
        <figure class="mt-10 reveal">
          <blockquote class="font-display font-medium text-[clamp(24px,3.5vw,36px)] leading-[1.4]" data-i18n="r1.quote">“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”</blockquote>
          <figcaption class="mt-4 text-[15px] text-muted" data-i18n="r1.name">ปฐมาวดี ชูมี · รีวิวบนเพจ Facebook 17 ก.ค. 2569 · เล็บเจล</figcaption>
        </figure>
        <dl class="grid grid-cols-2 gap-6 mt-10 max-w-[400px] mx-auto reveal">
          <div><dt class="num text-[32px] leading-none text-pink-deep">1,000+</dt><dd class="mt-1 text-[14px] text-muted" data-i18n="stat.1">ผู้ติดตามเพจหลัก</dd></div>
          <div><dt class="num text-[32px] leading-none text-pink-deep">100+</dt><dd class="mt-1 text-[14px] text-muted" data-i18n="stat.2">เฉดสีเจลให้เลือก</dd></div>
        </dl>
        <a class="inline-flex items-center gap-2 mt-8 text-[15px] underline decoration-gold underline-offset-4 hover:text-pink-deep reveal" href="https://www.facebook.com/profile.php?id=61580350351076" target="_blank" rel="noopener" data-track="facebook"><span data-i18n="reviews.more">อ่านรีวิวทั้งหมดบนเพจ</span><i class="ph ph-arrow-up-right" aria-hidden="true"></i></a>
      </div>
    </section>
"""

D2_BOOKING = """    <!-- ===== 8. กรุณาจองคิว (ตาม seeUnail "Please make a reservation") + 3 ขั้นตอน ===== -->
    <section id="booking" class="bg-pink-deep text-cream py-14 md:py-20" aria-labelledby="booking-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8 text-center">
        <p class="label !text-gold-light" data-i18n="bk.label">Please make a reservation</p>
        <h2 id="booking-title" class="font-display font-semibold text-[clamp(32px,4.5vw,48px)] mt-2 reveal" data-i18n="bk.title">จองคิวง่าย ๆ 3&nbsp;<span class="whitespace-nowrap">ขั้นตอน</span></h2>
        <ol class="mt-10 grid md:grid-cols-3 gap-8 md:gap-12 text-left reveal">
          <li class="border-t border-cream/30 pt-4"><p class="num text-[40px] text-gold-light leading-none">1</p><h3 class="font-display font-semibold text-[24px] mt-3" data-i18n="bk.1">โทรหรือทักเพจ</h3><p class="mt-2 text-[15px] text-cream/80" data-i18n="bk.1.d">บอกบริการที่อยากทำและเวลาที่สะดวก ร้านตอบกลับเร็ว</p></li>
          <li class="border-t border-cream/30 pt-4"><p class="num text-[40px] text-gold-light leading-none">2</p><h3 class="font-display font-semibold text-[24px] mt-3" data-i18n="bk.2">เลือกสีและลายหน้าร้าน</h3><p class="mt-2 text-[15px] text-cream/80" data-i18n="bk.2.d">มีสีเจลกว่า 100 เฉดให้ลอง ช่างช่วยแนะนำ ส่งรูปลายที่ชอบมาก่อนได้</p></li>
          <li class="border-t border-cream/30 pt-4"><p class="num text-[40px] text-gold-light leading-none">3</p><h3 class="font-display font-semibold text-[24px] mt-3" data-i18n="bk.3">มาถึงร้าน ใช้โปรได้เลย</h3><p class="mt-2 text-[15px] text-cream/80" data-i18n="bk.3.d">แคปโพสต์โปรให้ช่างดูก่อนรับบริการ walk-in ก็ได้ถ้าคิวว่าง</p></li>
        </ol>
        <div class="flex flex-wrap justify-center gap-4 mt-10 reveal">
          <a class="btn btn-lg bg-cream text-pink-deep hover:bg-gold-light" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
          <a class="btn btn-lg btn-on-dark" href="https://m.me/nailmesuratthani" target="_blank" rel="noopener" data-track="message"><i class="ph ph-messenger-logo" aria-hidden="true"></i><span data-i18n="cta.line">ทักเพจ</span></a>
        </div>
      </div>
    </section>
"""

# ---------------------------------------------------------------- แบบ 3: "Garden" (โครงตาม nailgarden.com: hero รูป+ข้อความกลาง → "เลือกบริการ" การ์ดเลข 01/02/03 → เรื่องร้าน รูป+ข้อความ → เมนู → แกลเลอรี 6 รูป → รีวิว → CTA ปิดกลางหน้า · ลิงก์ข้อความ "→" · ป้าย eyebrow)
D3_COLORS = {
    'blush': '#F7F5F0',      # กระดาษ
    'cream': '#FFFFFF',
    'rose': '#DFE6DC',       # เขียวอ่อน
    'pink': '#6E8A74',       # เซจ
    'pink-deep': '#476650',  # เขียวสวน = ปุ่มหลัก/ราคา
    'gold': '#B99A5B', 'gold-deep': '#86703A', 'gold-light': '#E4D6B3',
    'ink': '#24302A', 'muted': '#5F6B64', 'cocoa': '#2B3D33', 'line': '#DEDFD6',
}
D3_FONTS = {
    'tw': "display: ['\"Cormorant Garamond\"', '\"Noto Serif Thai\"', 'serif'],\n            body: ['Anuphan', 'sans-serif']",
    'link': '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Noto+Serif+Thai:wght@500;600&family=Anuphan:wght@300;400;500;600&display=swap">',
    'display_css': '"Cormorant Garamond", serif', 'body_css': 'Anuphan, sans-serif',
}

D3_CSS = """
    /* แบบ 3: ลิงก์ลูกศร + การ์ดเลข */
    .arrow-link { display: inline-flex; align-items: center; gap: 8px; min-height: 48px; font-weight: 500; color: var(--pink-deep); border-bottom: 1px solid transparent; transition: border-color .3s var(--ease); }
    .arrow-link:hover { border-color: var(--pink-deep); }
    .arrow-link::after { content: "→"; }
    .ncard { border-top: 2px solid var(--pink-deep); padding-top: 24px; }
    .ncard .n { font-family: "Cormorant Garamond", serif; font-size: 40px; line-height: 1; color: var(--pink-deep); }
    .hero-dim { background: linear-gradient(180deg, rgba(36,48,42,.30) 0%, rgba(36,48,42,.60) 100%); }
"""

D3_HERO = f"""    <!-- ===== 1. Hero: รูปเต็มจอ ข้อความกลาง + 2 ปุ่ม (ตาม nailgarden) ===== -->
    <section id="top" class="relative text-cream overflow-hidden min-h-[560px] md:min-h-[680px] flex items-center">
      <img src="{P_GLIT}" alt="" class="absolute inset-0 w-full h-full object-cover" width="900" height="1200" fetchpriority="high" decoding="async">
      <div class="absolute inset-0 hero-dim" aria-hidden="true"></div>
      <div class="relative mx-auto max-w-[820px] px-4 md:px-8 py-20 md:py-28 text-center">
        <p class="label !text-gold-light" data-stagger style="--d:0ms" data-i18n="hero.welcome">ยินดีต้อนรับสู่ Nail Me</p>
        <h1 class="font-display font-medium text-[clamp(44px,8vw,88px)] mt-4 leading-[1.05]" data-stagger style="--d:120ms">
          <span data-i18n="hero.title1">ร้านหรู</span> <span class="text-gold-light whitespace-nowrap" data-i18n="hero.title2">แต่ราคาน่ารัก</span>
        </h1>
        <p class="text-cream/90 mt-6 max-w-[30em] mx-auto text-[17px] md:text-[19px]" data-stagger style="--d:240ms" data-i18n="hero.sub">Nail Me ร้านทำเล็บ สปาเท้า สปามือ และสระไดร์ ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สีเจลให้เลือกกว่า 100 เฉด ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน</p>
        <p class="mt-4 font-medium text-gold-light" data-stagger style="--d:300ms"><span data-i18n="hero.eyebrow">ร้านทำเล็บ สุราษฎร์ธานี · ข้างตลาดศาลเจ้า</span> · <span data-i18n="hero.hours">เปิดทุกวัน 09:00–21:00</span></p>
        <div class="flex flex-wrap justify-center gap-4 mt-8" data-stagger style="--d:360ms">
          <a class="btn btn-lg bg-cream text-pink-deep hover:bg-gold-light" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
          <a class="btn btn-lg btn-on-dark" href="#visit" data-track="directions"><i class="ph ph-map-pin" aria-hidden="true"></i><span data-i18n="cta.find">ดูที่ตั้งร้าน</span></a>
        </div>
      </div>
    </section>
"""

D3_PROMO = """    <!-- ===== 2. โปรโมชั่น: การ์ดกว้างมีป้าย (ตาม nailgarden banner card) ===== -->
    <section id="promo" class="py-14 md:py-20" aria-labelledby="promo-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="border border-pink-deep rounded-lg p-6 md:p-10 grid lg:grid-cols-12 gap-8 items-center reveal">
          <div class="lg:col-span-5">
            <span class="inline-flex items-center h-7 px-3 rounded-full bg-pink-deep text-cream text-[12px] tracking-[.1em] uppercase" data-i18n="promo.label">โปรเดือนนี้</span>
            <h2 id="promo-title" class="font-display font-medium text-[28px] md:text-[36px] mt-4 text-pink-deep" data-i18n="promo.title">แคปโพสต์โปร ให้ช่างก่อนรับบริการ</h2>
            <a class="arrow-link mt-2" href="https://www.facebook.com/profile.php?id=61580350351076" target="_blank" rel="noopener" data-track="facebook" data-i18n="promo.cta">ดูโพสต์โปรบนเพจ</a>
          </div>
          <ul class="lg:col-span-7 grid grid-cols-3 gap-4 md:gap-8">
            <li><p class="num text-[40px] md:text-[56px] leading-none text-pink-deep">฿200</p><p class="mt-2 text-[14px] text-muted" data-i18n="promo.p0">ทาสีเจล ตัดแต่งหนังฟรี <span class="line-through opacity-70">250</span></p></li>
            <li><p class="num text-[40px] md:text-[56px] leading-none text-pink-deep">฿450</p><p class="mt-2 text-[14px] text-muted" data-i18n="promo.p1">สปาเท้า 9 ขั้นตอน <span class="line-through opacity-70">499</span></p></li>
            <li><p class="num text-[40px] md:text-[56px] leading-none text-pink-deep">฿150</p><p class="mt-2 text-[14px] text-muted" data-i18n="promo.p2">สระไดร์ ทุกความยาว</p></li>
          </ul>
        </div>
      </div>
    </section>
"""

D3_RITUAL = """    <!-- ===== 3a. เลือกบริการของคุณ: การ์ดเลข 01/02/03 (ตาม nailgarden "Choose your ritual") ===== -->
    <section id="ritual" class="bg-cream border-t border-line py-14 md:py-20" aria-labelledby="ritual-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <p class="label reveal">Choose your ritual</p>
        <h2 id="ritual-title" class="font-display font-medium text-[clamp(32px,4.5vw,48px)] mt-2 text-pink-deep reveal" data-i18n="rit.title">วันนี้อยากดูแลตรงไหน</h2>
        <div class="grid md:grid-cols-3 gap-8 mt-10 reveal">
          <div class="ncard"><p class="n">01</p><h3 class="font-display font-medium text-[26px] mt-4" data-i18n="rit.1">เล็บ</h3><p class="mt-2 text-[15px] text-muted" data-i18n="rit.1.d">ทาสีเจล สีลูกแก้ว ต่อเล็บ PVC เพ้นท์ลาย เริ่มต้น 250 บาท (โปร 200)</p><a class="arrow-link mt-2" href="#services" data-i18n="rit.more">ดูบริการและราคา</a></div>
          <div class="ncard"><p class="n">02</p><h3 class="font-display font-medium text-[26px] mt-4" data-i18n="rit.2">สปาและดูแลเล็บ</h3><p class="mt-2 text-[15px] text-muted" data-i18n="rit.2.d">สปาเท้า 10 ขั้นตอน 499 สปามือ 9 ขั้นตอน 399 Manicure / Pedicure 200</p><a class="arrow-link mt-2" href="#spa" data-i18n="rit.more2">ดูขั้นตอนสปา</a></div>
          <div class="ncard"><p class="n">03</p><h3 class="font-display font-medium text-[26px] mt-4" data-i18n="rit.3">ผม</h3><p class="mt-2 text-[15px] text-muted" data-i18n="rit.3.d">สระไดร์ทุกความยาว 150 บาท บริการผมอื่น ๆ สอบถามทางโทรศัพท์หรือเพจ</p><a class="arrow-link mt-2" href="tel:+66646542666" data-track="call" data-i18n="rit.more3">โทรสอบถาม</a></div>
        </div>
      </div>
    </section>
"""

D3_WHY = f"""    <!-- ===== 5. เรื่องของร้าน: รูป + ข้อความ (ตาม nailgarden brand story) ===== -->
    <section id="why" class="bg-cream border-t border-line py-14 md:py-20 lg:py-24" aria-labelledby="why-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8 grid lg:grid-cols-12 gap-10 lg:gap-16 items-center">
        <div class="lg:col-span-6 reveal"><div class="aspect-[4/5] overflow-hidden rounded-lg"><img src="{P_ART}" alt="ผลงานเล็บเฟรนช์ปลายลายดอกไม้ จากร้าน Nail Me" class="photo" loading="lazy" decoding="async" width="900" height="1200"></div></div>
        <div class="lg:col-span-6 reveal">
          <p class="label">Our story</p>
          <h2 id="why-title" class="font-display font-medium text-[clamp(32px,4.5vw,48px)] mt-2 text-pink-deep" data-i18n="why.title">เราจะดูแลคุณอย่างดี เพราะคุณคือคนพิเศษ</h2>
          <p class="mt-4 text-muted" data-i18n="why.sub">คำสัญญาที่เขียนไว้ท้ายป้ายราคาของร้าน และเป็นเหตุผลที่ลูกค้ากลับมา</p>
          <ul class="mt-6 grid sm:grid-cols-2 gap-x-8">
            <li class="py-3 border-t border-line"><strong class="font-medium" data-i18n="w1">ดูแลให้หลังทำ ไม่ทิ้งงาน</strong><p class="text-[14px] text-muted" data-i18n="w1.d">ทำแล้วมีปัญหา กลับมาให้ช่างดูได้ ร้านดูแลต่อให้</p></li>
            <li class="py-3 border-t border-line"><strong class="font-medium" data-i18n="w2">สีเจลกว่า 100 เฉด</strong><p class="text-[14px] text-muted" data-i18n="w2.d">สายหวาน มินิมอล แฟชั่น สีลูกแก้ว ช่างช่วยเลือกสีให้เข้ากับคุณ</p></li>
            <li class="py-3 border-t border-line"><strong class="font-medium" data-i18n="w3">ราคาชัดตามป้าย ไม่มีบวกเพิ่ม</strong><p class="text-[14px] text-muted" data-i18n="w3.d">ราคาทุกบริการติดไว้หน้าร้าน งานเพ้นท์คิดเพิ่มต่อนิ้วตามป้าย</p></li>
            <li class="py-3 border-t border-line"><strong class="font-medium" data-i18n="w4">ใจกลางเมือง มาง่าย</strong><p class="text-[14px] text-muted" data-i18n="w4.d">ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน เยื้อง Tops</p></li>
            <li class="py-3 border-t border-line sm:col-span-2 border-b"><strong class="font-medium" data-i18n="w5">ยินดีต้อนรับนักท่องเที่ยว</strong><p class="text-[14px] text-muted" data-i18n="w5.d">We welcome both Thai customers and international travellers.</p></li>
          </ul>
          <a class="arrow-link mt-4" href="#visit" data-i18n="why.more">แวะมาที่ร้าน</a>
        </div>
      </div>
    </section>
"""

D3_GALLERY = """    <!-- ===== 6. ผลงาน: กริด 6 รูป ไม่มีคำบรรยาย (ตาม nailgarden "Life in the garden") ===== -->
    <section id="gallery" class="border-t border-line py-14 md:py-20" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="max-w-[640px] reveal">
          <p class="label">Gallery</p>
          <h2 id="gallery-title" class="font-display font-medium text-[clamp(32px,4.5vw,48px)] mt-2 text-pink-deep" data-i18n="gallery.title">ผลงานจากร้าน</h2>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-3 gap-3 md:gap-4 mt-8 reveal">
__PHOTOS__
        </div>
        <a class="arrow-link mt-6" href="https://www.facebook.com/nailmesuratthani" target="_blank" rel="noopener" data-track="facebook" data-i18n="gallery.more">ดูผลงานล่าสุดบนเพจ</a>
      </div>
    </section>
"""

D3_REVIEWS = """    <!-- ===== 7. รีวิว: quote เรียงลง (ตาม nailgarden testimonials) ===== -->
    <section id="reviews" class="bg-cream border-t border-line py-14 md:py-20 lg:py-24" aria-labelledby="reviews-title">
      <div class="mx-auto max-w-[800px] px-4 md:px-8">
        <p class="label reveal">Guests say</p>
        <h2 id="reviews-title" class="font-display font-medium text-[clamp(32px,4.5vw,48px)] mt-2 text-pink-deep reveal" data-i18n="reviews.title">รีวิวจากลูกค้า</h2>
        <figure class="mt-8 border-l-2 border-pink-deep pl-6 reveal">
          <blockquote class="font-display font-medium text-[clamp(24px,3.5vw,36px)] leading-[1.4]" data-i18n="r1.quote">“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”</blockquote>
          <figcaption class="mt-3 text-[15px] text-muted" data-i18n="r1.name">ปฐมาวดี ชูมี · รีวิวบนเพจ Facebook 17 ก.ค. 2569 · เล็บเจล</figcaption>
        </figure>
        <p class="mt-8 text-muted reveal"><span class="num text-[28px] text-pink-deep">100%</span> <span data-i18n="stat.0">แนะนำ จาก 6 รีวิวบนเพจ</span> · <span class="num text-[28px] text-pink-deep">1,000+</span> <span data-i18n="stat.1">ผู้ติดตามเพจหลัก</span></p>
        <a class="arrow-link reveal" href="https://www.facebook.com/profile.php?id=61580350351076" target="_blank" rel="noopener" data-track="facebook" data-i18n="reviews.more">อ่านรีวิวทั้งหมดบนเพจ</a>
      </div>
    </section>
"""

D3_BOOKING = """    <!-- ===== 8. CTA ปิด กลางหน้า (ตาม nailgarden) + 3 ขั้นตอน ===== -->
    <section id="booking" class="bg-pink-deep text-cream py-14 md:py-20 lg:py-24" aria-labelledby="booking-title">
      <div class="mx-auto max-w-[800px] px-4 md:px-8 text-center">
        <p class="label !text-gold-light" data-i18n="bk.label2">Ready when you are</p>
        <h2 id="booking-title" class="font-display font-medium text-[clamp(32px,5vw,56px)] mt-2 reveal" data-i18n="bk.title">จองคิวง่าย ๆ 3&nbsp;<span class="whitespace-nowrap">ขั้นตอน</span></h2>
        <ol class="mt-8 grid sm:grid-cols-3 gap-6 text-[15px] text-cream/85 reveal">
          <li><span class="num text-[28px] text-gold-light">1</span><br><span data-i18n="bk.1">โทรหรือทักเพจ</span></li>
          <li><span class="num text-[28px] text-gold-light">2</span><br><span data-i18n="bk.2">เลือกสีและลายหน้าร้าน</span></li>
          <li><span class="num text-[28px] text-gold-light">3</span><br><span data-i18n="bk.3">มาถึงร้าน ใช้โปรได้เลย</span></li>
        </ol>
        <div class="flex flex-wrap justify-center gap-4 mt-10 reveal">
          <a class="btn btn-lg bg-cream text-pink-deep hover:bg-gold-light" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
          <a class="btn btn-lg btn-on-dark" href="https://m.me/nailmesuratthani" target="_blank" rel="noopener" data-track="message"><i class="ph ph-messenger-logo" aria-hidden="true"></i><span data-i18n="cta.line">ทักเพจ</span></a>
        </div>
      </div>
    </section>
"""

EXTRA_EN = """      'hero.welcome': 'Welcome to Nail Me', 'cta.find': 'Find the salon', 'bk.label': 'Please make a reservation', 'bk.label2': 'Ready when you are',
      'rit.title': 'What would you like to treat today?', 'rit.1': 'Nails', 'rit.1.d': 'Gel polish, cat eye, PVC extensions and nail art from 250 THB (promo 200).', 'rit.more': 'Services &amp; prices',
      'rit.2': 'Spa &amp; nail care', 'rit.2.d': '10-step foot spa 499, 9-step hand spa 399, manicure / pedicure 200.', 'rit.more2': 'See the spa steps',
      'rit.3': 'Hair', 'rit.3.d': 'Wash &amp; blow-dry, any length, 150 THB. Other hair services: please call or message.', 'rit.more3': 'Call to ask',
      'why.more': 'Visit us',
"""

def build():
    src = SRC.read_text()
    a, b = section(src, 6)
    imgs = re.findall(r'<img [^>]*>', src[a:b])
    def grid(ims, n=None):
        return '\n'.join(f'          <div class="aspect-square overflow-hidden rounded-lg">{im}</div>' for im in (ims if n is None else ims[:n]))
    extra = EXTRA_EN

    # ---- design2 (seeUnail structure)
    d2 = sub_colors(src, D2_COLORS, D2_FONTS, 'bg-blush')
    d2 = d2.replace('<!-- web-dev/freelance/websites/nail-me/index.html · แบบ "Blush & Gold" อิงโลโก้ร้าน (หน้าเดียว TH/EN) · ดู DESIGN.md -->',
                    '<!-- web-dev/freelance/websites/nail-me/design2.html · แบบ 2 "Private & Calm" โครงตาม seeunail.com (สร้างจาก builder/variants.py อย่าแก้ตรงนี้) -->')
    d2 = d2.replace('    .reveal { opacity: 0;', D2_CSS + '    .reveal { opacity: 0;')
    d2 = swap(d2, 1, D2_HERO); d2 = swap(d2, 2, D2_PROMO); d2 = swap(d2, 3, D2_SERVICES); d2 = swap(d2, 5, D2_WHY)
    d2 = swap(d2, 6, D2_GALLERY.replace('__PHOTOS__', grid(imgs))); d2 = swap(d2, 7, D2_REVIEWS); d2 = swap(d2, 8, D2_BOOKING)
    d2 = d2.replace('<meta name="theme-color" content="#FBEDEA">', '<meta name="theme-color" content="#F4EFE9">')
    d2 = d2.replace('.site-header.is-scrolled { background: rgba(251,237,234,.94);', '.site-header.is-scrolled { background: rgba(244,239,233,.94);')
    d2 = re.sub(r'    <p class="wordmark[^\n]*\n', '', d2)
    d2 = d2.replace("    const I18N_EN = {\n", "    const I18N_EN = {\n" + extra)
    (ROOT / 'design2.html').write_text(d2)

    # ---- design3 (nailgarden structure)
    d3 = sub_colors(src, D3_COLORS, D3_FONTS, 'bg-blush')
    d3 = d3.replace('<!-- web-dev/freelance/websites/nail-me/index.html · แบบ "Blush & Gold" อิงโลโก้ร้าน (หน้าเดียว TH/EN) · ดู DESIGN.md -->',
                    '<!-- web-dev/freelance/websites/nail-me/design3.html · แบบ 3 "Garden" โครงตาม nailgarden.com (สร้างจาก builder/variants.py อย่าแก้ตรงนี้) -->')
    d3 = d3.replace('    .reveal { opacity: 0;', D3_CSS + '    .reveal { opacity: 0;')
    d3 = swap(d3, 1, D3_HERO); d3 = swap(d3, 2, D3_PROMO)
    a3, _ = section(d3, 3); d3 = d3[:a3] + D3_RITUAL + '\n' + d3[a3:]   # แทรก "เลือกบริการ" ก่อนเมนูเต็ม
    d3 = swap(d3, 5, D3_WHY); d3 = swap(d3, 6, D3_GALLERY.replace('__PHOTOS__', grid(imgs, 6))); d3 = swap(d3, 7, D3_REVIEWS); d3 = swap(d3, 8, D3_BOOKING)
    d3 = d3.replace('<meta name="theme-color" content="#FBEDEA">', '<meta name="theme-color" content="#476650">')
    d3 = d3.replace('.site-header.is-scrolled { background: rgba(251,237,234,.94);', '.site-header.is-scrolled { background: rgba(247,245,240,.94);')
    d3 = d3.replace('class="font-display font-semibold text-[clamp(32px,4.5vw,48px)]"', 'class="font-display font-medium text-[clamp(32px,4.5vw,48px)] text-pink-deep"')
    d3 = d3.replace('class="font-display font-semibold text-[clamp(36px,5vw,56px)]"', 'class="font-display font-medium text-[clamp(36px,5vw,56px)] text-pink-deep"')
    d3 = d3.replace('<span class="font-display text-[24px] font-semibold italic text-pink-deep">Nail Me</span>', '<span class="font-display text-[24px] font-medium italic text-pink-deep">Nail Me</span>')
    d3 = re.sub(r'    <p class="wordmark[^\n]*\n', '', d3)
    d3 = d3.replace("    const I18N_EN = {\n", "    const I18N_EN = {\n" + extra)
    (ROOT / 'design3.html').write_text(d3)
    print('built design2.html, design3.html')

if __name__ == '__main__':
    build()
