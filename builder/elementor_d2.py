# web-dev/freelance/websites/nail-me/builder/elementor_d2.py
# สร้างเทมเพลต Elementor (widget ล้วน ไม่มี CSS/JS แยก) จากแบบ 2 "Private & Calm" (design2.html)
# ใช้: python builder/elementor_d2.py [th|en]  → elementor/nailme-home-<lang>.json
# รูปอยู่ใน Media Library ของ nailmesurat.com (id 6–25 อัป 11 ต.ค. 2569)
import json, random, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from showcase_data import CARDS, CATS

LANG = sys.argv[1] if len(sys.argv) > 1 else 'th'
EN = LANG == 'en'
T = lambda th, en: en if EN else th

# ---------- โทเคน (ตรงกับ design2.html) ----------
BLUSH='#F4EFE9'; CREAM='#FFFDFA'; ROSE='#E9DDD3'; PINK='#B98C7A'; PDEEP='#6B4A3E'; GOLD='#C9A24B'
GDEEP='#8F6D22'; GLIGHT='#E9D7A5'; INK='#2E2622'; MUTE='#6C5F58'; COCOA='#3A2A24'; LINE='#E2D8CF'
SERIF='Noto Serif Thai'      # หัวข้อภาษาไทย (มีตัวละตินในตัว)
NUM='Cormorant Garamond'     # ตัวเลขราคา / ชื่อร้าน
BODY='Noto Sans Thai'

U = 'https://nailmesurat.com/wp-content/uploads/2026/10/'
MEDIA = {'hero':6,'glitter':7,'french':8,'toes_daisy':9,'toes_brown':10,'toes_glitter':11,'chrome':12,'polka':13,
         'red':14,'red_long':15,'gold_white':16,'french_dots':17,'white_dots':18,'pink_gems':19,'pink_sparkle':20,
         'nude2':21,'long_clear':22,'lace':23}
def IMG(k): return {"url": U + 'nailme-' + k.replace('_','-') + '.webp', "id": MEDIA[k], "source": "library"}
LOGO = {"url": U + 'nailme-logo.png', "id": 24, "source": "library"}

TEL = 'tel:+66646542666'; LINE_URL = 'https://line.me/ti/p/~jenny5667'; WA = 'https://wa.me/66849996109'
MSG = 'https://m.me/nailmesuratthani'; FB1 = 'https://www.facebook.com/profile.php?id=61580350351076'
FB2 = 'https://www.facebook.com/nailmesuratthani'; PID = 'ChIJPZAmpMgHVDARfxVDRsiT0jc'
GPLACE = 'https://maps.google.com/?cid=4022439905576818047'
WRITE = 'https://search.google.com/local/writereview?placeid=' + PID
DIR = 'https://www.google.com/maps/dir/?api=1&destination=Nail+Me&destination_place_id=' + PID
HOME_OTHER = '/' if EN else '/en/'

random.seed(20261011 + (1 if EN else 0))
_ids = set()
def nid():
    while True:
        i = '%07x' % random.getrandbits(28)
        if i not in _ids: _ids.add(i); return i

def D(t, r=None, b=None, l=None, unit='px'):
    r = t if r is None else r; b = t if b is None else b; l = r if l is None else l
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": t == r == b == l}
def S(v, unit='px'): return {"unit": unit, "size": v, "sizes": []}
def GAP(c, r=None): r = c if r is None else r; return {"column": str(c), "row": str(r), "isLinked": c == r, "unit": "px", "size": c}
def L(url, ext=False): return {"url": url, "is_external": "on" if ext else "", "nofollow": "", "custom_attributes": ""}
def ext(url): return url.startswith('http')

def typo(fam, size, weight=400, lh=None, ls=None, tr=None, tab=None, mob=None, style=None, pre='typography'):
    d = {f"{pre}_typography": "custom", f"{pre}_font_family": fam, f"{pre}_font_weight": str(weight), f"{pre}_font_size": S(size)}
    if tab: d[f"{pre}_font_size_tablet"] = S(tab)
    if mob: d[f"{pre}_font_size_mobile"] = S(mob)
    if lh: d[f"{pre}_line_height"] = S(lh, 'em')
    if ls is not None: d[f"{pre}_letter_spacing"] = S(ls)
    if tr: d[f"{pre}_text_transform"] = tr
    if style: d[f"{pre}_font_style"] = style
    return d

def W(kind, s): return {"id": nid(), "elType": "widget", "widgetType": kind, "settings": s, "elements": []}
def C(s=None, kids=None, inner=True):
    base = {"content_width": "full", "flex_direction": "column", "padding": D(0), "flex_gap": GAP(0)}
    base.update(s or {})
    return {"id": nid(), "elType": "container", "settings": base, "elements": kids or [], "isInner": inner}

# ---------- ตัวช่วยข้อความ ----------
def H(text, tag='div', color=INK, size=16, weight=400, fam=BODY, lh=1.4, ls=None, tr=None, tab=None, mob=None,
      align='start', link=None, extra=None, style=None):
    s = {"title": text, "header_size": tag, "title_color": color, "align": align}
    s.update(typo(fam, size, weight, lh, ls, tr, tab, mob, style))
    if link: s["link"] = L(link, ext(link))
    if extra: s.update(extra)
    return W('heading', s)
def P(html, color=MUTE, size=17, mob=16, align='start', lh=1.75, extra=None):
    s = {"editor": html, "text_color": color, "align": align}
    s.update(typo(BODY, size, 400, lh, None, None, None, mob))
    if extra: s.update(extra)
    return W('text-editor', s)
def label(text, color=GDEEP, align='start'):
    return H(text, 'p', color, 13, 500, BODY, 1.4, 0.5 if not EN else 2, 'uppercase', align=align)
def h2(text, color=INK, align='start', big=False):
    return H(text, 'h2', color, 56 if big else 48, 600, SERIF, 1.3, None, None, 44 if big else 40, 36 if big else 32, align)
def h3(text, color=INK, size=22, mob=20, align='start'):
    return H(text, 'h3', color, size, 600, SERIF, 1.35, None, None, None, mob, align)
def price(text, color=PDEEP, size=28, mob=None, align='start'):
    return H(text, 'p', color, size, 600, NUM, 1, None, None, None, mob, align)

