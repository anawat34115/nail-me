# web-dev/freelance/websites/nail-me/builder/showcase.py
# เรนเดอร์ section "ผลงานจากร้าน" (section 6) 4 เลย์เอาต์ จากข้อมูลเดียวกันใน showcase_data.py
#   L1 rows      : แถวการ์ดเลื่อนแนวนอนแยกหมวด (ตาม ref nailhousebangkok)            → index.html
#   L2 lookbook  : กริดนิตยสาร ใบแรกใหญ่ ป้ายราคาบนรูป ตัวกรองแบบขีดเส้นใต้           → design2.html (seeUnail / สงบ)
#   L3 catalogue : ดัชนี 01/02/03 ติดซ้าย + รูปทรงโค้งประตู ชื่อ…ราคา                 → design3.html (nailgarden / สวน)
#   L4 evening   : พื้นเข้ม แท็บทอง ชื่อ+ราคาพิมพ์บนรูป ใบแรกของหมวดใหญ่               → design4.html (Hojicha)
from showcase_data import CATS, CARDS, P

HEAD = '''        <div class="flex flex-wrap items-end justify-between gap-4 mb-8 reveal">
          <div>
            <h2 id="gallery-title" class="font-display font-semibold text-[clamp(32px,4.5vw,48px)]" data-i18n="gallery.title">ผลงานจากร้าน</h2>
            <p class="mt-3 text-muted max-w-[36em]" data-i18n="gallery.sub">ลายที่ทำได้จริงจากร้าน พร้อมราคาตามป้าย เลือกลายแล้วโทรจองได้เลย หรือส่งรูปลายที่ชอบมาทาง LINE</p>
          </div>
          <a class="text-[15px] underline decoration-gold underline-offset-4 hover:text-pink-deep" href="https://www.facebook.com/nailmesuratthani" target="_blank" rel="noopener" data-track="facebook" data-i18n="gallery.more">ดูผลงานล่าสุดบนเพจ</a>
        </div>
'''
NOTE = '''        <p class="mt-6 text-[13px] text-muted" data-i18n="gallery.note">ราคาในการ์ดคือราคาตามป้ายราคาในร้าน ราคางานเพ้นท์/ตกแต่งขึ้นกับจำนวนนิ้วและลาย สอบถามช่างก่อนทำได้</p>
'''
TODO = '        <!-- TODO ก่อนขึ้นจริง: โหลดรูปจาก Drive มาไว้ใน img/ แปลง WebP ≤300KB · ชื่อลาย/ราคาต่อใบให้ร้านตรวจ -->\n'

def img(c, cls='photo', lazy=True):
    return f'<img src="{P(c[1])}" alt="{c[2]}" class="{cls}" loading="lazy" decoding="async" width="900" height="1200">'

def price_html(c, big='text-[26px]', small='text-[13px]'):
    if c[7]:
        return f'<span class="num {big} text-pink-deep leading-none">฿{c[7]}</span> <span class="{small} text-muted line-through">฿{c[6]}</span>'
    return f'<span class="num {big} text-pink-deep leading-none">฿{c[6]}</span>'

