# web-dev/freelance/websites/nail-me/builder/showcase_data.py
# ข้อมูลการ์ดผลงาน+ราคา (แหล่งเดียว ใช้ทั้ง 4 แบบ) · รูป = รหัสไฟล์ในโฟลเดอร์ Drive ที่ร้านแชร์ (img/photos.json)
# ราคา = ตามป้ายราคาในร้าน · promo = ราคาโปร ก.ย. 69 (ถ้ามี) · ชื่อลาย/ราคาต่อใบเป็นการจับคู่โดยเรา ต้องให้ร้านตรวจ
import json, pathlib
PH = json.load(open(pathlib.Path(__file__).resolve().parent.parent / 'img' / 'photos.json'))
P = lambda k: f'https://lh3.googleusercontent.com/d/{PH[k]}=w1200'

# (id, label_key, label_th, label_en)
CATS = [
    ('color', 'show.c1', 'ทาสีเจล · Nail color', 'Nail colour'),
    ('art', 'show.c2', 'เพ้นท์ · ติดอะไหล่ · Nail art', 'Nail art &amp; decorations'),
    ('ext', 'show.c3', 'ต่อเล็บ · สปา · Extensions &amp; spa', 'Extensions &amp; spa'),
]

# (cat, photo_key, alt, key, title_th, desc_th, price, promo, title_en, desc_en)
CARDS = [
    ('color', 'hero', 'ทาสีเจลมือสีนู้ด ผลงาน Nail Me', 'sc1', 'ทาสีเจลมือ สีพื้น', 'ตัดแต่งหนัง + ทาสีเจล 1 สี เลือกได้กว่า 100 เฉด', 250, 200, 'Gel polish, hands', 'Cuticle care + one-colour gel, 100+ shades'),
    ('color', 'nude2', 'ทาสีเจลมือสีนู้ดเงา ผลงาน Nail Me', 'sc2', 'ทาสีเจลมือ โทนนู้ด', 'สีเรียบ เงางาม ติดทน 1–3 เดือน', 250, 200, 'Nude gel, hands', 'Clean glossy finish, lasts 1–3 months'),
    ('color', 'red', 'ทาสีเจลสีแดงเงา ผลงาน Nail Me', 'sc3', 'ทาสีเจลมือ สีเข้ม', 'แดง น้ำตาล เบอร์กันดี สีฤดูกาล', 250, 200, 'Deep-colour gel, hands', 'Red, brown, burgundy, seasonal shades'),
    ('color', 'toes_brown', 'ทาสีเจลเท้าสีน้ำตาล ผลงาน Nail Me', 'sc4', 'ทาสีเจลเท้า', 'ตัดแต่งหนัง + ทาสีเจลเท้า แห้งไว ใส่รองเท้าได้เลย', 300, None, 'Gel polish, feet', 'Cuticle care + gel pedicure, quick dry'),
    ('color', 'glitter', 'เล็บเจลกลิตเตอร์ทอง ผลงาน Nail Me', 'sc5', 'กลิตเตอร์ · สีลูกแก้ว', 'สีประกาย กลิตเตอร์ หรือ Cat Eye เจลแม่เหล็ก', 350, None, 'Glitter · cat eye', 'Sparkle, glitter or magnetic cat-eye gel'),
    ('color', 'chrome', 'เล็บเจลปลายโครมเงิน ผลงาน Nail Me', 'sc6', 'ปลายโครม', 'ทาสีเจล + ผงโครมที่ปลายเล็บ คิดเพิ่มต่อนิ้วตามป้าย', 250, None, 'Chrome tips', 'Gel + chrome powder on the tips, priced per nail'),
    ('art', 'polka', 'เล็บเจลลายจุดโบว์ ผลงาน Nail Me', 'sa1', 'เพ้นท์ลายจุด โบว์', 'โปร ทาสีเจล + เพ้นท์กี่นิ้วก็ได้ 350 (ปกติ 250 + 20/นิ้ว)', 450, 350, 'Dots &amp; bows', 'Promo: gel + art on any number of nails 350 (regular 250 + 20/nail)'),
    ('art', 'french', 'เล็บเฟรนช์ปลายลายดอกไม้ ผลงาน Nail Me', 'sa2', 'เฟรนช์ปลาย + ดอกไม้', 'เฟรนช์ +30/นิ้ว เพ้นท์ดอกไม้ +20/นิ้ว', 280, None, 'French + flowers', 'French tip +30/nail, painted flowers +20/nail'),
    ('art', 'french_dots', 'เล็บเฟรนช์ลายจุด ผลงาน Nail Me', 'sa3', 'เฟรนช์ลายจุด', 'เฟรนช์ปลาย +30/นิ้ว ลายจุด +20/นิ้ว', 280, None, 'French with dots', 'French tip +30/nail, dots +20/nail'),
    ('art', 'pink_gems', 'เล็บเจลชมพูติดอะไหล่ ผลงาน Nail Me', 'sa4', 'ติดอะไหล่ เพชร', 'ติดอะไหล่เล็ก +20/นิ้ว ปั้นนูน +50/นิ้ว', 270, None, 'Gems &amp; charms', 'Small decorations +20/nail, 3D +50/nail'),
    ('art', 'gold_white', 'เล็บเจลสีขาวแต่งทอง ผลงาน Nail Me', 'sa5', 'ขาวแต่งฟอยล์ทอง', 'ทาสีเจล + ตกแต่งฟอยล์ คิดเพิ่มต่อนิ้ว', 270, None, 'White with gold foil', 'Gel + foil decoration, priced per nail'),
    ('art', 'white_dots', 'เล็บเจลขาวลายจุด ผลงาน Nail Me', 'sa6', 'ขาวมินิมอล ลายจุด', 'เพ้นท์ลาย +20/นิ้ว', 270, None, 'Minimal white dots', 'Hand-painted +20/nail'),
    ('ext', 'long_clear', 'ต่อเล็บ PVC ทรงยาว ผลงาน Nail Me', 'se1', 'ต่อเล็บ PVC ทรงยาว', 'ต่อเล็บ PVC เจลเว้นโคน ดูเป็นธรรมชาติ', 350, 250, 'Long PVC extensions', 'PVC extensions with gel, natural look'),
    ('ext', 'red_long', 'ต่อเล็บ PVC สีแดง ผลงาน Nail Me', 'se2', 'ต่อเล็บ PVC + ทาสีเจล', 'ต่อเล็บ 350 + ทาสีเจลตามป้าย', 350, None, 'PVC extensions + gel', 'Extensions 350 + gel colour as listed'),
    ('ext', 'pink_sparkle', 'เล็บเจลชมพูประกาย ผลงาน Nail Me', 'se3', 'เสริมหน้าเล็บ + สี', 'เสริมหน้าเล็บก่อนทาสี 450 · หลังทาสี 150', 150, None, 'Overlay + colour', 'Overlay before gel 450 · after gel 150'),
    ('ext', 'toes_glitter', 'ทาสีเจลเท้ากลิตเตอร์ ผลงาน Nail Me', 'se4', 'สปาเท้า 10 ขั้นตอน', 'แช่ ขัด มาร์ก นวด บำรุง ขัดถึงใต้เข่า', 499, 450, '10-step foot spa', 'Soak, scrub, mask, massage, up to the knee'),
    ('ext', 'toes_daisy', 'ทาสีเจลเท้าลายเดซี่ ผลงาน Nail Me', 'se5', 'สปาเท้า + ทาสีเจลเท้า', 'สปาเท้า 499 + ทาสีเจลเท้า 300', 799, None, 'Foot spa + gel pedicure', 'Foot spa 499 + gel pedicure 300'),
    ('ext', 'lace', 'เล็บเจลลายลูกไม้ ผลงาน Nail Me', 'se6', 'สปามือ 9 ขั้นตอน', 'บำรุงล้ำลึก ตัดหนัง นวด บำรุงจมูกเล็บ', 399, None, '9-step hand spa', 'Deep nourishment, cuticle care, massage, cuticle oil'),
]

def en_dict():
    d = {}
    for cat, k, th, en in CATS: d[k] = en
    for c in CARDS:
        d[c[3]] = c[8]; d[c[3] + '.d'] = c[9]
    return d
