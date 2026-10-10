# web-dev/freelance/websites/nail-me/builder/variants.py
# สร้าง design2.html (Emerald & Co.) และ design3.html (Botanical Menu) จาก index.html
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

HERO_IMG = 'https://lh3.googleusercontent.com/d/15XJ6vhagHu2wiS42nPKwGygAmkw32Ddo=w1200'
IMG2 = 'https://lh3.googleusercontent.com/d/1YmKe5tEzvpZkWJGLssCTW6MaXt49mOmg=w1200'
IMG3 = 'https://lh3.googleusercontent.com/d/1pntTSKYGk-EFayT3rF-0HT8P55UZXQ5F=w1200'

# ---------------------------------------------------------------- แบบ 2: Emerald & Co. (จากปกเพจ)
D2_COLORS = {
    'blush': '#F6F1E7',      # พื้นครีม
    'cream': '#FFFCF5',      # พื้นสลับ
    'rose': '#DCE5DC',       # พื้นอ่อนเขียว (placeholder/ไอคอน)
    'pink': '#2E6B52',       # เขียวกลาง (hover)
    'pink-deep': '#0F3D2E',  # เขียวมรกต = ปุ่มหลัก/ราคา
    'gold': '#C9A24B', 'gold-deep': '#8F6D22', 'gold-light': '#E9D7A5',
    'ink': '#1B2A24', 'muted': '#56655D', 'cocoa': '#0B2A20', 'line': '#DDD6C6',
}
D2_FONTS = {
    'tw': "display: ['\"Cormorant Garamond\"', '\"Noto Serif Thai\"', 'serif'],\n            body: ['\"Noto Sans Thai\"', 'sans-serif']",
    'link': '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Noto+Serif+Thai:wght@500;600&family=Noto+Sans+Thai:wght@300;400;500&display=swap">',
    'display_css': '"Cormorant Garamond", serif', 'body_css': '"Noto Sans Thai", sans-serif',
}

D2_HERO = f'''    <!-- ===== 1. Hero: รูปเต็มจอ + ข้อความทับ (ตามปกเพจ) ===== -->
    <section id="top" class="relative bg-cocoa text-cream overflow-hidden">
      <img src="{HERO_IMG}" alt="" class="absolute inset-0 w-full h-full object-cover opacity-40" width="900" height="1200" fetchpriority="high" decoding="async">
      <div class="absolute inset-0" style="background: linear-gradient(90deg, rgba(11,42,32,.96) 0%, rgba(11,42,32,.85) 45%, rgba(11,42,32,.35) 100%);" aria-hidden="true"></div>
      <div class="relative mx-auto max-w-[1200px] px-4 md:px-8 pt-16 pb-16 md:pt-24 md:pb-24 lg:pt-32 lg:pb-32">
        <p class="label !text-gold-light" data-stagger style="--d:0ms" data-i18n="hero.eyebrow">ร้านทำเล็บ สุราษฎร์ธานี · ข้างตลาดศาลเจ้า</p>
        <h1 class="font-display font-semibold text-[clamp(44px,8vw,96px)] mt-4 leading-[1.05] max-w-[12em]" data-stagger style="--d:120ms">
          <span class="text-gold-light" data-i18n="hero.title1">ร้านหรู</span><br>
          <span class="text-cream" data-i18n="hero.title2">แต่ราคาน่ารัก</span>
        </h1>
        <p class="text-cream/85 mt-6 max-w-[30em] text-[17px] md:text-[19px]" data-stagger style="--d:240ms" data-i18n="hero.sub">Nail Me ร้านทำเล็บ สปาเท้า สปามือ และสระไดร์ ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สีเจลให้เลือกกว่า 100 เฉด ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน</p>
        <div class="flex flex-wrap gap-4 mt-8" data-stagger style="--d:360ms">
          <a class="btn btn-lg bg-gold-light text-cocoa hover:bg-cream" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
          <a class="btn btn-lg btn-on-dark" href="https://m.me/nailmesuratthani" target="_blank" rel="noopener" data-track="message"><i class="ph ph-messenger-logo" aria-hidden="true"></i><span data-i18n="cta.line">ทักเพจ</span></a>
        </div>
        <ul class="flex flex-wrap gap-x-8 gap-y-2 mt-10 text-[13px] tracking-[.14em] uppercase text-gold-light/90" data-stagger style="--d:480ms" aria-label="บริการ">
          <li>Nail</li><li>Hair</li><li>Lash</li><li>Spa</li><li>Wax</li>
        </ul>
        <p class="mt-6 text-[15px] text-cream/75" data-stagger style="--d:560ms"><span data-i18n="hero.hours">เปิดทุกวัน 09:00–21:00</span> · <span data-i18n="hero.walkin">จองคิวหรือ walk-in</span> · <a href="tel:+66646542666" data-track="call" class="text-gold-light underline underline-offset-4">064-654-2666</a></p>
      </div>
    </section>
'''