def btn(text, url, kind='pink', icon=None, lg=True, align='left', extra=None):
    s = {"text": text, "link": L(url, ext(url)), "align": align, "border_radius": D(999),
         "text_padding": D(18, 32) if lg else D(14, 24), "border_border": "solid", "border_width": D(1)}
    s.update(typo(BODY, 16 if lg else 15, 500, 1.2))
    pal = {
        'pink':   (PDEEP, CREAM, PDEEP, '#9E414E', CREAM, '#9E414E'),
        'gold':   ('rgba(0,0,0,0)', GDEEP, GDEEP, GDEEP, CREAM, GDEEP),
        'cream':  (CREAM, PDEEP, CREAM, GLIGHT, PDEEP, GLIGHT),
        'ondark': ('rgba(0,0,0,0)', GLIGHT, GLIGHT, GLIGHT, COCOA, GLIGHT),
    }[kind]
    s.update({"background_color": pal[0], "button_text_color": pal[1], "border_color": pal[2],
              "button_background_hover_color": pal[3], "hover_color": pal[4], "button_hover_border_color": pal[5]})
    if icon:
        s.update({"selected_icon": icon, "icon_align": "left", "icon_indent": S(8)})
    if extra: s.update(extra)
    return W('button', s)
I_PHONE = {"value": "fas fa-phone", "library": "fa-solid"}
I_LINE = {"value": "fab fa-line", "library": "fa-brands"}
I_WA = {"value": "fab fa-whatsapp", "library": "fa-brands"}
I_MSG = {"value": "fab fa-facebook-messenger", "library": "fa-brands"}
I_FB = {"value": "fab fa-facebook", "library": "fa-brands"}
I_NAV = {"value": "fas fa-location-arrow", "library": "fa-solid"}
I_STAR = {"value": "far fa-star", "library": "fa-regular"}
I_CHECK = {"value": "fas fa-check-circle", "library": "fa-solid"}
I_ARROW = {"value": "fas fa-arrow-right", "library": "fa-solid"}

def tlink(text, url, color=INK, size=15, align='start'):
    """ลิงก์ข้อความขีดเส้นใต้สีทอง"""
    return H(f'<span style="text-decoration:underline;text-decoration-color:{GOLD};text-underline-offset:4px">{text}</span> ↗' if ext(url) else
             f'<span style="text-decoration:underline;text-decoration-color:{GOLD};text-underline-offset:4px">{text}</span>',
             'div', color, size, 400, BODY, 1.5, align=align, link=url)

# ---------- โครง section ----------
def section(sid, bg, kids, pad=(96, 64, 56), border=None, extra=None, boxed=1200, gap=40, align=None):
    inner = C({"content_width": "boxed", "boxed_width": S(boxed), "width": S(100, '%'), "flex_gap": GAP(gap),
               "padding": D(0, 32), "padding_tablet": D(0, 24), "padding_mobile": D(0, 16),
               **({"flex_align_items": align} if align else {})}, kids)
    s = {"_element_id": sid, "html_tag": "section", "flex_align_items": "center", "background_background": "classic",
         "background_color": bg, "padding": D(pad[0], 0), "padding_tablet": D(pad[1], 0), "padding_mobile": D(pad[2], 0)}
    if border: s.update({"border_border": "solid", "border_width": border, "border_color": LINE})
    if extra: s.update(extra)
    return C(s, [inner], inner=False)

def cols(kids, widths, gap=64, tab_stack=True, align='flex-start', wrap=True, mob_order=None):
    """แถวหลายคอลัมน์ widths เป็น % (รวม gap แล้วต้อง ≤ 100)"""
    for k, w in zip(kids, widths):
        k['settings']['width'] = S(w, '%')
        k['settings']['width_tablet'] = S(100 if tab_stack else w, '%')
        k['settings']['width_mobile'] = S(100, '%')
    return C({"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_gap": GAP(gap, 40),
              "flex_gap_mobile": GAP(gap, 32), "flex_align_items": align, "flex_justify_content": "space-between",
              "width": S(100, '%')}, kids)

def image(k, h, h_mob=None, radius=8, alt_th=None):
    s = {"image": IMG(k), "image_size": "full", "width": S(100, '%'), "height": S(h), "object-fit": "cover",
         "image_border_radius": D(radius)}
    if h_mob: s["height_mobile"] = S(h_mob)
    return W('image', s)

# ======================= sections =======================
def header():
    logo = C({"flex_direction": "row", "flex_align_items": "center", "flex_gap": GAP(12), "width": S(240), "width_mobile": S(184),
              "html_tag": "a", "link": L('#top')},
             [W('image', {"image": LOGO, "image_size": "full", "width": S(44), "image_border_radius": D(999),
                          "_element_width": "initial", "_element_custom_width": S(44)}),
              C({"flex_gap": GAP(4), "width": S(150)}, [
                  H('Nail Me', 'p', PDEEP, 24, 600, NUM, 1, style='italic'),
                  H(T('ตลาดศาลเจ้า · Surat Thani', 'San Chao Market · Surat Thani'), 'p', GDEEP, 12, 400, BODY, 1.2, 1, mob=11)])])
    items = [(T('โปรโมชั่น','Promotion'),'#promo'),(T('บริการและราคา','Services & prices'),'#services'),(T('สปา','Spa'),'#spa'),
             (T('ผลงาน','Gallery'),'#gallery'),(T('รีวิว','Reviews'),'#reviews'),(T('คำถามที่พบบ่อย','FAQ'),'#faq'),(T('ที่ตั้งร้าน','Visit'),'#visit')]
    nav = W('icon-list', {"view": "inline", "icon_list": [{"text": t, "link": L(h), "selected_icon": {"value": "", "library": ""}, "_id": nid()} for t, h in items],
                          "space_between": S(28), "icon_align": "center", "text_color": INK, "text_color_hover": PDEEP,
                          **typo(BODY, 15, 400, 1.4, pre='icon_typography'),
                          "hide_tablet": "hidden-tablet", "hide_mobile": "hidden-mobile"})
    lang = H('EN' if not EN else 'TH', 'div', GDEEP, 13, 500, BODY, 1, 1.5, link=HOME_OTHER, align='center',
             extra={"_padding": D(8, 14), "_border_border": "solid", "_border_width": D(1), "_border_color": GOLD,
                    "_border_radius": D(999), "_element_width": "initial", "_background_background": "classic", "_background_color": CREAM})
    call = btn(T('โทรจองคิว','Call to book'), TEL, 'pink', I_PHONE, lg=False, extra={"hide_mobile": "hidden-mobile"})
    right = C({"flex_direction": "row", "flex_align_items": "center", "flex_gap": GAP(8), "width": S(240), "width_mobile": S(64),
               "flex_justify_content": "flex-end"}, [lang, call])
    row = C({"content_width": "boxed", "boxed_width": S(1200), "flex_direction": "row", "flex_wrap": "nowrap",
             "flex_justify_content": "space-between", "flex_align_items": "center", "width": S(100, '%'), "min_height": S(72),
             "min_height_mobile": S(64), "padding": D(8, 32), "padding_tablet": D(8, 24), "padding_mobile": D(8, 16)}, [logo, nav, right])
    return C({"html_tag": "header", "background_background": "classic", "background_color": BLUSH, "flex_align_items": "center",
              "border_border": "solid", "border_width": D(0, 0, 1, 0), "border_color": LINE}, [row], inner=False)

