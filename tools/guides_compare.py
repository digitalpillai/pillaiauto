#!/usr/bin/env python3
"""
guides_compare.py  —  Version: V1  (12 Nov 2026)
"Ather vs Ather" comparison guides. Facts from Ather's published specification
sheets (Nov 2026); verdicts are Pillai Auto's own. Markup: see build_guides.py.
"""
M = "https://media.atherenergy.com/"

GUIDES = [
# ---------------------------------------------------------------------------
{
"slug": "ather-450x-vs-450s",
"cluster": "compare",
"title": "Ather 450X vs 450S: Differences, Price and Which to Buy",
"desc": "Ather 450X vs 450S compared: power, Warp mode, touchscreen, Google Maps, traction control and fast charging — and whether the 450X is worth ₹13,000 more.",
"h1": "Ather 450X vs 450S",
"lede": "Same chassis, same brakes, same top speed — and roughly ₹13,000 apart at ex-showroom prices. The 450X vs 450S question comes up at our counter every day. The answer depends on four features, not on speed.",
"img": M + "Ather-450X-vs-Ather-450S-electric-scooter-model.webp",
"img_alt": "Ather 450X and 450S",
"models": ["ather-450x", "ather-450s"],
"facts": [("450X from", "₹1,48,998"), ("450S from", "₹1,35,999"), ("Same", "Chassis, brakes, 90 km/h, batteries"),
          ("Different", "Power, screen, Warp, traction control")],
"body": [
("Spec by spec", """
| | 450X | 450S |
|---|---|---|
| Ex-showroom from | ₹1,48,998 | ₹1,35,999 |
| Peak power | 6.4 kW | 5.4 kW |
| Torque | 26 Nm | 22 Nm |
| 0–40 km/h | 3.3 s | 3.9 s |
| Top speed | 90 km/h | 90 km/h |
| Ride modes | SmartEco, Eco, Ride, Sport, Warp | SmartEco, Eco, Ride, Sport |
| Battery | 2.9 / 3.5 kWh | 2.9 / 3.5 kWh |
| IDC range | 126 / 161 km | 122 / 161 km |
| Ather Grid, 10 min (3.5 kWh) | up to 30 km | up to 15 km |
| Dashboard | 7-inch touchscreen | 7-inch DeepView |
| Google Maps | Yes | No |
| Magic Twist | Yes | No |
| Traction control | Multi-Mode (Rain, Road, Rally) | No |
| Infinite Cruise | Yes | No |
"""),
("The four differences that matter", """
### 1. Warp mode and the extra power
Warp is noticeably quicker away from a signal. If you enjoy that, the 450X is the one. If you mostly ride in Eco or Ride mode anyway, the 450S's 5.4 kW is plenty.

### 2. Touchscreen with Google Maps
The 450X shows turn-by-turn Google Maps on its own screen, so your phone stays in your pocket. On the 450S you navigate with your phone.

### 3. Traction control and Magic Twist
Multi-Mode Traction Control reduces wheelspin on wet roads — useful through the north-east monsoon. Magic Twist lets you slow down by rolling the throttle back, which becomes second nature within a week.

### 4. Fast charging with the 3.5 kWh battery
With the bigger battery, the 450X takes up to 30 km in ten minutes at an Ather Grid charger; the 450S takes 15. If you rely on fast chargers, that halves your stops.
"""),
("Choose the 450X if…", """
- You will use navigation most days, or ride in the rain often.
- You rely on fast charging, or ride long distances with the 3.5 kWh battery.
- You want Infinite Cruise for stop-go traffic.
"""),
("Choose the 450S if…", """
- You mostly ride in town and navigate with your phone.
- You want the 450's handling and dual disc brakes at the lowest price.
- You prefer a high-contrast, non-touch screen that stays readable in bright sun.
"""),
],
"faqs": [
("Is the 450X faster than the 450S?", "Both top out at 90 km/h. The 450X is quicker to accelerate — 0–40 km/h in 3.3 seconds against 3.9 — and has the Warp mode."),
("Do the 450X and 450S have the same brakes?", "Yes. Both use a 200 mm triple-piston front disc and a 190 mm rear disc with combined braking."),
("Is the 450X worth the extra money?", "If you will use Google Maps on the dashboard, traction control or faster fast-charging, yes. If not, the 450S gives you the same chassis and brakes for about ₹13,000 less ex-showroom."),
],
"related": ["ather-450s-buyers-guide", "ather-450-battery-2-9-vs-3-5-kwh", "magic-twist-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-rizta-z-vs-rizta-s",
"cluster": "compare",
"title": "Ather Rizta Z vs Rizta S: Which Family Scooter to Buy",
"desc": "Rizta Z vs Rizta S: touchscreen, Google Maps, SkidControl, Crash Alert, colours and price compared. What the ₹15,000 difference buys a family.",
"h1": "Ather Rizta Z vs Rizta S",
"lede": "The two Riztas share the body, the seat, the storage and the motor. What separates them is the technology — and with a family scooter, some of that technology is about safety, not gadgets.",
"img": M + "rizz1-terracotta-red-dt-electric-scooter.webp",
"img_alt": "Ather Rizta Z",
"models": ["ather-rizta-z", "ather-rizta-s"],
"facts": [("Rizta Z from", "₹1,36,999"), ("Rizta S from", "₹1,21,999"), ("Same", "Seat, 56 L storage, 4.3 kW, 80 km/h"),
          ("Z adds", "Touchscreen, Maps, SkidControl, Crash Alert")],
"body": [
("Side by side", """
| | Rizta Z | Rizta S |
|---|---|---|
| Ex-showroom from | ₹1,36,999 | ₹1,21,999 |
| Motor / top speed | 4.3 kW / 80 km/h | 4.3 kW / 80 km/h |
| Storage | 34 L + 22 L frunk | 34 L + 22 L frunk |
| Dashboard | 7-inch touchscreen | 7-inch DeepView |
| Google Maps | Yes | No |
| Multi-language dash (incl. Tamil) | Yes | No |
| SkidControl | Yes | No |
| Crash Alert | Yes | No |
| Magic Twist | Yes | No |
| Voice on Ather | Yes | No |
| Ather Grid, 10 min (3.5 kWh) | up to 30 km | up to 15 km |
| Seat | Premium dual-tone | Standard black |
| Colour options | 9 | 4 |

The frunk is an accessory on both.
"""),
("Where the Rizta Z earns its premium", """
**SkidControl** keeps the scooter composed when a wheel meets sand, wet paint or a slippery patch — the sort of moment that unsettles a rider with a child on the back. **Crash Alert** notifies family with your location if a crash is detected. Those two are the reasons we lean towards the Z for families who carry children or elderly parents.

The **Tamil-language touchscreen** with Google Maps is the other big one, especially for riders who prefer not to read English menus.
"""),
("Where the Rizta S is the smarter buy", """
If the scooter mostly does short local trips — school, market, temple — with one rider, the Rizta S gives you every bit of the Rizta's comfort and storage for about ₹15,000 less ex-showroom. Its DeepView display is clear in bright sun, and you still get FallSafe, AutoHold, Reverse Mode, the Emergency Stop Signal and theft alerts.
"""),
("Our verdict", """
For a family scooter that regularly carries a pillion, the Rizta Z. For a single rider on a budget who values space over gadgets, the Rizta S. Either way, consider the frunk — it turns 34 litres into 56.
"""),
],
"faqs": [
("What is the difference between Rizta Z and Rizta S?", "They share the body, motor, seat and storage. The Rizta Z adds a touchscreen with Google Maps and a multi-language dashboard, SkidControl, Crash Alert, Magic Twist, Voice on Ather, a premium seat and more colour options."),
("Does the Rizta S have SkidControl?", "No. SkidControl is on the Rizta Z."),
("Do both Riztas have the same range?", "Yes, range depends on the battery rather than the variant: 123 km IDC on the smaller packs and 161 km on the 3.5 kWh."),
],
"related": ["ather-rizta-family-guide", "skidcontrol-explained", "ather-rizta-battery-options"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-konarc-vs-rizta-s",
"cluster": "compare",
"title": "Ather Konarc vs Rizta S: Value Family Scooters Compared",
"desc": "Ather Konarc vs Rizta S: price, seat, storage, wheels, top speed, charging and servicing compared — which budget Ather suits your household?",
"h1": "Ather Konarc vs Rizta S",
"lede": "These are the two most affordable Athers, and both are aimed at everyday practicality rather than speed. The Konarc is the tougher, simpler one; the Rizta S is the roomier one. Here is how to choose.",
"img": M + "1-Celestial-Gold-desk.webp",
"img_alt": "Ather Konarc",
"models": ["ather-konarc", "ather-rizta-s"],
"facts": [("Konarc from", "₹99,999 introductory"), ("Rizta S from", "₹1,21,999"), ("Bigger boot", "Rizta S, 34 L"), ("Bigger front wheel", "Konarc, 14 inch")],
"body": [
("Head to head", """
| | Konarc S | Rizta S |
|---|---|---|
| Ex-showroom from | ₹99,999 (introductory) | ₹1,21,999 |
| Battery | 2.1 / 2.7 / 3.5 kWh | 2.7 / 2.9 / 3.5 kWh |
| TrueRange | 80 / 100 / 130 km | 100 / 125 km |
| Top speed | 70 km/h | 80 km/h |
| Boot | 31 L | 34 L (+22 L frunk accessory) |
| Front wheel | 14 inch | 12 inch |
| Ground clearance | 16 cm | 15 cm |
| Body | Metal, steel unibody chassis | Plastic panels |
| Drive | Silent Gear Drive | Belt |
| Fastest home charge (0–80%) | 2 hr (combined charger) | 3 hr 25 min (900 W) |
| Kerb weight | 126.5–129 kg | 125 kg |
"""),
("The Konarc's case", """
It is cheaper to buy, simpler to look after (one service a year, no belt) and rides rough roads better thanks to its 14-inch front wheel and long-travel suspension. The combined charger gives the fastest home charging in the Ather range. For a single rider on mixed roads, it is excellent value.
"""),
("The Rizta S's case", """
The Rizta was designed around two people. Its seat is longer, the pillion gets a backrest as standard, and with the frunk you have 56 litres of storage against the Konarc's 31. It is also 10 km/h faster, which matters on the bypass. If someone rides pillion most days, the Rizta S is worth the extra.
"""),
("Quick verdict", """
- **Mostly solo, rough roads, tight budget:** Konarc S.
- **Regular pillion or lots of luggage:** Rizta S.
- **Both, and budget allows:** look at the [Rizta Z](/scooters/ather-rizta-z.html) for SkidControl and Crash Alert.
"""),
],
"faqs": [
("Is the Konarc cheaper than the Rizta S?", "Yes. The Konarc S starts at an introductory ₹99,999 ex-showroom; the Rizta S starts at ₹1,21,999."),
("Which has more storage, Konarc or Rizta?", "The Rizta: a 34 L boot plus the 22 L frunk accessory, against the Konarc's 31 L boot."),
("Which is better on bad roads?", "The Konarc, thanks to its 14-inch front wheel, 90 mm / 100 mm suspension travel and 16 cm ground clearance."),
],
"related": ["ather-konarc-buyers-guide", "ather-rizta-family-guide", "which-ather-scooter-should-i-buy"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450-apex-vs-450x",
"cluster": "compare",
"title": "Ather 450 Apex vs 450X: Is the Apex Worth the Extra?",
"desc": "Ather 450 Apex vs 450X compared: 7 kW vs 6.4 kW, 100 vs 90 km/h, Warp+ vs Warp, range and AtherStack Pro — and who should pay for the Apex.",
"h1": "Ather 450 Apex vs 450X",
"lede": "The 450 Apex is a 450X turned up: more power, a higher top speed, Warp+ and AtherStack Pro included. The question is not which is better — it is whether you will use the difference.",
"img": M + "450xahr-indium-blue-electric-scooter.webp",
"img_alt": "Ather 450 Apex in Indium Blue",
"models": ["ather-450-apex", "ather-450x"],
"facts": [("Apex", "7 kW · 100 km/h · 2.9 s"), ("450X", "6.4 kW · 90 km/h · 3.3 s"), ("Shared", "Chassis, brakes, touchscreen, Infinite Cruise")],
"body": [
("The differences, all of them", """
| | 450 Apex | 450X |
|---|---|---|
| Peak power | 7 kW | 6.4 kW |
| Torque | 26 Nm | 26 Nm |
| Top speed | 100 km/h | 90 km/h |
| 0–40 km/h | 2.9 s | 3.3 s |
| Fastest mode | Warp+ | Warp |
| Battery | 3.5 kWh only | 2.9 / 3.5 kWh |
| IDC range | 165 km | 126 / 161 km |
| AtherStack Pro | Included | Optional |
| Colour | Indium Blue | 7 options |
"""),
("What they share", """
The aluminium chassis, the triple-piston front disc and rear disc, the 7-inch touchscreen with Google Maps, Magic Twist, Multi-Mode Traction Control, Infinite Cruise, Pothole+ alerts and Voice on Ather. Day to day in city traffic, the two feel very similar.
"""),
("Where you feel the Apex", """
Away from a standstill in Warp+, and above 70 km/h. On a clear stretch of the ECR or the OMR in the early morning, the extra 10 km/h and 0.6 kW give the Apex a relaxed, unstrained feel. In Chennai's evening traffic you will rarely notice either.
"""),
("Do the maths on AtherStack Pro", """
AtherStack Pro is included with the Apex but optional on the 450X. If you would add it to a 450X anyway — many owners do, for the connected features and the warranty benefits — the effective gap between the two scooters narrows. Ask us for both quotes with AtherStack Pro included so you compare like with like. More in our [AtherStack Pro guide](@atherstack-pro-explained).
"""),
("Verdict", """
Buy the **Apex** if you enjoy riding fast on open roads and want the best 450 Ather makes. Buy the **450X with the 3.5 kWh battery** if your riding is mostly urban — you keep almost everything that makes the Apex good, at a lower price.
"""),
],
"faqs": [
("How much faster is the 450 Apex than the 450X?", "The Apex reaches 100 km/h against the 450X's 90 km/h, and does 0–40 km/h in 2.9 seconds against 3.3."),
("Does the 450X have Warp+?", "No. The 450X has Warp mode; Warp+ is exclusive to the 450 Apex."),
("Is the Apex's range better?", "Slightly: 165 km IDC against 161 km for the 3.5 kWh 450X. Ather's real-world TrueRange is about 130 km for both."),
],
"related": ["ather-450-apex-buyers-guide", "warp-mode-explained", "infinite-cruise-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-konarc-vs-450s",
"cluster": "compare",
"title": "Ather Konarc vs 450S: Everyday vs Sporty Ather Compared",
"desc": "Ather Konarc vs 450S compared: price, speed, brakes, weight, wheels, charging and servicing. Which suits a solo commuter in Chennai?",
"h1": "Ather Konarc vs 450S",
"lede": "Both appeal to solo riders who want an Ather without paying for the top models. They could hardly be more different in character: the Konarc is built for rough roads and low upkeep, the 450S for agility and speed.",
"img": M + "450s-cosmic-black-electric-scooter.webp",
"img_alt": "Ather 450S",
"models": ["ather-konarc", "ather-450s"],
"facts": [("Konarc from", "₹99,999 introductory"), ("450S from", "₹1,35,999"), ("Top speed", "70 vs 90 km/h"), ("Weight", "126.5–129 vs 108–111.6 kg")],
"body": [
("How they compare", """
| | Konarc S (2.7 / 3.5 kWh) | 450S |
|---|---|---|
| Ex-showroom from | ₹99,999 (2.1 kWh, introductory) | ₹1,35,999 |
| Peak power / torque | 4.7 kW / 16 Nm | 5.4 kW / 22 Nm |
| Top speed | 70 km/h | 90 km/h |
| 0–40 km/h | 4.7 s | 3.9 s |
| Brakes | 220 mm disc front, drum rear | Disc front and rear |
| Front wheel | 14 inch | 12 inch |
| Suspension travel | 90 mm / 100 mm | Telescopic fork / monoshock |
| Boot | 31 L | 22 L |
| Kerb weight | 126.5–129 kg | 108–111.6 kg |
| Service interval | 1 year | Every 5,000 km or 6 months |
"""),
("Pick the Konarc if…", """
- Your roads are rough, and comfort matters more than pace.
- You want the lowest running and service costs — one visit a year.
- You need more boot space for a helmet and a bag.
- Your budget is firmly around ₹1 lakh.
"""),
("Pick the 450S if…", """
- You ride faster roads where 80–90 km/h is normal.
- You want the 450's light, sharp handling and rear disc brake.
- You often filter through traffic or park in tight spots, where 18 kg less weight is noticeable.
"""),
("A note on servicing", """
Ather's guidance for belt-driven scooters like the 450 is an inspection every 5,000 km or 6 months; the Konarc's sealed gearbox is quoted at once a year. Our [service guide](@ather-service-schedule-and-costs) has the detail and typical parts prices.
"""),
("Running costs side by side", """
Energy costs are almost identical with the same battery — around 24 paise per km on home electricity at ₹8 a unit. The difference is upkeep. The 450S follows the 5,000 km / 6-month inspection schedule and its drive belt is due for replacement at 50,000 km; the Konarc's sealed gearbox means one service a year and no belt. Over five years of heavy use, that gap adds up in both money and time spent at the service centre.
"""),
],
"faqs": [
("Which is faster, the Konarc or 450S?", "The 450S: 90 km/h top speed and 0–40 km/h in 3.9 seconds, against the Konarc's 70 km/h and 4.7–5.0 seconds."),
("Which is cheaper to maintain?", "The Konarc. Its sealed Silent Gear Drive means a once-a-year service interval and no drive belt to replace."),
("Which has a bigger boot?", "The Konarc, with 31 L against the 450S's 22 L."),
],
"related": ["ather-konarc-buyers-guide", "ather-450s-buyers-guide", "ather-service-schedule-and-costs"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450s-vs-rizta-s",
"cluster": "compare",
"title": "Ather 450S vs Rizta S: Sporty or Practical at the Same Budget?",
"desc": "Ather 450S vs Rizta S: speed, handling, brakes, seat, storage and price compared — the classic choice between a sporty and a practical Ather.",
"h1": "Ather 450S vs Rizta S",
"lede": "At similar money, the 450S and Rizta S are the classic Ather choice between head and heart: the 450S is the one that is fun to ride, the Rizta S is the one that fits your life. Here is how to tell which matters more to you.",
"img": M + "rizs1-pangong-blue-mono-electric-scooter.webp",
"img_alt": "Ather Rizta S",
"models": ["ather-450s", "ather-rizta-s"],
"facts": [("450S from", "₹1,35,999"), ("Rizta S from", "₹1,21,999"), ("Faster", "450S, 90 km/h"), ("Roomier", "Rizta S, 34 L + frunk")],
"body": [
("Compared", """
| | 450S | Rizta S |
|---|---|---|
| Ex-showroom from | ₹1,35,999 | ₹1,21,999 |
| Peak power / torque | 5.4 kW / 22 Nm | 4.3 kW / 22 Nm |
| Top speed | 90 km/h | 80 km/h |
| 0–40 km/h | 3.9 s | 4.7 s |
| Rear brake | Disc | Drum |
| Seat | Sporty, shorter | Long, flat, pillion backrest |
| Storage | 22 L | 34 L (+22 L frunk) |
| Kerb weight | 108–111.6 kg | 125 kg |
| Dashboard | 7-inch DeepView | 7-inch DeepView |
| IDC range (3.5 kWh) | 161 km | 161 km |
"""),
("How they feel", """
The 450S is light, low and eager. It changes direction quickly, its rear disc brake gives more confidence when braking hard, and it pulls harder above 50 km/h. The Rizta S feels calmer and more upright, and its long seat and flat floor make it easier to live with for errands and passengers.
"""),
("The deciding question", """
Does someone ride pillion more than twice a week, or do you regularly carry shopping? If yes, the Rizta S — the 450S's seat and 22-litre boot will annoy you. If no, and you enjoy the ride itself, the 450S is the more rewarding scooter.
"""),
("Price check", """
At ex-showroom prices the Rizta S is around ₹14,000 cheaper. Both share the same 7-inch DeepView display, the same battery choices and the same warranty terms, so the money is mostly buying the 450S's performance and brakes.
"""),
],
"faqs": [
("Is the 450S or Rizta S better for two riders?", "The Rizta S. Its long seat and standard pillion backrest are designed for two; the 450S's seat is sportier and shorter."),
("Which has better brakes?", "The 450S uses discs front and rear. The Rizta S has a front disc and rear drum with combined braking."),
("Do they have the same range?", "Yes, with the same battery. Both are rated at 161 km IDC with the 3.5 kWh pack."),
],
"related": ["ather-450s-buyers-guide", "ather-rizta-family-guide", "ather-450x-vs-rizta-z"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450x-vs-rizta-z",
"cluster": "compare",
"title": "Ather 450X vs Rizta Z: Which Flagship Fits Your Life?",
"desc": "Ather 450X vs Rizta Z: the top performance and top family Ather compared on speed, comfort, storage, safety tech, charging and price.",
"h1": "Ather 450X vs Rizta Z",
"lede": "Both are fully loaded: touchscreen, Google Maps, Magic Twist and the 30-km-in-10-minutes fast-charge rate with the bigger battery. One is built for speed, the other for space. Choosing comes down to who else rides with you.",
"img": M + "450x-hyper-sand-electric-scooter.webp",
"img_alt": "Ather 450X in Hyper Sand",
"models": ["ather-450x", "ather-rizta-z"],
"facts": [("450X from", "₹1,48,998"), ("Rizta Z from", "₹1,36,999"), ("Shared", "Touchscreen, Maps, Magic Twist"),
          ("450X only", "Warp, traction control, Infinite Cruise"), ("Rizta Z only", "SkidControl, Crash Alert, Tamil dash")],
"body": [
("Side by side", """
| | 450X | Rizta Z |
|---|---|---|
| Ex-showroom from | ₹1,48,998 | ₹1,36,999 |
| Peak power / torque | 6.4 kW / 26 Nm | 4.3 kW / 22 Nm |
| Top speed | 90 km/h | 80 km/h |
| 0–40 km/h | 3.3 s | 4.7 s |
| Storage | 22 L | 34 L (+22 L frunk) |
| Kerb weight | 108–111.6 kg | 125 kg |
| Rear brake | Disc | Drum |
| Rider aids | Multi-Mode Traction Control, Infinite Cruise | SkidControl, Crash Alert |
| Dashboard languages | English | Tamil, Hindi, Malayalam, Kannada |
| Ather Grid, 10 min (3.5 kWh) | up to 30 km | up to 30 km |
"""),
("The 450X is for you if…", """
You ride alone most of the time, enjoy acceleration, and spend time on faster roads. Warp mode, the rear disc and Infinite Cruise make it the better scooter for a long solo commute along the OMR or GST Road.
"""),
("The Rizta Z is for you if…", """
The scooter carries a family member most days, or you want a Tamil-language dashboard. SkidControl and Crash Alert are the two features we would most want on a scooter carrying people we love, and the extra storage removes the need for a backpack.
"""),
("Some households buy both", """
It is common for a household to have a 450X for the daily commuter and a Rizta for everything else. Both use the same Ather app, the same chargers and the same service centre — and we can usually offer a better deal on the pair.
"""),
],
"faqs": [
("Is the 450X or Rizta Z better for a family?", "The Rizta Z — longer seat, pillion backrest, 56 L of storage with the frunk, SkidControl and Crash Alert."),
("Do both have Google Maps on the dashboard?", "Yes, both have the 7-inch touchscreen with Google Maps."),
("Which charges faster?", "With the 3.5 kWh battery, both take up to 30 km of range in ten minutes at an Ather Grid fast charger, and both charge 0–80% at home in about 3 hours 25 minutes on the 900 W charger."),
],
"related": ["ather-450s-vs-rizta-s", "ather-rizta-z-vs-rizta-s", "which-ather-scooter-should-i-buy"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-konarc-vs-450x",
"cluster": "compare",
"title": "Ather Konarc vs 450X: Should You Save or Spend?",
"desc": "Ather Konarc vs 450X compared on price, performance, smart features, comfort and running costs — when the cheaper Konarc is enough, and when it is not.",
"h1": "Ather Konarc vs 450X",
"lede": "The Konarc starts about ₹49,000 below the 450X at ex-showroom prices. That is a big gap, and for many riders the Konarc does everything they need. For others, the 450X's speed and technology are the point. Here is where the line falls.",
"img": M + "konarc-gallery-t-desk-2.webp",
"img_alt": "Ather Konarc on the road",
"models": ["ather-konarc", "ather-450x"],
"facts": [("Price gap", "≈ ₹49,000 ex-showroom"), ("Konarc strength", "Comfort, toughness, low upkeep"), ("450X strength", "Speed, Maps, rider aids")],
"body": [
("The big differences", """
| | Konarc S (3.5 kWh) | 450X (3.5 kWh) |
|---|---|---|
| Peak power | 4.7 kW | 6.4 kW |
| Top speed | 70 km/h | 90 km/h |
| 0–40 km/h | 4.7 s | 3.3 s |
| TrueRange | 130 km | 130 km |
| Dashboard | 7-inch DeepView | 7-inch touchscreen, Google Maps |
| Rider aids | AutoHold, FallSafe, Reverse Park Assist | Plus Warp, traction control, Magic Twist, Infinite Cruise |
| Ather Grid, 10 min | up to 15 km | up to 30 km |
| Boot | 31 L | 22 L |
| Service interval | 1 year | Every 5,000 km or 6 months |
"""),
("What the extra money buys", """
Mostly performance and technology: 20 km/h more top speed, much quicker acceleration, a touchscreen with Google Maps, traction control for wet roads, Infinite Cruise for traffic, and fast charging at twice the rate. If you value those every day, the 450X is worth it.
"""),
("What you keep by saving", """
The same real-world range with the 3.5 kWh battery, a bigger boot, a more comfortable ride on bad roads, and lower maintenance. For a commute that never goes above 60 km/h, the Konarc gives up surprisingly little.
"""),
("A simple test", """
Look at your daily route. If more than a quarter of it is open road where traffic moves above 60 km/h, test ride the 450X. If it is mostly city streets and service roads, the Konarc will serve you well and the savings can go towards the extended battery warranty and a good helmet.
"""),
],
"faqs": [
("How much cheaper is the Konarc than the 450X?", "At ex-showroom prices, the Konarc S starts at an introductory ₹99,999 and the 450X at ₹1,48,998 — a gap of about ₹49,000 at the entry level."),
("Do the Konarc and 450X have the same range?", "With the 3.5 kWh battery, both have a TrueRange estimate of about 130 km."),
("Does the Konarc have Google Maps?", "Not on the Konarc S. Ather lists Google Maps for the upcoming Konarc Z."),
],
"related": ["ather-konarc-vs-450s", "ather-konarc-variants-explained", "ather-450x-vs-450s"],
},
]
