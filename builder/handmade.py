# web-dev/freelance/websites/nail-me/builder/handmade.py
# สร้างแบบ 1–3 ฉบับทำมือ (ไม่ใช้ Tailwind ไม่ใช้โครงร่วม) จากข้อมูลร้านชุดเดียว
#   index.html   แบบ 1 "แมกกาซีน"   ตัวอักษรใหญ่ รูปเต็มความกว้าง ตัวเลขยักษ์ สีโลโก้ ไม่มีทอง
#   design2.html แบบ 2 "ห้องส่วนตัว" ขาวนวล เงียบ รูปใหญ่ทีละรูป (seeUnail)
#   design3.html แบบ 3 "ป้ายหน้าร้าน" กระดาษครีม เขียวเซจ กล่องเมนูหัวแคปซูล ใบไม้วาดเอง (ป้ายราคาในร้าน)
# ใช้: python builder/handmade.py (รันจากโฟลเดอร์ websites/nail-me)
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
PH = json.load(open(ROOT / 'img' / 'photos.json'))
P = lambda k: f'https://lh3.googleusercontent.com/d/{PH[k]}=w1200'
LINE = 'https://line.me/ti/p/~jenny5667'; WA = 'https://wa.me/66849996109'; TEL = 'tel:+66646542666'; MSG = 'https://m.me/nailmesuratthani'
FB1 = 'https://www.facebook.com/profile.php?id=61580350351076'; FB2 = 'https://www.facebook.com/nailmesuratthani'
MAPS_Q = 'Nail+Me+%E0%B8%95%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B8%A8%E0%B8%B2%E0%B8%A5%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2+%E0%B8%AA%E0%B8%B8%E0%B8%A3%E0%B8%B2%E0%B8%A9%E0%B8%8E%E0%B8%A3%E0%B9%8C%E0%B8%98%E0%B8%B2%E0%B8%99%E0%B8%B5'
MAPS = 'https://www.google.com/maps/search/?api=1&query=' + MAPS_Q
EMBED = 'https://www.google.com/maps?q=' + MAPS_Q + '&output=embed&hl=th'

# เมนูเต็มจากป้ายในร้าน
MENU = [
    ('ทาสีเจล', [('ทาสีเจลมือ', 250), ('ทาสีเจลเท้า', 300), ('สีลูกแก้ว Cat Eye', 350)]),
    ('ต่อเล็บ · เสริมเล็บ', [('ต่อเล็บ PVC', 350), ('เสริมหน้าเล็บหลังทาสี', 150), ('เสริมหน้าเล็บก่อนทาสี', 450)]),
    ('ดูแลเล็บ · สปา', [('สปาเท้า 10 ขั้นตอน', 499), ('สปามือ 9 ขั้นตอน', 399), ('Manicure / Pedicure', 200)]),
    ('ถอดเล็บ', [('ถอดสีเจล ทำต่อ (ปกติ 100)', 50), ('ถอด PVC ทำต่อ (ปกติ 200)', 100), ('ถอดไม่ทำ', 100)]),
    ('งานเพิ่ม ต่อ 1 นิ้ว', [('เพ้นท์ลาย', '20+'), ('เฟรนช์ปลาย', '30+'), ('ออมเบร / ไล่ปลาย', '30+'), ('ติดอะไหล่เล็ก ๆ', '20+'), ('ปั้นนูน', '50+')]),
    ('ผม', [('สระไดร์ ทุกความยาว', 150)]),
]
PROMO = [(200, 'ทาสีเจล ตัดแต่งหนังฟรี', 250), (450, 'สปาเท้า 9 ขั้นตอน', 499), (350, 'ทาสีเจล + เพ้นท์ กี่นิ้วก็ได้', None), (250, 'ต่อเล็บ PVC เจลเว้นโคน', 350), (150, 'สระไดร์ ทุกความยาว', None)]
FEED = [('hero', 'ทาสีเจลมือ สีพื้น', 250, 200), ('polka', 'เพ้นท์ลายจุด โบว์', 450, 350), ('toes_brown', 'ทาสีเจลเท้า', 300, None), ('glitter', 'กลิตเตอร์ทอง', 350, None),
        ('french', 'เฟรนช์ + ดอกไม้', 280, None), ('red', 'สีแดงเงา', 250, 200), ('long_clear', 'ต่อเล็บ PVC', 350, 250), ('pink_gems', 'ติดอะไหล่ เพชร', 270, None),
        ('toes_glitter', 'สปาเท้า + กลิตเตอร์', 499, 450), ('white_dots', 'ขาวมินิมอล ลายจุด', 270, None), ('chrome', 'ปลายโครม', 250, None), ('red_long', 'PVC + สีแดง', 350, None),
        ('gold_white', 'ขาวแต่งฟอยล์ทอง', 270, None), ('toes_daisy', 'เท้าลายเดซี่', 300, None), ('french_dots', 'เฟรนช์ลายจุด', 280, None), ('nude2', 'นู้ดเงา', 250, 200),
        ('pink_sparkle', 'ชมพูประกาย', 150, None), ('lace', 'ลายลูกไม้ · สปามือ', 399, None)]
STEPS = ['แช่เกลือ ดีท็อกซ์', 'แช่น้ำนม', 'ฟอก ขัด ล้างเท้า', 'สครับเกลือ', 'มาร์ก + แรป บำรุงล้ำลึก', 'ตัดหนัง', 'ขัดส้นเท้า', 'บำรุงโลชั่น', 'นวดผ่อนคลาย', 'สเปรย์ให้ความชุ่มชื้น']
FAQ = [('ต้องจองคิวล่วงหน้าไหม', 'โทร 064-654-2666 หรือ LINE jenny5667 จองล่วงหน้าได้ หรือ walk-in มาที่ร้านได้เลย เปิดทุกวัน 09:00–21:00'),
       ('ทาสีเจลราคาเท่าไหร่', 'ราคาปกติ มือ 250 เท้า 300 สีลูกแก้ว 350 บาท ช่วงโปรโมชั่นเริ่มต้น 200 บาท ตัดแต่งหนังฟรี แคปโพสต์โปรให้ช่างก่อนรับบริการ'),
       ('ถอดสีเจลที่ทำจากร้านอื่นได้ไหม', 'ได้ ถอดอย่างเดียว 100 บาท ถอดแล้วทำต่อที่ร้าน เจล 50 บาท PVC 100 บาท'),
       ('Do you welcome international travellers?', 'Yes. WhatsApp +66 84 999 6109 or call +66 64 654 2666. Next to San Chao Market, central Surat Thani, open daily 09:00–21:00.')]