def hero():
    btns = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(16), "flex_justify_content": "center", "width": S(100, '%')},
             [btn(T('โทรจองคิว','Call to book'), TEL, 'cream', I_PHONE), btn(T('ทัก LINE','Message on LINE'), LINE_URL, 'ondark', I_LINE)])
    info = P(T('เปิดทุกวัน 09:00–21:00 · จองคิวหรือ walk-in · ', 'Open daily 09:00–21:00 · Booking or walk-in · ') +
             f'<a href="{TEL}" style="color:{GLIGHT};text-decoration:underline;text-underline-offset:4px">064-654-2666</a> · LINE '
             f'<a href="{LINE_URL}" target="_blank" rel="noopener" style="color:{GLIGHT};text-decoration:underline;text-underline-offset:4px">jenny5667</a>',
             'rgba(255,253,250,0.8)', 15, 14, 'center', 1.7)
    inner = C({"content_width": "boxed", "boxed_width": S(800), "width": S(100, '%'), "flex_align_items": "center", "flex_gap": GAP(24),
               "padding": D(96, 32), "padding_tablet": D(80, 24), "padding_mobile": D(64, 16)}, [
        label(T('ร้านทำเล็บ สุราษฎร์ธานี · ข้างตลาดศาลเจ้า', 'Nail salon in Surat Thani · next to San Chao Market'), GLIGHT, 'center'),
        H(T('ร้านหรู <span style="color:%s">แต่ราคาน่ารัก</span>' % GLIGHT, 'Luxury salon, <span style="color:%s">lovely prices</span>' % GLIGHT),
          'h1', CREAM, 80, 600, SERIF, 1.2, None, None, 64, 44, 'center'),
        P(T('Nail Me ร้านทำเล็บ สปาเท้า สปามือ และสระไดร์ ใจกลางเมืองสุราษฎร์ธานี ทาสีเจลเริ่มต้น 200 บาท สีเจลให้เลือกกว่า 100 เฉด ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน',
            'Nail Me is a nail salon, foot spa, hand spa and blow-dry bar in central Surat Thani. Gel polish from 200 THB, 100+ gel shades, and aftercare you can count on.'),
          'rgba(255,253,250,0.9)', 19, 17, 'center', 1.75, {"_element_width": "initial", "_element_custom_width": S(560), "_element_custom_width_mobile": S(100, '%')}),
        btns, info])
    s = {"_element_id": "top", "html_tag": "section", "min_height": S(640), "min_height_mobile": S(560), "flex_justify_content": "center",
         "flex_align_items": "center", "background_background": "classic", "background_image": IMG('hero'),
         "background_position": "center center", "background_size": "cover", "background_repeat": "no-repeat",
         "background_overlay_background": "gradient", "background_overlay_color": "rgba(46,38,34,0.25)", "background_overlay_color_stop": S(0, '%'),
         "background_overlay_color_b": "rgba(46,38,34,0.6)", "background_overlay_color_b_stop": S(100, '%'),
         "background_overlay_gradient_type": "linear", "background_overlay_gradient_angle": S(180, 'deg'), "background_overlay_opacity": S(1)}
    return C(s, [inner], inner=False)

def promo_card(k, bg, big, rows):
    s = {"min_height": S(320), "min_height_mobile": S(240), "flex_justify_content": "flex-end", "padding": D(32), "padding_mobile": D(24),
         "border_radius": D(8), "overflow": "hidden", "flex_gap": GAP(8), "background_background": "classic", "background_image": IMG(k),
         "background_position": "center center", "background_size": "cover", "background_overlay_background": "classic",
         "background_overlay_color": bg, "background_overlay_opacity": S(0.55)}
    return C(s, [price(big, CREAM, 72, 56)] + rows)

def promo():
    head = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_justify_content": "space-between", "flex_align_items": "flex-end",
              "flex_gap": GAP(16), "width": S(100, '%')}, [
        C({"flex_gap": GAP(8), "width": S(640), "width_mobile": S(100, '%')}, [label(T('โปรเดือนนี้', 'This month')),
            h2(T('แคปโพสต์โปร ให้ช่างก่อนรับบริการ', 'Show this promo to your technician'))]),
        tlink(T('ดูโพสต์โปรบนเพจ', 'See the promo post'), FB1)])
    c1 = promo_card('glitter', PDEEP, '฿200', [P(T('ทาสีเจล ตัดแต่งหนังฟรี <s>250</s>', 'Gel polish with free cuticle care <s>250</s>'), CREAM, 16, 15)])
    c2 = promo_card('toes_glitter', COCOA, '฿450', [P(T('สปาเท้า 10 ขั้นตอน <s>499</s>', '10-step foot spa <s>499</s>'), CREAM, 16, 15),
        P(T('<b style="font-family:Cormorant Garamond;font-size:22px">฿150</b> สระไดร์ ทุกความยาว', '<b style="font-family:Cormorant Garamond;font-size:22px">฿150</b> wash &amp; blow-dry, any length'),
          'rgba(255,253,250,0.85)', 15, 14)])
    return section('promo', BLUSH, [head, cols([c1, c2], [48.5, 48.5], 24, tab_stack=False)], pad=(80, 64, 56))

SVC = [('hero', 'ทาสีเจลมือ', 'Gel polish, hands', 'สีเจลคุณภาพดี ติดทน 1–3 เดือน เลือกได้กว่า 100 เฉด', 'Quality gel that lasts 1–3 months, 100+ shades', '฿250'),
       ('toes_brown', 'ทาสีเจลเท้า', 'Gel polish, feet', 'สีสวย เงางาม แห้งไว ไม่ทำลายหน้าเล็บ', 'Glossy colour, quick dry, gentle on nails', '฿300'),
       ('chrome', 'สีลูกแก้ว Cat Eye', 'Cat-eye gel', 'เจลแม่เหล็ก ประกายลึกเหมือนตาแมว', 'Magnetic gel with a deep cat-eye shimmer', '฿350'),
       ('long_clear', 'ต่อเล็บ PVC', 'PVC extensions', 'ต่อเล็บยาวสวยเป็นธรรมชาติ เจลเว้นโคน', 'Natural-looking long nails with gel', '฿350'),
       ('toes_glitter', 'สปาเท้า 10 ขั้นตอน', '10-step foot spa', 'ขัดถึงใต้เข่า แช่ ขัด มาร์ก นวด บำรุง', 'Soak, scrub, mask, massage — up to the knee', '฿499'),
       ('nude2', 'สปามือ 9 ขั้นตอน', '9-step hand spa', 'บำรุงล้ำลึก ผ่อนคลายสุดมือ', 'Deep nourishment and a relaxing massage', '฿399')]