D2_PROMO = '''    <!-- ===== 2. โปรโมชั่น: แถบทอง ตัวเลขเรียงแถว ===== -->
    <section id="promo" class="bg-gold-light text-cocoa border-y border-gold" aria-labelledby="promo-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8 py-8 md:py-10 flex flex-wrap items-center gap-x-10 gap-y-6">
        <div class="shrink-0">
          <p class="label !text-gold-deep" data-i18n="promo.label">โปรเดือนนี้</p>
          <h2 id="promo-title" class="font-display font-semibold text-[24px] md:text-[28px] mt-1 max-w-[14em]" data-i18n="promo.title">แคปโพสต์โปร ให้ช่างก่อนรับบริการ</h2>
        </div>
        <ul class="flex flex-wrap gap-x-10 gap-y-4 grow">
          <li class="flex items-baseline gap-3"><p class="num text-[40px] md:text-[48px] leading-none">฿200</p><p class="text-[14px] max-w-[9em] leading-[1.4]" data-i18n="promo.p0">ทาสีเจล ตัดแต่งหนังฟรี <span class="line-through opacity-70">250</span></p></li>
          <li class="flex items-baseline gap-3"><p class="num text-[40px] md:text-[48px] leading-none">฿450</p><p class="text-[14px] max-w-[9em] leading-[1.4]" data-i18n="promo.p1">สปาเท้า 9 ขั้นตอน <span class="line-through opacity-70">499</span></p></li>
          <li class="flex items-baseline gap-3"><p class="num text-[40px] md:text-[48px] leading-none">฿150</p><p class="text-[14px] max-w-[9em] leading-[1.4]" data-i18n="promo.p2">สระไดร์ ทุกความยาว</p></li>
        </ul>
        <a class="btn border border-cocoa text-cocoa hover:bg-cocoa hover:text-gold-light shrink-0" href="https://www.facebook.com/profile.php?id=61580350351076" target="_blank" rel="noopener" data-track="facebook"><i class="ph ph-facebook-logo" aria-hidden="true"></i><span data-i18n="promo.cta">ดูโพสต์โปรบนเพจ</span></a>
      </div>
    </section>
'''

D2_GALLERY = '''    <!-- ===== 6. ผลงาน: แถบเลื่อนแนวนอน บนพื้นเข้ม ===== -->
    <section id="gallery" class="bg-cocoa text-cream py-14 md:py-20" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="flex flex-wrap items-baseline justify-between gap-4 mb-8 reveal">
          <h2 id="gallery-title" class="font-display font-semibold text-[clamp(32px,4.5vw,48px)] text-gold-light" data-i18n="gallery.title">ผลงานจากร้าน</h2>
          <a class="text-[15px] text-gold-light underline underline-offset-4 hover:text-cream" href="https://www.facebook.com/nailmesuratthani" target="_blank" rel="noopener" data-track="facebook" data-i18n="gallery.more">ดูผลงานล่าสุดบนเพจ</a>
        </div>
        <div class="strip reveal">
__PHOTOS__
        </div>
      </div>
    </section>
'''

