#!/usr/bin/env python3
"""
guides_ownership.py  —  Version: V1  (12 Nov 2026)
"Owning an Ather" guides. Sources: Ather specification sheets and Ather's
service blog (Nov 2026); Tamil Nadu EV road-tax extension (Jan 2026 notification,
to 31 Dec 2027); fuel prices Chennai ₹107.77 (9 Nov 2026), Puducherry ₹103.58
(1 Nov 2026). Re-check prices and policy each quarter.
"""
M = "https://media.atherenergy.com/"

GUIDES = [
# ---------------------------------------------------------------------------
{
"slug": "charging-ather-at-home-in-a-chennai-apartment",
"cluster": "ownership",
"title": "Charging an Ather at Home in a Chennai Apartment",
"desc": "How to charge an Ather in an apartment or independent house in Chennai: sockets, wiring, association permission, metering and charging times.",
"h1": "Charging your Ather at home in a Chennai apartment",
"lede": "The question we hear most from apartment dwellers on the OMR is not about range — it is \"where will I plug it in?\" The good news: an Ather needs far less than people assume. Here is how residents in Chennai apartments and houses set it up.",
"img": M + "450-charging-duo-d.webp",
"img_alt": "Ather home charger",
"models": ["ather-rizta-z", "ather-450x", "ather-konarc"],
"facts": [("What you need", "A properly earthed household socket"), ("450 W charger", "Overnight charging"), ("900 W / combined", "3–4 hours to 80%"),
          ("Energy per full charge", "Roughly 2.5–4 units")],
"body": [
("What the charger needs", """
Ather's home chargers plug into a regular household socket. What matters is that the socket is **properly earthed**, on a circuit in good condition, and not shared with something heavy like a geyser or air conditioner on the same line. Avoid extension boards and multi-plug adapters — they are the most common cause of charging trouble we see.
"""),
("Independent houses", """
Usually the simplest case. A socket near where the scooter is parked — on the porch, by the gate, in the car shed — is all you need. Have an electrician check the earthing and fit a socket at waist height, away from where rain splashes. If the scooter is parked outdoors, keep the charger itself dry and under cover.
"""),
("Apartments: the four routes", """
1. **A socket at your parking slot.** The ideal. Many newer OMR and Pallikaranai complexes already provide one, or allow residents to install one with the association's permission.
2. **A line from your own meter.** An electrician runs a cable from your flat's distribution board down to the parking slot. It needs association approval, but the electricity is billed to you, which avoids disputes.
3. **A sub-meter on a common supply.** Some associations install a metered socket and charge residents for what they use.
4. **Charging in the flat.** Not practical for the scooter itself — and we do not recommend carrying anything heavy up stairs — so in buildings without parking sockets, owners rely on fast charging and charging at work.
"""),
("Talking to your association", """
Associations worry about three things: safety, fair billing and appearance. A short written request that covers all three — a licensed electrician, a separate meter or a line from your own board, and a neat conduit — gets approved far more often than an informal ask. We are happy to share specifications for your electrician.
"""),
("How long it takes", """
| Charger | Typical time |
|---|---|
| 450 W (450 series, Rizta) | Overnight — about 5–7.5 hours for a full charge depending on battery |
| 900 W (3.5 kWh 450 and Rizta) | About 3 hr 25 min to 80%, 4 hr 30 min to 100% |
| Konarc combined charger | 2 hr to 3 hr 10 min to 80% |

Most owners simply plug in after the evening ride and unplug in the morning. See [what each charge costs](@ather-charging-cost-per-km).
"""),
],
"faqs": [
("Do I need a special socket to charge an Ather?", "No special socket is required, but it must be a properly earthed household socket on a sound circuit. Avoid extension boards and adapters."),
("Can I charge an Ather in my apartment parking?", "Yes, if there is a suitable socket — your own line from your flat's meter, an association-approved metered socket, or a socket already provided at your slot."),
("How many units does an Ather use per charge?", "Roughly 2.5 to 4 units for a full charge depending on battery size, allowing for charging losses."),
],
"related": ["ather-charging-cost-per-km", "ather-grid-fast-charging-guide", "omr-it-corridor-commute-on-an-ather"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-grid-fast-charging-guide",
"cluster": "ownership",
"title": "Ather Grid Fast Charging Guide: Speeds, Finding Chargers",
"desc": "How Ather Grid fast charging works: 6,100+ points, how much range each model adds in 10 minutes, finding chargers near Chennai and Puducherry, and etiquette.",
"h1": "Ather Grid fast charging: a practical guide",
"lede": "Ather Grid is India's largest fast-charging network for two-wheelers, with more than 6,100 points across 370+ cities. For most owners it is a safety net rather than a daily habit — but knowing how it works makes long days and trips much easier.",
"img": M + "450-charging-grid-d.webp",
"img_alt": "Ather Grid fast charger",
"models": ["ather-450x", "ather-rizta-z", "ather-450-apex", "ather-konarc"],
"facts": [("Network", "6,100+ points, 370+ cities"), ("Fastest rate", "Up to 30 km in 10 min"), ("Find chargers", "Ather app, dashboard, Google Maps")],
"body": [
("How much range in ten minutes", """
| Model and battery | Range added in 10 minutes |
|---|---|
| 450X 3.5 kWh, 450 Apex, Rizta Z 3.5 kWh | up to 30 km |
| 450X / Rizta Z smaller battery, 450S, Rizta S | up to 15 km |
| Konarc S 2.7 / 3.5 kWh | up to 15 km |
| Konarc S 2.1 kWh | up to 13 km (Grid access is an add-on) |
"""),
("Finding a charger", """
The Ather app shows nearby Ather Grid points with live availability, and on models with Google Maps the dashboard can route you to one. Ather Grid points also appear in Google Maps. Before a long trip, open the app and note two chargers along the way — a primary and a backup — rather than relying on one.
"""),
("Using a fast charger", """
1. Park so the cable reaches without strain, and switch the scooter off.
2. Connect the charger and start the session from the app or the charger, following the on-screen steps.
3. Watch the charge on your app; you do not need to stand by the scooter.
4. Unplug and move on as soon as you have what you need — the next rider may be waiting.
"""),
("When to use Grid, and when not to", """
Fast charging is perfect for topping up during a long day or a trip. For everyday charging, home charging overnight is cheaper and gentler on the battery. A good habit: charge at home daily, use Grid when the day runs longer than planned. For long routes in our region, see the [ECR trip guide](@chennai-to-puducherry-ecr-on-an-ather) and the [Chengalpattu commute guide](@daily-commute-chengalpattu-to-chennai-on-an-ather).
"""),
],
"faqs": [
("How many Ather Grid chargers are there?", "Ather lists more than 6,100 fast-charging points across 370+ cities in India."),
("How fast does an Ather fast charge?", "Up to 30 km of range in ten minutes on the 3.5 kWh 450X, 450 Apex and Rizta Z, and up to 15 km on most other variants."),
("Can the Konarc use Ather Grid?", "Yes, the Konarc S 2.7 and 3.5 kWh variants support Ather Grid. On the 2.1 kWh variant it is an add-on."),
],
"related": ["charging-ather-at-home-in-a-chennai-apartment", "ather-450-battery-2-9-vs-3-5-kwh", "ather-battery-care-in-hot-weather"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-charging-cost-per-km",
"cluster": "ownership",
"title": "Ather Charging Cost per km in Tamil Nadu and Puducherry",
"desc": "What it costs to charge an Ather at home, per charge and per km, with examples at different electricity rates — and how that compares with petrol.",
"h1": "What does it cost to charge an Ather?",
"lede": "Less than most people expect. A full charge uses a few units of electricity, which works out to around 20–30 paise per kilometre at typical home rates. Here is the arithmetic, so you can check it against your own EB bill.",
"img": M + "ather-app-Real-time-Charge-Status.webp",
"img_alt": "Charge status in the Ather app",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc"],
"facts": [("Units per full charge", "≈ 3.9 units (3.5 kWh pack)"), ("Per km at ₹8/unit", "≈ 24 paise"), ("Petrol scooter per km", "≈ ₹2.30–2.40")],
"body": [
("The arithmetic", """
Take a 3.5 kWh battery. Allowing roughly 10% for charging losses, a full charge from empty draws about **3.9 units** from the wall. With a real-world TrueRange of about 130 km, that is roughly **0.03 units per kilometre**.

| Your electricity rate | Cost of a full charge | Cost per km |
|---|---|---|
| ₹6 per unit | ≈ ₹23 | ≈ 18 paise |
| ₹8 per unit | ≈ ₹31 | ≈ 24 paise |
| ₹10 per unit | ≈ ₹39 | ≈ 30 paise |

Your rate depends on your tariff slab — check the per-unit figure on your latest electricity bill and use the closest row.
"""),
("Compared with petrol", """
A typical 110 cc petrol scooter managing about 45 km per litre costs:

| | Petrol price | Cost per km |
|---|---|---|
| Chennai (9 Nov 2026) | ₹107.77 / litre | ≈ ₹2.39 |
| Puducherry (1 Nov 2026) | ₹103.58 / litre | ≈ ₹2.30 |

At around 24 paise per km, an Ather costs roughly a tenth as much to run on energy alone.
"""),
("A month of commuting", """
Riding 1,000 km a month — about 40 km a day, 25 days a month:

- **Petrol scooter in Chennai:** about ₹2,390
- **Ather, charged at home at ₹8/unit:** about ₹240

That is a difference of around ₹2,150 a month, or about ₹25,800 a year, before service savings. Our [cost of ownership guide](@ather-vs-petrol-scooter-cost-of-ownership) adds servicing and other costs.
"""),
("What about fast charging?", """
Ather Grid fast charging is priced per session or per unit in the Ather app and costs more than charging at home. Use it to top up on long days; do most of your charging at home to keep costs lowest.
"""),
],
"faqs": [
("How much does it cost to fully charge an Ather?", "Roughly ₹23–39 at home for a 3.5 kWh battery, depending on whether you pay ₹6 or ₹10 per unit. Smaller batteries cost proportionally less."),
("What is an Ather's running cost per km?", "Around 18–30 paise per km on home electricity, depending on your tariff."),
("Is fast charging more expensive than home charging?", "Yes. Ather Grid fast charging costs more per unit than typical home electricity. The current price is shown in the Ather app before you start."),
],
"related": ["ather-vs-petrol-scooter-cost-of-ownership", "how-to-get-more-range-from-your-ather", "charging-ather-at-home-in-a-chennai-apartment"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-vs-petrol-scooter-cost-of-ownership",
"cluster": "ownership",
"title": "Ather vs Petrol Scooter: 5-Year Cost of Ownership",
"desc": "Five-year cost of owning an Ather versus a petrol scooter in Chennai and Puducherry: fuel, electricity, service, road tax and insurance compared.",
"h1": "Ather vs petrol scooter: the five-year cost",
"lede": "An Ather costs more to buy than a 110 cc petrol scooter. The question is how quickly it earns that back. With petrol above ₹100 a litre in both Tamil Nadu and Puducherry, the answer for a daily commuter is: faster than you might think.",
"models": ["ather-konarc", "ather-rizta-s", "ather-450s"],
"facts": [("Energy saving", "≈ ₹2,150 / month at 1,000 km"), ("TN road tax on EVs", "100% exempt to 31 Dec 2027"), ("Service", "No oil, filters or spark plugs")],
"body": [
("Where the savings come from", """
1. **Energy.** About 24 paise per km on home electricity against roughly ₹2.30–2.40 per km in petrol. See [the charging cost guide](@ather-charging-cost-per-km).
2. **Road tax.** Tamil Nadu has extended its 100% motor vehicle tax exemption for electric vehicles until 31 December 2027. Puducherry has its own rules — see [our registration guide](@ev-registration-tamil-nadu-vs-puducherry).
3. **Servicing.** No engine oil, oil filter, spark plug, air filter or clutch. Ather's own blog lists typical wear parts — brake pads from about ₹260, drive belts at 50,000 km — and the Konarc's sealed gearbox needs servicing just once a year.
"""),
("A worked example over five years", """
For a commuter riding 1,000 km a month (60,000 km over five years) in Chennai:

| | Petrol scooter | Ather (home charging at ₹8/unit) |
|---|---|---|
| Fuel / electricity | ≈ ₹1,43,700 | ≈ ₹14,400 |
| Difference | | ≈ ₹1,29,000 in the Ather's favour |

This assumes petrol stays at ₹107.77 and a petrol scooter averages 45 km/l. It excludes servicing, where the Ather is also usually cheaper, and the purchase price, which varies by model.
"""),
("What to weigh on the other side", """
- **Purchase price.** Compare like for like — an Ather against a well-equipped petrol scooter, not the cheapest one.
- **Battery.** The standard warranty covers 3 years / 30,000 km; extending it to up to 10 years / 1,00,000 km protects the biggest cost item. See the [battery warranty guide](@ather-battery-warranty-explained).
- **Insurance.** Comprehensive cover is needed for both; ask us for quotes on the model you choose.
- **How much you ride.** The savings scale with kilometres. At 300 km a month, payback takes much longer than at 1,500.
"""),
("Our honest take", """
For anyone riding 30 km or more a day, an Ather usually costs less over five years than a petrol scooter, even after the higher purchase price. For very light use, buy one because you prefer how it rides — not for the savings. Use our [EMI calculator](/emi-calculator.html) to see how the monthly payment compares with your current fuel spend.
"""),
],
"faqs": [
("Is an Ather cheaper than a petrol scooter in the long run?", "For regular commuters, usually yes. At 1,000 km a month in Chennai, energy alone saves about ₹2,150 a month compared with a petrol scooter, before service savings."),
("Do I pay road tax on an Ather in Tamil Nadu?", "Tamil Nadu has extended its 100% road tax exemption for electric vehicles until 31 December 2027."),
("What maintenance does an Ather need?", "Periodic inspections, brake pads, tyres and (on belt-driven models) a belt around 50,000 km. There is no engine oil, filter, spark plug or clutch."),
],
"related": ["ather-charging-cost-per-km", "exchange-your-petrol-scooter-for-an-ather", "ather-finance-and-loan-documents"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-service-schedule-and-costs",
"cluster": "ownership",
"title": "Ather Service Schedule and Costs: 450, Rizta and Konarc",
"desc": "How often an Ather needs servicing, what is checked, typical parts prices, Ather Care plans, and how servicing works at Pillai Auto's four showrooms.",
"h1": "Ather service schedule and costs",
"lede": "An Ather needs far less servicing than a petrol scooter, but it still needs some. Here is how often, what gets checked, what parts typically cost, and how to book with us.",
"img": M + "450-bodyguard-d.webp",
"img_alt": "Ather 450",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc"],
"facts": [("450 & Rizta", "Inspection every 5,000 km or 6 months"), ("Konarc", "Once a year"), ("Drive belt", "Replace at 50,000 km"), ("Same-day service", "Usually")],
"body": [
("How often", """
| Model | Periodic service | Notes |
|---|---|---|
| 450S / 450X / 450 Apex | Every 5,000 km or 6 months | Steering bearings lubricated every 10,000 km / 12 months |
| Rizta S / Z | Every 5,000 km or 6 months | Same schedule as the 450 |
| Konarc | Once a year | Sealed Silent Gear Drive, no belt |

These follow Ather's published guidance; your scooter's app shows the next due date.
"""),
("What gets checked", """
Ather's periodic service is a multi-point inspection plus a wash. It covers the drive belt and pulleys (on belt-driven models), tyres and brakes, brake fluid, suspension, wheel bearings and seals, chassis fasteners, and a software check with the latest updates installed. Battery diagnostics are run when you report a range or overnight charge-drop concern.
"""),
("Typical parts prices", """
Ather lists these indicative prices, including GST, for the 450 series and Rizta:

| Part | 450 series | Rizta |
|---|---|---|
| Front brake pad | ₹370 | ₹349 |
| Rear brake pad | ₹260 | ₹260 |
| Primary belt | ₹999 | ₹999 |
| Secondary belt | ₹1,499 | ₹1,499 |

Prices change from time to time; we confirm them on your job card before starting work.
"""),
("Ather Care plans", """
Ather offers prepaid care plans. **Ather Care** covers the essentials for 1 year or 10,000 km, including two free periodic maintenance sessions and a discount on wear-and-tear parts and labour. **Care Plus** adds a polish and a wash with bigger discounts, and **Care Max** adds free brake pad replacements, belt lubrication, washes, polishing and ExpressCare sessions. Ask us which plan matches your yearly kilometres.
"""),
("Servicing with us", """
All four Pillai Auto showrooms — [Chennai OMR](/locations/chennai-omr.html), [Chengalpattu](/locations/chengalpattu.html), [Puducherry](/locations/pondicherry.html) and [Chidambaram](/locations/chidambaram.html) — have service bays. Book through the Ather app or on our [service page](/service.html). Periodic maintenance is usually same-day, and an express service takes about an hour.
"""),
],
"faqs": [
("How often should an Ather 450X be serviced?", "Ather's guidance is a periodic inspection every 5,000 km or 6 months, whichever comes first."),
("How often does the Ather Konarc need servicing?", "Once a year. Its sealed Silent Gear Drive removes the belt that needs regular checks on other models."),
("When does the Ather drive belt need replacing?", "Ather's guidance is to replace the belt at 50,000 km, with tension and condition checked at every service."),
],
"related": ["ather-battery-warranty-explained", "ather-vs-petrol-scooter-cost-of-ownership", "riding-your-ather-in-the-chennai-monsoon"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-battery-warranty-explained",
"cluster": "ownership",
"title": "Ather Battery Warranty Explained: 3, 5 and 10 Years",
"desc": "Ather battery warranty explained: 3 years / 30,000 km standard, 5 years with AtherStack Pro, up to 10 years / 1,00,000 km, and the 70% health promise.",
"h1": "Ather battery warranty, explained",
"lede": "The battery is the most valuable part of any electric scooter, so the warranty on it matters more than almost anything on the spec sheet. Ather offers three levels of cover. Here is how they work and how to claim.",
"img": M + "450-charging-d.webp",
"img_alt": "Ather battery charging",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc", "ather-450-apex"],
"facts": [("Standard", "3 yr / 30,000 km"), ("With AtherStack Pro", "5 yr / 60,000 km (free upgrade)"), ("Extended", "Up to 10 yr / 1,00,000 km"), ("Health assured", "70% state of health")],
"body": [
("The three levels", """
| Cover | Duration | How you get it |
|---|---|---|
| Standard | 3 years or 30,000 km | Every new Ather, vehicle and battery |
| AtherStack Pro upgrade | 5 years or 60,000 km | Free with AtherStack Pro |
| Extended battery warranty | Up to 10 years or 1,00,000 km | Add-on, with AtherStack Pro |

Whichever limit comes first applies. The charger has its own 3-year warranty.
"""),
("What \"70% state of health\" means", """
Every lithium-ion battery slowly loses capacity with age and use. State of health (SOH) measures how much capacity remains compared with new. Ather's warranty assures that the battery will stay at or above 70% SOH for the warranty period; if it falls below, the battery is covered. The extended warranty also includes an idle-state assurance for scooters that sit unused for a while.
"""),
("Is the extended warranty worth it?", """
- **Yes** if you ride more than about 1,000 km a month — you will cross 30,000 km in under three years.
- **Yes** if you plan to keep the scooter for five years or more, or want stronger resale value.
- **Less important** if you ride very little and plan to sell within three years.
"""),
("How claims work at Pillai Auto", """
If you notice range dropping more than you would expect, book a battery check at any of our showrooms. We read the pack's actual state of health from the scooter's diagnostics rather than guessing, explain whether the drop is normal, and if it qualifies we handle the warranty claim with Ather for you. Keep your service records up to date — they make claims straightforward.
"""),
],
"faqs": [
("What is the Ather battery warranty?", "3 years or 30,000 km as standard; a free upgrade to 5 years or 60,000 km with AtherStack Pro; and an extended battery warranty of up to 10 years or 1,00,000 km, with 70% state of health assured."),
("Does the warranty transfer if I sell my Ather?", "Ask us when you sell — warranty transfer terms are set by Ather and we will check the current rules for your scooter."),
("What voids the battery warranty?", "Typical exclusions include damage from accidents, water ingress through misuse, unauthorised repairs and non-genuine parts. We will give you Ather's full terms at purchase."),
],
"related": ["atherstack-pro-explained", "ather-battery-care-in-hot-weather", "ather-service-schedule-and-costs"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-battery-care-in-hot-weather",
"cluster": "ownership",
"title": "Ather Battery Care in Chennai Heat: Charging and Parking Tips",
"desc": "How to look after an Ather battery in Tamil Nadu's heat: charging habits, parking in shade, long trips, leaving it unused, and signs to get it checked.",
"h1": "Looking after your Ather battery in Chennai's heat",
"lede": "Lithium-ion batteries prefer moderate temperatures, and Chennai rarely offers them. Ather's battery-management system protects the pack, but a few simple habits help it stay healthy for longer.",
"img": M + "Desk-charge-your-way.webp",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc"],
"facts": [("Best habit", "Charge little and often"), ("Park", "In shade where possible"), ("Unused for weeks", "Leave around half charged")],
"body": [
("Charging habits", """
- **Charge little and often.** Topping up every evening is better for the battery than regularly running it down to almost empty.
- **You do not need 100% every day.** If your daily ride is short, charging to around 80–90% is plenty; charge to full before a long day.
- **Let it cool after a hard ride.** After a long fast run on a hot afternoon, give the scooter a few minutes in the shade before plugging in.
- **Use the supplied charger** in a properly earthed socket, never through an extension board.
"""),
("Parking in the heat", """
Direct sun on a parked scooter on a May afternoon heats the whole vehicle. Wherever you can, park in shade — under a tree, in a basement, or with a breathable scooter cover. It helps the battery and the seat you are about to sit on.
"""),
("If the scooter will sit unused", """
Going away for a few weeks? Leave the battery at roughly half charge rather than full or nearly empty, park it somewhere cool and dry, and check the charge in the app now and then. If it sits for a long time, top it up periodically so it never runs flat.
"""),
("Signs it is worth a check", """
- Range dropping noticeably faster than before, in similar riding.
- Charge falling overnight when the scooter is not used.
- Unusual warnings on the dashboard or in the app.

Book a battery check at any of our showrooms. We read the actual state of health and tell you whether what you are seeing is normal. See the [battery warranty guide](@ather-battery-warranty-explained) for what is covered.
"""),
],
"faqs": [
("Is it okay to charge an Ather every day?", "Yes. Daily top-ups are better for a lithium-ion battery than repeatedly running it nearly empty."),
("Should I charge my Ather to 100%?", "You can, and you should before a long ride. For short daily use, charging to around 80–90% is plenty."),
("Does Chennai heat damage the Ather battery?", "Ather's battery-management system protects the pack, but sustained heat ages any lithium-ion battery faster. Parking in shade and letting the scooter cool before charging after hard rides helps."),
],
"related": ["ather-battery-warranty-explained", "how-to-get-more-range-from-your-ather", "riding-your-ather-in-the-chennai-monsoon"],
},
# ---------------------------------------------------------------------------
{
"slug": "riding-your-ather-in-the-chennai-monsoon",
"cluster": "ownership",
"title": "Riding an Ather in the Chennai Monsoon: Water and Safety",
"desc": "Can you ride an Ather in the rain? Water ratings, flooded roads, charging in wet weather, traction settings and monsoon care for Chennai and the coast.",
"h1": "Riding your Ather through the Chennai monsoon",
"lede": "The north-east monsoon is when we get the most phone calls — usually starting with \"Is it safe to ride in this?\" Ather designs its scooters to be ridden in the rain. Flooded streets are a different matter. Here is where the line is.",
"img": M + "450-floor-mat-d.webp",
"img_alt": "Ather floor mat for the monsoon",
"models": ["ather-rizta-z", "ather-450x", "ather-konarc"],
"facts": [("Motor rating", "IP67 Konarc & Rizta · IP66 450"), ("450 dashboard", "IP65"), ("Wet roads", "Rain traction mode on 450X / Apex")],
"body": [
("Rain is fine; floods are not", """
Ather scooters are built and tested for riding in rain, with sealed electrical components. The motors are rated IP67 on the Konarc and Rizta and IP66 on the 450 series, which means they are protected against heavy water jets and, for IP67, temporary immersion in controlled conditions.

That does **not** make any scooter safe to ride through a flooded street. Water hides potholes, open drains and debris, and deep water can enter places no rating covers. Our rule: **if you cannot see the road surface, do not ride through it.** Wait, or take another route.
"""),
("Riding in the wet", """
- Switch to **Rain** traction mode on the 450X and 450 Apex; the Rizta Z's [SkidControl](@skidcontrol-explained) works automatically.
- Avoid Warp and hard acceleration — smooth inputs keep the tyres gripping.
- Treat painted lines, manhole covers and metal plates as ice.
- Brake earlier and more gently, using both brakes together.
- Check tyre pressure and tread before October — worn tyres are the biggest wet-weather risk.
"""),
("Charging in wet weather", """
Keep the charger and the socket dry. Never charge with water pooled around the charging point, and do not handle the plug with wet hands. If the scooter is parked in the open, charge it under cover. Ather's chargers and charging ports are designed with safety in mind, but common sense around electricity applies.
"""),
("If your scooter has been in deep water", """
Do not try to start or charge it. Push it to higher ground, call us, and we will advise or arrange to inspect it. Water damage caused by riding through floods may not be covered by the warranty, which is one more reason to avoid it. Our four showrooms keep monsoon-season slots open for exactly this.
"""),
],
"faqs": [
("Can I ride my Ather in the rain?", "Yes. Ather scooters are designed to be ridden in rain. Use gentle inputs, Rain traction mode where available, and avoid flooded roads."),
("Is the Ather waterproof?", "Its components are sealed and rated against water — IP67 motors on the Konarc and Rizta, IP66 on the 450 — but no scooter should be ridden through flooded streets."),
("Can I charge my Ather in the rain?", "Charge under cover with the charger and socket kept dry. Do not charge with water around the charging point."),
],
"related": ["traction-control-explained", "skidcontrol-explained", "ather-insurance-guide"],
},
# ---------------------------------------------------------------------------
{
"slug": "ev-registration-tamil-nadu-vs-puducherry",
"cluster": "ownership",
"title": "Registering an Ather: Tamil Nadu vs Puducherry Explained",
"desc": "How electric scooter registration works in Tamil Nadu and Puducherry: road tax, green number plates, documents, and buying across the state border.",
"h1": "Registering an Ather in Tamil Nadu and Puducherry",
"lede": "We sell Athers on both sides of the Tamil Nadu–Puducherry border, and the registration rules are not the same. Here is how it works, what you need to bring, and what to know if you live in one and buy in the other.",
"models": ["ather-konarc", "ather-rizta-s", "ather-450x"],
"facts": [("TN road tax on EVs", "100% exempt to 31 Dec 2027"), ("Number plate", "Green, for electric vehicles"), ("Register in", "The state or UT where you live")],
"body": [
("Every Ather needs registration", """
All current Ather models are high-speed electric scooters, so they need registration, a number plate, insurance and a valid driving licence to ride — exactly like a petrol scooter. We handle the registration paperwork at all four showrooms.
"""),
("Tamil Nadu", """
Tamil Nadu has extended its **100% motor vehicle tax exemption for electric vehicles** from 1 January 2026 to **31 December 2027**, under the Tamil Nadu Motor Vehicles Taxation Act. For an Ather registered in Tamil Nadu, that means no road tax during this period. Registration, number plate and insurance charges still apply. This covers our Chennai, Chengalpattu and Chidambaram showrooms.
"""),
("Puducherry", """
Puducherry is a Union Territory with its own transport department and its own EV concessions, which have changed over recent years. Rather than print figures that may be out of date, our Puducherry showroom on 100 Ft Road gives you the exact registration and tax amounts on your written quote. Vehicles registered here carry Puducherry's PY registration.
"""),
("Buying across the border", """
You register a vehicle where you live. A Cuddalore resident buying at our Puducherry showroom, or a Puducherry resident buying in Chidambaram, registers in their home state or UT — and pays that jurisdiction's charges. Tell us your address at the start and we will quote correctly and route the paperwork to the right office.
"""),
("What to bring", """
- Proof of identity and address (Aadhaar is the simplest)
- PAN card, or Form 60 if you do not have one
- Passport-size photographs
- Your driving licence details

If you are financing, the lender will ask for income documents too — see our [finance guide](@ather-finance-and-loan-documents).
"""),
],
"faqs": [
("Is there road tax on electric scooters in Tamil Nadu?", "Tamil Nadu has extended its 100% road tax exemption for electric vehicles until 31 December 2027."),
("What colour is an electric scooter's number plate?", "Electric vehicles carry green number plates."),
("Can I buy an Ather in Puducherry if I live in Tamil Nadu?", "Yes, but the scooter is registered where you live, under that state's rules and charges. Tell us your address and we will quote accordingly."),
],
"related": ["ather-finance-and-loan-documents", "ather-insurance-guide", "ather-vs-petrol-scooter-cost-of-ownership"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-finance-and-loan-documents",
"cluster": "ownership",
"title": "Ather Finance and EMI: Flexipay, Loans and Documents",
"desc": "How to finance an Ather: Flexipay zero down payment, interest rates, tenures up to 5 years, the documents lenders ask for, and how approval works.",
"h1": "Financing an Ather: options and documents",
"lede": "Most of our customers buy on finance, and approval is usually quick. Here is how Ather's Flexipay scheme and our partner lenders work, what interest to expect, and the documents that make approval fastest.",
"models": ["ather-konarc", "ather-rizta-s", "ather-450x"],
"facts": [("Flexipay", "Zero down payment available"), ("Interest from", "3.99% (450, Rizta) · 5.75% (Konarc)"), ("Tenure", "Up to 5 years"), ("Konarc EMI from", "₹1,964 / month")],
"body": [
("Ather Flexipay", """
Ather's Flexipay finance offers **zero down payment**, simplified approval and tenures up to **five years**. Ather advertises interest from **3.99%** on the 450 and Rizta and from **5.75%** on the Konarc, with Konarc EMIs from ₹1,964 a month and Rizta EMIs from about ₹2,235. Actual rates depend on the lender, your credit profile, the tenure and the down payment.
"""),
("Other lenders", """
We also work with banks and NBFCs. Our finance desk compares the offers you qualify for and lays them side by side — interest rate, processing fee, total payable — so you can choose on the full cost, not just the EMI.
"""),
("Documents to bring", """
| For | Typical documents |
|---|---|
| Identity and address | Aadhaar, PAN card |
| Salaried | Latest salary slips, bank statements for recent months |
| Self-employed | Bank statements, recent income-tax returns or business proof |
| Everyone | Passport-size photos, an active mobile number linked to your bank |

Lenders vary; we tell you exactly what your chosen lender needs before you visit.
"""),
("Make approval quicker", """
- Check your credit score beforehand.
- Bring complete documents in one visit.
- Choose a tenure that keeps the EMI comfortable — a longer tenure lowers the EMI but raises total interest.
- Combine finance with an [exchange of your old scooter](@exchange-your-petrol-scooter-for-an-ather) to reduce the loan amount.

Try different amounts in our [EMI calculator](/emi-calculator.html).
"""),
("Look at the total, not just the EMI", """
A longer tenure always looks cheaper per month. As an illustration, a ₹1,20,000 loan at 9% interest:

| Tenure | Monthly EMI | Total repaid |
|---|---|---|
| 36 months | ≈ ₹3,816 | ≈ ₹1,37,400 |
| 60 months | ≈ ₹2,491 | ≈ ₹1,49,500 |

The five-year loan costs about ₹12,000 more overall. Choose the shortest tenure whose EMI you are comfortable with — and compare it with the petrol you will stop buying.
"""),
],
"faqs": [
("Can I buy an Ather with zero down payment?", "Ather's Flexipay scheme offers zero down payment options, subject to lender approval."),
("What is the interest rate on an Ather loan?", "Ather advertises rates from 3.99% on the 450 and Rizta and from 5.75% on the Konarc. Your actual rate depends on the lender and your credit profile."),
("How long does Ather finance approval take?", "With complete documents, approvals often come through the same day."),
],
"related": ["exchange-your-petrol-scooter-for-an-ather", "ather-vs-petrol-scooter-cost-of-ownership", "ev-registration-tamil-nadu-vs-puducherry"],
},
# ---------------------------------------------------------------------------
{
"slug": "exchange-your-petrol-scooter-for-an-ather",
"cluster": "ownership",
"title": "Exchange Your Petrol Scooter for an Ather | Pillai Auto",
"desc": "How exchanging an old petrol two-wheeler for a new Ather works at Pillai Auto: valuation, documents, loan closure and what affects the price you get.",
"h1": "Exchanging your petrol scooter for an Ather",
"lede": "Many of our customers trade in a petrol scooter or motorcycle when they switch. It reduces the price of the new Ather and saves you the hassle of selling privately. Here is how it works.",
"models": ["ather-konarc", "ather-rizta-s", "ather-450s"],
"facts": [("Accepted", "Petrol scooters and motorcycles"), ("Valuation", "At the showroom, same day"), ("Value used for", "Down payment or price reduction")],
"body": [
("How it works", """
1. **Bring the vehicle and its papers** to any of our showrooms.
2. **We inspect and value it** — usually within half an hour.
3. **The agreed value comes off** your new Ather's price or goes towards the down payment.
4. **We handle the transfer paperwork** for the old vehicle.
"""),
("What affects the price", """
- **Age and kilometres.** The biggest factors.
- **Condition.** Body panels, tyres, how it starts and runs.
- **Service history.** Receipts and a clean record help.
- **Papers in order.** A valid RC, insurance and no pending challans make the process smoother and the offer better.
- **Make and model demand** in the used market around our showrooms.
"""),
("Documents for the old vehicle", """
- Original RC (registration certificate)
- Valid insurance
- Your ID proof matching the RC owner
- Both keys, if you have them
- **If there is an outstanding loan:** the lender's details, so we can arrange the loan closure and the hypothecation removal (Form 35 / NOC)
"""),
("Exchange plus finance", """
Using your exchange value as the down payment can bring the loan amount — and the EMI — down noticeably. Our finance desk works out the combination with you. See the [finance guide](@ather-finance-and-loan-documents) and try the numbers in the [EMI calculator](/emi-calculator.html).
"""),
("Exchange or sell privately?", """
| | Exchange at the showroom | Sell privately |
|---|---|---|
| Price | Fair market offer | Sometimes a little higher |
| Time | Same day | Days to weeks |
| Paperwork | We handle the transfer | You arrange it |
| Risk | None — paid against your new scooter | Test rides by strangers, payment risk |

If you have the time and patience, a private sale can fetch slightly more. Most customers find the convenience of exchange worth it, especially when the value goes straight into the down payment.
"""),
],
"faqs": [
("Can I exchange my petrol scooter for an Ather?", "Yes. We value petrol scooters and motorcycles at all four showrooms and adjust the value against your new Ather."),
("Can I exchange a vehicle that still has a loan?", "Yes, with the lender's details. We arrange the loan closure and removal of hypothecation as part of the exchange."),
("Do I need the original RC to exchange?", "Yes, the original registration certificate is needed to transfer ownership."),
],
"related": ["ather-finance-and-loan-documents", "ather-vs-petrol-scooter-cost-of-ownership", "ather-test-ride-checklist"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-insurance-guide",
"cluster": "ownership",
"title": "Ather Scooter Insurance Guide: Cover and Add-ons",
"desc": "Insuring an Ather: third-party vs comprehensive cover, the five-year third-party rule for new two-wheelers, useful add-ons, and how claims work.",
"h1": "Insuring your Ather: what you need",
"lede": "Insurance on an electric scooter works much like on a petrol one, with a few points worth knowing because the battery is such a large share of the value. Here is a plain guide to the cover and the add-ons we suggest.",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc"],
"facts": [("Required by law", "Third-party cover"), ("New two-wheelers", "Long-term third-party cover"), ("Recommended", "Comprehensive + zero depreciation")],
"body": [
("The two parts of a policy", """
**Third-party liability** covers injury or damage you cause to others. It is mandatory, and for new two-wheelers it is sold as long-term cover (five years).

**Own damage** covers your scooter against accidents, theft, fire, floods and similar events. Together with third-party cover this is a **comprehensive** policy, which we strongly recommend for a new Ather.
"""),
("Add-ons worth considering", """
| Add-on | Why it helps |
|---|---|
| Zero depreciation | Claims pay for replaced parts without deducting for age — valuable in the first few years |
| Roadside assistance | Help if the scooter stops on the road |
| Return to invoice | Pays the invoice value if the scooter is stolen or written off |
| Consumables | Covers small items like nuts, bolts and fluids used in repairs |

Ask specifically how each insurer treats the **battery** in an own-damage claim — it is the most expensive component, and policy wording varies.
"""),
("Monsoon and flooding", """
Comprehensive policies generally cover flood damage, but damage caused by deliberately riding through deep water can be disputed. Our [monsoon guide](@riding-your-ather-in-the-chennai-monsoon) explains how to avoid it in the first place.
"""),
("Claims through Pillai Auto", """
Our service bays handle insurance repairs with the major insurers, including cashless claims where the insurer offers them. Call us before moving a damaged scooter far, take photographs, and file the claim with your insurer promptly.
"""),
],
"faqs": [
("Is insurance compulsory for an Ather?", "Yes. Third-party insurance is mandatory for all registered scooters, including electric ones."),
("Is zero depreciation worth it on an electric scooter?", "For a new scooter, usually yes. It means claims pay for replaced parts without deducting for depreciation."),
("Does insurance cover the Ather battery?", "Own-damage cover generally includes the battery as part of the vehicle, but wording varies between insurers. Check how your policy treats it before you buy."),
],
"related": ["riding-your-ather-in-the-chennai-monsoon", "ev-registration-tamil-nadu-vs-puducherry", "chidambaram-cuddalore-neyveli-on-an-ather"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-test-ride-checklist",
"cluster": "ownership",
"title": "Ather Test Ride Checklist: What to Try Before You Buy",
"desc": "Make the most of an Ather test ride: what to check on the seat, brakes, ride modes, regen, reverse and dashboard — and which two models to ride back to back.",
"h1": "Your Ather test ride checklist",
"lede": "A test ride is the only reliable way to choose between scooters that look similar on paper. Most people use it to check the scooter goes. Use it instead to answer the questions you will live with every day.",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc"],
"facts": [("Bring", "Driving licence, your usual pillion"), ("Ride", "Two models back to back"), ("Time", "About 30 minutes")],
"body": [
("Before you ride", """
- **Sit on it with your feet down.** Can you comfortably flat-foot or tip-toe? Try every model on your shortlist.
- **Bring your usual pillion** and sit them on it too. Seat length and backrest matter a lot to them.
- **Open the boot** and check your helmet fits. Bring it along if it is a large one.
"""),
("On the road", """
1. **Ride modes.** Start in Eco, then try Ride and Sport (or Warp on the 450X and Apex). Notice which feels natural.
2. **Brakes.** In a safe spot, brake firmly from 40 km/h. Feel how progressive they are.
3. **Regeneration and Magic Twist** (450X, Apex, Rizta Z). Roll the throttle back and feel the scooter slow.
4. **Bad road.** Ask us to include a rough patch — this is where the Konarc's 14-inch wheel or the Rizta's comfort shows.
5. **U-turn and slow traffic.** Low-speed balance matters more than top speed in Chennai.
"""),
("Back in the car park", """
- Try **reverse** and **AutoHold** on the ramp.
- Play with the **dashboard**: navigation on touchscreen models, readability of DeepView in sunlight.
- Ask us to show the **app**: charge status, theft alerts, ride stats.
"""),
("Ride two back to back", """
The most useful thing you can do is ride your top two choices one after the other — 450X and 450S, Rizta Z and Rizta S, or Konarc and Rizta S. Differences that are invisible on paper become obvious in ten minutes. Book at any of our [four showrooms](/locations/index.html) or on the [test ride page](/test-ride.html).
"""),
],
"faqs": [
("Is the Ather test ride free?", "Yes, test rides are free at all four Pillai Auto showrooms."),
("What do I need for a test ride?", "A valid two-wheeler driving licence, and ideally your usual pillion so they can try the seat."),
("Can I test ride two Ather models?", "Yes. We encourage riding your top two choices back to back."),
],
"related": ["which-ather-scooter-should-i-buy", "ather-delivery-day-checklist", "ather-450x-vs-450s"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-delivery-day-checklist",
"cluster": "ownership",
"title": "Ather Delivery Day Checklist: What to Check and Set Up",
"desc": "What to check when you take delivery of a new Ather: paperwork, charger, app pairing, safety settings, accessories and your first ride home.",
"h1": "Your Ather delivery day checklist",
"lede": "Delivery day is exciting, and it is easy to ride off without setting up the features you paid for. We go through everything with you at handover; this checklist is so you know what to expect and nothing gets missed.",
"models": ["ather-konarc", "ather-rizta-z", "ather-450x"],
"facts": [("Time needed", "About 45–60 minutes"), ("Bring", "Your phone, ID, payment confirmation"), ("Set up", "App, contacts, alerts")],
"body": [
("Paperwork", """
- Invoice and payment receipts
- Insurance policy (comprehensive, with any add-ons you chose)
- Registration status and number plate timeline
- Warranty details, including any extended battery warranty or AtherStack Pro
- Finance documents, if applicable
"""),
("Inspect the scooter", """
Walk round it in daylight with our team. Check paint and panels for marks, the colour is the one you ordered, tyres, lights, indicators and horn all work, and both keys are handed over. The battery should arrive with a healthy charge.
"""),
("Set up the technology", """
1. **Install the Ather app** and pair the scooter to your phone.
2. **Add family members** who will ride, with their own access.
3. **Add emergency contacts** for safety features such as Crash Alert where available.
4. **Turn on notifications** for Theft & Tow alerts.
5. **Pair your Halo helmet** if you bought one.
6. **Check for software updates** — we install the latest before handover.
"""),
("The charger", """
Make sure the right charger is in the box for your variant — 450 W, 900 W or the Konarc combined charger — and ask us to show how to connect it. See our [home charging guide](@charging-ather-at-home-in-a-chennai-apartment) before you plug in at home.
"""),
("Your first week", """
Ride in Eco or Ride mode at first while you get used to the instant response, practise reverse and AutoHold in a quiet spot, and charge every evening. Your first periodic service date appears in the app. Any question at all, call the showroom you bought from.
"""),
],
"faqs": [
("How long does Ather delivery take at the showroom?", "Allow about 45–60 minutes for paperwork, inspection and setting up the app and safety features."),
("Is the Ather charger included?", "Yes, a home charger is included. Which one depends on the model and battery; the Konarc 3.5 kWh includes the combined charger."),
("Should I set up the Ather app before delivery?", "Install it beforehand if you like; we pair it with the scooter and set up contacts and alerts with you at handover."),
],
"related": ["ather-test-ride-checklist", "theft-and-tow-alerts-explained", "ather-halo-smart-helmet-guide"],
},
# ---------------------------------------------------------------------------
{
"slug": "how-to-get-more-range-from-your-ather",
"cluster": "ownership",
"title": "How to Get More Range From Your Ather: 9 Practical Tips",
"desc": "Practical ways to get more real-world range from an Ather 450, Rizta or Konarc: ride modes, speed, tyre pressure, regen, load and charging habits.",
"h1": "How to get more range from your Ather",
"lede": "Two riders on the same Ather can see very different range. Almost all of the difference comes from a handful of habits — none of which means riding slowly. Here are the ones that matter most.",
"img": M + "ather-app-Find-Ather-Grid-near-you.webp",
"img_alt": "Finding Ather Grid chargers in the app",
"models": ["ather-450x", "ather-rizta-z", "ather-konarc", "ather-450s"],
"facts": [("Biggest factor", "Ride mode and throttle"), ("Easiest win", "Correct tyre pressure"), ("Best mode for range", "SmartEco")],
"body": [
("The nine habits", """
1. **Use SmartEco** for everyday riding. It adapts power delivery to how you ride and is the most efficient mode.
2. **Save Warp and Sport** for overtaking and empty roads.
3. **Roll on the throttle smoothly.** Hard launches from every signal cost more than any other habit.
4. **Hold a steady 40–60 km/h** where traffic allows. Range drops faster at higher speeds.
5. **Use regeneration.** Lift off early and let the scooter slow itself — Magic Twist on the 450X, Apex and Rizta Z makes this easy.
6. **Check tyre pressure fortnightly.** Soft tyres quietly cost range and wear faster.
7. **Carry only what you need.** A full boot and a pillion every day add up.
8. **Park in shade and charge after the scooter cools** on very hot days.
9. **Keep software up to date.** Updates sometimes improve efficiency and range estimates.
"""),
("Read the range estimate correctly", """
The range on your dashboard is calculated from your recent riding. After a weekend of hard riding it will look lower; after a week of calm commuting, higher. It is an estimate of the next stretch, not a fixed number. See [TrueRange vs IDC range](@truerange-vs-idc-range).
"""),
("When range drops suddenly", """
A sudden, lasting drop in similar riding — not a gradual one — is worth a battery check. Book one at any of our showrooms; we will read the pack's state of health and tell you whether it is within normal limits. See the [battery warranty guide](@ather-battery-warranty-explained).
"""),
],
"faqs": [
("Which Ather ride mode gives the most range?", "SmartEco, which adapts power delivery to your riding to maximise efficiency."),
("Does tyre pressure affect electric scooter range?", "Yes. Under-inflated tyres increase rolling resistance, reducing range and increasing tyre wear."),
("Why does my Ather's range estimate change?", "The dashboard estimate is based on your recent riding. Harder riding lowers it; calmer riding raises it."),
],
"related": ["truerange-vs-idc-range", "ather-battery-care-in-hot-weather", "ather-charging-cost-per-km"],
},
]