PRICE_ROWS = [('เสริมหน้าเล็บหลังทาสี', 'Overlay after gel', '฿150'), ('เสริมหน้าเล็บก่อนทาสี', 'Overlay before gel', '฿450'),
              ('Manicure / Pedicure', 'Manicure / Pedicure', '฿200'),
              ('ถอดแล้วทำต่อที่ร้าน เจล 50 · PVC 100 · ถอดอย่างเดียว 100', 'Removal + redo: gel 50 · PVC 100 · removal only 100', 'เริ่ม ฿50|from ฿50'),
              ('งานเพ้นท์ คิดเพิ่มต่อนิ้ว · เพ้นท์ลาย +20 · เฟรนช์ปลาย +30 · ออมเบร +30 · ติดอะไหล่ +20 · ปั้นนูน +50',
               'Nail art, per nail · painted +20 · French tip +30 · ombré +30 · gems +20 · 3D +50', 'เริ่ม ฿20|from ฿20')]

def services():
    head = C({"flex_align_items": "center", "flex_gap": GAP(12), "width": S(100, '%')}, [
        label('Our services', GDEEP, 'center'), h2(T('บริการและราคา', 'Services & prices'), INK, 'center', big=True),
        P(T('ทาสีเจล ต่อเล็บ ดูแลเล็บมือ-เท้า และสปา ราคาปกติตามป้ายราคาในร้าน ช่วงโปรโมชั่นถูกกว่านี้ ดูที่โปรเดือนนี้',
            'Gel polish, extensions, hand and foot care, and spa. Regular prices as shown in the salon — promotions are even lower.'),
          MUTE, 17, 16, 'center', extra={"_element_width": "initial", "_element_custom_width": S(640), "_element_custom_width_mobile": S(100, '%')})])
    cards = []
    for k, th, en, dth, den, pr in SVC:
        body = C({"flex_gap": GAP(4), "padding": D(20), "flex_grow": 1}, [h3(T(th, en), INK, 22), P(T(dth, den), MUTE, 14, 14, lh=1.6),
                                                                      price(pr)])
        body['elements'][-1]['settings']['_margin'] = D(12, 0, 0, 0)
        cards.append(C({"background_background": "classic", "background_color": CREAM, "border_border": "solid", "border_width": D(1),
                        "border_color": LINE, "border_radius": D(8), "overflow": "hidden"}, [image(k, 240, 220, 0), body]))
    for c in cards:
        c['settings'].update({"width": S(31.5, '%'), "width_tablet": S(48.5, '%'), "width_mobile": S(100, '%')})
    grid = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(24), "flex_justify_content": "space-between",
              "flex_align_items": "stretch", "width": S(100, '%')}, cards)
    rows = []
    for i, (th, en, pr) in enumerate(PRICE_ROWS):
        last = i == len(PRICE_ROWS) - 1
        if '|' in pr: pr = pr.split('|')[1 if EN else 0]
        rows.append(C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_justify_content": "space-between", "flex_align_items": "baseline",
                       "flex_gap": GAP(16), "padding": D(12, 0), "border_border": "solid", "border_width": D(1, 0, 1 if last else 0, 0),
                       "border_color": LINE, "width": S(100 if last else 47, '%'), "width_mobile": S(100, '%')},
                      [P(T(th, en), INK, 15, 15, lh=1.6, extra={"_flex_size": "grow"}),
                       H(pr, 'p', PDEEP, 20, 600, NUM, 1, extra={"_element_width": "initial"})]))
    plist = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(48, 0), "flex_justify_content": "space-between",
               "content_width": "boxed", "boxed_width": S(960), "width": S(100, '%')}, rows)
    note = P(T('ราคาตามป้ายราคาในร้าน (ต.ค. 2569) · บริการผม ขนตา แว็กซ์ สอบถามทางโทรศัพท์หรือเพจ',
               'Prices as listed in the salon (Oct 2026) · Ask us about hair, lash and wax services.'), MUTE, 14, 14, 'center')
    cta = C({"flex_align_items": "center", "width": S(100, '%')}, [btn(T('โทรจองคิว', 'Call to book'), TEL, 'pink', I_PHONE, align='center')])
    return section('services', CREAM, [head, grid, plist, note, cta], border=D(1, 0, 1, 0), gap=40)

STEPS = [('แช่เกลือ ดีท็อกซ์ผิวเท้า', 'Salt soak to detox'), ('แช่น้ำนม', 'Milk soak'), ('ฟอก ขัด ล้างเท้า', 'Wash and scrub'), ('สครับเกลือ', 'Salt scrub'),
         ('มาร์กสครับ + แรป บำรุงล้ำลึก', 'Mask + wrap'), ('ตัดหนัง', 'Cuticle care'), ('ขัดส้นเท้า', 'Heel buffing'), ('บำรุงโลชั่น', 'Lotion'),
         ('นวดผ่อนคลาย', 'Relaxing massage'), ('ฉีดสเปรย์ให้ความชุ่มชื้น', 'Hydrating mist')]

def spa():
    left = C({"flex_gap": GAP(16)}, [
        h2(T('สปาเท้า 10 ขั้นตอน ขัดถึงใต้เข่า', '10-step foot spa, up to the knee')),
        P(T('ผ่อนคลาย บำรุงล้ำลึก เพื่อเท้าที่คุณรัก ใช้เวลาเต็มขั้นตอน ไม่รีบ เหมาะกับหลังเลิกงานหรือหลังเดินเที่ยวทั้งวัน',
            'Relax and nourish your feet. We take our time with every step — perfect after work or a long day of sightseeing.')),
        H(f'<span style="font-family:{NUM};font-size:48px;font-weight:600;color:{PDEEP}">฿499</span> ' + T('· โปรเดือนนี้ 450', '· this month 450'),
          'p', MUTE, 14, 400, BODY, 1.2, extra={"_margin": D(8, 0, 16, 0)}),
        image('toes_daisy', 520, 400)])
    items = []
    for i, (th, en) in enumerate(STEPS, 1):
        items.append(C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_gap": GAP(12), "flex_align_items": "baseline",
                        "padding": D(12, 0), "border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": LINE,
                        "width": S(47, '%'), "width_mobile": S(100, '%')},
                       [H(str(i), 'span', GOLD, 24, 600, NUM, 1, extra={"_element_width": "initial", "_element_custom_width": S(32)}),
                        P(T(th, en), INK, 16, 15, lh=1.6, extra={"_flex_size": "grow"})]))
    steps = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(32, 0), "flex_justify_content": "space-between", "width": S(100, '%')}, items)
    sub = cols([C({"flex_gap": GAP(8)}, [h3(T('สปามือ 9 ขั้นตอน', '9-step hand spa') + f' <span style="font-family:{NUM};color:{PDEEP}">฿399</span>', INK, 24),
                    P(T('แช่เกลือ แช่น้ำนม ฟอกขัดล้าง สครับ มาร์ก+แรป ตัดหนัง ทาโลชั่น นวด และบำรุงจมูกเล็บด้วยออยล์',
                        'Salt and milk soak, scrub, mask and wrap, cuticle care, lotion, massage and cuticle oil.'), MUTE, 15, 15)]),
                C({"flex_gap": GAP(8)}, [h3(T('ทาสีเจลเท้า', 'Gel pedicure') + f' <span style="font-family:{NUM};color:{PDEEP}">฿300</span>', INK, 24),
                    P(T('สีสวย เงางาม ติดทน 1–3 เดือน แห้งไวพร้อมใส่รองเท้าทันที ไม่ทำลายหน้าเล็บ',
                        'Glossy colour that lasts 1–3 months, dries fast so you can wear shoes right away.'), MUTE, 15, 15)])],
               [47, 47], 32, tab_stack=False)
    right = C({"flex_gap": GAP(40)}, [steps, sub, btn(T('โทรจองสปา', 'Call to book a spa'), TEL, 'pink', I_PHONE)])
    return section('spa', BLUSH, [cols([left, right], [40, 55], 64)], border=D(1, 0, 0, 0))