# ---------------------------------------------------------------- แบบ 3: Botanical Menu (จากป้ายราคาในร้าน)
D3_COLORS = {
    'blush': '#FAF6EE',      # กระดาษครีม
    'cream': '#FFFFFF',
    'rose': '#E6E9DD',       # เขียวอ่อน
    'pink': '#8A9A7B',       # เซจ
    'pink-deep': '#5F7052',  # เซจเข้ม = ปุ่มหลัก/ราคา
    'gold': '#B99A5B', 'gold-deep': '#86703A', 'gold-light': '#E4D6B3',
    'ink': '#3B3A33', 'muted': '#6B6A5F', 'cocoa': '#3F4A38', 'line': '#E3DCCB',
}
D3_FONTS = {
    'tw': "display: ['\"Cormorant Garamond\"', '\"Noto Serif Thai\"', 'serif'],\n            body: ['Anuphan', 'sans-serif']",
    'link': '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Noto+Serif+Thai:wght@500;600&family=Anuphan:wght@300;400;500;600&display=swap">',
    'display_css': '"Cormorant Garamond", serif', 'body_css': 'Anuphan, sans-serif',
}

D3_HERO = f'''    <!-- ===== 1. Hero: โลโก้กลาง + ชื่อร้านแบบป้ายเมนู + รูป 2 ข้าง ===== -->
    <section id="top" class="border-b border-line">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8 pt-12 pb-14 md:pt-16 md:pb-20 text-center">
        <img src="img/nail-me-logo-512.png" width="96" height="96" alt="โลโก้ Nail Me" class="w-20 h-20 md:w-24 md:h-24 rounded-full mx-auto" data-stagger style="--d:0ms" fetchpriority="high">
        <p class="label mt-6" data-stagger style="--d:80ms" data-i18n="hero.eyebrow">ร้านทำเล็บ สุราษฎร์ธานี · ข้างตลาดศาลเจ้า</p>
        <h1 class="font-display font-medium text-[clamp(44px,8vw,96px)] mt-3 leading-[1.05] text-pink-deep" data-stagger style="--d:160ms">
          <span data-i18n="hero.title1">ร้านหรู</span> <span class="text-gold-deep" data-i18n="hero.title2">แต่ราคาน่ารัก</span>
        </h1>
        <p class="text-ink mt-6 max-w-[34em] mx-auto text-[17px] md:text-[19px]" data-stagger style="--d:240ms" data-i18n="hero.sub">Nail Me ร้านทำเล็บ สปาเท้า สปามือ และสระไดร์ ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สีเจลให้เลือกกว่า 100 เฉด ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน</p>
        <div class="flex flex-wrap justify-center gap-4 mt-8" data-stagger style="--d:320ms">
          <a class="btn btn-pink btn-lg" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>
          <a class="btn btn-gold btn-lg" href="https://m.me/nailmesuratthani" target="_blank" rel="noopener" data-track="message"><i class="ph ph-messenger-logo" aria-hidden="true"></i><span data-i18n="cta.line">ทักเพจ</span></a>
        </div>
        <p class="mt-6 text-[15px] text-muted" data-stagger style="--d:400ms"><span data-i18n="hero.hours">เปิดทุกวัน 09:00–21:00</span> · <span data-i18n="hero.walkin">จองคิวหรือ walk-in</span> · <a href="tel:+66646542666" data-track="call" class="text-ink underline decoration-gold underline-offset-4">064-654-2666</a></p>
        <div class="grid grid-cols-3 gap-3 md:gap-6 mt-12 max-w-[900px] mx-auto" data-stagger style="--d:480ms">
          <div class="aspect-[3/4] overflow-hidden rounded-lg translate-y-6"><img src="{IMG2}" alt="เล็บเจลกลิตเตอร์ทอง ผลงาน Nail Me" class="photo" width="900" height="1200" loading="eager" decoding="async"></div>
          <div class="aspect-[3/4] overflow-hidden rounded-lg"><img src="{HERO_IMG}" alt="ผลงานทาสีเจลสีนู้ด Nail Me สุราษฎร์ธานี" class="photo" width="900" height="1200" fetchpriority="high" decoding="async"></div>
          <div class="aspect-[3/4] overflow-hidden rounded-lg translate-y-6"><img src="{IMG3}" alt="เล็บเฟรนช์ลายดอกไม้ ผลงาน Nail Me" class="photo" width="900" height="1200" loading="eager" decoding="async"></div>
        </div>
      </div>
    </section>
'''

