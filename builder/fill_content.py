# web-dev/freelance/websites/nail-me/builder/fill_content.py
# ใส่ข้อมูลจริงจากเพจ Facebook ทั้ง 2 เพจ (ดึง 10 ต.ค. 2569) ลงดราฟต์ทั้ง 3 แบบ
# รันซ้ำได้: แทนค่า element ที่มี data-i18n="key" และรายการใน I18N_EN
import re, sys, pathlib

FB1 = "https://www.facebook.com/profile.php?id=61580350351076"   # Nail Me ตลาดศาลเจ้า สุราษฎร์ (1 พันผู้ติดตาม, 6 รีวิว)
FB2 = "https://www.facebook.com/nailmesuratthani"                 # Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี (สำรอง)
MSG = "https://m.me/nailmesuratthani"
TEL = "064-654-2666"          # จากหน้า "เกี่ยวกับ" ทั้ง 2 เพจ
TEL_HREF = "tel:+66646542666"
MAPS = "https://www.google.com/maps/search/?api=1&query=Nail+Me+%E0%B8%95%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B8%A8%E0%B8%B2%E0%B8%A5%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2+%E0%B8%AA%E0%B8%B8%E0%B8%A3%E0%B8%B2%E0%B8%A9%E0%B8%8E%E0%B8%A3%E0%B9%8C%E0%B8%98%E0%B8%B2%E0%B8%99%E0%B8%B5"