WHY = [('ดูแลให้หลังทำ ไม่ทิ้งงาน', 'Aftercare included', 'ทำแล้วมีปัญหา กลับมาให้ช่างดูได้ ร้านดูแลต่อให้', 'Any issue after your visit? Come back and we will fix it.'),
       ('สีเจลกว่า 100 เฉด', '100+ gel shades', 'สายหวาน มินิมอล แฟชั่น สีลูกแก้ว ช่างช่วยเลือกสีให้เข้ากับคุณ', 'Sweet, minimal, trendy or cat-eye — we help you pick.'),
       ('ราคาชัดตามป้าย ไม่มีบวกเพิ่ม', 'Clear prices, no surprises', 'ราคาทุกบริการติดไว้หน้าร้าน งานเพ้นท์คิดเพิ่มต่อนิ้วตามป้าย', 'All prices are posted in the salon. Nail art is priced per nail.'),
       ('ใจกลางเมือง มาง่าย', 'Central and easy to find', 'ข้างตลาดศาลเจ้า ตรงข้ามรถไฟฟ้าบ้านดอน เยื้อง Tops', 'Next to San Chao Market, near Tops.'),
       ('ยินดีต้อนรับนักท่องเที่ยว', 'Travellers welcome', 'We welcome both Thai customers and international travellers.', 'We welcome both Thai customers and international travellers.')]

def why():
    items = []
    for i, (th, en, dth, den) in enumerate(WHY):
        last = i == len(WHY) - 1
        items.append(C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_gap": GAP(12), "padding": D(12, 0), "border_border": "solid",
                        "border_width": D(1, 0, 1 if last else 0, 0), "border_color": LINE, "width": S(100, '%')},
                       [W('icon', {"selected_icon": I_CHECK, "primary_color": PDEEP, "size": S(20), "_margin": D(4, 0, 0, 0),
                                   "_element_width": "initial"}),
                        C({"flex_gap": GAP(2), "flex_grow": 1}, [H(T(th, en), 'p', INK, 17, 500, BODY, 1.5), P(T(dth, den), MUTE, 14, 14, lh=1.6)])]))
    right = C({"flex_gap": GAP(16)}, [h2(T('เราจะดูแลคุณอย่างดี เพราะคุณคือคนพิเศษ', 'We take good care of you, because you are special')),
        P(T('คำสัญญาที่เขียนไว้ท้ายป้ายราคาของร้าน และเป็นเหตุผลที่ลูกค้ากลับมา', 'The promise written on our price board — and why guests keep coming back.')),
        C({"padding": D(16, 0, 16, 0)}, items), btn(T('โทรจองคิว', 'Call to book'), TEL, 'pink', I_PHONE)])
    left = C({}, [image('french', 560, 400)])
    row = cols([left, right], [40, 55], 64, align='center')
    row['settings']['flex_direction_tablet'] = 'column-reverse'
    return section('why', BLUSH, [row])

def gallery():
    head = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_justify_content": "space-between", "flex_align_items": "flex-end",
              "flex_gap": GAP(16), "width": S(100, '%')}, [
        C({"flex_gap": GAP(12), "width": S(640), "width_mobile": S(100, '%')}, [h2(T('ผลงานจากร้าน', 'Our work')),
            P(T('ลายที่ทำได้จริงจากร้าน พร้อมราคาตามป้าย เลือกลายแล้วโทรจองได้เลย หรือส่งรูปลายที่ชอบมาทาง LINE',
                'Real designs from our salon with listed prices. Pick one and call to book, or send us a photo on LINE.'))]),
        tlink(T('ดูผลงานล่าสุดบนเพจ', 'See our latest work'), FB2)])
    blocks = [head]
    for cat, _, cth, cen in CATS:
        cards = []
        for c in [x for x in CARDS if x[0] == cat]:
            _, k, alt, key, tth, dth, pr, promo, ten, den = c
            tag = (f'฿{promo} <s style="font-family:{BODY};font-size:11px;font-weight:400;color:{MUTE}">฿{pr}</s>' if promo else f'฿{pr}')
            pic = C({"overflow": "hidden", "border_radius": D(8)}, [
                image(k, 340, 220, 0),
                H(tag, 'span', PDEEP, 18, 600, NUM, 1, extra={"_position": "absolute", "_offset_orientation_h": "start", "_offset_x": S(12),
                    "_offset_orientation_v": "start", "_offset_y": S(12), "_background_background": "classic", "_background_color": CREAM,
                    "_padding": D(8, 12), "_border_radius": D(4), "_z_index": 2, "_element_width": "initial"})])
            cards.append(C({"flex_gap": GAP(4), "html_tag": "a", "link": L(TEL), "width": S(31.5, '%'), "width_tablet": S(48, '%'),
                            "width_mobile": S(48, '%')},
                           [pic, H(T(tth, ten), 'h3', INK, 16, 500, BODY, 1.4, mob=15, extra={"_margin": D(8, 0, 0, 0)}),
                            P(T(dth, den), MUTE, 13, 13, lh=1.5)]))
        grid = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(24, 32), "flex_gap_mobile": GAP(12, 24),
                  "flex_justify_content": "space-between", "width": S(100, '%')}, cards)
        blocks.append(C({"flex_gap": GAP(20), "width": S(100, '%')}, [
            H(T(cth.split(' · Nail')[0].split(' · Ext')[0], cen.replace('&amp;', '&')), 'h3', INK, 24, 600, SERIF, 1.35, mob=20,
              extra={"_padding": D(0, 0, 12, 0), "_border_border": "solid", "_border_width": D(0, 0, 1, 0), "_border_color": LINE}), grid]))
    blocks.append(P(T('ราคาในการ์ดคือราคาตามป้ายราคาในร้าน ราคางานเพ้นท์/ตกแต่งขึ้นกับจำนวนนิ้วและลาย สอบถามช่างก่อนทำได้',
                      'Card prices follow the salon price board. Nail-art prices depend on design and number of nails — just ask.'), MUTE, 14, 14))
    return section('gallery', BLUSH, blocks, gap=48)