D3_PROMO = '''    <!-- ===== 2. โปรโมชั่น: คูปองกระดาษ ===== -->
    <section id="promo" class="py-14 md:py-20" aria-labelledby="promo-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="coupon reveal">
          <div class="p-6 md:p-10 grid md:grid-cols-12 gap-8 items-center">
            <div class="md:col-span-4">
              <p class="label" data-i18n="promo.label">โปรเดือนนี้</p>
              <h2 id="promo-title" class="font-display font-medium text-[28px] md:text-[32px] mt-1 text-pink-deep" data-i18n="promo.title">แคปโพสต์โปร ให้ช่างก่อนรับบริการ</h2>
              <a class="btn btn-gold mt-6" href="https://www.facebook.com/profile.php?id=61580350351076" target="_blank" rel="noopener" data-track="facebook"><i class="ph ph-facebook-logo" aria-hidden="true"></i><span data-i18n="promo.cta">ดูโพสต์โปรบนเพจ</span></a>
            </div>
            <ul class="md:col-span-8 grid grid-cols-3 gap-4 md:gap-8 md:border-l border-dashed border-gold md:pl-10">
              <li><p class="num text-[40px] md:text-[56px] leading-none text-pink-deep">฿200</p><p class="mt-2 text-[14px] text-muted" data-i18n="promo.p0">ทาสีเจล ตัดแต่งหนังฟรี <span class="line-through opacity-70">250</span></p></li>
              <li><p class="num text-[40px] md:text-[56px] leading-none text-pink-deep">฿450</p><p class="mt-2 text-[14px] text-muted" data-i18n="promo.p1">สปาเท้า 9 ขั้นตอน <span class="line-through opacity-70">499</span></p></li>
              <li><p class="num text-[40px] md:text-[56px] leading-none text-pink-deep">฿150</p><p class="mt-2 text-[14px] text-muted" data-i18n="promo.p2">สระไดร์ ทุกความยาว</p></li>
            </ul>
          </div>
        </div>
      </div>
    </section>
'''

D3_CSS = '''
    /* แบบ 3: กล่องเมนูแบบป้ายราคาในร้าน */
    .coupon { background: var(--cream); border: 1px solid var(--gold); border-radius: 16px; position: relative; }
    .coupon::before, .coupon::after { content: ""; position: absolute; top: 50%; width: 24px; height: 24px; border-radius: 999px; background: var(--blush); border: 1px solid var(--gold); transform: translateY(-50%); }
    .coupon::before { left: -13px; } .coupon::after { right: -13px; }
    .menu-box { background: var(--cream); border: 1px solid var(--line); border-radius: 16px; padding: 24px; }
    .menu-box .pill { display: inline-flex; align-items: center; height: 36px; padding: 0 16px; border-radius: 999px; background: var(--pink-deep); color: var(--cream); font-family: "Noto Serif Thai", serif; font-weight: 600; font-size: 18px; }
    .menu-box .row { display: flex; justify-content: space-between; gap: 16px; align-items: baseline; padding: 10px 0; border-top: 1px dotted var(--line); }
    .menu-box .row:first-of-type { border-top: 0; }
    .menu-box .row .p { font-family: "Cormorant Garamond", serif; font-weight: 600; font-size: 24px; color: var(--pink-deep); white-space: nowrap; }
    @media (min-width: 768px) { .menu-box { padding: 32px; } }
'''

