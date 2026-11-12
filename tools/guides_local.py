#!/usr/bin/env python3
"""
guides_local.py  —  Version: V1  (12 Nov 2026)
"Routes and commutes" guides for Pillai Auto's four regions. Distances are
approximate road distances; charger locations are deliberately not listed
(they change) — riders are pointed to the Ather app instead.
"""
M = "https://media.atherenergy.com/"

GUIDES = [
# ---------------------------------------------------------------------------
{
"slug": "chennai-to-puducherry-ecr-on-an-ather",
"cluster": "local",
"title": "Chennai to Puducherry on an Ather via ECR: Range and Charging",
"desc": "Riding an Ather from Chennai to Puducherry on the ECR: which model and battery, planning a charging stop, riding tips and help at our Puducherry showroom.",
"h1": "Chennai to Puducherry on an Ather, via the ECR",
"lede": "The East Coast Road from Chennai to Puducherry is one of the best rides in Tamil Nadu, and it is very doable on an Ather. At roughly 150 km it is a little beyond a single charge for most riders, so the trick is planning one relaxed stop.",
"img": M + "ather-450-overtones-new-d.webp",
"img_alt": "Ather 450 on the open road",
"models": ["ather-450x", "ather-450-apex", "ather-rizta-z"],
"facts": [("Distance", "About 150 km, Chennai to Puducherry"), ("Best battery", "3.5 kWh"), ("Plan", "One fast-charge stop"),
          ("Help at the end", "Our Puducherry showroom, 100 Ft Road")],
"body": [
("Can an Ather do it?", """
Yes, comfortably, with planning. With the 3.5 kWh battery, Ather's real-world TrueRange is about 125–130 km. Starting from full and riding at a steady 50–60 km/h, many riders cover most of the distance on one charge — but cruising faster, carrying a pillion or riding in a headwind uses more. Plan on **one fast-charge stop** and the ride becomes stress-free.
"""),
("Which scooter suits the ECR", """
| Scooter | Why |
|---|---|
| [450X 3.5 kWh](/scooters/ather-450x.html) | 90 km/h, Infinite Cruise, up to 30 km in 10 min fast charging |
| [450 Apex](/scooters/ather-450-apex.html) | 100 km/h and the most relaxed at speed |
| [Rizta Z 3.5 kWh](/scooters/ather-rizta-z.html) | Best for two people and luggage, also up to 30 km in 10 min |

Smaller batteries and the Konarc can do it with more stops; we would suggest them for shorter coastal rides, such as Mahabalipuram and back.
"""),
("Planning the charging stop", """
1. **Leave with a full charge**, charged at home overnight.
2. **The night before, open the Ather app** and note two Ather Grid points around the halfway mark — one to use and one as a backup.
3. **Stop when you have about 30–40% left**, not when you are nearly empty. Twenty minutes over a coffee at the 3.5 kWh rate adds a large margin.
4. **Ride in SmartEco or Ride mode** on the long stretches and save Warp for overtaking. See [range tips](@how-to-get-more-range-from-your-ather).
"""),
("Riding tips for the coast road", """
- Start early. Morning traffic is lighter and the heat builds by noon.
- Watch for **sand on the road** near beach villages, and for cattle and slow vehicles on single-lane sections.
- Sea breezes can be strong; a headwind costs range, a tailwind gives it back.
- Wear a full-face helmet — a long ride at speed is not the place for a half helmet.
"""),
("When you arrive", """
Our [Puducherry showroom](/locations/pondicherry.html) on 100 Ft Road, Sundarraja Nagar, can help with a top-up, a quick check, or advice on the ride back. Call ahead and we will expect you.
"""),
],
"faqs": [
("Can an Ather go from Chennai to Puducherry on one charge?", "It is about 150 km. With the 3.5 kWh battery and gentle riding some riders manage most of it, but we recommend planning one fast-charge stop."),
("Which Ather is best for long rides on the ECR?", "The 450X or 450 Apex with the 3.5 kWh battery for a solo rider, or the Rizta Z 3.5 kWh for two. All three take up to 30 km of range in ten minutes at an Ather Grid charger."),
("Is there Ather service in Puducherry?", "Yes. Pillai Auto's Puducherry showroom on 100 Ft Road has sales, service and charging."),
],
"related": ["ather-grid-fast-charging-guide", "ather-scooter-for-long-commutes", "ather-450-battery-2-9-vs-3-5-kwh"],
},
# ---------------------------------------------------------------------------
{
"slug": "daily-commute-chengalpattu-to-chennai-on-an-ather",
"cluster": "local",
"title": "Chengalpattu to Chennai Daily on an Ather: Commute Guide",
"desc": "Commuting from Chengalpattu or Maraimalai Nagar to Chennai on an Ather: battery choice, charging at work, GST Road riding and local service.",
"h1": "Commuting from Chengalpattu to Chennai on an Ather",
"lede": "Many of our Chengalpattu customers ride up the GST Road to Chennai every day — to Tambaram, Guindy or beyond. It is one of the longer EV commutes in the region, and it works well with the right battery and a simple charging routine.",
"img": M + "Ather-450-electric-scooter-front-view.webp",
"img_alt": "Ather 450 on the road",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc"],
"facts": [("Chengalpattu–Guindy", "About 55 km each way"), ("Round trip", "About 110 km"), ("Battery", "3.5 kWh recommended"),
          ("Showroom", "GST Road, Pulipakkam")],
"body": [
("Does the range work?", """
A round trip of around 110 km is within the 3.5 kWh battery's TrueRange of about 125–130 km, but not with much to spare if you ride fast or carry a pillion. The reliable approach is to **charge every night** at home and **top up during the day** — at work if your office allows it, or at an Ather Grid point.

From Maraimalai Nagar or Guduvancheri to Tambaram, the distances are much shorter, and a smaller battery is usually fine.
"""),
("Our recommended setup", """
| Commute | Suggested scooter |
|---|---|
| Chengalpattu to Guindy / city centre, daily | [450X 3.5 kWh](/scooters/ather-450x.html) — speed for the GST Road, 30 km in 10 min fast charging |
| Same, with a pillion | [Rizta Z 3.5 kWh](/scooters/ather-rizta-z.html) |
| Maraimalai Nagar / Guduvancheri to Tambaram | [Konarc S](/scooters/ather-konarc.html) 2.7 or 3.5 kWh, or a 450S |
"""),
("Charging at work", """
A portable charger in the boot and a socket at the office car park can turn a tight day into an easy one. Two or three hours on a 900 W charger adds a lot of range. Ask your facilities team; many offices along the GST Road and in the Mahindra World City area already allow it. Otherwise, identify an Ather Grid point near your workplace in the Ather app.
"""),
("Riding the GST Road", """
- The GST Road carries heavy, fast traffic. A 450X's Warp mode helps you merge and overtake safely; keep to the left lane otherwise.
- Expect slow stretches through Perungalathur and Tambaram at peak hours — Infinite Cruise's Crawl Control on the 450X takes the strain.
- Watch for buses pulling in to stops without warning.
"""),
("Service close to home", """
Our [Chengalpattu showroom](/locations/chengalpattu.html) on the GST Pulipakkam Road handles periodic service, so you can drop the scooter on a weekend rather than taking it into the city. See the [service schedule guide](@ather-service-schedule-and-costs).
"""),
],
"faqs": [
("Can I commute from Chengalpattu to Chennai daily on an Ather?", "Yes. With the 3.5 kWh battery, a daily home charge and a top-up at work or on Ather Grid, a round trip of around 110 km is comfortable."),
("Which Ather is best for the GST Road?", "The 450X with the 3.5 kWh battery: 90 km/h top speed, Warp mode for merging, and up to 30 km of fast charge in ten minutes."),
("Is there an Ather service centre in Chengalpattu?", "Yes. Pillai Auto's Chengalpattu showroom on GST Road, Pulipakkam, offers sales and service."),
],
"related": ["ather-scooter-for-long-commutes", "ather-grid-fast-charging-guide", "infinite-cruise-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "omr-it-corridor-commute-on-an-ather",
"cluster": "local",
"title": "Riding an Ather on the OMR IT Corridor: Commuter's Guide",
"desc": "An Ather for the OMR IT corridor: Perungudi, Sholinganallur, Navalur and Siruseri commutes, apartment and office charging, and service at our OMR showroom.",
"h1": "Commuting on the OMR IT corridor with an Ather",
"lede": "The OMR is where we sell more Athers than anywhere else, and it is easy to see why: apartment living, office commutes of 10–30 km, and a long, straight road with service lanes on both sides. Here is how owners here make it work.",
"img": M + "homepagekv.webp",
"img_alt": "Ather Konarc",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc", "ather-450s"],
"facts": [("Typical commute", "10–30 km each way"), ("Battery", "Smaller pack is often enough"), ("Showroom", "Rajiv Gandhi Salai (OMR), Chennai")],
"body": [
("Typical OMR commutes", """
Most OMR commutes run between neighbourhoods like Thiruvanmiyur, Perungudi, Thoraipakkam, Sholinganallur, Navalur and Siruseri — usually 10–30 km each way. That is well within the range of every Ather, even on the smaller batteries, as long as you charge regularly.
"""),
("Which Ather suits the OMR", """
- **Solo commuter who likes to ride:** [450X](/scooters/ather-450x.html) — Google Maps on the dash for meetings across the city, and Infinite Cruise for the evening crawl.
- **Value commuter:** [450S](/scooters/ather-450s.html) or [Konarc S](/scooters/ather-konarc.html) 2.7 kWh.
- **Couples and families** sharing one scooter: [Rizta Z](/scooters/ather-rizta-z.html).
"""),
("Charging when you live in an apartment", """
Many OMR complexes now have parking-slot sockets, and associations are increasingly used to EV requests. Our [apartment charging guide](@charging-ather-at-home-in-a-chennai-apartment) walks through the options and how to approach your association. If home charging is not possible yet, an office socket two or three days a week covers most commutes on its own.
"""),
("Office parking and charging", """
Several IT parks on the corridor allow two-wheeler charging; check with your facilities team. A portable charger lives happily in the boot of every Ather. Ather Grid points across the corridor are shown live in the Ather app.
"""),
("Traffic and safety on the OMR", """
- Use the service lanes at peak hours where they move better.
- Watch for vehicles cutting across from the median openings.
- At night, the long straights invite speed — the Emergency Stop Signal and good lights help, but a sensible pace helps more.
"""),
("Your local showroom", """
Our [OMR showroom](/locations/chennai-omr.html) on Rajiv Gandhi Salai is the flagship: full line-up, test rides from the door, service bays and finance in one building. Book a test ride before or after office hours.
"""),
],
"faqs": [
("Is an Ather good for OMR office commutes?", "Yes. Typical OMR commutes of 10–30 km each way are well within every Ather's range, and service lanes make the ride easy."),
("Where can I charge an Ather on the OMR?", "At home or at your apartment parking slot, at offices that allow it, and at Ather Grid fast chargers shown in the Ather app."),
("Where is Pillai Auto's OMR showroom?", "On Rajiv Gandhi Salai (OMR), Chennai. See our Chennai OMR page for the address and directions."),
],
"related": ["charging-ather-at-home-in-a-chennai-apartment", "ather-450x-vs-450s", "infinite-cruise-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "chidambaram-cuddalore-neyveli-on-an-ather",
"cluster": "local",
"title": "Riding an Ather Around Chidambaram, Cuddalore and Neyveli",
"desc": "Owning an Ather in Chidambaram, Cuddalore, Neyveli and Sirkazhi: town and highway distances, rough-road choices, home charging and local service.",
"h1": "Riding an Ather around Chidambaram, Cuddalore and Neyveli",
"lede": "Our Chidambaram showroom serves a wide area — from Sirkazhi to Cuddalore and Neyveli — with a mix of town streets, state highways and village roads. That mix shapes which Ather we recommend, and how owners here charge.",
"img": M + "konarc-gallery-t-desk-4.webp",
"img_alt": "Ather Konarc",
"models": ["ather-konarc", "ather-rizta-s", "ather-rizta-z", "ather-450x"],
"facts": [("Chidambaram–Cuddalore", "About 45 km"), ("Chidambaram–Neyveli", "About 45 km"), ("Chidambaram–Sirkazhi", "About 20 km"),
          ("Showroom", "Cuddalore Bye-Pass Road")],
"body": [
("Distances that matter", """
| Trip from Chidambaram | Approx. one way | Round trip on one charge? |
|---|---|---|
| Sirkazhi | 20 km | Yes, any Ather |
| Cuddalore | 45 km | Yes with 2.7 kWh and above |
| Neyveli | 45 km | Yes with 2.7 kWh and above |
| Kattumannarkoil | 25 km | Yes, any Ather |

For a daily round trip of 90 km or more, choose the 3.5 kWh battery for a comfortable margin.
"""),
("Choosing for mixed roads", """
Village roads and broken patches favour the [Konarc](/scooters/ather-konarc.html): its 14-inch front wheel, long-travel suspension and 16 cm ground clearance make rough stretches far more comfortable. Families who travel two-up to temple and market often prefer the [Rizta](/scooters/ather-rizta-z.html) for its seat and storage. Riders who spend most of their time on the highway towards Cuddalore will enjoy a [450X](/scooters/ather-450x.html).
"""),
("Charging here", """
Most owners in the region charge at home — independent houses make it simple, with a properly earthed socket near where the scooter is parked. Ather Grid is growing across the region; check the Ather app for points on your regular routes, and plan longer trips around them. See the [fast charging guide](@ather-grid-fast-charging-guide).
"""),
("Heat, dust and rain", """
- Park in shade where you can; Cuddalore district summers are hard on any battery. See [battery care in the heat](@ather-battery-care-in-hot-weather).
- Coastal and village roads carry sand — ride gently on it, and the Rizta Z's SkidControl helps.
- During the north-east monsoon, avoid waterlogged roads entirely. See the [monsoon guide](@riding-your-ather-in-the-chennai-monsoon).
"""),
("Service without the trip to Chennai", """
Our [Chidambaram showroom](/locations/chidambaram.html) on the Cuddalore Bye-Pass Road, Thillainayagapuram, handles sales, periodic service, battery checks and warranty work for the whole area, so there is no need to travel to a city for an Ather service.
"""),
],
"faqs": [
("Is there an Ather showroom in Chidambaram?", "Yes. Pillai Auto's Chidambaram showroom is on the Cuddalore Bye-Pass Road, Thillainayagapuram, with sales and service."),
("Which Ather is best for village roads?", "The Konarc, thanks to its 14-inch front wheel, 90 mm / 100 mm suspension travel and 16 cm ground clearance."),
("Can I ride an Ather from Chidambaram to Cuddalore and back?", "Yes. At about 45 km each way, the round trip is within range of the 2.7 kWh and larger batteries on one charge."),
],
"related": ["ather-konarc-buyers-guide", "ather-battery-care-in-hot-weather", "ather-rizta-family-guide"],
},
]