def reviews():
    stat = lambda n, t: C({"flex_align_items": "center", "flex_gap": GAP(4), "width": S(47, '%')},
                          [price(n, PDEEP, 32, align='center'), P(t, MUTE, 14, 14, 'center')])
    stats = C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_justify_content": "space-between", "content_width": "boxed",
               "boxed_width": S(400), "width": S(100, '%')}, [stat('1,000+', T('ผู้ติดตามเพจหลัก', 'followers on our main page')),
                                                          stat('100+', T('เฉดสีเจลให้เลือก', 'gel shades to choose from'))])
    kids = [H(T('รีวิวจากลูกค้า', 'Guest reviews'), 'h2', GDEEP, 13, 500, BODY, 1.4, 0.5, 'uppercase', align='center'),
            price('100%', PDEEP, 96, 72, 'center'),
            P(T('แนะนำ จาก 6 รีวิวบนเพจ', 'recommended, from 6 reviews on our page'), MUTE, 17, 16, 'center'),
            H(T('“ทำเล็บเท้าสวยค่ะ ชอบมาก สวยมากค้า”', '“Beautiful pedicure — I love it, so pretty!”'), 'blockquote', INK, 36, 500, SERIF, 1.45,
              None, None, 30, 24, 'center', extra={"_margin": D(24, 0, 0, 0)}),
            P(T('ปฐมาวดี ชูมี · รีวิวบนเพจ Facebook 17 ก.ค. 2569 · เล็บเจล', 'Pathamawadee C. · Facebook review, 17 Jul 2026 · gel nails'), MUTE, 15, 14, 'center'),
            stats,
            C({"flex_align_items": "center", "flex_gap": GAP(12), "width": S(100, '%')},
              [tlink(T('อ่านรีวิวทั้งหมดบนเพจ', 'Read all reviews on our page'), FB1, align='center'),
               tlink(T('ดูรีวิวบน Google · 4.5 ★ (28)', 'See reviews on Google · 4.5 ★ (28)'), GPLACE, align='center')])]
    return section('reviews', BLUSH, kids, boxed=800, gap=16, align='center')

BK = [('โทรหรือทักเพจ', 'Call or message us', 'บอกบริการที่อยากทำและเวลาที่สะดวก ร้านตอบกลับเร็ว', 'Tell us the service and time you prefer — we reply quickly.'),
      ('เลือกสีและลายหน้าร้าน', 'Choose colours in the salon', 'มีสีเจลกว่า 100 เฉดให้ลอง ช่างช่วยแนะนำ ส่งรูปลายที่ชอบมาก่อนได้', 'Try 100+ gel shades with our help, or send a design photo first.'),
      ('มาถึงร้าน ใช้โปรได้เลย', 'Arrive and enjoy the promo', 'แคปโพสต์โปรให้ช่างดูก่อนรับบริการ walk-in ก็ได้ถ้าคิวว่าง', 'Show the promo post before your service. Walk-ins welcome when free.')]

def booking():
    steps = []
    for i, (th, en, dth, den) in enumerate(BK, 1):
        steps.append(C({"flex_gap": GAP(8), "padding": D(16, 0, 0, 0), "border_border": "solid", "border_width": D(1, 0, 0, 0),
                        "border_color": "rgba(255,253,250,0.3)"},
                       [price(str(i), GLIGHT, 40), h3(T(th, en), CREAM, 24, 22), P(T(dth, den), 'rgba(255,253,250,0.8)', 15, 15)]))
    btns = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(16), "flex_justify_content": "center", "width": S(100, '%')},
             [btn(T('โทรจองคิว', 'Call to book'), TEL, 'cream', I_PHONE), btn(T('ทัก LINE', 'Message on LINE'), LINE_URL, 'ondark', I_LINE)])
    head = C({"flex_align_items": "center", "flex_gap": GAP(8), "width": S(100, '%')},
             [label('Please make a reservation', GLIGHT, 'center'), h2(T('จองคิวง่าย ๆ 3 ขั้นตอน', 'Book in 3 easy steps'), CREAM, 'center')])
    return section('booking', PDEEP, [head, cols(steps, [31, 31, 31], 32), btns], pad=(80, 64, 56))

FAQ = [('ต้องจองคิวล่วงหน้าไหม', 'Do I need to book in advance?',
        'จองล่วงหน้าทางโทรศัพท์ 064-654-2666, LINE jenny5667 หรือทักเพจได้ หรือ walk-in มาที่ร้านได้เลย เปิดทุกวัน 09:00–21:00',
        'You can book by phone (064-654-2666), LINE (jenny5667) or Facebook, or simply walk in. Open daily 09:00–21:00.'),
       ('ทาสีเจลราคาเท่าไหร่', 'How much is gel polish?',
        'ราคาปกติ ทาสีเจลมือ 250 เท้า 300 สีลูกแก้ว 350 บาท ช่วงโปรโมชั่นเริ่มต้น 200 บาท ตัดแต่งหนังฟรี (แคปโพสต์โปรให้ช่างก่อนรับบริการ)',
        'Regular prices: hands 250, feet 300, cat-eye 350 THB. During promotions from 200 THB with free cuticle care.'),
       ('สปาเท้ามีขั้นตอนอะไรบ้าง ใช้เวลานานไหม', 'What is included in the foot spa?',
        'สปาเท้า 10 ขั้นตอน 499 บาท ขัดถึงใต้เข่า ตั้งแต่แช่เกลือ แช่น้ำนม ขัด สครับ มาร์ก+แรป ตัดหนัง ขัดส้นเท้า บำรุง นวด จนถึงสเปรย์ให้ความชุ่มชื้น ทำเต็มทุกขั้นตอน ไม่รีบ',
        'Our 10-step foot spa (499 THB) covers up to the knee: salt and milk soak, scrub, mask and wrap, cuticle care, heel buffing, lotion, massage and hydrating mist.'),
       ('ถอดสีเจลที่ทำจากร้านอื่นได้ไหม', 'Can you remove gel done elsewhere?',
        'ได้ ถอดสีเจลอย่างเดียว 100 บาท ถอดแล้วทำต่อที่ร้าน 50 บาท ถอด PVC แล้วทำต่อ 100 บาท',
        'Yes. Removal only 100 THB, removal with a new set 50 THB, PVC removal with a new set 100 THB.'),
       ('เพ้นท์ลายคิดราคายังไง', 'How is nail art priced?',
        'คิดเพิ่มต่อนิ้วจากราคาทาสีเจล เพ้นท์ลาย +20 เฟรนช์ปลาย +30 ออมเบร +30 ติดอะไหล่เล็ก +20 ปั้นนูน +50 บาทต่อนิ้ว ช่วงโปรทาสีเจล+เพ้นท์กี่นิ้วก็ได้ 350 บาท',
        'Per nail on top of gel: painted +20, French tip +30, ombré +30, small gems +20, 3D +50 THB. Promo: gel + art on any number of nails 350 THB.'),
       ('Do you welcome international travellers?', 'Do you welcome international travellers?',
        'Yes. We welcome both Thai customers and international travellers. We are next to San Chao Market in central Surat Thani, open daily 09:00–21:00. WhatsApp +66 84 999 6109, call +66 64 654 2666 or message our Facebook page.',
        'Yes. We are next to San Chao Market in central Surat Thani, open daily 09:00–21:00. WhatsApp +66 84 999 6109, call +66 64 654 2666 or message our Facebook page.')]