D3_SERVICES = '''    <!-- ===== 3. บริการและราคา: กล่องเมนู 4 หมวด แบบป้ายราคาในร้าน ===== -->
    <section id="services" class="border-t border-line py-14 md:py-20 lg:py-24" aria-labelledby="services-title">
      <div id="menu" class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="max-w-[640px] reveal">
          <h2 id="services-title" class="font-display font-medium text-[clamp(36px,5vw,56px)] text-pink-deep" data-i18n="services.title">บริการและราคา</h2>
          <p class="mt-4 text-muted" data-i18n="services.intro">ทาสีเจล ต่อเล็บ ดูแลเล็บมือ-เท้า และสปา ราคาปกติตามป้ายราคาในร้าน ช่วงโปรโมชั่นถูกกว่านี้ ดูที่โปรเดือนนี้</p>
        </div>
        <div class="grid md:grid-cols-2 gap-6 mt-10 reveal">
          <div class="menu-box">
            <span class="pill" data-i18n="g.gel">ทาสีเจล · Gel polish</span>
            <div class="mt-4">
              <div class="row"><div><h3 class="font-medium" data-i18n="s.gelh">ทาสีเจลมือ</h3><p class="text-[14px] text-muted" data-i18n="s.gelh.d">สีเจลคุณภาพดี ติดทน 1–3 เดือน เลือกได้กว่า 100 เฉด</p></div><span class="p">฿250</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.gelf">ทาสีเจลเท้า</h3><p class="text-[14px] text-muted" data-i18n="s.gelf.d">สีสวย เงางาม แห้งไว ไม่ทำลายหน้าเล็บ</p></div><span class="p">฿300</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.cat">สีลูกแก้ว Cat Eye</h3><p class="text-[14px] text-muted" data-i18n="s.cat.d">เจลแม่เหล็ก ประกายลึกเหมือนตาแมว</p></div><span class="p">฿350</span></div>
            </div>
          </div>
          <div class="menu-box">
            <span class="pill" data-i18n="g.ext">ต่อเล็บ · เสริมเล็บ</span>
            <div class="mt-4">
              <div class="row"><div><h3 class="font-medium" data-i18n="s.pvc">ต่อเล็บ PVC</h3><p class="text-[14px] text-muted" data-i18n="s.pvc.d">ต่อเล็บยาวสวยเป็นธรรมชาติ เจลเว้นโคน</p></div><span class="p">฿350</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.ov1">เสริมหน้าเล็บหลังทาสี</h3><p class="text-[14px] text-muted" data-i18n="s.ov1.d">เคลือบเสริมความแข็งแรงบนเล็บที่ทาสีแล้ว</p></div><span class="p">฿150</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.ov2">เสริมหน้าเล็บก่อนทาสี</h3><p class="text-[14px] text-muted" data-i18n="s.ov2.d">เสริมฐานเล็บให้หนาแข็งแรงก่อนลงสีเจล</p></div><span class="p">฿450</span></div>
            </div>
          </div>
          <div class="menu-box">
            <span class="pill" data-i18n="g.care">ดูแลเล็บ · สปา</span>
            <div class="mt-4">
              <div class="row"><div><h3 class="font-medium" data-i18n="s.fspa">สปาเท้า 10&nbsp;<span class="whitespace-nowrap">ขั้นตอน</span></h3><p class="text-[14px] text-muted" data-i18n="s.fspa.d">ขัดถึงใต้เข่า แช่ ขัด มาร์ก นวด บำรุง <a href="#spa" class="underline decoration-gold underline-offset-4" data-i18n="s.steps">ดูขั้นตอน</a></p></div><span class="p">฿499</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.hspa">สปามือ 9&nbsp;<span class="whitespace-nowrap">ขั้นตอน</span></h3><p class="text-[14px] text-muted" data-i18n="s.hspa.d">บำรุงล้ำลึก ผ่อนคลายสุดมือ</p></div><span class="p">฿399</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.mani">Manicure / Pedicure</h3><p class="text-[14px] text-muted" data-i18n="s.mani.d">ตัดแต่งเล็บและหนังรอบเล็บ มือหรือเท้า</p></div><span class="p">฿200</span></div>
            </div>
          </div>
          <div class="menu-box">
            <span class="pill" data-i18n="g.rem">ถอดเล็บ · งานเพิ่ม</span>
            <div class="mt-4">
              <div class="row"><div><h3 class="font-medium" data-i18n="s.rem">ถอดสีเจล / ถอด PVC</h3><p class="text-[14px] text-muted" data-i18n="s.rem.d">ถอดแล้วทำต่อที่ร้าน เจล 50 · PVC 100 · ถอดอย่างเดียว 100</p></div><span class="p"><small class="font-body text-[13px] font-normal text-muted mr-1" data-i18n="from">เริ่ม</small>฿50</span></div>
              <div class="row"><div><h3 class="font-medium" data-i18n="s.art">งานเพ้นท์ คิดเพิ่มต่อนิ้ว</h3><p class="text-[14px] text-muted" data-i18n="s.art.d">เพ้นท์ลาย +20 · เฟรนช์ปลาย +30 · ออมเบร +30 · ติดอะไหล่ +20 · ปั้นนูน +50</p></div><span class="p"><small class="font-body text-[13px] font-normal text-muted mr-1" data-i18n="from">เริ่ม</small>฿20</span></div>
            </div>
          </div>
        </div>
        <p class="mt-6 text-[14px] text-muted text-center" data-i18n="services.note">ราคาตามป้ายราคาในร้าน (ต.ค. 2569) · บริการผม ขนตา แว็กซ์ สอบถามทางโทรศัพท์หรือเพจ</p>
      </div>
    </section>
'''