TH = {
 'draft': 'ดราฟต์ · ข้อมูลร้านอิงจากเพจ Facebook (10 ต.ค. 69) · รูปจริงรอจากร้าน',
 'hero.eyebrow': 'ร้านทำเล็บ ตลาดศาลเจ้า · ใจกลางเมืองสุราษฎร์ธานี',
 'hero.title': 'ร้านหรู<br>แต่ราคาน่ารัก',
 'hero.sub': 'ทาสีเจลเริ่มต้น 200 บาท ตัดแต่งหนังฟรี · สปาเท้า 9 ขั้นตอน · สระไดร์ · เปิดทุกวัน 09:00–21:00 จองคิวหรือ walk-in ได้เลย',
 'd2.title': 'พักเท้าให้หายเหนื่อย<br>แล้วสวยกลับไป',
 'd2.sub': 'ร้านทำเล็บใจกลางเมืองสุราษฎร์ธานี ข้างตลาดศาลเจ้า ทาสีเจล ทำเล็บมือ-เท้า และสปาเท้า 9 ขั้นตอน ในบรรยากาศสะอาด สบาย เป็นกันเอง เปิดทุกวัน 09:00–21:00',
 'd3.title': 'เปลี่ยนเล็บสวยให้โดดเด่นในทุกวัน',
 'd3.sub': 'ร้านทำเล็บข้างตลาดศาลเจ้า ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท เปิดทุกวัน 09:00–21:00 จองคิวหรือ walk-in ได้เลย',
 'promo.title': 'โปรเดือนนี้: ทาสีเจล 200 · สปาเท้า 450 · สระไดร์ 150',
 'promo.desc': 'ทาสีเจล + เพ้นท์ 350 (กี่นิ้วก็ได้) · ต่อเล็บ PVC เจลเว้นโคน 250 · ใช้โปรโมชั่น แคปรูปโพสต์ให้ช่างก่อนรับบริการ',
 'promo.cta': 'โทรจองโปรนี้',
 'services.title': 'บริการของเรา',
 'services.intro': 'ทาสีเจล ทำเล็บมือ-เท้า และสปาเท้าเป็นหลัก สีเจลให้เลือกกว่า 100 เฉด ทั้งสายหวาน มินิมอล และแฟชั่น',
 'services.tag': 'บริการเด่น',
 's1.title': 'ทาสีเจล · ทำเล็บมือ-เท้า',
 's1.desc': 'สีเจลคุณภาพดี ติดทนนาน เลือกได้กว่า 100 เฉด ช่างช่วยเลือกสีและสไตล์ให้เหมาะกับคุณ ตัดแต่งหนังฟรี',
 's2.title': 'สปาเท้า 9 ขั้นตอน',
 's2.desc': 'แช่ ขัด บำรุงผิวเท้า ผ่อนคลายหลังเลิกงานหรือหลังเดินเที่ยวทั้งวัน',
 's3.title': 'สระ ไดร์',
 's3.desc': 'สระไดร์ทุกความยาว 150 บาท เติมความสดชื่นในที่เดียวกับที่ทำเล็บ',
 'reviews.title': 'เสียงจากลูกค้า',
 'r1.quote': '“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”',
 'r1.quoteShort': 'ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า',
 'r1.name': '— ปฐมาวดี ชูมี · รีวิวบน Facebook (เล็บเจล)',
 'r2.quote': '“100% แนะนำ จาก 6 รีวิวบนเพจ Facebook”',
 'r2.quote2': '100% แนะนำ จาก 6 รีวิวบนเพจ Facebook',
 'r2.name': '— Nail Me ตลาดศาลเจ้า สุราษฎร์ · ผู้ติดตาม 1 พันคน',
 'r3.quote': '“เราดูแลให้หลังทำ ไม่ทิ้งงาน”',
 'r3.quote3': 'เราดูแลให้หลังทำ ไม่ทิ้งงาน',
 'r3.name': '— คำสัญญาจากร้าน',
 'reviews.more': 'ดูรีวิวทั้งหมดบนเพจ',
 'gallery.title': 'ผลงานจากร้าน',
 'menu.title': 'เมนูและราคา',
 'menu.note': 'ราคาตามโพสต์โปรโมชั่นล่าสุดบนเพจ (กันยายน 2569)',
 'menu.ask': 'ใช้โปรโมชั่น แคปรูปโพสต์ให้ช่างก่อนรับบริการ · สอบถามบริการอื่นหรือจองคิวได้ทางโทรศัพท์และเพจ',
 'm1.title': 'เล็บ', 'm2.title': 'สปาเท้า', 'm3.title': 'สระ ไดร์',
 'visit.title': 'แวะมาที่ร้าน',
 'visit.sub': 'ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน เยื้อง Tops ติดกับห้างทองก้องไพศาล · มาเที่ยวสุราษฎร์ฯ แวะได้เลย เรายินดีต้อนรับทั้งลูกค้าไทยและนักท่องเที่ยว',
 'visit.addr': 'ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน อ.เมือง สุราษฎร์ธานี',
 'visit.addrTodo': 'เยื้อง Tops · ติดห้างทองก้องไพศาล',
 'visit.hours': 'เปิดทุกวัน 09:00–21:00 · จองคิวหรือ walk-in',
 'visit.phone': TEL,
 'visit.line': 'Facebook: Nail Me ตลาดศาลเจ้า สุราษฎร์',
 'visit.lineOnly': 'ทักเพจ Nail Me ตลาดศาลเจ้า',
 'cta.line': 'ทักเพจ',
 'footer.fb1': 'เพจ Nail Me ตลาดศาลเจ้า สุราษฎร์',
 'footer.fb2': 'เพจ Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี',
}
EN = {
 'draft': 'Draft · salon details taken from the Facebook pages (10 Oct 2026) · real photos pending',
 'hero.eyebrow': 'Nail salon at San Chao Market · central Surat Thani',
 'hero.title': 'A lovely salon,<br>lovely prices',
 'hero.sub': 'Gel polish from 200 THB with free cuticle care · 9-step foot spa · wash &amp; blow-dry · open daily 09:00–21:00, bookings and walk-ins welcome',
 'd2.title': 'Rest your feet,<br>leave beautiful',
 'd2.sub': 'A nail salon in central Surat Thani, next to San Chao Market. Gel polish, manicure, pedicure and a 9-step foot spa in a clean, relaxed space. Open daily 09:00–21:00.',
 'd3.title': 'Beautiful nails, every day',
 'd3.sub': 'Next to San Chao Market in central Surat Thani. Gel polish from 200 THB. Open daily 09:00–21:00, bookings and walk-ins welcome.',
 'promo.title': 'This month: gel polish 200 · foot spa 450 · wash &amp; blow-dry 150',
 'promo.desc': 'Gel + nail art 350 (any number of nails) · PVC extensions with gel 250 · show the promo post to your technician before service',
 'promo.cta': 'Call to book this offer',
 'services.title': 'Our services',
 'services.intro': 'Gel polish, manicure, pedicure and foot spa are our specialty, with 100+ gel shades from sweet to minimal to fashion.',
 'services.tag': 'Signature',
 's1.title': 'Gel polish · manicure &amp; pedicure',
 's1.desc': 'Long-lasting quality gel in 100+ shades. Our technicians help you pick a colour and style. Free cuticle care.',
 's2.title': '9-step foot spa',
 's2.desc': 'Soak, scrub and nourish tired feet after work or a day of sightseeing.',
 's3.title': 'Wash &amp; blow-dry',
 's3.desc': 'Any hair length, 150 THB. Freshen up while you are here for your nails.',
 'reviews.title': 'What guests say',
 'r1.quote': '“Beautiful pedicure, I love it, so pretty!”',
 'r1.quoteShort': 'Beautiful pedicure, I love it, so pretty!',
 'r1.name': '— Pathamawadee C. · Facebook review (gel nails) · translated from Thai',
 'r2.quote': '“100% recommended from 6 reviews on Facebook”',
 'r2.quote2': '100% recommended from 6 reviews on Facebook',
 'r2.name': '— Nail Me San Chao Market page · 1K followers',
 'r3.quote': '“We look after you after your visit, we never leave a job unfinished.”',
 'r3.quote3': 'We look after you after your visit, we never leave a job unfinished.',
 'r3.name': '— The salon’s promise',
 'reviews.more': 'See all reviews on our page',
 'gallery.title': 'From the salon',
 'menu.title': 'Menu &amp; prices',
 'menu.note': 'Prices from the salon’s latest promotion post (September 2026).',
 'menu.ask': 'Show the promo post to your technician before service · for other services or bookings, call or message the page.',
 'm1.title': 'Nails', 'm2.title': 'Foot spa', 'm3.title': 'Wash &amp; blow-dry',
 'visit.title': 'Visit us',
 'visit.sub': 'Next to San Chao Market, opposite the Ban Don electric train stop, near Tops and the Kong Paisan gold shop. Thai customers and international travellers are all welcome.',
 'visit.addr': 'Next to San Chao Market, opposite Ban Don electric train stop, Mueang Surat Thani',
 'visit.addrTodo': 'Near Tops · beside Kong Paisan gold shop',
 'visit.hours': 'Open daily 09:00–21:00 · bookings and walk-ins',
 'visit.phone': TEL,
 'visit.line': 'Facebook: Nail Me San Chao Market',
 'visit.lineOnly': 'Message the Facebook page',
 'cta.line': 'Message us',
 'footer.fb1': 'Nail Me San Chao Market (page 1)',
 'footer.fb2': 'Nail Me San Chao Market (page 2)',
}
MENU = {  # หมวด → รายการ
 'm1': [('ทาสีเจล (ตัดแต่งหนังฟรี)', 'Gel polish (free cuticle care)', '200'),
        ('ทาสีเจล + เพ้นท์ กี่นิ้วก็ได้', 'Gel polish + nail art, any nails', '350'),
        ('ต่อเล็บ PVC เจลเว้นโคน', 'PVC extensions, gel', '250')],
 'm2': [('สปาเท้า 9 ขั้นตอน', '9-step foot spa', '450')],
 'm3': [('สระไดร์ ทุกความยาว', 'Wash &amp; blow-dry, any length', '150')],
}