def faq():
    acc = W('accordion', {"tabs": [{"tab_title": T(q, qe), "tab_content": f'<p>{T(a, ae)}</p>', "_id": nid()} for q, qe, a, ae in FAQ],
        "selected_icon": {"value": "fas fa-plus", "library": "fa-solid"}, "selected_active_icon": {"value": "fas fa-minus", "library": "fa-solid"},
        "icon_align": "right", "title_html_tag": "h3", "border_width": S(0), "border_color": LINE,
        "title_background": "rgba(0,0,0,0)", "title_color": INK, "tab_active_color": PDEEP, "icon_color": GDEEP, "icon_active_color": PDEEP,
        "content_background_color": "rgba(0,0,0,0)", "content_color": MUTE, "title_padding": D(16, 0), "content_padding": D(0, 0, 16, 0),
        **typo(BODY, 17, 500, 1.5, pre='title_typography'), **typo(BODY, 16, 400, 1.75, pre='content_typography')})
    acc['settings'].update({"_border_border": "solid", "_border_width": D(1, 0, 1, 0), "_border_color": LINE})
    left = C({"flex_gap": GAP(16)}, [h2(T('คำถามที่พบบ่อย', 'FAQ')), P(T('ไม่เจอคำตอบ โทรหรือทักเพจได้เลย', 'Can’t find your answer? Call or message us.'))])
    return section('faq', BLUSH, [cols([left, C({}, [acc])], [30, 64], 64)])

CONTACT = [(I_PHONE, T('โทร', 'Call'), '064-654-2666', TEL), (I_LINE, 'LINE', 'jenny5667', LINE_URL),
           (I_WA, 'WhatsApp', '084-999-6109', WA), (I_MSG, 'Facebook', T('ทักเพจ', 'Message'), MSG)]

def visit():
    marks = []
    for i, (th, en) in enumerate([('ตรงข้ามรถไฟฟ้าบ้านดอน', 'Opposite the Ban Don electric train stop'), ('เยื้อง ๆ Tops', 'Across from Tops'),
                                  ('ติดกับห้างทองก้องไพศาล', 'Beside Kong Paisan gold shop')], 1):
        marks.append(C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_gap": GAP(16), "flex_align_items": "baseline", "padding": D(12, 0),
                        "border_border": "solid", "border_width": D(0, 0, 1, 0), "border_color": LINE},
                       [H(str(i), 'span', GOLD, 22, 600, NUM, 1, extra={"_element_width": "initial", "_element_custom_width": S(24)}),
                        P(T(th, en), INK, 16, 15, lh=1.6, extra={"_flex_size": "grow"})]))
    tiles = []
    for ic, lab, val, url in CONTACT:
        tiles.append(C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_align_items": "center", "flex_gap": GAP(12), "html_tag": "a",
                        "link": L(url, ext(url)), "min_height": S(56), "padding": D(8, 16), "border_border": "solid", "border_width": D(1),
                        "border_color": LINE, "border_radius": D(8), "background_background": "classic", "background_color": CREAM,
                        "border_hover_border": "solid", "border_hover_color": PDEEP, "width": S(48, '%')},
                       [W('icon', {"selected_icon": ic, "primary_color": PDEEP, "size": S(20), "_element_width": "initial"}),
                        C({"flex_gap": GAP(0)}, [H(lab, 'span', MUTE, 12, 400, BODY, 1.4), H(val, 'span', INK, 15, 500, BODY, 1.4)])]))
    tgrid = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(12), "flex_justify_content": "space-between", "width": S(100, '%')}, tiles)
    info = cols([C({"flex_gap": GAP(4)}, [label(T('เวลาเปิด', 'Hours')), P(T('ทุกวัน 09:00–21:00', 'Daily 09:00–21:00'), INK, 16, 15)]),
                 C({"flex_gap": GAP(4)}, [label(T('โทร', 'Phone')), tlink('064-654-2666', TEL, INK, 16)])], [47, 47], 24, tab_stack=False)
    for k in info['elements']: k['settings']['width_mobile'] = S(47, '%')
    btns = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(16)},
             [btn(T('โทรจองคิว', 'Call to book'), TEL, 'pink', I_PHONE), btn(T('นำทาง', 'Directions'), DIR, 'gold', I_NAV)])
    left = C({"flex_gap": GAP(16)}, [
        h2(T('แวะมาที่ร้าน ตลาดศาลเจ้า สุราษฎร์ธานี', 'Visit us at San Chao Market, Surat Thani')),
        P(T('ข้างตลาดศาลเจ้า ใจกลางเมืองสุราษฎร์ธานี มาเที่ยวแวะได้เลย ยินดีต้อนรับทั้งลูกค้าไทยและนักท่องเที่ยว',
            'Next to San Chao Market in the heart of Surat Thani. Thai customers and international travellers are all welcome.')),
        C({"flex_gap": GAP(0), "padding": D(16, 0, 0, 0)}, [label(T('จุดสังเกต', 'How to find us')),
            C({"border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": GOLD, "_margin": D(8, 0, 0, 0)}, marks)]),
        info, label(T('ช่องทางติดต่อ', 'Contact')), tgrid, btns,
        H(f'<span style="text-decoration:underline;text-decoration-color:{GOLD};text-underline-offset:4px">' +
          T('★ เคยมาแล้ว? รีวิวให้เราบน Google', '★ Been here? Leave us a Google review') + '</span>', 'div', MUTE, 14, 400, BODY, 1.5, link=WRITE)])
    gmap = W('google_maps', {"address": "Nail Me ตลาดศาลเจ้า สุราษฎร์", "zoom": S(17), "height": S(440), "height_mobile": S(320),
                             "_border_border": "solid", "_border_width": D(1), "_border_color": LINE, "_border_radius": D(8)})
    right = C({"flex_gap": GAP(12)}, [gmap,
        P(T('285/6 ถ.หน้าเมือง ต.ตลาด อ.เมือง สุราษฎร์ธานี 84000', '285/6 Na Mueang Rd, Talat, Mueang Surat Thani 84000'), MUTE, 13, 13),
        C({"flex_gap": GAP(12), "padding": D(32, 0, 0, 0), "border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": LINE,
           "_margin": D(24, 0, 0, 0)}, [
            h3(T('เกี่ยวกับ Nail Me ร้านทำเล็บ สุราษฎร์ธานี', 'About Nail Me, nail salon in Surat Thani'), INK, 24),
            P(T('Nail Me เป็นร้านทำเล็บในสุราษฎร์ธานี ตั้งอยู่ข้างตลาดศาลเจ้า ใจกลางเมือง ให้บริการทำเล็บเจล ต่อเล็บ PVC เพ้นท์เล็บ สปาเท้า 10 ขั้นตอน สปามือ 9 ขั้นตอน รวมถึงสระไดร์ ใครหาร้านทำเล็บสุราษฎร์ที่ราคาชัด เดินทางง่าย แวะมาได้เลย ในคอนเซปต์ “ร้านหรู แต่ราคาน่ารัก” ราคาติดชัดตามป้ายหน้าร้าน ทำแล้วดูแลให้หลังทำ ไม่ทิ้งงาน',
                'Nail Me is a nail salon next to San Chao Market in central Surat Thani, offering gel polish, PVC nail extensions, nail art, a 10-step foot spa, a 9-step hand spa and blow-dry. Our idea is simple: a luxury salon with lovely prices — clear prices on the board and aftercare you can count on.'), MUTE, 15, 15),
            P('Nail Me is a nail salon next to San Chao Market in central Surat Thani, offering gel polish, PVC nail extensions, nail art, a 10-step foot spa and a 9-step hand spa. Open daily 09:00–21:00. Thai customers and international travellers are all welcome.', MUTE, 15, 15) if not EN else
            P('Open daily 09:00–21:00 · 285/6 Na Mueang Rd, Surat Thani 84000.', MUTE, 15, 15)])])
    return section('visit', CREAM, [cols([left, right], [40, 55], 64)], border=D(1, 0, 0, 0))