def photos_from_index(html):
    a, b = section(html, 6)
    imgs = re.findall(r'<img [^>]*>', html[a:b])
    return '\n'.join(f'          <div class="aspect-[3/4] overflow-hidden rounded-lg">{im}</div>' for im in imgs)

def build():
    src = SRC.read_text()
    photos = photos_from_index(src)

    # ---- design2
    d2 = sub_colors(src, D2_COLORS, D2_FONTS, 'bg-blush')
    d2 = d2.replace('<!-- web-dev/freelance/websites/nail-me/index.html · แบบ "Blush & Gold" อิงโลโก้ร้าน (หน้าเดียว TH/EN) · ดู DESIGN.md -->',
                    '<!-- web-dev/freelance/websites/nail-me/design2.html · แบบ 2 "Emerald & Co." อิงปกเพจ (สร้างจาก builder/variants.py อย่าแก้ตรงนี้) -->')
    d2 = swap(d2, 1, D2_HERO)
    d2 = swap(d2, 2, D2_PROMO)
    d2 = swap(d2, 6, D2_GALLERY.replace('__PHOTOS__', photos))
    # header: โลโก้ชื่อเขียว, ปุ่มโทรเขียว (btn-pink = pink-deep = เขียว อยู่แล้ว)
    d2 = d2.replace('<meta name="theme-color" content="#FBEDEA">', '<meta name="theme-color" content="#0F3D2E">')
    d2 = d2.replace('.site-header.is-scrolled { background: rgba(251,237,234,.94);', '.site-header.is-scrolled { background: rgba(246,241,231,.94);')
    d2 = d2.replace('class="md:hidden fixed inset-x-0 bottom-0 z-40 grid grid-cols-2 gap-2 px-4 pt-2 bg-blush/95', 'class="md:hidden fixed inset-x-0 bottom-0 z-40 grid grid-cols-2 gap-2 px-4 pt-2 bg-blush/95')
    # จองคิว section 8 บนพื้นเข้มอยู่แล้ว → ทำเป็นพื้นครีมเพื่อสลับกับ gallery เข้ม
    d2 = d2.replace('<section id="booking" class="bg-cocoa text-cream py-14 md:py-20"', '<section id="booking" class="bg-cream border-t border-line py-14 md:py-20"')
    d2 = d2.replace('text-[clamp(32px,4.5vw,48px)] text-gold-light reveal" data-i18n="bk.title"', 'text-[clamp(32px,4.5vw,48px)] text-pink-deep reveal" data-i18n="bk.title"')
    d2 = d2.replace('border-t border-gold-light/40 pt-4"><p class="num text-[40px] text-gold-light leading-none">', 'border-t border-gold pt-4"><p class="num text-[40px] text-gold-deep leading-none">')
    d2 = d2.replace('<p class="mt-2 text-[15px] text-cream/80" data-i18n="bk.', '<p class="mt-2 text-[15px] text-muted" data-i18n="bk.')
    d2 = d2.replace('<a class="btn btn-lg bg-gold-light text-cocoa hover:bg-cream" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>\n          <a class="btn btn-lg btn-on-dark"',
                    '<a class="btn btn-lg btn-pink" href="tel:+66646542666" data-track="call"><i class="ph ph-phone" aria-hidden="true"></i><span data-i18n="cta.call">โทรจองคิว</span></a>\n          <a class="btn btn-lg btn-gold"')
    (ROOT / 'design2.html').write_text(d2)

    # ---- design3
    d3 = sub_colors(src, D3_COLORS, D3_FONTS, 'bg-blush')
    d3 = d3.replace('<!-- web-dev/freelance/websites/nail-me/index.html · แบบ "Blush & Gold" อิงโลโก้ร้าน (หน้าเดียว TH/EN) · ดู DESIGN.md -->',
                    '<!-- web-dev/freelance/websites/nail-me/design3.html · แบบ 3 "Botanical Menu" อิงป้ายราคาในร้าน (สร้างจาก builder/variants.py อย่าแก้ตรงนี้) -->')
    d3 = d3.replace('    .reveal { opacity: 0;', D3_CSS + '    .reveal { opacity: 0;')
    d3 = swap(d3, 1, D3_HERO)
    d3 = swap(d3, 2, D3_PROMO)
    d3 = swap(d3, 3, D3_SERVICES)
    d3 = d3.replace('<meta name="theme-color" content="#FBEDEA">', '<meta name="theme-color" content="#FAF6EE">')
    d3 = d3.replace('.site-header.is-scrolled { background: rgba(251,237,234,.94);', '.site-header.is-scrolled { background: rgba(250,246,238,.94);')
    # หัวข้อแบบ 3 ใช้ตัวบางกว่า
    d3 = d3.replace('class="font-display font-semibold text-[clamp(32px,4.5vw,48px)]"', 'class="font-display font-medium text-[clamp(32px,4.5vw,48px)] text-pink-deep"')
    d3 = d3.replace('<span class="font-display text-[24px] font-semibold italic text-pink-deep">Nail Me</span>', '<span class="font-display text-[24px] font-medium italic text-pink-deep">Nail Me</span>')
    # ไม่ใช้ wordmark โปร่งท้ายหน้าในแบบ 3 (จุดจำของแบบ 1)
    d3 = re.sub(r'    <p class="wordmark[^\n]*\n', '', d3)
    (ROOT / 'design3.html').write_text(d3)
    print('built design2.html, design3.html')

if __name__ == '__main__':
    build()