def set_th(s, key, html):
    pat = re.compile(r'(<[^>]*data-i18n="%s"[^>]*>)(.*?)(</[a-z0-9]+>)' % re.escape(key), re.S)
    return pat.sub(lambda m: m.group(1)+html+m.group(3), s)

def set_en(s, key, text):
    pat = re.compile(r"('%s':\s*')(.*?)('(?=,|\s*\n|\s*}))" % re.escape(key), re.S)
    return pat.sub(lambda m: m.group(1)+text.replace("'", "’")+m.group(3), s)

def fill_menu(s):
    # แทนรายการ [ชื่อบริการ] ทีละหมวด: หา block ของแต่ละหมวดด้วย m1.title/m2.title/m3.title
    for cat, items in MENU.items():
        start = s.find('data-i18n="%s.title"' % cat)
        if start < 0: continue
        nxt = [s.find('data-i18n="%s.title"' % c, start+1) for c in MENU if c != cat]
        end = min([e for e in nxt if e > 0] + [len(s)])
        block = s[start:end]
        rows = list(re.finditer(r'<(li|tr)[^>]*>.*?data-i18n="m\.item".*?</\1>', block, re.S))
        if not rows: continue
        tmpl = rows[0].group(0)
        new_rows = []
        for i,(th,en,price) in enumerate(items):
            r = tmpl.replace('data-i18n="m.item"', 'data-i18n="%s.i%d"' % (cat,i))
            r = re.sub(r'(data-i18n="%s\.i%d"[^>]*>)\[ชื่อบริการ\]' % (cat,i), r'\g<1>'+th, r)
            r = r.replace('฿ —', '฿ ' + price)
            new_rows.append(r)
        first, last = rows[0].start(), rows[-1].end()
        block = block[:first] + '\n'.join(new_rows) + block[last:]
        s = s[:start] + block + s[end:]
        # EN entries
        add = ''.join("      '%s.i%d': '%s',\n" % (cat,i,en) for i,(th,en,_) in enumerate(items))
        s = s.replace("      'm.item': '[Service name]',\n", "      'm.item': '[Service name]',\n" + add, 1)
    return s

