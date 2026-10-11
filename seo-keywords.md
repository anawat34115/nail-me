# คีย์เวิร์ด SEO · Nail me (ลูกค้าเลือกชุดที่แนะนำ 11 ต.ค. 2569)

## ชุดหลัก (ใส่ใน title / description / h1 / about / alt แล้ว)
| ภาษา | คีย์เวิร์ด | ใช้ที่ |
|---|---|---|
| TH | ร้านทำเล็บ สุราษฎร์ธานี | title, description, h1 eyebrow, about |
| TH | ทำเล็บเจล สุราษฎร์ / ทาสีเจล สุราษฎร์ | title, description, section บริการ |
| TH | สปาเท้า สุราษฎร์ | title, section สปา, FAQ |
| TH | ต่อเล็บ สุราษฎร์ธานี | title, section บริการ |
| TH | ร้านเล็บ ตลาดศาลเจ้า | description, ที่ตั้ง, about |
| EN | nail salon Surat Thani | EN title, og:description, about EN |
| EN | gel nails Surat Thani | EN title |
| EN | foot spa Surat Thani | EN title, FAQ EN |

## รอง (ค่อยเพิ่มเมื่อมีหน้า/เนื้อหา)
เพ้นท์เล็บ สุราษฎร์ · สปามือ สุราษฎร์ · ร้านทำเล็บ ใกล้ฉัน (ต้องพึ่ง Google Business Profile) · nail art Surat Thani · manicure pedicure Surat Thani

## กฎ
- ชื่อร้าน + ที่อยู่ + เบอร์ ต้องตรงกันทุกที่ (เว็บ, GBP, เพจ FB 2 เพจ) — รอร้านยืนยันเบอร์หลัก
- ไม่ยัดคีย์เวิร์ดซ้ำเกินในย่อหน้าเดียว ใช้ภาษาคนอ่าน
- ขึ้นจริงแล้วส่ง sitemap ใน Search Console และใส่ลิงก์เว็บใน GBP + เพจ

## ออนเพจที่ทำแล้ว (11 ต.ค. 16:54 · ทุกแบบ)
- [x] title / meta description TH+EN มีคีย์เวิร์ดหลัก + เบอร์ + LINE
- [x] h1 มีคีย์เวิร์ด "ร้านทำเล็บ สุราษฎร์ธานี · ข้างตลาดศาลเจ้า" (บรรทัดเล็กใน h1) + "ร้านหรู แต่ราคาน่ารัก"
- [x] h2 มีคีย์เวิร์ดแบบธรรมชาติ: บริการทำเล็บและราคา / ผลงานทำเล็บจากร้าน / แวะมาที่ร้าน ตลาดศาลเจ้า สุราษฎร์ธานี
- [x] canonical, og:url, og:locale th_TH + en_US, og:site_name, twitter:card, geo.region TH-84
- [x] JSON-LD NailSalon ครบ: url, logo, openingHoursSpecification, priceRange ฿150–฿799, areaServed, hasMap, makesOffer 5 บริการ, sameAs (FB 2 เพจ + LINE) + FAQPage 6 ข้อ
- [x] รูปทุกใบมี alt บอกบริการ+ชื่อร้าน, width/height, lazy ยกเว้น hero (fetchpriority=high)
- [x] ลิงก์ภายใน (#menu #spa #faq) และ data-track ทุกปุ่มติดต่อ

## ต้องทำตอนขึ้นจริง (ยังทำไม่ได้ตอนนี้)
- [ ] ลบ `<meta name="robots" content="noindex">` และเปลี่ยน canonical / og:url / JSON-LD url เป็นโดเมนจริง (มี TODO ในโค้ด)
- [ ] โหลดรูปจาก Drive มาไว้ใน img/ แปลง WebP ≤300KB (ตอนนี้ลิงก์ lh3 ไม่ติดอันดับรูปและเสี่ยงหาย)
- [ ] ใส่ GTM/GA4 + Search Console + ส่ง sitemap.xml + robots.txt
- [ ] แยกหน้า /en/ (หรือ hreflang) ถ้าอยากให้ Google จัดอันดับภาษาอังกฤษแยก — ตอนนี้สลับด้วย JS Google เห็นเฉพาะไทย
- [ ] ยืนยันเบอร์/เวลาเปิดกับร้านแล้วแก้ให้ตรง GBP
- [ ] หน้านโยบายความเป็นส่วนตัว