# ------------------------------------------------------------------ L1 rows
L1_CSS = '''    .scroller { scrollbar-width: none; } .scroller::-webkit-scrollbar { display: none; }
    .chip { display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 999px; border: 1px solid var(--line); background: var(--blush); font-size: 14px; white-space: nowrap; color: var(--ink); }
    .chip:hover { border-color: var(--pink-deep); color: var(--pink-deep); }
    .show-row { display: grid; grid-auto-flow: column; grid-auto-columns: 76%; gap: 16px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 8px; scrollbar-width: none; -webkit-overflow-scrolling: touch; }
    .show-row::-webkit-scrollbar { display: none; }
    @media (min-width: 640px) { .show-row { grid-auto-columns: 46%; } }
    @media (min-width: 1024px) { .show-row { grid-auto-columns: calc((100% - 48px) / 4); } }
    .row-btn { width: 40px; height: 40px; border-radius: 999px; border: 1px solid var(--line); display: inline-flex; align-items: center; justify-content: center; color: var(--ink); font-size: 18px; background: var(--cream); }
    .row-btn:hover { border-color: var(--pink-deep); color: var(--pink-deep); }
    .show-card { background: var(--cream); border: 1px solid var(--line); border-radius: 16px; overflow: hidden; }
    .show-card .ph { aspect-ratio: 1 / 1; overflow: hidden; background: var(--rose); }
'''
L1_JS = '''    document.querySelectorAll('[data-row-prev],[data-row-next]').forEach(b => b.addEventListener('click', () => {
      const row = b.closest('div[id^="show-"]').querySelector('.show-row'); const card = row.firstElementChild; const w = card ? card.getBoundingClientRect().width + 16 : 300;
      row.scrollBy({ left: b.hasAttribute('data-row-next') ? w : -w, behavior: 'smooth' });
    }));
'''
def l1_card(c):
    return f'''          <article class="show-card snap-start">
            <div class="ph">{img(c)}</div>
            <div class="p-4 md:p-5">
              <h3 class="font-medium text-[17px] leading-[1.4]" data-i18n="{c[3]}">{c[4]}</h3>
              <p class="mt-1 text-[13px] text-muted leading-[1.6]" data-i18n="{c[3]}.d">{c[5]}</p>
              <div class="mt-3 flex items-baseline justify-between gap-3"><p>{price_html(c)}</p><a class="text-[13px] text-pink-deep underline decoration-gold underline-offset-4 whitespace-nowrap" href="tel:+66646542666" data-track="call" data-i18n="show.book">จองคิว</a></div>
            </div>
          </article>
'''
def render_l1():
    rows = ''
    for cid, k, th, en in CATS:
        cards = ''.join(l1_card(c) for c in CARDS if c[0] == cid)
        rows += f'''        <div class="mt-10 first:mt-0" id="show-{cid}">
          <div class="flex items-baseline justify-between gap-4 mb-4"><h3 class="font-display font-medium text-[24px] md:text-[28px]" data-i18n="{k}">{th}</h3><div class="flex items-center gap-3"><a class="text-[14px] underline decoration-gold underline-offset-4 hover:text-pink-deep" href="#menu" data-i18n="show.all">ดูราคาทั้งหมด</a><span class="hidden md:inline-flex gap-2"><button type="button" class="row-btn" data-row-prev aria-label="ก่อนหน้า"><i class="ph ph-arrow-left" aria-hidden="true"></i></button><button type="button" class="row-btn" data-row-next aria-label="ถัดไป"><i class="ph ph-arrow-right" aria-hidden="true"></i></button></span></div></div>
          <div class="show-row">
{cards}          </div>
        </div>
'''
    chips = ''.join(f'<a class="chip" href="#show-{cid}" data-i18n="chip.{i+1}">{t}</a>' for i, (cid, t) in enumerate([('color','ทาสีเจล'),('art','เพ้นท์ · อะไหล่'),('ext','ต่อเล็บ · สปา')])) + '<a class="chip" href="#menu" data-i18n="chip.4">ราคาทั้งหมด</a>'
    return f'''    <!-- ===== 6. ผลงานและบริการ: การ์ดรูป+ราคา แยกหมวด เลื่อนแนวนอน (โครงตาม nailhousebangkok) ===== -->
    <section id="gallery" class="bg-cream border-t border-line py-14 md:py-20 lg:py-24" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
{HEAD}        <nav class="flex gap-3 overflow-x-auto scroller pb-2 mb-8 reveal" aria-label="หมวดผลงาน">
          {chips}
        </nav>
{TODO}        <div class="reveal">
{rows}        </div>
{NOTE}      </div>
    </section>
'''