def links(s):
    s = s.replace('href="#" data-todo="เบอร์ร้าน (tel:)"', 'href="%s"' % TEL_HREF)
    s = s.replace('href="#" data-todo="LINE ID ใหม่"', 'href="%s" target="_blank" rel="noopener"' % MSG)
    s = s.replace('href="#" data-todo="ลิงก์หมุด Google Maps"', 'href="%s" target="_blank" rel="noopener"' % MAPS)
    s = s.replace('https://www.facebook.com/share/19eZVxAMZj/', FB1)
    s = s.replace('https://www.facebook.com/share/p/14rrNbiGFDz/', FB2)
    # JSON-LD
    s = s.replace('"address": { "@type": "PostalAddress", "addressLocality": "Surat Thani", "addressCountry": "TH" },',
      '"telephone": "+66646542666",\n    "openingHours": "Mo-Su 09:00-21:00",\n    "priceRange": "฿",\n    "address": { "@type": "PostalAddress", "streetAddress": "ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน", "addressLocality": "Mueang Surat Thani", "addressRegion": "Surat Thani", "addressCountry": "TH" },')
    s = s.replace('"sameAs": ["%s"]' % FB1, '"sameAs": ["%s", "%s"]' % (FB1, FB2))
    # ป้าย DEMO ที่ไม่จำเป็นแล้ว (โปร รีวิว เมนู) → เหลือเฉพาะแกลเลอรี/แผนที่
    s = re.sub(r'\s*<span class="demo[^"]*"[^>]*data-i18n="demo">[^<]*</span>', lambda m: m.group(0) if 'gallery' in s[max(0,m.start()-1200):m.start()] else '', s)
    return s

def run(path):
    s = pathlib.Path(path).read_text(encoding='utf-8')
    for k,v in TH.items(): s = set_th(s, k, v)
    for k,v in EN.items(): s = set_en(s, k, v)
    s = fill_menu(s)
    s = links(s)
    # title / description
    s = s.replace('<title>Nail me (San Chao Market) | ทำเล็บ สปาเท้า สุราษฎร์ธานี</title>', '<title>Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี | ทาสีเจลเริ่มต้น 200 · สปาเท้า 9 ขั้นตอน</title>')
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Nail Me ร้านทำเล็บข้างตลาดศาลเจ้า ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สปาเท้า 9 ขั้นตอน สระไดร์ เปิดทุกวัน 09:00–21:00 โทร 064-654-2666">', s, 1)
    s = s.replace("desc: 'Nail me: nails, foot spa, cut, wash & blow-dry at San Chao Market, Surat Thani. A relaxing stop after work or a day of sightseeing.'", "desc: 'Nail Me: gel nails from 200 THB, 9-step foot spa and blow-dry next to San Chao Market, central Surat Thani. Open daily 09:00–21:00. Thai and international guests welcome.'")
    pathlib.Path(path).write_text(s, encoding='utf-8')
    left = len(re.findall(r'\[[^\]]*\]', re.sub(r'<script.*?</script>', '', s, flags=re.S)))
    print(path, 'ok · วงเล็บ [ ] ที่เหลือ:', left)

for p in sys.argv[1:]: run(p)