def jsonld():
    faq = ','.join('{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (json.dumps(q, ensure_ascii=False), json.dumps(a, ensure_ascii=False)) for q, a in FAQ)
    return f'''  <script type="application/ld+json">
  {{"@context":"https://schema.org","@graph":[
    {{"@type":"NailSalon","name":"Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี","image":"img/og-logo.jpg","telephone":"+66646542666","openingHours":"Mo-Su 09:00-21:00","priceRange":"฿",
     "address":{{"@type":"PostalAddress","streetAddress":"ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน","addressLocality":"Mueang Surat Thani","addressRegion":"Surat Thani","addressCountry":"TH"}},
     "sameAs":["{FB1}","{FB2}","{LINE}"]}},
    {{"@type":"FAQPage","mainEntity":[{faq}]}}]}}
  </script>
'''

def head(title, desc, theme, fonts_link, css, comment):
    return f'''<!doctype html>
<!-- {comment} -->
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex, nofollow">
  <meta property="og:title" content="Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี · ร้านหรู แต่ราคาน่ารัก">
  <meta property="og:image" content="img/og-logo.jpg">
  <meta name="theme-color" content="{theme}">
  <link rel="icon" type="image/png" href="img/favicon-64.png">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{fonts_link}">
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
  <style>
{css}
  </style>
{jsonld()}</head>
'''

JS = '''  <script>
    window.dataLayer = window.dataLayer || [];
    document.addEventListener('click', e => { const el = e.target.closest('[data-track]'); if (el) window.dataLayer.push({ event: 'contact_click', channel: el.dataset.track, href: el.getAttribute('href') }); });
    const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }), { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach((el, i) => { el.style.transitionDelay = (i % 3) * 90 + 'ms'; io.observe(el); });
  </script>
'''

def faq_html(cls='faq'):
    return ''.join(f'<details class="{cls}"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)

TITLE = 'ร้านทำเล็บ สุราษฎร์ธานี · Nail Me ตลาดศาลเจ้า | ทาสีเจล 200 สปาเท้า ต่อเล็บ'
DESC = 'Nail Me ร้านทำเล็บข้างตลาดศาลเจ้า สุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สปาเท้า 10 ขั้นตอน สปามือ ต่อเล็บ PVC เปิดทุกวัน 09:00–21:00 โทร 064-654-2666 LINE jenny5667'

# =====================================================================================
# แบบ 1 "แมกกาซีน"
# =====================================================================================
def build_magazine():
    css = '''    :root { --bg:#FFF7F5; --ink:#241B1C; --pink:#E8929F; --deep:#B5505F; --mute:#7A6A6D; --ease:cubic-bezier(.16,1,.3,1); }
    * { box-sizing: border-box; } html { scroll-behavior: smooth; }
    body { margin: 0; background: var(--bg); color: var(--ink); font-family: "Athiti", sans-serif; font-weight: 400; font-size: 18px; line-height: 1.6; -webkit-font-smoothing: antialiased; }
    img { display: block; max-width: 100%; height: auto; } a { color: inherit; text-decoration: none; }
    .d { font-family: "Pridi", serif; font-weight: 600; line-height: 1.05; letter-spacing: -.02em; }
    .n { font-family: "Chonburi", serif; font-weight: 400; line-height: 1; }
    .wrap { max-width: 1320px; margin: 0 auto; padding: 0 20px; } @media (min-width: 900px) { .wrap { padding: 0 48px; } }
    .rule { border-top: 2px solid var(--ink); }
    /* masthead แบบหนังสือ */
    .mast { display: grid; grid-template-columns: 1fr auto; align-items: center; padding: 14px 0; border-bottom: 2px solid var(--ink); position: sticky; top: 0; background: var(--bg); z-index: 40; }
    .mast .name { font-family: "Pridi", serif; font-weight: 600; font-size: 22px; letter-spacing: -.01em; }
    .mast .meta { display: none; font-size: 13px; color: var(--mute); text-transform: uppercase; letter-spacing: .12em; }
    @media (min-width: 900px) { .mast { grid-template-columns: auto 1fr auto; gap: 32px; } .mast .meta { display: block; } }
    .mast a.tel { font-family: "Chonburi", serif; font-size: 20px; border-bottom: 3px solid var(--deep); }
    /* cover */
    .cover { padding: 28px 0 0; }
    .cover h1 { font-size: clamp(64px, 14.5vw, 232px); margin: 0; line-height: .92; letter-spacing: -.04em; }
    .cover h1 .l2 { color: var(--deep); display: block; }
    .cover .lead { display: grid; gap: 24px; margin-top: 24px; align-items: end; }
    @media (min-width: 900px) { .cover .lead { grid-template-columns: 1fr 1fr 1fr; } }
    .cover .lead p { margin: 0; font-size: 17px; max-width: 24em; }
    .cover .lead .k { font-size: 13px; text-transform: uppercase; letter-spacing: .14em; color: var(--mute); display: block; margin-bottom: 6px; }
    .cover .photo { margin-top: 28px; aspect-ratio: 16 / 9; overflow: hidden; background: #F2DCDC; }
    .cover .photo img { width: 100%; height: 100%; object-fit: cover; }
    .cover .cap { display: flex; justify-content: space-between; gap: 16px; font-size: 13px; color: var(--mute); padding: 10px 0; border-bottom: 1px solid var(--ink); }
    /* ตัวเลขยักษ์ */
    .big { padding: 56px 0 32px; display: grid; gap: 24px; align-items: end; }
    @media (min-width: 900px) { .big { grid-template-columns: auto 1fr; gap: 48px; padding: 96px 0 56px; } }
    .big .num { font-size: clamp(120px, 26vw, 420px); letter-spacing: -.05em; line-height: .8; color: var(--deep); }
    .big .num small { font-size: .28em; vertical-align: top; margin-right: .1em; color: var(--ink); }
    .big .txt h2 { font-size: clamp(28px, 4vw, 48px); margin: 0; }
    .big .txt p { margin: 12px 0 0; max-width: 30em; }
    .big .txt s { color: var(--mute); }
    /* รายการโปร */
    .ticker { display: grid; border-top: 2px solid var(--ink); border-bottom: 2px solid var(--ink); }
    @media (min-width: 900px) { .ticker { grid-template-columns: repeat(5, 1fr); } }
    .ticker div { padding: 20px 0; border-bottom: 1px solid rgba(36,27,28,.2); }
    @media (min-width: 900px) { .ticker div { border-bottom: 0; border-right: 1px solid rgba(36,27,28,.2); padding: 24px 20px 24px 0; } .ticker div:last-child { border-right: 0; } .ticker div + div { padding-left: 20px; } }
    .ticker b { display: block; font-family: "Chonburi", serif; font-weight: 400; font-size: 44px; line-height: 1; }
    .ticker span { font-size: 15px; } .ticker s { color: var(--mute); font-size: 14px; }
    /* spread: รูปเต็มกว้าง + ข้อความชิดขอบ */
    .spread { display: grid; gap: 0; margin-top: 80px; }
    @media (min-width: 900px) { .spread { grid-template-columns: 7fr 5fr; } .spread.flip { grid-template-columns: 5fr 7fr; } .spread.flip .ph { order: 2; } }
    .spread .ph { aspect-ratio: 4 / 5; overflow: hidden; background: #F2DCDC; }
    @media (min-width: 900px) { .spread .ph { aspect-ratio: auto; min-height: 640px; } }
    .spread .ph img { width: 100%; height: 100%; object-fit: cover; }
    .spread .tx { padding: 28px 0 0; } @media (min-width: 900px) { .spread .tx { padding: 48px 0 0 48px; } .spread.flip .tx { padding: 48px 48px 0 0; } }
    .spread .tx .k { font-size: 13px; text-transform: uppercase; letter-spacing: .14em; color: var(--mute); }
    .spread .tx h2 { font-size: clamp(36px, 5vw, 72px); margin: 8px 0 0; }
    .spread .tx p { max-width: 28em; }
    .list { list-style: none; margin: 24px 0 0; padding: 0; }
    .list li { display: flex; justify-content: space-between; gap: 16px; padding: 12px 0; border-top: 1px solid var(--ink); font-size: 17px; }
    .list li b { font-family: "Chonburi", serif; font-weight: 400; font-size: 24px; }
    /* contact sheet: รูปเล็บเรียงแน่นเหมือน contact sheet */
    .sheet { margin-top: 96px; }
    .sheet h2 { font-size: clamp(40px, 7vw, 112px); margin: 0 0 16px; letter-spacing: -.03em; }
    .sheet .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; background: var(--ink); border: 2px solid var(--ink); }
    @media (min-width: 700px) { .sheet .grid { grid-template-columns: repeat(6, 1fr); } }
    .sheet figure { margin: 0; position: relative; background: var(--bg); }
    .sheet img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; }
    .sheet figcaption { padding: 8px 8px 10px; font-size: 12px; line-height: 1.3; display: flex; justify-content: space-between; gap: 6px; }
    .sheet figcaption b { font-family: "Chonburi", serif; font-weight: 400; font-size: 15px; white-space: nowrap; }
    .sheet figcaption s { color: var(--mute); font-size: 11px; }
    /* ราคาเต็ม 3 คอลัมน์แบบหน้าโฆษณา */
    .price { margin-top: 96px; }
    .price h2 { font-size: clamp(40px, 7vw, 112px); margin: 0; letter-spacing: -.03em; }
    .price .cols { display: grid; gap: 0 48px; margin-top: 24px; border-top: 2px solid var(--ink); }
    @media (min-width: 900px) { .price .cols { grid-template-columns: repeat(3, 1fr); } }
    .price h3 { font-family: "Athiti", sans-serif; font-weight: 600; font-size: 14px; text-transform: uppercase; letter-spacing: .14em; margin: 24px 0 4px; color: var(--deep); }
    .price ul { list-style: none; margin: 0; padding: 0; }
    .price li { display: flex; justify-content: space-between; gap: 12px; padding: 8px 0; border-bottom: 1px solid rgba(36,27,28,.2); font-size: 16px; }
    .price li b { font-family: "Chonburi", serif; font-weight: 400; font-size: 20px; }
    /* quote */
    .quote { margin-top: 96px; padding: 64px 0; border-top: 2px solid var(--ink); border-bottom: 2px solid var(--ink); display: grid; gap: 24px; }
    @media (min-width: 900px) { .quote { grid-template-columns: 2fr 1fr; gap: 64px; } }
    .quote blockquote { margin: 0; font-size: clamp(32px, 5vw, 72px); }
    .quote cite { display: block; font-style: normal; font-size: 14px; color: var(--mute); margin-top: 16px; }
    .quote .stat b { display: block; font-family: "Chonburi", serif; font-weight: 400; font-size: 72px; line-height: 1; color: var(--deep); }
    /* steps */
    .steps { margin-top: 96px; display: grid; gap: 32px; } @media (min-width: 900px) { .steps { grid-template-columns: 1fr 1fr; gap: 64px; } }
    .steps ol { list-style: none; padding: 0; margin: 16px 0 0; counter-reset: s; columns: 2; column-gap: 32px; }
    .steps li { counter-increment: s; padding: 8px 0; border-bottom: 1px solid rgba(36,27,28,.2); break-inside: avoid; font-size: 16px; }
    .steps li::before { content: counter(s, decimal-leading-zero); font-family: "Chonburi", serif; color: var(--deep); margin-right: 12px; }
    /* visit */
    .visit { margin-top: 96px; display: grid; gap: 32px; } @media (min-width: 900px) { .visit { grid-template-columns: 1fr 1fr; gap: 64px; } }
    .visit iframe { width: 100%; aspect-ratio: 4 / 3; border: 0; filter: grayscale(1) contrast(1.05); }
    .visit .tel { font-family: "Chonburi", serif; font-size: clamp(36px, 5vw, 64px); line-height: 1; display: block; margin-top: 16px; border-bottom: 4px solid var(--deep); width: max-content; max-width: 100%; }
    .ch { display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin-top: 24px; border-top: 2px solid var(--ink); }
    .ch a { padding: 14px 0; border-bottom: 1px solid rgba(36,27,28,.2); } .ch a small { display: block; font-size: 12px; text-transform: uppercase; letter-spacing: .12em; color: var(--mute); }
    .ch a b { font-family: "Pridi", serif; font-weight: 600; font-size: 20px; }
    .faq { border-bottom: 1px solid rgba(36,27,28,.2); } .faq summary { list-style: none; cursor: pointer; padding: 14px 0; font-weight: 500; display: flex; justify-content: space-between; } .faq summary::-webkit-details-marker { display: none; } .faq summary::after { content: "+"; font-family: "Chonburi", serif; color: var(--deep); } .faq[open] summary::after { content: "–"; } .faq p { margin: 0 0 14px; color: var(--mute); font-size: 15px; }
    footer { margin-top: 96px; padding: 24px 0 110px; border-top: 2px solid var(--ink); font-size: 13px; color: var(--mute); display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; }
    @media (min-width: 768px) { footer { padding-bottom: 40px; } }
    .bar { position: fixed; left: 0; right: 0; bottom: 0; z-index: 50; display: grid; grid-template-columns: 1fr 1fr; background: var(--ink); color: var(--bg); }
    .bar a { display: flex; align-items: center; justify-content: center; gap: 8px; height: 56px; font-weight: 500; } .bar a + a { border-left: 1px solid rgba(255,247,245,.3); }
    @media (min-width: 768px) { .bar { display: none; } }
    .reveal { opacity: 0; transform: translateY(16px); transition: opacity .9s var(--ease), transform .9s var(--ease); } .reveal.in { opacity: 1; transform: none; }
    @media (prefers-reduced-motion: reduce) { .reveal { opacity: 1; transform: none; transition: none; } }'''
    feed = ''.join(f'<figure><img src="{P(k)}" alt="{c} ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"><figcaption><span>{c}</span><b>{("<s>"+str(p)+"</s> " if pr else "")}{pr or p}</b></figcaption></figure>' for k, c, p, pr in FEED)
    ticker = ''.join(f'<div><b>{a}</b><span>{t}{(" <s>"+str(r)+"</s>") if r else ""}</span></div>' for a, t, r in PROMO)
    cols = ''.join(f'<div><h3>{g}</h3><ul>' + ''.join(f'<li><span>{n}</span><b>{v}</b></li>' for n, v in items) + '</ul></div>' for g, items in MENU)
    steps = ''.join(f'<li>{s}</li>' for s in STEPS)
    body = f'''<body>
  <div style="background:var(--ink);color:var(--bg);font-size:12px;text-align:center;padding:6px 16px">ดราฟต์แบบ 1 "แมกกาซีน" · ข้อมูลและรูปจากเพจ/โฟลเดอร์ร้าน 10 ต.ค. 69 · ภาษาอังกฤษทำหลังเลือกแบบ</div>
  <div class="wrap">
    <header class="mast">
      <a class="name" href="#top">Nail Me <span style="font-weight:400;color:var(--mute)">· ตลาดศาลเจ้า</span></a>
      <p class="meta">ร้านทำเล็บ สุราษฎร์ธานี · เปิดทุกวัน 09:00–21:00 · ฉบับ ต.ค. 2569</p>
      <a class="tel" href="{TEL}" data-track="call">064-654-2666</a>
    </header>

    <main id="top">
      <section class="cover">
        <h1 class="d">ร้านหรู<span class="l2">แต่ราคาน่ารัก</span></h1>
        <div class="lead">
          <p><span class="k">ที่ไหน</span>ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน ใจกลางเมืองสุราษฎร์ธานี เยื้อง Tops</p>
          <p><span class="k">ทำอะไร</span>ทาสีเจล 100+ เฉด เพ้นท์ ต่อเล็บ PVC สปาเท้า 10 ขั้นตอน สปามือ สระไดร์ ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน</p>
          <p><span class="k">จองยังไง</span>โทร 064-654-2666 · LINE <a href="{LINE}" data-track="line" target="_blank" rel="noopener" style="border-bottom:2px solid var(--deep)">jenny5667</a> · WhatsApp <a href="{WA}" data-track="whatsapp" target="_blank" rel="noopener" style="border-bottom:2px solid var(--deep)">084-999-6109</a> หรือ walk-in</p>
        </div>
        <div class="photo"><img src="{P('polka')}" alt="เพ้นท์ลายจุดโบว์ ผลงาน Nail Me สุราษฎร์ธานี" fetchpriority="high" width="900" height="1200"></div>
        <p class="cap"><span>ภาพ: เพ้นท์ลายจุด โบว์ · โปร ทาสีเจล + เพ้นท์กี่นิ้วก็ได้ 350</span><span>Nail Me ตลาดศาลเจ้า</span></p>
      </section>

      <section class="big" id="promo">
        <p class="n num"><small>฿</small>200</p>
        <div class="txt">
          <h2 class="d">ทาสีเจล โปรเดือนนี้ <s>250</s></h2>
          <p>ตัดแต่งหนังฟรี เลือกสีได้กว่า 100 เฉด · แคปโพสต์โปรบนเพจให้ช่างดูก่อนรับบริการ · <a href="{FB1}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:2px solid var(--ink)">ดูโพสต์โปร ↗</a></p>
        </div>
      </section>
      <div class="ticker">{ticker}</div>

      <section class="spread reveal" id="spa">
        <div class="ph"><img src="{P('toes_glitter')}" alt="สปาเท้า ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"></div>
        <div class="tx">
          <p class="k">สปา</p>
          <h2 class="d">สปาเท้า 10 ขั้นตอน ขัดถึงใต้เข่า</h2>
          <p>ทำเต็มทุกขั้นตอน ไม่รีบ เหมาะหลังเลิกงานหรือเดินเที่ยวทั้งวัน</p>
          <ul class="list"><li><span>สปาเท้า 10 ขั้นตอน <s style="color:var(--mute)">499</s> โปร</span><b>450</b></li><li><span>สปามือ 9 ขั้นตอน</span><b>399</b></li><li><span>ทาสีเจลเท้า</span><b>300</b></li><li><span>Manicure / Pedicure</span><b>200</b></li></ul>
        </div>
      </section>
      <section class="spread flip reveal">
        <div class="ph"><img src="{P('long_clear')}" alt="ต่อเล็บ PVC ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"></div>
        <div class="tx">
          <p class="k">ต่อเล็บ · เพ้นท์</p>
          <h2 class="d">ต่อเล็บ PVC เจลเว้นโคน</h2>
          <p>ยาวสวยเป็นธรรมชาติ เพ้นท์ลาย เฟรนช์ ออมเบร อะไหล่ คิดเพิ่มต่อนิ้วตามป้าย</p>
          <ul class="list"><li><span>ต่อเล็บ PVC <s style="color:var(--mute)">350</s> โปร</span><b>250</b></li><li><span>ทาสีเจล + เพ้นท์ กี่นิ้วก็ได้ (โปร)</span><b>350</b></li><li><span>เพ้นท์ลาย / ติดอะไหล่ ต่อนิ้ว</span><b>20+</b></li><li><span>เฟรนช์ / ออมเบร ต่อนิ้ว</span><b>30+</b></li></ul>
        </div>
      </section>

      <section class="sheet reveal" id="feed">
        <h2 class="d">ลายที่ทำได้</h2>
        <div class="grid">{feed}</div>
        <p style="font-size:13px;color:var(--mute);margin:10px 0 0">ราคาตามป้ายในร้าน · งานเพ้นท์ขึ้นกับจำนวนนิ้ว · <a href="{FB2}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--ink)">ผลงานล่าสุดบนเพจ ↗</a></p>
      </section>

      <section class="price reveal" id="price">
        <h2 class="d">ราคาเต็ม</h2>
        <div class="cols">{cols}</div>
        <p style="font-size:13px;color:var(--mute);margin:12px 0 0">ตามป้ายราคาในร้าน ต.ค. 69 · บริการผม ขนตา แว็กซ์ สอบถามทางโทรศัพท์</p>
      </section>

      <section class="quote reveal" id="review">
        <div><blockquote class="d">“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”</blockquote><cite>ปฐมาวดี ชูมี · รีวิวบนเพจ Facebook 17 ก.ค. 69 · เล็บเจล · <a href="{FB1}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--ink)">อ่านทั้งหมด ↗</a></cite></div>
        <div class="stat"><b>100%</b>แนะนำ จาก 6 รีวิวบนเพจ · ผู้ติดตาม 1,000+ · เราดูแลให้หลังทำ ไม่ทิ้งงาน</div>
      </section>

      <section class="steps reveal">
        <div><p class="k" style="font-size:13px;text-transform:uppercase;letter-spacing:.14em;color:var(--mute);margin:0">ขั้นตอน</p><h2 class="d" style="font-size:clamp(32px,5vw,64px);margin:8px 0 0">สปาเท้า 10 ขั้นตอน</h2><p>สปามือ 9 ขั้นตอน ลำดับเดียวกัน จบด้วยบำรุงจมูกเล็บด้วยออยล์</p></div>
        <ol>{steps}</ol>
      </section>

      <section class="visit reveal" id="visit">
        <div>
          <h2 class="d" style="font-size:clamp(40px,6vw,88px);margin:0">มาหาเรา</h2>
          <p>ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน เยื้อง ๆ Tops ติดห้างทองก้องไพศาล · เปิดทุกวัน 09:00–21:00 · Thai &amp; international guests welcome</p>
          <a class="tel" href="{TEL}" data-track="call">064-654-2666</a>
          <div class="ch"><a href="{LINE}" target="_blank" rel="noopener" data-track="line"><small>LINE</small><b>jenny5667</b></a><a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp"><small>WhatsApp</small><b>084-999-6109</b></a><a href="{MSG}" target="_blank" rel="noopener" data-track="message"><small>Facebook</small><b>ทักเพจ</b></a><a href="{MAPS}" target="_blank" rel="noopener" data-track="directions"><small>Google Maps</small><b>นำทาง ↗</b></a></div>
          <div style="margin-top:32px">{faq_html()}</div>
        </div>
        <iframe src="{EMBED}" title="แผนที่ Nail Me ตลาดศาลเจ้า" loading="lazy"></iframe>
      </section>
    </main>
    <footer><span>© 2026 Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี</span><span><a href="{FB1}" target="_blank" rel="noopener" data-track="facebook">เพจหลัก</a> · <a href="{FB2}" target="_blank" rel="noopener" data-track="facebook">เพจสำรอง</a> · <a href="#" data-todo="หน้านโยบายความเป็นส่วนตัว">นโยบายความเป็นส่วนตัว</a></span></footer>
  </div>
  <div class="bar"><a href="{TEL}" data-track="call"><i class="ph ph-phone"></i>โทรจองคิว</a><a href="{LINE}" target="_blank" rel="noopener" data-track="line"><i class="ph ph-chat-circle-dots"></i>ทัก LINE</a></div>
{JS}</body>
</html>
'''
    fonts = 'https://fonts.googleapis.com/css2?family=Pridi:wght@600&family=Chonburi&family=Athiti:wght@400;500;600&display=swap'
    (ROOT / 'index.html').write_text(head(TITLE, DESC, '#FFF7F5', fonts, css, 'web-dev/freelance/websites/nail-me/index.html · แบบ 1 "แมกกาซีน" ทำมือ (builder/handmade.py)') + body)

# =====================================================================================
# แบบ 2 "ห้องส่วนตัว" (seeUnail: ส่วนตัว สะอาด เงียบ)
# =====================================================================================
def build_quiet():
    css = '''    :root { --bg:#FBFAF8; --ink:#1F1D1B; --mute:#8A8580; --line:#E6E2DC; --rose:#C98E95; --ease:cubic-bezier(.16,1,.3,1); }
    * { box-sizing: border-box; } html { scroll-behavior: smooth; }
    body { margin: 0; background: var(--bg); color: var(--ink); font-family: "Sarabun", sans-serif; font-weight: 300; font-size: 17px; line-height: 1.8; -webkit-font-smoothing: antialiased; }
    img { display: block; max-width: 100%; height: auto; } a { color: inherit; text-decoration: none; }
    .d { font-family: "Pridi", serif; font-weight: 300; line-height: 1.25; letter-spacing: -.01em; }
    .wrap { max-width: 1120px; margin: 0 auto; padding: 0 24px; } @media (min-width: 900px) { .wrap { padding: 0 40px; } }
    .k { font-size: 11px; letter-spacing: .28em; text-transform: uppercase; color: var(--mute); }
    header { position: sticky; top: 0; z-index: 40; background: rgba(251,250,248,.9); backdrop-filter: blur(8px); }
    header .wrap { height: 64px; display: flex; align-items: center; justify-content: space-between; }
    header .brand { font-family: "Pridi", serif; font-weight: 300; font-size: 20px; letter-spacing: .04em; }
    header nav { display: none; gap: 28px; font-size: 12px; letter-spacing: .2em; text-transform: uppercase; } @media (min-width: 900px) { header nav { display: flex; } }
    header .tel { font-size: 13px; letter-spacing: .1em; border-bottom: 1px solid var(--ink); padding-bottom: 2px; }
    /* chapter 1 */
    .c1 { min-height: calc(100svh - 64px); display: grid; align-content: center; padding: 56px 0; gap: 32px; }
    @media (min-width: 900px) { .c1 { grid-template-columns: 5fr 7fr; gap: 64px; align-items: center; } }
    .c1 h1 { font-size: clamp(36px, 5vw, 64px); margin: 0; font-weight: 300; }
    .c1 h1 i { font-style: normal; color: var(--rose); }
    .c1 p { max-width: 26em; margin: 20px 0 0; }
    .c1 .ph { aspect-ratio: 4 / 5; overflow: hidden; } .c1 .ph img { width: 100%; height: 100%; object-fit: cover; }
    .c1 .ph figcaption { font-size: 12px; color: var(--mute); margin-top: 10px; letter-spacing: .04em; }
    .c1 .cta { margin-top: 32px; display: flex; gap: 28px; flex-wrap: wrap; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; }
    .c1 .cta a { border-bottom: 1px solid var(--ink); padding-bottom: 4px; }
    /* chapter: ทีละรูป */
    .ch { padding: 96px 0 0; display: grid; gap: 24px; } @media (min-width: 900px) { .ch { grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; } .ch.r .ph { order: 2; } }
    .ch .ph { aspect-ratio: 3 / 4; overflow: hidden; } .ch .ph img { width: 100%; height: 100%; object-fit: cover; }
    .ch h2 { font-size: clamp(28px, 3.5vw, 44px); margin: 12px 0 0; font-weight: 300; }
    .ch p { max-width: 26em; }
    .ch dl { margin: 24px 0 0; display: grid; grid-template-columns: 1fr auto; gap: 8px 24px; font-size: 15px; }
    .ch dt { border-top: 1px solid var(--line); padding-top: 8px; } .ch dd { margin: 0; border-top: 1px solid var(--line); padding-top: 8px; font-family: "Pridi", serif; font-weight: 400; font-size: 18px; text-align: right; }
    .ch dd s { color: var(--mute); font-size: 13px; margin-right: 6px; font-family: "Sarabun", sans-serif; }
    /* โปร: แถวเงียบ */
    .promo { margin-top: 112px; border-top: 1px solid var(--ink); padding-top: 24px; display: grid; gap: 24px; } @media (min-width: 900px) { .promo { grid-template-columns: 1fr 2fr; } }
    .promo ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 0; }
    .promo li { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 14px 0; border-bottom: 1px solid var(--line); }
    .promo li b { font-family: "Pridi", serif; font-weight: 400; font-size: 26px; } .promo li s { color: var(--mute); font-size: 13px; margin-left: 8px; }
    /* album */
    .album { margin-top: 112px; }
    .album .row { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-top: 24px; } @media (min-width: 700px) { .album .row { grid-template-columns: repeat(3, 1fr); gap: 24px; } }
    .album figure { margin: 0; } .album img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; }
    .album figcaption { display: flex; justify-content: space-between; gap: 8px; font-size: 12px; color: var(--mute); margin-top: 8px; letter-spacing: .02em; }
    .album figcaption b { font-family: "Pridi", serif; font-weight: 400; font-size: 15px; color: var(--ink); white-space: nowrap; }
    .album .row.wide figure:first-child { grid-column: span 2; } .album .row.wide figure:first-child img { aspect-ratio: 16 / 10; height: 100%; }
    /* price */
    .price { margin-top: 112px; display: grid; gap: 24px; } @media (min-width: 900px) { .price { grid-template-columns: 1fr 2fr; gap: 80px; } }
    .price .cols { display: grid; gap: 0 40px; } @media (min-width: 700px) { .price .cols { grid-template-columns: 1fr 1fr; } }
    .price h3 { font-size: 11px; letter-spacing: .28em; text-transform: uppercase; color: var(--mute); font-weight: 400; margin: 24px 0 4px; }
    .price ul { list-style: none; margin: 0; padding: 0; } .price li { display: flex; justify-content: space-between; gap: 12px; padding: 8px 0; border-bottom: 1px solid var(--line); font-size: 15px; }
    .price li b { font-family: "Pridi", serif; font-weight: 400; font-size: 17px; }
    /* review */
    .rev { margin-top: 112px; text-align: center; max-width: 720px; margin-left: auto; margin-right: auto; }
    .rev blockquote { margin: 16px 0 0; font-size: clamp(26px, 3.5vw, 40px); }
    .rev cite { display: block; font-style: normal; font-size: 13px; color: var(--mute); margin-top: 16px; letter-spacing: .04em; }
    .rev .stat { margin-top: 32px; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; color: var(--mute); }
    .rev .stat b { font-family: "Pridi", serif; font-weight: 300; font-size: 48px; color: var(--ink); display: block; letter-spacing: 0; text-transform: none; }
    /* steps */
    .steps { margin-top: 112px; display: grid; gap: 24px; } @media (min-width: 900px) { .steps { grid-template-columns: 1fr 2fr; gap: 80px; } }
    .steps ol { list-style: none; padding: 0; margin: 0; counter-reset: s; columns: 2; column-gap: 40px; }
    .steps li { counter-increment: s; padding: 8px 0; border-bottom: 1px solid var(--line); break-inside: avoid; font-size: 15px; }
    .steps li::before { content: counter(s, decimal-leading-zero); color: var(--mute); margin-right: 14px; font-size: 12px; letter-spacing: .1em; }
    /* visit */
    .visit { margin-top: 112px; display: grid; gap: 32px; } @media (min-width: 900px) { .visit { grid-template-columns: 1fr 1fr; gap: 80px; } }
    .visit iframe { width: 100%; aspect-ratio: 4 / 3; border: 0; filter: grayscale(1); }
    .visit .lines a { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid var(--line); font-size: 15px; } .visit .lines a span:first-child { color: var(--mute); font-size: 12px; letter-spacing: .2em; text-transform: uppercase; }
    .faq { border-bottom: 1px solid var(--line); } .faq summary { list-style: none; cursor: pointer; padding: 12px 0; display: flex; justify-content: space-between; font-size: 15px; } .faq summary::-webkit-details-marker { display: none; } .faq summary::after { content: "+"; color: var(--mute); } .faq[open] summary::after { content: "–"; } .faq p { margin: 0 0 12px; color: var(--mute); font-size: 14px; }
    footer { margin-top: 112px; padding: 24px 0 110px; border-top: 1px solid var(--line); font-size: 12px; color: var(--mute); letter-spacing: .04em; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; }
    @media (min-width: 768px) { footer { padding-bottom: 40px; } }
    .bar { position: fixed; left: 0; right: 0; bottom: 0; z-index: 50; display: grid; grid-template-columns: 1fr 1fr; background: var(--bg); border-top: 1px solid var(--line); }
    .bar a { display: flex; align-items: center; justify-content: center; gap: 8px; height: 56px; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; } .bar a + a { border-left: 1px solid var(--line); }
    @media (min-width: 768px) { .bar { display: none; } }
    .reveal { opacity: 0; transform: translateY(12px); transition: opacity 1.2s var(--ease), transform 1.2s var(--ease); } .reveal.in { opacity: 1; transform: none; }
    @media (prefers-reduced-motion: reduce) { .reveal { opacity: 1; transform: none; transition: none; } }'''
    rows = ''; i = 0; k = 0
    while i < len(FEED):
        n = 3 if k % 2 == 0 else 2
        chunk = FEED[i:i+n]; i += n; k += 1
        cls = 'row' if n == 3 else 'row wide'
        rows += f'<div class="{cls}">' + ''.join(f'<figure><img src="{P(kk)}" alt="{c} ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"><figcaption><span>{c}</span><b>{("<s style=\'color:var(--mute);font-weight:300;font-size:11px\'>"+str(p)+"</s> " if pr else "")}฿{pr or p}</b></figcaption></figure>' for kk, c, p, pr in chunk) + '</div>'
    promo = ''.join(f'<li><span>{t}{(" <s>"+str(r)+"</s>") if r else ""}</span><b>฿{a}</b></li>' for a, t, r in PROMO)
    cols = ''.join(f'<div><h3>{g}</h3><ul>' + ''.join(f'<li><span>{n}</span><b>{v}</b></li>' for n, v in items) + '</ul></div>' for g, items in MENU)
    steps = ''.join(f'<li>{s}</li>' for s in STEPS)
    body = f'''<body>
  <div style="background:var(--ink);color:var(--bg);font-size:12px;text-align:center;padding:6px 16px;letter-spacing:.04em">ดราฟต์แบบ 2 "ห้องส่วนตัว" · ข้อมูลและรูปจากเพจ/โฟลเดอร์ร้าน 10 ต.ค. 69 · ภาษาอังกฤษทำหลังเลือกแบบ</div>
  <header><div class="wrap"><a class="brand" href="#top">Nail Me</a><nav><a href="#album">ผลงาน</a><a href="#price">ราคา</a><a href="#spa">สปา</a><a href="#visit">ที่ตั้ง</a></nav><a class="tel" href="{TEL}" data-track="call">064-654-2666</a></div></header>
  <main id="top" class="wrap">
    <section class="c1">
      <div>
        <p class="k">ร้านทำเล็บ · ตลาดศาลเจ้า สุราษฎร์ธานี</p>
        <h1 class="d">ร้านเล็ก ๆ ที่เงียบ สะอาด<br>และ<i>ราคาน่ารัก</i></h1>
        <p>ทาสีเจลเริ่มต้น 200 บาท สีให้เลือกกว่า 100 เฉด สปาเท้า 10 ขั้นตอน สปามือ ต่อเล็บ PVC ช่างดูแลทีละคน ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน ยินดีต้อนรับทั้งลูกค้าไทยและนักท่องเที่ยว</p>
        <div class="cta"><a href="{TEL}" data-track="call">โทรจองคิว</a><a href="{LINE}" target="_blank" rel="noopener" data-track="line">LINE jenny5667</a><a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">WhatsApp</a></div>
        <p style="font-size:12px;color:var(--mute);letter-spacing:.06em;margin-top:24px">เปิดทุกวัน 09:00–21:00 · จองคิวหรือ walk-in</p>
      </div>
      <figure class="ph" style="margin:0"><img src="{P('hero')}" alt="ทาสีเจลมือสีนู้ด ผลงาน Nail Me" fetchpriority="high" width="900" height="1200"><figcaption>ทาสีเจลมือ สีพื้น · 250 (โปร 200)</figcaption></figure>
    </section>

    <section class="ch reveal" id="spa">
      <div class="ph"><img src="{P('toes_glitter')}" alt="สปาเท้า ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"></div>
      <div><p class="k">01 · สปา</p><h2 class="d">สปาเท้า 10 ขั้นตอน ขัดถึงใต้เข่า</h2><p>แช่เกลือ แช่น้ำนม ขัด สครับ มาร์ก ตัดหนัง ขัดส้น บำรุง นวด จบด้วยสเปรย์ชุ่มชื้น ทำเต็มทุกขั้นตอน ไม่รีบ</p>
        <dl><dt>สปาเท้า 10 ขั้นตอน</dt><dd><s>499</s>450</dd><dt>สปามือ 9 ขั้นตอน</dt><dd>399</dd><dt>ทาสีเจลเท้า</dt><dd>300</dd></dl></div>
    </section>
    <section class="ch r reveal">
      <div class="ph"><img src="{P('french')}" alt="เล็บเฟรนช์ปลายลายดอกไม้ ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"></div>
      <div><p class="k">02 · ทาสีเจล · เพ้นท์</p><h2 class="d">สีเจล 100+ เฉด เพ้นท์ลายคิดต่อนิ้ว</h2><p>สีพื้น เฟรนช์ ออมเบร โครม อะไหล่ ช่างช่วยเลือกให้เข้ากับมือ ส่งรูปลายที่ชอบมาทาง LINE ได้ก่อน</p>
        <dl><dt>ทาสีเจลมือ</dt><dd><s>250</s>200</dd><dt>ทาสีเจล + เพ้นท์ กี่นิ้วก็ได้ (โปร)</dt><dd>350</dd><dt>เพ้นท์ / อะไหล่ · เฟรนช์ / ออมเบร ต่อนิ้ว</dt><dd>20+ · 30+</dd></dl></div>
    </section>
    <section class="ch reveal">
      <div class="ph"><img src="{P('long_clear')}" alt="ต่อเล็บ PVC ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"></div>
      <div><p class="k">03 · ต่อเล็บ</p><h2 class="d">ต่อเล็บ PVC เจลเว้นโคน</h2><p>ยาวสวยเป็นธรรมชาติ เสริมหน้าเล็บให้แข็งแรงก่อนหรือหลังลงสี ถอดของร้านอื่นแล้วทำต่อได้</p>
        <dl><dt>ต่อเล็บ PVC</dt><dd><s>350</s>250</dd><dt>เสริมหน้าเล็บ ก่อน / หลังทาสี</dt><dd>450 / 150</dd><dt>ถอดเจล ทำต่อ</dt><dd>50</dd></dl></div>
    </section>

    <section class="promo reveal" id="promo"><div><p class="k">โปรเดือนนี้</p><p style="margin:8px 0 0;max-width:22em">แคปโพสต์โปรบนเพจให้ช่างดูก่อนรับบริการ · <a href="{FB1}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--ink)">ดูโพสต์</a></p></div><ul>{promo}</ul></section>

    <section class="album reveal" id="album"><p class="k">ผลงาน</p><h2 class="d" style="font-size:clamp(28px,3.5vw,44px);margin:8px 0 0;font-weight:300">ลายที่ทำได้ ราคาตามป้าย</h2>{rows}<p style="font-size:12px;color:var(--mute);margin-top:16px;letter-spacing:.04em">งานเพ้นท์ขึ้นกับจำนวนนิ้ว · <a href="{FB2}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--ink)">ผลงานล่าสุดบนเพจ</a></p></section>

    <section class="price reveal" id="price"><div><p class="k">ราคาเต็ม</p><h2 class="d" style="font-size:clamp(28px,3.5vw,44px);margin:8px 0 0;font-weight:300">ตามป้ายในร้าน</h2><p style="font-size:14px;color:var(--mute)">ต.ค. 2569 · บริการผม ขนตา แว็กซ์ สอบถามทางโทรศัพท์</p></div><div class="cols">{cols}</div></section>

    <section class="rev reveal" id="review"><p class="k">ลูกค้าว่า</p><blockquote class="d">“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”</blockquote><cite>ปฐมาวดี ชูมี · รีวิวบนเพจ Facebook 17 ก.ค. 69 · เล็บเจล</cite><p class="stat"><b>100%</b>แนะนำ จาก 6 รีวิว · ผู้ติดตาม 1,000+ · <a href="{FB1}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--ink)">อ่านทั้งหมด</a></p></section>

    <section class="steps reveal"><div><p class="k">ขั้นตอน</p><h2 class="d" style="font-size:clamp(28px,3.5vw,44px);margin:8px 0 0;font-weight:300">สปาเท้า 10 ขั้นตอน</h2><p style="font-size:14px;color:var(--mute)">สปามือ 9 ขั้นตอน ลำดับเดียวกัน จบด้วยบำรุงจมูกเล็บด้วยออยล์</p></div><ol>{steps}</ol></section>

    <section class="visit reveal" id="visit">
      <div><p class="k">ที่ตั้ง</p><h2 class="d" style="font-size:clamp(28px,3.5vw,44px);margin:8px 0 0;font-weight:300">ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน</h2><p>เยื้อง ๆ Tops ติดห้างทองก้องไพศาล · เปิดทุกวัน 09:00–21:00 · Thai &amp; international guests welcome</p>
        <div class="lines"><a href="{TEL}" data-track="call"><span>โทร</span><span>064-654-2666</span></a><a href="{LINE}" target="_blank" rel="noopener" data-track="line"><span>LINE</span><span>jenny5667</span></a><a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp"><span>WhatsApp</span><span>084-999-6109</span></a><a href="{MSG}" target="_blank" rel="noopener" data-track="message"><span>Facebook</span><span>ทักเพจ</span></a><a href="{MAPS}" target="_blank" rel="noopener" data-track="directions"><span>Maps</span><span>นำทาง ↗</span></a></div>
        <div style="margin-top:32px">{faq_html()}</div></div>
      <iframe src="{EMBED}" title="แผนที่ Nail Me ตลาดศาลเจ้า" loading="lazy"></iframe>
    </section>
    <footer><span>© 2026 Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี</span><span><a href="{FB1}" target="_blank" rel="noopener" data-track="facebook">เพจหลัก</a> · <a href="{FB2}" target="_blank" rel="noopener" data-track="facebook">เพจสำรอง</a> · <a href="#" data-todo="หน้านโยบายความเป็นส่วนตัว">นโยบายความเป็นส่วนตัว</a></span></footer>
  </main>
  <div class="bar"><a href="{TEL}" data-track="call"><i class="ph ph-phone"></i>โทรจอง</a><a href="{LINE}" target="_blank" rel="noopener" data-track="line"><i class="ph ph-chat-circle-dots"></i>LINE</a></div>
{JS}</body>
</html>
'''
    fonts = 'https://fonts.googleapis.com/css2?family=Pridi:wght@300;400&family=Sarabun:wght@300;400;500&display=swap'
    (ROOT / 'design2.html').write_text(head(TITLE, DESC, '#FBFAF8', fonts, css, 'web-dev/freelance/websites/nail-me/design2.html · แบบ 2 "ห้องส่วนตัว" ทำมือ โครงจาก seeunail (builder/handmade.py)') + body)

# =====================================================================================
# แบบ 3 "ป้ายหน้าร้าน" (จากป้ายราคาพิมพ์ในร้าน: ครีม เซจ กล่องเมนูหัวแคปซูล ใบไม้วาดเอง)
# =====================================================================================
LEAF = '''<svg class="leaf" viewBox="0 0 120 60" aria-hidden="true"><path d="M4 50 C 30 10, 70 6, 116 12 C 80 20, 50 36, 4 50 Z M 4 50 C 40 30, 70 22, 112 14" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M26 40 l6 -12 M42 32 l5 -13 M60 26 l4 -12 M78 21 l3 -10" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>'''
def build_board():
    css = '''    :root { --paper:#FBF7EE; --paper2:#F3ECDD; --ink:#2F3A2E; --sage:#6F8468; --deep:#4B5C47; --mute:#7C8477; --rose:#D9A1A6; --ease:cubic-bezier(.16,1,.3,1); }
    * { box-sizing: border-box; } html { scroll-behavior: smooth; }
    body { margin: 0; background: var(--paper); color: var(--ink); font-family: "Mitr", sans-serif; font-weight: 300; font-size: 17px; line-height: 1.7; -webkit-font-smoothing: antialiased; }
    body::before { content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 60; opacity: .06; mix-blend-mode: multiply; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"); }
    img { display: block; max-width: 100%; height: auto; } a { color: inherit; text-decoration: none; }
    .d { font-family: "Pridi", serif; font-weight: 400; line-height: 1.2; }
    .wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px; } @media (min-width: 900px) { .wrap { padding: 0 40px; } }
    .leaf { width: 72px; height: 36px; color: var(--sage); }
    .pill { display: inline-flex; align-items: center; gap: 8px; height: 38px; padding: 0 18px; border-radius: 999px; background: var(--deep); color: var(--paper); font-family: "Pridi", serif; font-size: 18px; line-height: 1; }
    .pill.light { background: transparent; color: var(--deep); border: 1.5px solid var(--deep); }
    header { position: sticky; top: 0; z-index: 40; background: rgba(251,247,238,.92); backdrop-filter: blur(6px); border-bottom: 1px solid rgba(47,58,46,.15); }
    header .wrap { height: 62px; display: flex; align-items: center; justify-content: space-between; gap: 12px; }
    header .brand { display: flex; align-items: center; gap: 10px; font-family: "Pridi", serif; font-size: 20px; } header .brand img { width: 34px; height: 34px; border-radius: 50%; }
    header nav { display: none; gap: 22px; font-size: 14px; } @media (min-width: 900px) { header nav { display: flex; } } header nav a:hover { color: var(--sage); }
    /* ป้ายใหญ่ (hero) */
    .board { margin: 32px auto 0; background: #FFFDF8; border: 1px solid rgba(47,58,46,.2); border-radius: 18px; padding: 28px 22px 32px; box-shadow: 0 24px 60px rgba(47,58,46,.12); position: relative; }
    @media (min-width: 900px) { .board { padding: 48px 56px; margin-top: 48px; } }
    .board::before { content: ""; position: absolute; inset: 10px; border: 1px solid rgba(111,132,104,.35); border-radius: 12px; pointer-events: none; }
    .hero { display: grid; gap: 24px; align-items: center; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 1fr; gap: 48px; } }
    .hero .logo { width: 72px; height: 72px; border-radius: 50%; }
    .hero h1 { font-size: clamp(38px, 6vw, 72px); margin: 12px 0 0; }
    .hero h1 i { font-style: normal; color: var(--sage); }
    .hero .en { font-size: 12px; letter-spacing: .3em; text-transform: uppercase; color: var(--mute); margin-top: 4px; }
    .hero p { max-width: 28em; margin: 16px 0 0; }
    .hero .tel { display: inline-block; font-family: "Pridi", serif; font-size: clamp(30px, 4.5vw, 44px); line-height: 1; margin-top: 20px; color: var(--deep); border-bottom: 2px solid var(--sage); }
    .hero .ph { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; } .hero .ph img { width: 100%; aspect-ratio: 3 / 4; object-fit: cover; border-radius: 12px; }
    .hero .ph img:first-child { grid-row: span 2; aspect-ratio: auto; height: 100%; }
    .hero .ph figcaption { grid-column: span 2; font-size: 12px; color: var(--mute); }
    /* กล่องเมนูแบบป้ายในร้าน */
    .menus { margin-top: 56px; display: grid; gap: 20px; } @media (min-width: 760px) { .menus { grid-template-columns: 1fr 1fr; gap: 24px; } }
    .box { background: #FFFDF8; border: 1px solid rgba(47,58,46,.2); border-radius: 16px; padding: 20px; position: relative; }
    .box .pill { margin: -34px 0 0 -4px; }
    .box ul { list-style: none; margin: 14px 0 0; padding: 0; }
    .box li { display: flex; align-items: baseline; gap: 10px; padding: 8px 0; border-bottom: 1px dotted rgba(47,58,46,.35); font-size: 15px; }
    .box li span:first-child { flex: 1; } .box li small { color: var(--mute); font-size: 12px; display: block; }
    .box li b { font-family: "Pridi", serif; font-weight: 400; font-size: 19px; color: var(--deep); white-space: nowrap; } .box li b small { display: inline; margin-right: 4px; }
    .box .leaf { position: absolute; right: 14px; top: -16px; width: 56px; height: 28px; }
    .box img.thumb { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 10px; margin-top: 14px; }
    /* โปรเป็นป้ายแขวน */
    .hang { margin-top: 56px; background: var(--deep); color: var(--paper); border-radius: 16px; padding: 24px 22px; display: grid; gap: 16px; position: relative; }
    @media (min-width: 900px) { .hang { grid-template-columns: auto 1fr auto; align-items: center; gap: 40px; padding: 28px 40px; } }
    .hang::before { content: ""; position: absolute; left: 50%; top: -22px; width: 2px; height: 22px; background: var(--deep); }
    .hang h2 { font-size: 26px; margin: 0; } .hang ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px 28px; }
    .hang li b { font-family: "Pridi", serif; font-weight: 400; font-size: 32px; line-height: 1; margin-right: 6px; } .hang li s { opacity: .6; font-size: 13px; }
    .hang a { font-size: 14px; border-bottom: 1px solid rgba(251,247,238,.6); }
    /* feed: รูปแปะบนป้าย */
    .feed { margin-top: 64px; }
    .feed .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 20px; } @media (min-width: 700px) { .feed .grid { grid-template-columns: repeat(4, 1fr); gap: 18px; } }
    .feed figure { margin: 0; background: #FFFDF8; border: 1px solid rgba(47,58,46,.18); border-radius: 12px; padding: 8px; transform: rotate(var(--r, 0)); }
    .feed img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 8px; }
    .feed figcaption { display: flex; justify-content: space-between; gap: 6px; font-size: 12px; margin-top: 8px; padding: 0 2px; }
    .feed figcaption b { font-family: "Pridi", serif; font-weight: 400; font-size: 15px; color: var(--deep); white-space: nowrap; } .feed figcaption s { color: var(--mute); font-size: 11px; }
    /* สปา step board */
    .spa { margin-top: 64px; display: grid; gap: 24px; } @media (min-width: 900px) { .spa { grid-template-columns: 1fr 1.2fr; gap: 48px; align-items: center; } }
    .spa img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; border-radius: 16px; }
    .spa ol { list-style: none; padding: 0; margin: 16px 0 0; counter-reset: s; display: grid; grid-template-columns: 1fr 1fr; gap: 8px 20px; }
    .spa li { counter-increment: s; font-size: 15px; padding-left: 36px; position: relative; }
    .spa li::before { content: counter(s); position: absolute; left: 0; top: 2px; width: 26px; height: 26px; border-radius: 50%; border: 1.5px solid var(--sage); color: var(--sage); font-size: 12px; display: grid; place-items: center; font-family: "Pridi", serif; }
    .spa .big { font-family: "Pridi", serif; font-size: 48px; color: var(--deep); line-height: 1; } .spa .big s { font-size: 18px; color: var(--mute); margin-right: 8px; }
    /* review tag */
    .rev { margin-top: 64px; background: #FFFDF8; border: 1px solid rgba(47,58,46,.2); border-radius: 16px; padding: 28px 22px; display: grid; gap: 16px; } @media (min-width: 900px) { .rev { grid-template-columns: 2fr 1fr; padding: 40px; gap: 40px; } }
    .rev blockquote { margin: 0; font-size: clamp(24px, 3.5vw, 36px); } .rev cite { display: block; font-style: normal; font-size: 13px; color: var(--mute); margin-top: 12px; }
    .rev .stat { border-left: 1.5px solid var(--sage); padding-left: 20px; font-size: 14px; color: var(--mute); } .rev .stat b { display: block; font-family: "Pridi", serif; font-weight: 400; font-size: 44px; color: var(--deep); line-height: 1; }
    /* visit */
    .visit { margin-top: 64px; display: grid; gap: 24px; } @media (min-width: 900px) { .visit { grid-template-columns: 1fr 1fr; gap: 48px; } }
    .visit iframe { width: 100%; aspect-ratio: 4 / 3; border: 0; border-radius: 16px; filter: sepia(.2) saturate(.7); }
    .visit .ch { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 16px; }
    .visit .ch a { background: #FFFDF8; border: 1px solid rgba(47,58,46,.2); border-radius: 12px; padding: 10px 14px; font-size: 15px; } .visit .ch a small { display: block; font-size: 11px; color: var(--mute); letter-spacing: .1em; text-transform: uppercase; }
    .faq { border-bottom: 1px dotted rgba(47,58,46,.35); } .faq summary { list-style: none; cursor: pointer; padding: 12px 0; display: flex; justify-content: space-between; font-weight: 400; } .faq summary::-webkit-details-marker { display: none; } .faq summary::after { content: "+"; color: var(--sage); } .faq[open] summary::after { content: "–"; } .faq p { margin: 0 0 12px; color: var(--mute); font-size: 14px; }
    footer { margin-top: 64px; padding: 24px 0 110px; border-top: 1px solid rgba(47,58,46,.2); font-size: 13px; color: var(--mute); text-align: center; } @media (min-width: 768px) { footer { padding-bottom: 40px; } }
    .bar { position: fixed; left: 0; right: 0; bottom: 0; z-index: 50; display: grid; grid-template-columns: 1fr 1fr; gap: 8px; padding: 10px 16px calc(10px + env(safe-area-inset-bottom)); background: rgba(251,247,238,.95); border-top: 1px solid rgba(47,58,46,.15); }
    .bar a { display: flex; align-items: center; justify-content: center; gap: 8px; height: 46px; border-radius: 999px; font-weight: 400; } .bar .a1 { background: var(--deep); color: var(--paper); } .bar .a2 { border: 1.5px solid var(--deep); color: var(--deep); }
    @media (min-width: 768px) { .bar { display: none; } }
    .reveal { opacity: 0; transform: translateY(14px); transition: opacity .9s var(--ease), transform .9s var(--ease); } .reveal.in { opacity: 1; transform: none; }
    @media (prefers-reduced-motion: reduce) { .reveal { opacity: 1; transform: none; transition: none; } }'''
    thumbs = {'ทาสีเจล': 'nude2', 'ต่อเล็บ · เสริมเล็บ': 'long_clear', 'ดูแลเล็บ · สปา': 'toes_glitter', 'ถอดเล็บ': None, 'งานเพิ่ม ต่อ 1 นิ้ว': 'pink_gems', 'ผม': None}
    boxes = ''
    for g, items in MENU:
        rows = ''.join(f'<li><span>{n}</span><b>{v}</b></li>' for n, v in items)
        th = thumbs.get(g)
        boxes += f'<div class="box reveal"><span class="pill">{g}</span>{LEAF}<ul>{rows}</ul>' + (f'<img class="thumb" src="{P(th)}" alt="{g} ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200">' if th else '') + '</div>'
    promo = ''.join(f'<li><b>{a}</b>{t}{(" <s>"+str(r)+"</s>") if r else ""}</li>' for a, t, r in PROMO)
    rots = [-1.2, .8, -.6, 1.4, .5, -1, 1, -.8]
    feed = ''.join(f'<figure style="--r:{rots[i % len(rots)]}deg"><img src="{P(k)}" alt="{c} ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200"><figcaption><span>{c}</span><b>{("<s>"+str(p)+"</s> " if pr else "")}{pr or p}</b></figcaption></figure>' for i, (k, c, p, pr) in enumerate(FEED[:12]))
    steps = ''.join(f'<li>{s}</li>' for s in STEPS)
    body = f'''<body>
  <div style="background:var(--deep);color:var(--paper);font-size:12px;text-align:center;padding:6px 16px">ดราฟต์แบบ 3 "ป้ายหน้าร้าน" · ข้อมูลและรูปจากเพจ/โฟลเดอร์ร้าน 10 ต.ค. 69 · ภาษาอังกฤษทำหลังเลือกแบบ</div>
  <header><div class="wrap"><a class="brand" href="#top"><img src="img/nail-me-logo-160.png" alt="" width="34" height="34">Nail Me</a><nav><a href="#menu">ราคา</a><a href="#promo">โปร</a><a href="#feed">ผลงาน</a><a href="#spa">สปา</a><a href="#visit">ที่ตั้ง</a></nav><a class="pill" style="height:36px;font-size:15px" href="{TEL}" data-track="call"><i class="ph ph-phone"></i>064-654-2666</a></div></header>
  <main id="top" class="wrap">
    <section class="board">
      <div class="hero">
        <div>
          <img class="logo" src="img/nail-me-logo-160.png" alt="โลโก้ Nail Me" width="72" height="72">
          <h1 class="d">Nail Me<br><i>ร้านหรู แต่ราคาน่ารัก</i></h1>
          <p class="en">Nail salon · San Chao Market · Surat Thani</p>
          <p>ทาสีเจลเริ่มต้น 200 บาท สีให้เลือกกว่า 100 เฉด สปาเท้า 10 ขั้นตอน สปามือ ต่อเล็บ PVC สระไดร์ · ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน · เปิดทุกวัน 09:00–21:00 · ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน</p>
          <a class="tel" href="{TEL}" data-track="call">064-654-2666</a>
          <p style="font-size:14px;color:var(--mute);margin-top:10px">LINE <a href="{LINE}" target="_blank" rel="noopener" data-track="line" style="color:var(--deep);border-bottom:1px solid var(--sage)">jenny5667</a> · WhatsApp <a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp" style="color:var(--deep);border-bottom:1px solid var(--sage)">084-999-6109</a> · walk-in ได้</p>
        </div>
        <figure class="ph" style="margin:0"><img src="{P('french')}" alt="เล็บเฟรนช์ลายดอกไม้ ผลงาน Nail Me" fetchpriority="high" width="900" height="1200"><img src="{P('toes_daisy')}" alt="ทาสีเจลเท้าลายเดซี่" loading="eager" width="900" height="1200"><img src="{P('glitter')}" alt="เล็บกลิตเตอร์ทอง" loading="eager" width="900" height="1200"><figcaption>ผลงานจริงจากร้าน · ราคาตามป้ายด้านล่าง</figcaption></figure>
      </div>
    </section>

    <section id="menu" class="menus" style="padding-top:16px">{boxes}</section>
    <p style="font-size:13px;color:var(--mute);margin:12px 0 0;text-align:center">ราคาตามป้ายในร้าน ต.ค. 69 · เราจะดูแลคุณอย่างดี เพราะคุณคือคนพิเศษ ♡</p>

    <section id="promo" class="hang reveal"><h2 class="d">โปรเดือนนี้</h2><ul>{promo}</ul><a href="{FB1}" target="_blank" rel="noopener" data-track="facebook">แคปโพสต์ให้ช่าง ↗</a></section>

    <section id="feed" class="feed reveal"><span class="pill light">ลายที่ทำได้</span><div class="grid">{feed}</div><p style="font-size:13px;color:var(--mute);margin-top:12px">งานเพ้นท์ขึ้นกับจำนวนนิ้ว · <a href="{FB2}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--sage)">ผลงานล่าสุดบนเพจ ↗</a></p></section>

    <section id="spa" class="spa reveal">
      <img src="{P('toes_glitter')}" alt="สปาเท้า ผลงาน Nail Me" loading="lazy" decoding="async" width="900" height="1200">
      <div><span class="pill light">สปาเท้า 10 ขั้นตอน</span><h2 class="d" style="font-size:clamp(28px,4vw,40px);margin:12px 0 0">ขัดถึงใต้เข่า ผ่อนคลาย บำรุงล้ำลึก</h2><p class="big" style="margin:8px 0 0"><s>499</s>450 <span style="font-family:'Mitr';font-size:14px;color:var(--mute)">โปรเดือนนี้ · สปามือ 9 ขั้นตอน 399</span></p><ol>{steps}</ol></div>
    </section>

    <section id="review" class="rev reveal"><div>{LEAF}<blockquote class="d">“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”</blockquote><cite>ปฐมาวดี ชูมี · รีวิวบนเพจ Facebook 17 ก.ค. 69 · เล็บเจล · <a href="{FB1}" target="_blank" rel="noopener" data-track="facebook" style="border-bottom:1px solid var(--sage)">อ่านทั้งหมด ↗</a></cite></div><div class="stat"><b>100%</b>แนะนำ จาก 6 รีวิวบนเพจ<br>ผู้ติดตาม 1,000+<br>ดูแลให้หลังทำ ไม่ทิ้งงาน</div></section>

    <section id="visit" class="visit reveal">
      <div><span class="pill light">มาหาเรา</span><h2 class="d" style="font-size:clamp(26px,3.5vw,36px);margin:12px 0 0">ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน</h2><p>เยื้อง ๆ Tops ติดห้างทองก้องไพศาล · เปิดทุกวัน 09:00–21:00 · Thai &amp; international guests welcome</p>
        <div class="ch"><a href="{TEL}" data-track="call"><small>โทร</small>064-654-2666</a><a href="{LINE}" target="_blank" rel="noopener" data-track="line"><small>LINE</small>jenny5667</a><a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp"><small>WhatsApp</small>084-999-6109</a><a href="{MAPS}" target="_blank" rel="noopener" data-track="directions"><small>Google Maps</small>นำทาง ↗</a></div>
        <div style="margin-top:28px">{faq_html()}</div></div>
      <iframe src="{EMBED}" title="แผนที่ Nail Me ตลาดศาลเจ้า" loading="lazy"></iframe>
    </section>
    <footer>© 2026 Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี · <a href="{FB1}" target="_blank" rel="noopener" data-track="facebook">เพจหลัก</a> · <a href="{FB2}" target="_blank" rel="noopener" data-track="facebook">เพจสำรอง</a> · <a href="{MSG}" target="_blank" rel="noopener" data-track="message">ทักเพจ</a> · <a href="#" data-todo="หน้านโยบายความเป็นส่วนตัว">นโยบายความเป็นส่วนตัว</a></footer>
  </main>
  <div class="bar"><a class="a1" href="{TEL}" data-track="call"><i class="ph ph-phone"></i>โทรจองคิว</a><a class="a2" href="{LINE}" target="_blank" rel="noopener" data-track="line"><i class="ph ph-chat-circle-dots"></i>ทัก LINE</a></div>
{JS}</body>
</html>
'''
    fonts = 'https://fonts.googleapis.com/css2?family=Pridi:wght@400&family=Mitr:wght@300;400&display=swap'
    (ROOT / 'design3.html').write_text(head(TITLE, DESC, '#FBF7EE', fonts, css, 'web-dev/freelance/websites/nail-me/design3.html · แบบ 3 "ป้ายหน้าร้าน" ทำมือ จากป้ายราคาในร้าน (builder/handmade.py)') + body)

if __name__ == '__main__':
    build_magazine(); build_quiet(); build_board()
    print('built index.html (magazine), design2.html (quiet), design3.html (board)')
