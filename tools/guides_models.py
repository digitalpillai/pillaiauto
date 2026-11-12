#!/usr/bin/env python3
"""
guides_models.py  —  Version: V1  (12 Nov 2026)
"Choosing your Ather" guides. Facts from Ather's published specification
sheets (Nov 2026); copy is Pillai Auto's own. Markup: see build_guides.py.
"""
M = "https://media.atherenergy.com/"

GUIDES = [
# ---------------------------------------------------------------------------
{
"slug": "which-ather-scooter-should-i-buy",
"cluster": "models",
"title": "Which Ather Scooter Should I Buy? 2026 Guide | Pillai Auto",
"desc": "Konarc, 450S, 450X, 450 Apex, Rizta S or Rizta Z? A plain-English way to pick the right Ather for your commute, family and budget in Chennai.",
"h1": "Which Ather scooter should I buy?",
"lede": "Ather now sells six scooters across three families. Most buyers who walk into our OMR showroom already know which one they want — and about a third leave with a different one. Here is the shortcut we use at the counter.",
"img": M + "Easy-on-ather-desktop.webp",
"models": ["ather-konarc", "ather-450x", "ather-rizta-z", "ather-450s", "ather-rizta-s", "ather-450-apex"],
"facts": [("Lowest price", "₹99,999 · Konarc S (introductory)"), ("Fastest", "450 Apex · 100 km/h"),
          ("Most storage", "Rizta · 56 L with frunk"), ("Longest IDC range", "Konarc · up to 200 km")],
"body": [
("Start with three questions", """
Forget the spec sheet for a minute. Three answers narrow six scooters down to one or two:

1. **Who rides pillion, and how often?** If someone is on the back most days — a child, a parent, a spouse — start with the Rizta.
2. **How much of your ride is open road?** If you regularly use the OMR, ECR or GST Road at speed, the 450 series' 90–100 km/h and stronger brakes matter.
3. **What is the budget, all in?** The Konarc starts under a lakh; a fully loaded 450 Apex is roughly double that.
"""),
("The three families in one paragraph each", """
**Konarc — the everyday one.** Ather's newest scooter, on the EL platform: metal body, steel unibody chassis, a 14-inch front wheel, 31 litres of boot and a 70 km/h top speed. It is the most forgiving on broken roads and the cheapest to own. See [the Konarc page](/scooters/ather-konarc.html).

**450 — the quick one.** The 450S, 450X and 450 Apex share a light aluminium chassis, dual disc brakes and a low, sporty stance. They are the scooters to pick if you enjoy riding, not just arriving.

**Rizta — the family one.** A long, flat seat with a pillion backrest, a 34-litre boot plus an optional 22-litre frunk, and SkidControl on the Rizta Z. Calm, roomy and very easy to live with.
"""),
("Our quick matches", """
| If you are… | Look at | Why |
|---|---|---|
| A first-time EV buyer on a budget | [Konarc S](/scooters/ather-konarc.html) | Under ₹1 lakh introductory, 1-year service interval |
| A solo commuter who likes to ride | [450X](/scooters/ather-450x.html) | Warp mode, Google Maps, Infinite Cruise |
| A 450 fan watching the budget | [450S](/scooters/ather-450s.html) | Same chassis and brakes for ₹13,000 less than the 450X |
| An enthusiast | [450 Apex](/scooters/ather-450-apex.html) | 100 km/h, 0–40 km/h in 2.9 s |
| A family with a regular pillion | [Rizta Z](/scooters/ather-rizta-z.html) | Space, SkidControl, touchscreen |
| A family on a budget | [Rizta S](/scooters/ather-rizta-s.html) | Same body and storage from ₹1,21,999 |
"""),
("Then pick the battery", """
Every family offers more than one battery. The bigger pack costs more, but it also charges faster at home on the 900 W charger and, on the 450X and Rizta Z, adds up to 30 km in ten minutes at an Ather Grid fast charger instead of 15. If your daily round trip is under 50 km and you charge at home, the smaller pack is usually enough. Our guides to the [450 batteries](@ather-450-battery-2-9-vs-3-5-kwh), [Rizta batteries](@ather-rizta-battery-options) and [Konarc variants](@ather-konarc-variants-explained) go through the numbers.
"""),
("Then ride two back to back", """
Spec sheets do not tell you how the seat feels after forty minutes, or whether your feet reach the ground comfortably. At any of our four showrooms we will happily line up two scooters so you can ride one straight after the other. That ten-minute comparison settles more decisions than any table.
"""),
],
"faqs": [
("What is the cheapest Ather scooter in 2026?", "The Ather Konarc S, at an introductory ex-showroom price of ₹99,999 for the 2.1 kWh variant. Among the established models, the Rizta S starts at ₹1,21,999 ex-showroom."),
("Which Ather has the longest range?", "Ather lists the Konarc at up to 200 km IDC on its top battery. Among the 450s, the 450 Apex has the highest IDC figure at 165 km. In real riding, Ather's TrueRange estimate for the 3.5 kWh packs is about 125–130 km."),
("Which Ather is best for two people?", "The Rizta. Its long, flat seat and standard pillion backrest are designed around a second rider, and its 56 L of total storage (with the frunk) handles the shopping as well."),
],
"related": ["ather-konarc-vs-rizta-s", "ather-450x-vs-450s", "ather-rizta-z-vs-rizta-s"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-konarc-variants-explained",
"cluster": "models",
"title": "Ather Konarc Variants Explained: 2.1 vs 2.7 vs 3.5 kWh",
"desc": "Konarc S comes with three batteries. Here is what changes between 2.1, 2.7 and 3.5 kWh — range, brakes, dashboard, charging — and what the Konarc Z adds.",
"h1": "Ather Konarc variants explained",
"lede": "The Konarc S comes with three battery sizes, and the differences go beyond range. The smallest pack also changes the brakes, the dashboard and some of the smart features — worth knowing before you settle on the ₹99,999 headline price.",
"img": M + "PDPKVDesktop.webp",
"models": ["ather-konarc"],
"facts": [("Batteries", "2.1 / 2.7 / 3.5 kWh"), ("IDC range", "100 / 125 / 161 km"), ("TrueRange", "80 / 100 / 130 km"),
          ("Top speed", "70 km/h"), ("Boot", "31 L, all variants")],
"body": [
("The three Konarc S batteries side by side", """
| | 2.1 kWh | 2.7 kWh | 3.5 kWh |
|---|---|---|---|
| IDC range | 100 km | 125 km | 161 km |
| TrueRange (real-world) | 80 km | 100 km | 130 km |
| Peak power | 4.0 kW | 4.7 kW | 4.7 kW |
| 0–40 km/h | 5.0 s | 4.7 s | 4.7 s |
| Front brake | 130 mm drum | 220 mm disc | 220 mm disc |
| Dashboard | 4.2-inch DeepView | 7-inch DeepView | 7-inch DeepView |
| Home charge 0–80% (combined charger) | 2 hr | 2 hr 25 min | 3 hr 10 min |
| Combined charger | Add-on | Add-on | Included |
| Ather Grid fast charging | Add-on | Yes | Yes |

Ather also lists a Konarc S battery with up to 200 km IDC range; ask us for its availability and price at your showroom.
"""),
("What you give up on the 2.1 kWh", """
The entry Konarc is a genuine Ather, but it is built to a price. Three things change besides range:

- **A drum front brake** instead of the 220 mm disc. Fine for town speeds; if you ride the OMR or GST Road at 60–70 km/h every day, we would spend the extra on a disc.
- **A smaller 4.2-inch screen** and fewer connected features. Over-the-air updates, Theft & Tow alerts, Find My Scooter, FallSafe and AirWalk come with the 2.7 and 3.5 kWh variants.
- **Ather Grid access is an add-on**, and its fast-charge rate is lower (up to 13 km in ten minutes rather than 15).
"""),
("Which one we recommend", """
**2.1 kWh** suits short, predictable trips — under 35 km a day, charged every night, mostly within the city. It is the lowest price of entry into an Ather.

**2.7 kWh** is the sweet spot for most commuters. You get the disc brake, the 7-inch screen and the full smart-feature set, and 100 km of real-world range covers most of a week of school runs.

**3.5 kWh** is for longer daily distances — Chengalpattu to Guindy, say, or Chidambaram to Neyveli and back. It is the only variant with the faster combined charger in the box.
"""),
("What the Konarc Z adds", """
Ather has listed a Konarc Z as coming soon, with an 80 km/h top speed, a TFT touchscreen with Google Maps, AeBS braking assistance and MagicKey. It had not been priced when this guide was written. If you are waiting for those features, tell us and we will call you the day it is announced.
"""),
],
"faqs": [
("Is the ₹99,999 Konarc price on-road?", "No. ₹99,999 is Ather's introductory ex-showroom price for the base Konarc S. Insurance, registration and handling are added on top; road tax on EVs is currently exempt in Tamil Nadu. We will give you the on-road figure for your showroom."),
("Can I add fast charging to the 2.1 kWh Konarc later?", "Ather lists Ather Grid access as an add-on for the 2.1 kWh variant. Ask us about adding it when you buy — it is simplest to sort out at the start."),
("Do all Konarc variants have the same boot?", "Yes. All three Konarc S batteries keep the same 31-litre boot."),
],
"related": ["ather-konarc-buyers-guide", "ather-konarc-vs-rizta-s", "ather-konarc-vs-450x"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-konarc-buyers-guide",
"cluster": "models",
"title": "Ather Konarc Buyer's Guide: Is It Right for You?",
"desc": "Metal body, 14-inch front wheel, once-a-year service. Who the new Ather Konarc suits, who should look elsewhere, and what to check on a test ride.",
"h1": "Is the Ather Konarc right for you?",
"lede": "The Konarc is Ather's answer to the most common question we hear at the counter: is there an Ather that just gets on with the job? It is built tougher and simpler than the 450 or Rizta, and priced to match. Here is who it suits — honestly.",
"img": M + "4Metalbodysteelunibodychassis.webp",
"img_alt": "Ather Konarc metal body and steel unibody chassis",
"models": ["ather-konarc"],
"facts": [("Price from", "₹99,999 introductory"), ("Front wheel", "14 inch"), ("Suspension travel", "90 mm / 100 mm"),
          ("Ground clearance", "16 cm"), ("Service interval", "1 year")],
"body": [
("What makes the Konarc different", """
Most of what sets the Konarc apart is under the panels:

- **Metal body on a steel unibody chassis.** Scrapes in a tight parking lot or a nudge in traffic are less of a worry than with plastic panels.
- **A 14-inch front wheel** with 90 mm of front and 100 mm of rear suspension travel. Bigger wheels roll over potholes and broken patches more easily — noticeable on interior Chengalpattu or Cuddalore district roads.
- **Silent Gear Drive.** A sealed gearbox replaces the belt used on the 450 and Rizta, which is why Ather can quote a once-a-year service interval.
- **Two-hour home charging** with the combined charger on the 2.1 kWh variant (0–80%).
"""),
("Who the Konarc suits", """
- Riders stepping off a 110 cc petrol scooter who want lower running costs without learning anything new.
- Anyone whose daily roads are rough — village roads, service lanes, construction zones.
- Buyers who want the lowest possible upkeep: one service a year and no belt to replace.
- Households adding a second scooter for errands and short trips.
"""),
("Who should look at something else", """
- **If you ride fast on open roads every day**, the Konarc's 70 km/h top speed will feel limiting. The [450S](/scooters/ather-450s.html) or [450X](/scooters/ather-450x.html) are happier at 80.
- **If you always carry a pillion and luggage**, the [Rizta](/scooters/ather-rizta-z.html) has the bigger seat and up to 56 L of storage.
- **If you want navigation on the dashboard today**, that arrives with the Konarc Z, which Ather lists as coming soon.
"""),
("What to check on your test ride", """
Ask for a 2.7 or 3.5 kWh Konarc so you try the disc brake and the 7-inch display. Ride it over the worst stretch near the showroom — we will point you to one — and notice how the 14-inch wheel handles it. Try AutoHold at a stop, and Reverse Park Assist when you bring it back. Then sit on it with your usual pillion for a minute; the seat is shorter than the Rizta's.
"""),
],
"faqs": [
("Is the Konarc slower than the 450?", "Yes, by design. The Konarc tops out at 70 km/h and reaches 40 km/h in 4.7–5.0 seconds. The 450X reaches 90 km/h and does 0–40 km/h in 3.3 seconds."),
("Why does the Konarc only need servicing once a year?", "Its sealed Silent Gear Drive replaces the drive belt, removing one of the main items checked and adjusted at each service on belt-driven scooters."),
("Is the Konarc's metal body heavier?", "The Konarc S weighs 126.5–129 kg at the kerb depending on battery, compared with 108–111.6 kg for the 450 series and 125 kg for the Rizta."),
],
"related": ["ather-konarc-variants-explained", "ather-konarc-vs-450s", "autohold-and-reverse-park-assist-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450-battery-2-9-vs-3-5-kwh",
"cluster": "models",
"title": "Ather 450 Battery: 2.9 kWh vs 3.5 kWh — Which to Buy",
"desc": "The 450S and 450X come with 2.9 or 3.5 kWh batteries. Real-world range, charging time and fast-charge speed compared, with advice for Chennai commutes.",
"h1": "Ather 450: 2.9 kWh or 3.5 kWh battery?",
"lede": "Both the 450S and 450X are sold with a 2.9 kWh or a 3.5 kWh battery. The bigger pack is not just about range — on the 450X it also doubles the fast-charge rate. Here is how to decide.",
"img": M + "450-charging-d.webp",
"models": ["ather-450x", "ather-450s"],
"facts": [("2.9 kWh TrueRange", "105 km"), ("3.5 kWh TrueRange", "130 km"), ("2.9 kWh 0–80% at home", "5 hr 10 min (450 W)"),
          ("3.5 kWh 0–80% at home", "3 hr 25 min (900 W)")],
"body": [
("The numbers", """
| | 2.9 kWh | 3.5 kWh |
|---|---|---|
| IDC range (450X) | 126 km | 161 km |
| IDC range (450S) | 122 km | 161 km |
| TrueRange (real-world) | 105 km | 130 km |
| Home charger | 450 W | 900 W |
| Home charging 0–80% | 5 hr 10 min | 3 hr 25 min |
| Home charging 0–100% | 6 hr 30 min | 4 hr 30 min |
| Ather Grid, 10 minutes (450X) | up to 15 km | up to 30 km |
| Ather Grid, 10 minutes (450S) | up to 15 km | up to 15 km |
| Kerb weight | 108 kg | 111.6 kg |

The 450 Apex is sold only with the 3.5 kWh battery.
"""),
("When 2.9 kWh is enough", """
TrueRange is Ather's own estimate for mixed real riding, and 105 km covers a lot. If your round trip is under 50 km — Velachery to Perungudi and back, say, or around Puducherry town — and you can charge at home overnight, the 2.9 kWh pack will rarely run low. It is also 3.6 kg lighter, which you notice when manoeuvring in a tight parking spot.
"""),
("When the 3.5 kWh pays for itself", """
- **Long daily commutes.** Chengalpattu to Chennai, or Siruseri to the city centre, eats into a 2.9 kWh pack quickly once you use Sport mode.
- **No overnight charging.** If you charge at work or rely on fast chargers, the 900 W home charger and (on the 450X) the 30-km-in-10-minutes Grid rate save real time.
- **Weekend trips.** A run down the ECR towards Mahabalipuram or Puducherry is far more relaxed with 130 km of real-world range. Our [ECR trip guide](@chennai-to-puducherry-ecr-on-an-ather) has the details.
- **Resale.** Buyers of used scooters look for the bigger battery.
"""),
("Our advice", """
If you are unsure, add up your longest regular day — not your average one — and double it. If that is over about 80 km, take the 3.5 kWh. Otherwise the 2.9 kWh saves money you can put towards the extended battery warranty or accessories. See our [cost-per-km guide](@ather-charging-cost-per-km) for what each kilometre costs.
"""),
],
"faqs": [
("Can I upgrade from 2.9 kWh to 3.5 kWh later?", "Batteries are not sold as an upgrade for an existing scooter. Choose at purchase — it is the one decision you cannot easily change."),
("Does the bigger battery make the 450X faster?", "Peak power and top speed are the same on both packs. The difference is range, charging time and, on the 450X, fast-charge speed."),
("Do both batteries have the same warranty?", "Yes: 3 years or 30,000 km as standard, extendable up to 10 years or 1,00,000 km with Ather's extended battery warranty."),
],
"related": ["ather-450x-vs-450s", "truerange-vs-idc-range", "ather-grid-fast-charging-guide"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-rizta-battery-options",
"cluster": "models",
"title": "Ather Rizta Battery Options: Range and Charging Compared",
"desc": "Rizta S and Rizta Z come with 2.7, 2.9 or 3.5 kWh batteries. Range, charging time and fast charging compared, and which suits a family.",
"h1": "Which Rizta battery should you choose?",
"lede": "The Rizta is the scooter families keep for years, which makes the battery choice more important than on a commuter. Here is what each pack gives you, and the questions we ask families before recommending one.",
"img": M + "Desk-charge-your-way.webp",
"models": ["ather-rizta-z", "ather-rizta-s"],
"facts": [("Battery choices", "2.7 / 2.9 / 3.5 kWh"), ("IDC range", "123 km / 161 km"), ("TrueRange", "100 km / 125 km"),
          ("Fastest home charge", "4 hr 30 min to 100% (900 W)")],
"body": [
("What changes between the packs", """
| | Smaller packs (2.7 / 2.9 kWh) | 3.5 kWh |
|---|---|---|
| IDC range | 123 km | 161 km |
| TrueRange (real-world) | 100 km | 125 km |
| Home charger | 450 W | 900 W |
| Home charging 0–80% | 6 hr | 3 hr 25 min |
| Home charging 0–100% | 7 hr 25 min | 4 hr 30 min |
| Ather Grid, 10 minutes (Rizta Z) | up to 15 km | up to 30 km |
| Ather Grid, 10 minutes (Rizta S) | up to 15 km | up to 15 km |

Exact battery availability varies by variant and month — ask us which packs are in stock at your showroom.
"""),
("Range with a pillion", """
TrueRange assumes typical mixed riding. Two adults, a full boot and a lot of stop-start traffic all use more energy, so plan on a little less than the headline when the Rizta is doing family duty. In practice, families on the smaller pack who charge every night almost never run short in town; the 3.5 kWh is about having slack for the unplanned trip to the hospital or the relative's house across the city.
"""),
("Questions we ask families", """
1. **Who else will ride it?** A teenager or a second adult using it during the day means less time on the charger.
2. **Where will it charge?** A ground-floor house with a socket by the gate is easy. An apartment basement may mean charging less often — see our [apartment charging guide](@charging-ather-at-home-in-a-chennai-apartment).
3. **How far are the regular trips?** School, work, parents' home, temple, market — add up the longest regular day.

If two of those answers point to "a lot", choose the 3.5 kWh.
"""),
("Rizta S or Rizta Z with the bigger battery?", """
Only the Rizta Z gets the 30-km-in-10-minutes Ather Grid rate with the 3.5 kWh pack, along with the touchscreen, Google Maps and SkidControl. If you are paying for the bigger battery because you ride further, the Z's extras tend to be worth it too. Our [Rizta Z vs Rizta S comparison](@ather-rizta-z-vs-rizta-s) covers the rest.
"""),
],
"faqs": [
("How long does a Rizta take to charge at home?", "On the 450 W charger, 0–80% takes about 6 hours and 0–100% about 7 hours 25 minutes. With the 3.5 kWh battery and 900 W charger, it is 3 hours 25 minutes to 80% and 4 hours 30 minutes to full."),
("Does battery size change the Rizta's storage?", "No. Every Rizta keeps the 34 L boot, and the 22 L frunk accessory fits all variants."),
("Which Rizta battery has the best resale?", "Used-scooter buyers look for range, so the 3.5 kWh pack tends to be easier to sell on. Warranty history and service records matter just as much."),
],
"related": ["ather-rizta-family-guide", "ather-rizta-z-vs-rizta-s", "charging-ather-at-home-in-a-chennai-apartment"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-rizta-family-guide",
"cluster": "models",
"title": "Ather Rizta for Families: Seat, Storage and Safety Guide",
"desc": "Why families pick the Ather Rizta: the long seat and backrest, 56 L of storage, SkidControl and Crash Alert. What fits, who fits, and what to check.",
"h1": "The Ather Rizta as a family scooter",
"lede": "Ather says more than 4,00,000 families ride a Rizta, and at our showrooms it is the scooter most often bought by a household rather than a person. Here is what makes it work as a family scooter — and its limits.",
"img": M + "Ather-Rizta-family-electric-scooter.webp",
"img_alt": "A family with the Ather Rizta",
"models": ["ather-rizta-z", "ather-rizta-s"],
"facts": [("Boot", "34 L"), ("With frunk", "56 L total"), ("Seat height", "78 cm"), ("Kerb weight", "125 kg"),
          ("Top speed", "80 km/h")],
"body": [
("Seat and floorboard", """
The Rizta's seat is long and flat, with a standard pillion backrest, so a second adult sits comfortably rather than perched. The floorboard is wide and flat too — handy for a bag of vegetables or a child's school bag between your feet. Seat height is 78 cm; most riders of average height can put both feet down, but bring the person who will ride it most to the test ride and check.
"""),
("What 56 litres actually holds", """
The 34-litre boot takes a full-face helmet with room to spare, or a week's groceries. Add the 22-litre frunk accessory at the front and you have 56 litres in total — enough for a second helmet or a laptop bag in front of your knees. If you carry a child's helmet every day, the frunk is the first accessory we suggest.
"""),
("Safety features that matter with a family", """
- **SkidControl** (Rizta Z) helps keep the scooter composed on wet, sandy or bumpy surfaces — exactly the patches you meet near the beach or after a monsoon shower.
- **Crash Alert** (Rizta Z) notifies family with your location if the scooter detects a crash, and shows their contact on the dashboard.
- **FallSafe** cuts the motor if the scooter tips over, and the **Emergency Stop Signal** flashes the brake light under hard braking.
- **AutoHold and Reverse Mode** make slopes and tight parking spots much easier with a pillion on board.
"""),
("Children as pillions", """
Every pillion needs a properly fitted helmet, whatever their age. Ather sells Junior helmets sized for children, and the Halo smart helmet for adults. A child should be able to sit with feet on the pillion footrests and hold on securely; if they cannot yet, they are too young to ride pillion. When in doubt, ask us — we will happily help size a helmet at the showroom.
"""),
("Rizta S or Rizta Z for a family?", """
Both have the same seat, storage and 80 km/h top speed. The Rizta Z adds the touchscreen with Google Maps, SkidControl, Crash Alert, Voice on Ather and a Tamil-language dashboard — features we think earn their keep when the scooter carries people you care about. The [Rizta S](/scooters/ather-rizta-s.html) is the budget choice with the same practicality. Compare them in [our Rizta Z vs S guide](@ather-rizta-z-vs-rizta-s).
"""),
],
"faqs": [
("Can two adults ride the Rizta comfortably?", "Yes. The long flat seat and standard pillion backrest were designed for two adults, and the 4.3 kW motor handles the extra load without fuss up to its 80 km/h top speed."),
("Does the Rizta have a Tamil dashboard?", "The Rizta Z's 7-inch touchscreen can be set to Tamil, Hindi, Malayalam or Kannada, and has a dark mode for night riding."),
("Is the frunk included with the Rizta?", "No, the 22-litre frunk is an accessory. Most family buyers add it at purchase."),
],
"related": ["ather-rizta-battery-options", "ather-450x-vs-rizta-z", "ather-scooter-for-senior-riders"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450-apex-buyers-guide",
"cluster": "models",
"title": "Ather 450 Apex Buyer's Guide: Is the Fastest Ather Worth It?",
"desc": "100 km/h, Warp+, 0–40 in 2.9 s and AtherStack Pro included. What the 450 Apex adds over the 450X, who it suits, and what it costs.",
"h1": "Is the Ather 450 Apex worth it?",
"lede": "The 450 Apex is India's fastest electric scooter, and the most expensive Ather. It is also a scooter that rewards a particular kind of rider. If that is you, here is what the extra money buys; if it is not, here is where to save.",
"img": M + "Ather-450-apex-electric-scooter-model.webp",
"img_alt": "Ather 450 Apex",
"models": ["ather-450-apex", "ather-450x"],
"facts": [("Top speed", "100 km/h"), ("0–40 km/h", "2.9 s (Warp+)"), ("Peak power", "7 kW"), ("IDC range", "165 km"),
          ("Battery", "3.5 kWh only")],
"body": [
("What the Apex adds over a 450X", """
| | 450 Apex | 450X (3.5 kWh) |
|---|---|---|
| Peak power | 7 kW | 6.4 kW |
| Top speed | 100 km/h | 90 km/h |
| 0–40 km/h | 2.9 s | 3.3 s |
| Top ride mode | Warp+ | Warp |
| IDC range | 165 km | 161 km |
| AtherStack Pro | Included | Optional |

Both share the aluminium chassis, triple-piston front disc, rear disc, 7-inch touchscreen with Google Maps, Magic Twist, Multi-Mode Traction Control and Infinite Cruise.
"""),
("Who the Apex is for", """
The Apex makes sense if you enjoy the ride itself: early-morning runs on the ECR, a commute that includes long fast stretches of the OMR, or simply wanting the best version of the 450. Warp+ is genuinely quicker off the line, and the extra 10 km/h of top speed adds composure when you are cruising at 70–80.
"""),
("Where the money goes", """
Part of the Apex's premium is AtherStack Pro, which is optional on the other models. AtherStack Pro unlocks the advanced connected features and is the route to Ather's longer battery warranty. If you would buy AtherStack Pro on a 450X anyway, the real gap between the two scooters is smaller than the sticker suggests — we will lay out both quotes side by side.
"""),
("When to buy a 450X instead", """
If your rides are mostly city traffic, the 450X's Warp mode already feels quick, and you will rarely use the Apex's last 10 km/h. Put the difference towards the 3.5 kWh battery, the extended battery warranty and a Halo helmet. Our [450 Apex vs 450X comparison](@ather-450-apex-vs-450x) goes deeper.
"""),
],
"faqs": [
("What is the 450 Apex's top speed?", "100 km/h, the highest of any Ather. It reaches 40 km/h in 2.9 seconds in Warp+ mode."),
("Does the 450 Apex come with AtherStack Pro?", "Yes, AtherStack Pro is included with the 450 Apex. On other models it is optional."),
("Is the Apex available with a smaller battery?", "No. The 450 Apex is sold only with the 3.5 kWh battery, rated at 165 km IDC and about 130 km TrueRange."),
],
"related": ["ather-450-apex-vs-450x", "warp-mode-explained", "atherstack-pro-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450s-buyers-guide",
"cluster": "models",
"title": "Ather 450S Buyer's Guide: What You Get and What You Skip",
"desc": "The 450S keeps the 450 chassis, dual discs and 90 km/h for less. Exactly which features it drops compared with the 450X, and who should buy it.",
"h1": "Ather 450S: what you get, and what you skip",
"lede": "The 450S is the easiest way into the 450 family, and the most misunderstood. It is not a slower, cheaper scooter in every way — it shares a lot with the 450X. The differences are specific, and whether they matter depends entirely on how you ride.",
"img": M + "Ather-450X-vs-Ather-450S-electric-scooter-model.webp",
"img_alt": "Ather 450X and Ather 450S",
"models": ["ather-450s", "ather-450x"],
"facts": [("Price from", "₹1,35,999 ex-showroom"), ("Top speed", "90 km/h"), ("Peak power", "5.4 kW"), ("Display", "7-inch DeepView (non-touch)")],
"body": [
("What the 450S shares with the 450X", """
- The same lightweight aluminium chassis and suspension.
- The same brakes: a 200 mm triple-piston front disc and 190 mm rear disc, with combined braking and regeneration.
- The same 90 km/h top speed and the same battery choices (2.9 or 3.5 kWh).
- AutoHold, FallSafe, Reverse Park Assist, Emergency Stop Signal, Theft & Tow alerts and over-the-air updates.
"""),
("What the 450S does without", """
| Feature | 450S | 450X |
|---|---|---|
| Peak power / torque | 5.4 kW / 22 Nm | 6.4 kW / 26 Nm |
| 0–40 km/h | 3.9 s | 3.3 s |
| Warp mode | No | Yes |
| Dashboard | 7-inch DeepView | 7-inch touchscreen |
| Google Maps on dash | No | Yes |
| Magic Twist | No | Yes |
| Multi-Mode Traction Control | No | Yes |
| Ather Grid with 3.5 kWh | 15 km / 10 min | 30 km / 10 min |
"""),
("Who should buy the 450S", """
Riders who want the 450's handling and brakes, mostly ride in town, and navigate with their phone. The DeepView display is high-contrast and easy to read in Chennai's midday sun. If you are cross-shopping a Rizta S and do not carry a pillion every day, the 450S feels livelier for similar money.
"""),
("When to stretch to the 450X", """
If you will miss navigation on the dashboard, ride in the rain a lot (traction control earns its keep from October to December), or use fast chargers regularly with the 3.5 kWh battery, the 450X's extras justify the gap. Our [450X vs 450S comparison](@ather-450x-vs-450s) sets out both cases.
"""),
],
"faqs": [
("Does the Ather 450S have a touchscreen?", "No. The 450S has a 7-inch DeepView display that is not touch-sensitive. The 450X and 450 Apex have touchscreens."),
("Does the 450S have Google Maps?", "No. Google Maps on the dashboard is available on the 450X, 450 Apex and Rizta Z."),
("Is the 450S slower than the 450X?", "It has the same 90 km/h top speed but less power: 5.4 kW against 6.4 kW, and 0–40 km/h in 3.9 seconds rather than 3.3."),
],
"related": ["ather-450x-vs-450s", "ather-450s-vs-rizta-s", "ather-450-battery-2-9-vs-3-5-kwh"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-450-colours-guide",
"cluster": "models",
"title": "Ather 450 Colours Guide: Overtones, Mono and Matte Finishes",
"desc": "Every Ather 450X, 450S and 450 Apex colour: the Overtones series, mono and Super Matte finishes, which cost extra, and how they look in Chennai sun.",
"h1": "Ather 450 colours: a practical guide",
"lede": "Colour is the one choice you will look at every day, and the 450 range now has more of them than ever. Here is the full list, what the finish names mean, and some practical advice from what we see coming back to our service bays.",
"img": M + "450x-overtones-still-white-d.webp",
"img_alt": "Ather 450X in Still White",
"models": ["ather-450x", "ather-450s", "ather-450-apex"],
"facts": [("450X colours", "7"), ("450S colours", "5"), ("450 Apex", "Indium Blue"), ("Premium finishes", "Some carry a ₹1,000 premium")],
"body": [
("The full colour list", """
| Colour | Finish | 450X | 450S |
|---|---|---|---|
| Cosmic Black | Mono | Yes | Yes |
| True Red | Mono | Yes | Yes |
| Space Grey | Overtones | Yes | — |
| Lunar Grey | Overtones | Yes | — |
| Still White | Overtones | Yes | Yes |
| Stealth Blue | Super Matte | Yes | Yes |
| Hyper Sand | — | Yes | Yes |

The 450 Apex comes in its own Indium Blue. Availability changes month to month; Ather notes that some colours carry a ₹1,000 premium.
"""),
("What the finish names mean", """
**Mono** is a single solid colour. **Overtones** is Ather's tone-on-tone series — graphics in a slightly different shade of the base colour, subtle from a distance and detailed up close. **Super Matte** is a flat, non-reflective finish.
"""),
("Living with each finish in Chennai", """
- **Matte finishes** look striking but need gentler cleaning: a soft cloth and plain water, no polish or wax, which leaves blotches.
- **White and light greys** hide dust well and stay cooler in direct sun; they show road grime after the monsoon more quickly.
- **Black** shows swirl marks from rough cleaning cloths. A body guard and a seat cover go a long way — see [accessories](/accessories.html).
"""),
("See them before you choose", """
Screens and photos never quite match paint. If you are deciding between two colours, call your nearest showroom first — we will tell you which are on the floor that week so you can see them in daylight.
"""),
],
"faqs": [
("Which Ather 450X colours cost extra?", "Ather notes that some 450X colours carry a ₹1,000 premium. We will confirm which ones on your quote."),
("Is the 450S available in Overtones?", "The 450S is offered in Cosmic Black, Hyper Sand, Stealth Blue, True Red and Still White. The Space Grey and Lunar Grey Overtones colours are listed for the 450X."),
("How do I clean a matte Ather?", "Use plain water, a gentle automotive shampoo if needed, and a soft microfibre cloth. Avoid polish, wax and abrasive pads, which leave shiny patches on matte paint."),
],
"related": ["ather-rizta-colours-guide", "ather-450x-vs-450s", "ather-delivery-day-checklist"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-rizta-colours-guide",
"cluster": "models",
"title": "Ather Rizta Colours: Duo, Mono and Super Matte Explained",
"desc": "All Ather Rizta Z and Rizta S colours, what Duo, Mono and Super Matte mean, which colours each variant gets, and tips for choosing a family scooter colour.",
"h1": "Ather Rizta colours explained",
"lede": "The Rizta Z comes in nine colour options and the Rizta S in four. The names — Duo, Mono, Super Matte — describe the finish as much as the colour, and the choice affects how the scooter looks after a year of family use.",
"img": M + "Ather-Rizta-family-electric-scooter-floor-board.webp",
"img_alt": "Ather Rizta",
"models": ["ather-rizta-z", "ather-rizta-s"],
"facts": [("Rizta Z options", "9"), ("Rizta S options", "4"), ("Duo", "Two-tone body"), ("Super Matte", "Flat finish")],
"body": [
("Every Rizta colour", """
| Colour | Rizta Z | Rizta S |
|---|---|---|
| Terracotta Red (Duo) | Yes | — |
| Terracotta Red (Super Matte) | Yes | Yes |
| Pangong Blue (Duo) | Yes | — |
| Pangong Blue (Super Matte) | Yes | Yes |
| Deccan Grey (Duo) | Yes | — |
| Deccan Grey (Mono) | Yes | Yes |
| Siachen White (Mono) | Yes | Yes |
| Alphonso Yellow (Duo) | Yes | — |
| Cardamom Green (Duo) | Yes | — |

Duo and Super Matte finishes carry a premium. Availability varies with stock.
"""),
("Duo, Mono or Super Matte?", """
**Duo** pairs a body colour with a contrasting white upper section — the look most people picture when they think of the Rizta. **Mono** is one colour all over and the simplest to keep looking new. **Super Matte** is a flat, low-sheen finish that looks premium but needs gentler cleaning.

The Rizta Z also gets a premium dual-tone seat; the Rizta S has a standard black seat.
"""),
("Choosing a colour for family use", """
- **Light colours and Duo whites** show scuffs from shoes and bags on the floorboard area more than dark ones. A floor mat helps.
- **Deccan Grey** is the most forgiving everyday colour — it hides dust and minor marks.
- **Bright Duo colours** like Alphonso Yellow and Cardamom Green are easy to spot in a crowded apartment parking lot, which matters more than you might think.
"""),
],
"faqs": [
("How many colours does the Rizta Z have?", "Nine options: Terracotta Red and Pangong Blue in Duo and Super Matte, Deccan Grey in Duo and Mono, Siachen White Mono, Alphonso Yellow Duo and Cardamom Green Duo."),
("Which colours are available on the Rizta S?", "Four: Siachen White (Mono), Deccan Grey (Mono), Pangong Blue (Super Matte) and Terracotta Red (Super Matte)."),
("Do Duo colours cost more?", "Yes, Ather prices Duo and Super Matte finishes at a premium over Mono. Your quote will show the exact amount."),
],
"related": ["ather-450-colours-guide", "ather-rizta-family-guide", "ather-rizta-z-vs-rizta-s"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-scooter-for-long-commutes",
"cluster": "models",
"title": "Best Ather for Long Daily Commutes (50 km+) | Pillai Auto",
"desc": "Riding 50–100 km a day? Which Ather and battery to choose, how to plan charging, and real routes from Chengalpattu, Chidambaram and the OMR.",
"h1": "The best Ather for a long daily commute",
"lede": "A growing number of our customers ride 50 km or more every day — Chengalpattu to Guindy, Siruseri to Anna Nagar, Chidambaram to Neyveli. An Ather handles that comfortably, but the model, the battery and the charging plan all need to be right.",
"img": M + "Ather-450-electric-scooter-front-view.webp",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc", "ather-450-apex"],
"facts": [("Rule of thumb", "Longest day × 1.5 ≤ TrueRange"), ("Best fast-charge rate", "30 km in 10 min"), ("Models with it", "450X & Rizta Z (3.5 kWh), 450 Apex")],
"body": [
("Choose the 3.5 kWh battery", """
For 50 km and over, we nearly always recommend the 3.5 kWh pack. Its TrueRange of about 125–130 km means a 60 km round trip uses less than half the battery, leaving a comfortable margin for traffic, detours and Sport mode. On the 450X, 450 Apex and Rizta Z it also unlocks fast charging at up to 30 km in ten minutes.
"""),
("Which model for which commute", """
| Commute | Our pick | Why |
|---|---|---|
| Fast highway stretches (GST Road, OMR) | [450X](/scooters/ather-450x.html) or [450 Apex](/scooters/ather-450-apex.html) | 90–100 km/h, dual discs, Infinite Cruise |
| Long commute with a pillion | [Rizta Z](/scooters/ather-rizta-z.html) | Comfortable seat, 3.5 kWh option, SkidControl |
| Long but slow, rough roads | [Konarc S 3.5 kWh](/scooters/ather-konarc.html) | 14-inch wheel, long-travel suspension |
"""),
("Plan your charging around the day", """
- **Charge at home every night** to about 80–90%. Daily top-ups are kinder to the battery than running it low.
- **Find one fast charger on your route** in the Ather app before you need it. Ten minutes while you buy tea is a useful safety net.
- **Ask about charging at work.** Many OMR offices allow it — a portable charger in the boot doubles your daily range.
"""),
("Ride efficiently without riding slowly", """
SmartEco mode adjusts power to how you ride and noticeably stretches range on long trips. Holding a steady 50–60 km/h uses far less energy than repeatedly accelerating hard to 80. On the 450X and Apex, Infinite Cruise's City Cruise keeps your speed steady without holding the throttle. See our [range tips](@how-to-get-more-range-from-your-ather).
"""),
],
"faqs": [
("Can an Ather do 100 km in a day?", "Yes. With the 3.5 kWh battery, Ather's real-world TrueRange estimate is about 125–130 km, so a 100 km day is possible on one charge with sensible riding, or comfortably with a short fast-charge stop."),
("Is the Konarc good for long commutes?", "On rough roads at moderate speeds, yes — especially the 3.5 kWh variant. If your commute includes long stretches above 60 km/h, a 450 is more relaxed."),
("Does riding long distances every day wear the battery faster?", "More cycles do age a battery over time, which is why the extended battery warranty (up to 10 years or 1,00,000 km) is worth considering for high-mileage riders."),
],
"related": ["daily-commute-chengalpattu-to-chennai-on-an-ather", "ather-battery-warranty-explained", "ather-grid-fast-charging-guide"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-scooter-for-senior-riders",
"cluster": "models",
"title": "Ather Scooters for Senior Riders: Easy, Safe Choices",
"desc": "Choosing an Ather for a parent or senior rider: seat height, weight, AutoHold, reverse, gentle ride modes and the features that make riding easier.",
"h1": "Choosing an Ather for a senior rider",
"lede": "Some of our happiest customers are in their sixties and seventies — often riding a scooter their children helped choose. Electric scooters are easier to ride than petrol ones in several ways, and a few Ather features make a real difference.",
"img": M + "3AutoHoldAtEveryStop.webp",
"img_alt": "Ather AutoHold at a stop",
"models": ["ather-rizta-s", "ather-rizta-z", "ather-konarc"],
"facts": [("Seat height", "77 cm (Konarc) · 78 cm (450, Rizta)"), ("Lightest", "450 series, 108 kg"), ("Gentle modes", "Eco / SmartEco")],
"body": [
("Why electric is easier", """
There is no kick-start or choke, no engine vibration, and no gears or clutch. The scooter is silent at a standstill, so there is no temptation to rev it, and power comes in smoothly in Eco mode. Charging at home also means no trips to the petrol pump.
"""),
("Features that help", """
- **AutoHold** keeps the scooter from rolling back on a slope, so there is no need to balance the brakes and throttle at the same time.
- **Reverse Mode / Reverse Park Assist** lets the rider back out of a tight spot without paddling with their feet.
- **Eco and SmartEco modes** soften acceleration so the scooter never surprises the rider.
- **FallSafe** cuts the motor if the scooter tips over.
- **Crash Alert** (Rizta Z) notifies family with a location if a crash is detected — a real comfort for children living elsewhere.
"""),
("Weight and seat height", """
| Model | Seat height | Kerb weight |
|---|---|---|
| Konarc S | 77 cm | 126.5–129 kg |
| 450S / 450X | 78 cm | 108–111.6 kg |
| Rizta S / Z | 78 cm | 125 kg |

The 450 series is the lightest to push around, but its sporty stance is not to everyone's taste. The Rizta is heavier but its flat floorboard and upright seating feel familiar to anyone who has ridden a family scooter.
"""),
("Our usual recommendation", """
For most senior riders we suggest the [Rizta S](/scooters/ather-rizta-s.html) for comfort and simplicity, or the [Rizta Z](/scooters/ather-rizta-z.html) if Crash Alert and a Tamil-language dashboard are wanted. Please bring the rider to the showroom: we let them sit on each model, put their feet down and try reverse in our car park before going on the road.
"""),
],
"faqs": [
("Is an electric scooter safe for elderly riders?", "With a properly fitted helmet and a model suited to their height and strength, many senior riders find an electric scooter easier than petrol. Gentle ride modes, AutoHold and reverse all help. If there is any doubt about balance or reflexes, speak to their doctor first."),
("Can the dashboard be set to Tamil?", "The Rizta Z's touchscreen can be set to Tamil, Hindi, Malayalam or Kannada."),
("Which Ather is easiest to park?", "Any model with Reverse Mode or Reverse Park Assist helps. The 450 series is the lightest; the Konarc and Rizta are heavier but have a flat floor and upright position."),
],
"related": ["autohold-and-reverse-park-assist-explained", "ather-rizta-family-guide", "crash-alert-and-safety-features-explained"],
},
]