# ------------------------------------------------------------------ L2 lookbook
L2_CSS = '''    /* showcase L2: lookbook */
    .lb-tabs { display: flex; gap: 24px; overflow-x: auto; scrollbar-width: none; border-bottom: 1px solid var(--line); }
    .lb-tabs::-webkit-scrollbar { display: none; }
    .lb-tab { padding: 12px 0; font-size: 15px; color: var(--muted); border-bottom: 2px solid transparent; margin-bottom: -1px; white-space: nowrap; transition: color .3s var(--ease), border-color .3s var(--ease); }
    .lb-tab[aria-selected="true"], .lb-tab:hover { color: var(--ink); border-color: var(--pink-deep); }
    .lb-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; grid-auto-flow: dense; }
    @media (min-width: 768px) { .lb-grid { grid-template-columns: repeat(4, 1fr); gap: 20px; } .lb-card.is-big { grid-column: span 2; grid-row: span 2; } }
    .lb-card { display: block; }
    .lb-card .ph { position: relative; aspect-ratio: 4 / 5; overflow: hidden; border-radius: 8px; background: var(--rose); }
    @media (min-width: 768px) { .lb-card.is-big { display: flex; flex-direction: column; } .lb-card.is-big .ph { flex: 1; aspect-ratio: auto; min-height: 0; } }
    .lb-card .ph img { transition: transform .9s var(--ease); }
    .lb-card:hover .ph img { transform: scale(1.04); }
    .lb-tag { position: absolute; left: 12px; top: 12px; background: var(--cream); color: var(--pink-deep); font-family: "Cormorant Garamond", serif; font-weight: 600; font-size: 18px; line-height: 1; padding: 8px 12px; border-radius: 4px; }
    .lb-tag s { font-family: "Noto Sans Thai", sans-serif; font-weight: 400; font-size: 11px; color: var(--muted); margin-left: 4px; }
    .lb-card[hidden] { display: none; }
'''
L2_JS = '''    (function(){ const tabs=[...document.querySelectorAll('.lb-tab')]; const cards=[...document.querySelectorAll('.lb-card')];
      tabs.forEach(t=>t.addEventListener('click',()=>{ const cat=t.dataset.cat; tabs.forEach(x=>x.setAttribute('aria-selected', String(x===t)));
        cards.forEach(c=>{ c.hidden = !(cat==='all' || c.dataset.cat===cat); }); })); })();
'''
def l2_card(c, big=False):
    tag = f'฿{c[7]}<s>฿{c[6]}</s>' if c[7] else f'฿{c[6]}'
    return f'''          <a class="lb-card{' is-big' if big else ''}" href="tel:+66646542666" data-track="call" data-cat="{c[0]}">
            <div class="ph">{img(c)}<span class="lb-tag">{tag}</span></div>
            <h3 class="mt-3 font-medium text-[15px] md:text-[16px] leading-[1.4]" data-i18n="{c[3]}">{c[4]}</h3>
            <p class="text-[13px] text-muted leading-[1.5]" data-i18n="{c[3]}.d">{c[5]}</p>
          </a>
'''
def render_l2():
    big_idx = {0, 7, 12}
    cards = ''.join(l2_card(c, i in big_idx) for i, c in enumerate(CARDS))
    tabs = '<button type="button" class="lb-tab" role="tab" aria-selected="true" data-cat="all" data-i18n="chip.0">ทั้งหมด</button>' + ''.join(
        f'<button type="button" class="lb-tab" role="tab" aria-selected="false" data-cat="{cid}" data-i18n="chip.{i+1}">{t}</button>' for i, (cid, t) in enumerate([('color','ทาสีเจล'),('art','เพ้นท์ · อะไหล่'),('ext','ต่อเล็บ · สปา')]))
    return f'''    <!-- ===== 6. ผลงาน: lookbook กริดนิตยสาร + ตัวกรอง (แบบ 2) ===== -->
    <section id="gallery" class="py-14 md:py-20 lg:py-24" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
{HEAD}        <div class="lb-tabs mb-8 reveal" role="tablist" aria-label="หมวดผลงาน">{tabs}</div>
{TODO}        <div class="lb-grid reveal">
{cards}        </div>
{NOTE}      </div>
    </section>
'''