def footer():
    brand = C({"flex_gap": GAP(24)}, [
        C({"flex_direction": "row", "flex_align_items": "center", "flex_gap": GAP(16)}, [
            W('image', {"image": LOGO, "image_size": "full", "width": S(56), "image_border_radius": D(999), "_element_width": "initial", "_element_custom_width": S(56)}),
            C({"flex_gap": GAP(4), "width": S(220)}, [H('Nail Me', 'p', GLIGHT, 28, 600, NUM, 1, style='italic'),
                                                     H('ตลาดศาลเจ้า · Surat Thani', 'p', 'rgba(233,215,165,0.8)', 12, 400, BODY, 1.3, 1)])]),
        P(T('เปลี่ยนเล็บสวยให้โดดเด่นในทุกวัน ยินดีต้อนรับทั้งลูกค้าไทยและนักท่องเที่ยว', 'Beautiful nails for every day. Thai customers and international travellers welcome.'),
          'rgba(255,253,250,0.8)', 15, 15)])
    contact = C({"flex_gap": GAP(8)}, [label(T('ติดต่อ', 'Contact'), GLIGHT),
        P(T('285/6 ถ.หน้าเมือง ข้างตลาดศาลเจ้า อ.เมือง สุราษฎร์ธานี 84000', '285/6 Na Mueang Rd, next to San Chao Market, Mueang Surat Thani 84000'), CREAM, 15, 15),
        P(T('เปิดทุกวัน 09:00–21:00', 'Open daily 09:00–21:00'), CREAM, 15, 15),
        H('064-654-2666', 'p', CREAM, 15, 400, BODY, 1.6, link=TEL)])
    follow_items = [(I_FB, T('เพจหลัก (สุราษฎร์)', 'Main page (Surat)'), FB1), (I_FB, T('เพจสำรอง (สุราษฎร์ธานี)', 'Second page (Surat Thani)'), FB2),
                    (I_LINE, 'LINE: jenny5667', LINE_URL), (I_WA, 'WhatsApp: 084-999-6109', WA), (I_MSG, T('ทักเพจ Facebook', 'Facebook Messenger'), MSG)]
    flist = W('icon-list', {"icon_list": [{"text": t, "link": L(u, True), "selected_icon": ic, "_id": nid()} for ic, t, u in follow_items],
                            "space_between": S(12), "icon_color": GLIGHT, "icon_size": S(18), "text_color": CREAM, "text_color_hover": GLIGHT,
                            "text_indent": S(8), **typo(BODY, 15, 400, 1.5, pre='icon_typography')})
    follow = C({"flex_gap": GAP(16)}, [label(T('ติดตาม', 'Follow'), GLIGHT), flist])
    top = cols([brand, contact, follow], [38, 30, 24], 48, align='flex-start')
    for k in top['elements']: k['settings']['width_tablet'] = S(100, '%')
    bottom = C({"flex_direction": "row", "flex_wrap": "wrap", "flex_justify_content": "space-between", "flex_gap": GAP(16), "padding": D(24, 0, 0, 0),
                "border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": "rgba(255,253,250,0.15)", "width": S(100, '%')},
               [P('© 2026 Nail Me ตลาดศาลเจ้า สุราษฎร์ธานี', 'rgba(255,253,250,0.7)', 13, 13),
                H(T('นโยบายความเป็นส่วนตัว', 'Privacy policy'), 'div', 'rgba(255,253,250,0.7)', 13, 400, BODY, 1.6,
                  link=T('/privacy-policy/', '/privacy-policy/'))])
    return section('footer', COCOA, [top, bottom], pad=(56, 48, 48), gap=48, extra={"html_tag": "footer"})

def build():
    content = [header(), hero(), promo(), services(), spa(), why(), gallery(), reviews(), booking(), faq(), visit(), footer()]
    return {"version": "0.4", "title": T('Nail Me หน้าแรก (TH) · แบบ 2 native', 'Nail Me Home (EN) · design 2 native'), "type": "page",
            "content": content,
            "page_settings": {"hide_title": "yes", "template": "elementor_canvas", "background_background": "classic", "background_color": BLUSH}}

if __name__ == '__main__':
    out = pathlib.Path(__file__).resolve().parent.parent / 'elementor'
    out.mkdir(exist_ok=True)
    d = build()
    p = out / f'nailme-home-{LANG}.json'
    p.write_text(json.dumps(d, ensure_ascii=False))
    def count(e): return 1 + sum(count(x) for x in e.get('elements', []))
    print(p, len(p.read_text()) // 1024, 'KB', sum(count(e) for e in d['content']), 'elements')