# ------------------------------------------------------------------ L3 catalogue (arch)
L3_CSS = '''    /* showcase L3: catalogue โค้งประตู */
    .cat-index a { display: flex; align-items: baseline; gap: 16px; padding: 12px 0; border-top: 1px solid var(--line); color: var(--ink); }
    .cat-index a:last-child { border-bottom: 1px solid var(--line); }
    .cat-index .n { font-family: "Cormorant Garamond", serif; font-size: 24px; color: var(--pink-deep); width: 32px; }
    .cat-index a:hover .t { text-decoration: underline; text-decoration-color: var(--gold); text-underline-offset: 4px; }
    .arch { aspect-ratio: 3 / 4; overflow: hidden; border-radius: 999px 999px 12px 12px; background: var(--rose); }
    .arch img { transition: transform .9s var(--ease); } .arch-card:hover .arch img { transform: scale(1.04); }
    .arch-row { display: flex; align-items: baseline; gap: 8px; margin-top: 12px; }
    .arch-row .lead { flex: 1; border-bottom: 1px dotted var(--gold); transform: translateY(-5px); min-width: 16px; }
'''
def l3_card(c):
    return f'''            <a class="arch-card block" href="tel:+66646542666" data-track="call">
              <div class="arch">{img(c)}</div>
              <div class="arch-row"><h4 class="font-medium text-[15px] leading-[1.4]" data-i18n="{c[3]}">{c[4]}</h4><span class="lead" aria-hidden="true"></span><span class="num text-[22px] text-pink-deep whitespace-nowrap">฿{c[7] or c[6]}</span></div>
              <p class="text-[13px] text-muted leading-[1.5]" data-i18n="{c[3]}.d">{c[5]}</p>
            </a>
'''
def render_l3():
    idx = ''.join(f'<a href="#show-{cid}"><span class="n">0{i+1}</span><span class="t" data-i18n="{k}">{th}</span><span class="ml-auto text-[13px] text-muted">{sum(1 for c in CARDS if c[0]==cid)}</span></a>' for i, (cid, k, th, en) in enumerate(CATS))
    groups = ''
    for i, (cid, k, th, en) in enumerate(CATS):
        cards = ''.join(l3_card(c) for c in CARDS if c[0] == cid)
        groups += f'''          <div id="show-{cid}" class="{'mt-14' if i else ''} reveal">
            <h3 class="font-display font-medium text-[24px] md:text-[28px] text-pink-deep mb-6"><span class="num text-gold mr-3">0{i+1}</span><span data-i18n="{k}">{th}</span></h3>
            <div class="grid grid-cols-2 lg:grid-cols-3 gap-5 md:gap-8">
{cards}            </div>
          </div>
'''
    return f'''    <!-- ===== 6. ผลงาน: แคตตาล็อก ดัชนี 01/02/03 + รูปโค้งประตู (แบบ 3) ===== -->
    <section id="gallery" class="border-t border-line py-14 md:py-20 lg:py-24" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
{HEAD}{TODO}        <div class="grid lg:grid-cols-12 gap-10 lg:gap-16 items-start">
          <nav class="cat-index lg:col-span-3 lg:sticky lg:top-24 reveal" aria-label="หมวดผลงาน">{idx}<a href="#menu" class="arrow-link !border-0 !py-2" data-i18n="show.all">ดูราคาทั้งหมด</a></nav>
          <div class="lg:col-span-9">
{groups}          </div>
        </div>
{NOTE}      </div>
    </section>
'''

# ------------------------------------------------------------------ L4 evening (dark, text on photo)
L4_CSS = '''    /* showcase L4: กระดานยามเย็น */
    .ev-tabs { display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; }
    .ev-tabs::-webkit-scrollbar { display: none; }
    .ev-tab { height: 40px; padding: 0 16px; border-radius: 999px; border: 1px solid rgba(233,215,165,.4); color: var(--gold-light); font-size: 14px; white-space: nowrap; transition: background .3s var(--ease), color .3s var(--ease); }
    .ev-tab[aria-selected="true"] { background: var(--gold-light); color: var(--cocoa); }
    .ev-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
    @media (min-width: 768px) { .ev-grid { grid-template-columns: repeat(3, 1fr); gap: 16px; } .ev-card:first-child { grid-column: span 2; grid-row: span 2; } }
    .ev-card { position: relative; display: block; aspect-ratio: 3 / 4; overflow: hidden; border-radius: 16px; background: #5c3a3f; }
    .ev-card:first-child { aspect-ratio: auto; min-height: 100%; }
    .ev-card img { transition: transform .9s var(--ease); } .ev-card:hover img { transform: scale(1.04); }
    .ev-card::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(74,44,48,0) 45%, rgba(74,44,48,.85) 100%); }
    .ev-card .cap { position: absolute; left: 0; right: 0; bottom: 0; padding: 16px; z-index: 1; color: var(--cream); }
    .ev-card .cap .pr { font-family: "Zen Old Mincho", serif; font-size: 24px; color: var(--gold-light); line-height: 1; }
    .ev-card .cap .pr s { font-family: "Noto Sans Thai", sans-serif; font-size: 12px; color: rgba(255,249,245,.6); margin-left: 6px; }
    .ev-card .cap p { font-size: 12px; color: rgba(255,249,245,.75); margin-top: 4px; }
    .ev-card:first-child .cap { padding: 24px; } .ev-card:first-child .cap .pr { font-size: 36px; }
    .ev-panel[hidden] { display: none; }
'''
L4_JS = '''    (function(){ const tabs=[...document.querySelectorAll('.ev-tab')]; const panels=[...document.querySelectorAll('.ev-panel')];
      tabs.forEach(t=>t.addEventListener('click',()=>{ tabs.forEach(x=>x.setAttribute('aria-selected', String(x===t))); panels.forEach(p=>{ p.hidden = p.dataset.cat!==t.dataset.cat; }); })); })();
'''
def l4_card(c):
    pr = f'฿{c[7]}<s>฿{c[6]}</s>' if c[7] else f'฿{c[6]}'
    return f'''            <a class="ev-card" href="tel:+66646542666" data-track="call">
              {img(c, 'photo')}
              <div class="cap"><h4 class="font-medium text-[15px] md:text-[16px] leading-[1.4]" data-i18n="{c[3]}">{c[4]}</h4><p data-i18n="{c[3]}.d">{c[5]}</p><p class="pr mt-2">{pr}</p></div>
            </a>
'''
def render_l4():
    tabs = ''.join(f'<button type="button" class="ev-tab" role="tab" aria-selected="{"true" if i==0 else "false"}" data-cat="{cid}" data-i18n="chip.{i+1}">{t}</button>' for i, (cid, t) in enumerate([('color','ทาสีเจล'),('art','เพ้นท์ · อะไหล่'),('ext','ต่อเล็บ · สปา')]))
    panels = ''
    for i, (cid, k, th, en) in enumerate(CATS):
        cards = ''.join(l4_card(c) for c in CARDS if c[0] == cid)
        panels += f'''          <div class="ev-panel ev-grid" data-cat="{cid}"{'' if i==0 else ' hidden'}>
{cards}          </div>
'''
    return f'''    <!-- ===== 6. ผลงาน: กระดานยามเย็น พื้นเข้ม แท็บทอง ชื่อ+ราคาบนรูป (แบบ 4) ===== -->
    <section id="gallery" class="bg-cocoa text-cream py-14 md:py-20 lg:py-24" aria-labelledby="gallery-title">
      <div class="mx-auto max-w-[1200px] px-4 md:px-8">
        <div class="flex flex-wrap items-end justify-between gap-6 mb-8 reveal">
          <div>
            <p class="label !text-gold-light" data-i18n="gallery.label">Nail art</p>
            <h2 id="gallery-title" class="font-display font-medium text-[clamp(32px,4.5vw,48px)] mt-2 text-gold-light" data-i18n="gallery.title2">ลายเล็บจากร้าน</h2>
            <p class="mt-3 text-cream/75 max-w-[36em]" data-i18n="gallery.sub">ลายที่ทำได้จริงจากร้าน พร้อมราคาตามป้าย เลือกลายแล้วโทรจองได้เลย หรือส่งรูปลายที่ชอบมาทาง LINE</p>
          </div>
          <a class="inline-flex items-center gap-2 text-[15px] text-gold-light underline underline-offset-4 hover:text-cream" href="https://www.facebook.com/nailmesuratthani" target="_blank" rel="noopener" data-track="facebook"><span data-i18n="gallery.more">ดูผลงานล่าสุดบนเพจ</span><i class="ph ph-arrow-up-right" aria-hidden="true"></i></a>
        </div>
        <div class="ev-tabs mb-6 reveal" role="tablist" aria-label="หมวดผลงาน">{tabs}</div>
{TODO}        <div class="reveal">
{panels}        </div>
        <p class="mt-6 text-[13px] text-cream/60" data-i18n="gallery.note">ราคาในการ์ดคือราคาตามป้ายราคาในร้าน ราคางานเพ้นท์/ตกแต่งขึ้นกับจำนวนนิ้วและลาย สอบถามช่างก่อนทำได้</p>
      </div>
    </section>
'''
