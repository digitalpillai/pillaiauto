#!/usr/bin/env python3
"""
guides_features.py  —  Version: V1  (12 Nov 2026)
"Features explained" guides. Feature availability from Ather's published
specification sheets (Nov 2026); copy is Pillai Auto's own.
"""
M = "https://media.atherenergy.com/"

GUIDES = [
# ---------------------------------------------------------------------------
{
"slug": "warp-mode-explained",
"cluster": "features",
"title": "Ather Warp and Warp+ Mode Explained | Pillai Auto",
"desc": "What Ather's Warp and Warp+ modes do, how they differ from Sport, what they cost in range, and which 450 models have them.",
"h1": "Warp and Warp+ mode, explained",
"lede": "Warp is the mode that made the Ather 450 famous: twist the throttle and the scooter simply goes. Here is what it actually changes, what it costs you in range, and when it is worth using.",
"img": M + "Ather-450-apex-electric-scooter-model.webp",
"models": ["ather-450x", "ather-450-apex"],
"facts": [("Warp", "450X"), ("Warp+", "450 Apex only"), ("Apex 0–40 km/h", "2.9 s"), ("450X 0–40 km/h", "3.3 s")],
"body": [
("What Warp changes", """
Every Ather has ride modes that change how much of the motor's power is available and how sharply it responds to the throttle. The 450 series offers SmartEco, Eco, Ride and Sport; the 450X adds **Warp**, which unlocks the motor's full output and the most immediate throttle response. On the 450X that means 6.4 kW and 26 Nm, and 0–40 km/h in 3.3 seconds.

**Warp+** is exclusive to the 450 Apex. It goes a step further with 7 kW of peak power, 0–40 km/h in 2.9 seconds and a 100 km/h top speed.
"""),
("Which models have it", """
| Model | Fastest mode | 0–40 km/h | Top speed |
|---|---|---|---|
| 450 Apex | Warp+ | 2.9 s | 100 km/h |
| 450X | Warp | 3.3 s | 90 km/h |
| 450S | Sport | 3.9 s | 90 km/h |
| Rizta S / Z | Zip | 4.7 s | 80 km/h |
| Konarc S | Power | 4.7–5.0 s | 70 km/h |
"""),
("What it costs in range", """
Hard acceleration uses energy quickly. Riding everywhere in Warp will cut your range noticeably compared with Ride or SmartEco — the motor is doing more work every time you pull away. Most owners we see use Ride or SmartEco day to day and switch to Warp for overtaking or an empty stretch of road. Switching takes a press of a button while riding.
"""),
("When Warp is genuinely useful", """
- **Merging and overtaking** on the OMR or GST Road, where a quick burst gets you clear of a bus or lorry safely.
- **Pulling away from a junction** across a busy road.
- **Climbing a flyover with a pillion**, where the extra torque keeps your speed up.

It is not a mode for wet roads or loose surfaces. On the 450X and Apex, Multi-Mode Traction Control helps, but smooth throttle is still your best friend in the rain.
"""),
],
"faqs": [
("Does the Ather 450S have Warp mode?", "No. The 450S's fastest mode is Sport. Warp is on the 450X, and Warp+ on the 450 Apex."),
("Can I switch to Warp while riding?", "Yes. Ride modes can be changed on the move from the switchgear."),
("Does Warp mode reduce battery life?", "Warp uses more energy per kilometre, so it reduces range on that charge. Using it occasionally does not meaningfully change the battery's long-term health."),
],
"related": ["ather-450-apex-vs-450x", "how-to-get-more-range-from-your-ather", "traction-control-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "infinite-cruise-explained",
"cluster": "features",
"title": "Ather Infinite Cruise Explained: City Cruise, Hill & Crawl",
"desc": "How Ather's Infinite Cruise works — City Cruise, Hill Control and Crawl Control — which models have it, and how it helps in Chennai traffic.",
"h1": "Infinite Cruise, explained",
"lede": "Cruise control on a scooter sounds like a highway feature. Ather's Infinite Cruise is built for the opposite: stop-go city traffic, flyovers and crawling queues. Here is what each part does.",
"img": M + "Apex-with-cruise.webp",
"img_alt": "Ather 450 Apex with Infinite Cruise",
"models": ["ather-450x", "ather-450-apex"],
"facts": [("Parts", "City Cruise · Hill Control · Crawl Control"), ("Models", "450X, 450 Apex"), ("Delivered", "Over-the-air update")],
"body": [
("The three parts", """
### City Cruise
Holds your chosen speed without you holding the throttle, so your wrist can relax on a steady stretch. Touch the brake or the throttle and control returns to you instantly.

### Hill Control
Manages speed on slopes — up a flyover ramp or down a basement car-park ramp — so the scooter neither rolls back nor runs away.

### Crawl Control
Keeps the scooter moving at walking pace in a crawling queue, so you are not constantly feathering the throttle in Kathipara-style traffic.
"""),
("Which Athers have it", """
Infinite Cruise is available on the 450X and the 450 Apex, delivered over the air through AtherStack updates. It is not offered on the 450S, Rizta or Konarc.
"""),
("Using it safely", """
Cruise features reduce fatigue; they do not replace attention. Keep a hand ready on the brake in traffic, switch cruise off on wet roads or in heavy rain, and remember that the scooter will not brake for you. The first few times, try City Cruise on a quiet road near home before using it in a queue.
"""),
("Why it matters on a long commute", """
Riders who do 30–60 km a day tell us the difference is in their wrist and shoulders at the end of the week. If that sounds like you, Infinite Cruise is one of the stronger reasons to choose a 450X over a 450S. See [our long-commute guide](@ather-scooter-for-long-commutes).
"""),
],
"faqs": [
("Does the Ather 450S have cruise control?", "No. Infinite Cruise is available on the 450X and 450 Apex."),
("How do I turn off cruise control?", "Applying the brake or using the throttle hands control straight back to you."),
("Did older 450X scooters get Infinite Cruise?", "Infinite Cruise is delivered over the air. Whether a particular older scooter is eligible depends on its hardware and software — bring it in or call us and we will check."),
],
"related": ["ather-450-apex-vs-450x", "atherstack-pro-explained", "magic-twist-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "magic-twist-explained",
"cluster": "features",
"title": "Ather Magic Twist Explained: Braking With the Throttle",
"desc": "How Ather's Magic Twist uses regenerative braking when you roll the throttle back, how it saves brake pads and range, and which models have it.",
"h1": "Magic Twist, explained",
"lede": "Magic Twist lets you slow an Ather down by rolling the throttle backwards, the motor recovering energy as it brakes. It feels odd for a day and natural for ever after. Here is how it works.",
"img": M + "450x-touchscreen-dashboard.webp",
"models": ["ather-450x", "ather-450-apex", "ather-rizta-z"],
"facts": [("Works by", "Regenerative braking"), ("Models", "450X, 450 Apex, Rizta Z"), ("Not on", "450S, Rizta S, Konarc S")],
"body": [
("How it works", """
Roll the throttle forward to accelerate as usual. Roll it **past the closed position** and the motor starts working as a generator: it slows the scooter and sends some of that energy back into the battery. The further you roll, the stronger the slowing effect. The brake light comes on so riders behind know you are slowing.
"""),
("Why owners like it", """
- **Smoother city riding.** Most slowing in traffic is gentle; you can do it without moving your fingers to the brake levers.
- **Less brake wear.** The pads do less work, so they last longer.
- **A little more range.** Energy recovered while slowing goes back into the battery.
"""),
("It does not replace the brakes", """
Magic Twist is for gradual slowing. For anything sudden — a pedestrian stepping out, a car pulling in — use the brakes. In the wet, make every input smooth, including Magic Twist.
"""),
("Which models have it", """
Magic Twist is available on the 450X, 450 Apex and Rizta Z. The 450S, Rizta S and Konarc S do not have it, though all Athers recover some energy through regeneration when you brake.
"""),
("Getting used to it", """
Most riders feel at home with Magic Twist within a few days. On your first ride, try it on an empty street: roll back a little and feel the scooter ease off, then a little more. Use it for the long, gentle slow-downs — approaching a signal you can see turning red, rolling off a flyover — and keep your fingers near the levers for everything else. Within a week you will notice you touch the brakes far less in town, and so will your brake pads.
"""),
],
"faqs": [
("Is Magic Twist available on the Rizta S?", "No. On the Rizta, Magic Twist is a Rizta Z feature."),
("Does Magic Twist turn on the brake light?", "Yes, the brake light comes on when Magic Twist is slowing the scooter."),
("Does Magic Twist increase range?", "It recovers some energy while slowing, which helps range slightly — most noticeably in stop-start traffic."),
],
"related": ["ather-450x-vs-450s", "how-to-get-more-range-from-your-ather", "infinite-cruise-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "skidcontrol-explained",
"cluster": "features",
"title": "Ather Rizta SkidControl Explained | Pillai Auto",
"desc": "What SkidControl does on the Ather Rizta Z, the road surfaces where it helps most in Chennai and Puducherry, and its limits.",
"h1": "SkidControl on the Rizta, explained",
"lede": "SkidControl is the Rizta Z's traction assistance system. It is designed for the moments that unsettle a family scooter most: a rear wheel meeting sand, wet paint or a slick patch while you are carrying someone.",
"img": M + "Ather-rizta-family-e-scooter-2026.webp",
"img_alt": "Ather Rizta Z",
"models": ["ather-rizta-z"],
"facts": [("Model", "Rizta Z"), ("Helps on", "Wet, sandy and bumpy surfaces"), ("Works with", "Your throttle — automatically")],
"body": [
("What it does", """
When the rear wheel starts to spin faster than the scooter is moving — the beginning of a skid under power — SkidControl reduces the motor's output until the tyre grips again. It all happens automatically, faster than a rider could react.
"""),
("Where it helps around here", """
- **Sand on the road** near the beach roads of the ECR and Puducherry, and on village roads in Cuddalore district.
- **Painted road markings and manhole covers** after rain, which are far more slippery than the asphalt around them.
- **Wet basement ramps** in apartment car parks.
- **Broken patches** where the rear wheel briefly leaves the ground over a bump.
"""),
("What it does not do", """
SkidControl manages traction under power. It does not stop a skid caused by braking too hard, and it cannot overcome the laws of physics on a flooded or oily road. Ride gently in the wet and keep tyres properly inflated — see our [monsoon guide](@riding-your-ather-in-the-chennai-monsoon).
"""),
("Rizta Z or Rizta S?", """
SkidControl is one of the main reasons we recommend the [Rizta Z](/scooters/ather-rizta-z.html) to families who regularly carry a child or parent. The [Rizta S](/scooters/ather-rizta-s.html) does without it. Our [Rizta Z vs S comparison](@ather-rizta-z-vs-rizta-s) has the full list.
"""),
("If the rear slides anyway", """
No system makes a scooter impossible to skid. If you feel the rear wheel step out, ease off the throttle smoothly rather than snapping it shut, keep looking where you want to go, and avoid grabbing the front brake hard while the scooter is leaning. Most small slides correct themselves once power comes off — which is exactly what SkidControl is doing for you, faster.
"""),
],
"faqs": [
("Does the Rizta S have SkidControl?", "No, SkidControl is a Rizta Z feature."),
("Is SkidControl the same as ABS?", "No. SkidControl manages traction when power is applied; ABS prevents wheels locking under braking. They solve different problems."),
("Can I switch SkidControl off?", "SkidControl is designed to work in the background. Ask us at delivery and we will walk you through the settings available on your software version."),
],
"related": ["ather-rizta-family-guide", "traction-control-explained", "crash-alert-and-safety-features-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "traction-control-explained",
"cluster": "features",
"title": "Ather Multi-Mode Traction Control: Rain, Road and Rally",
"desc": "How Ather's Multi-Mode Traction Control works on the 450X and 450 Apex, when to use Rain, Road or Rally, and how it compares with SkidControl.",
"h1": "Multi-Mode Traction Control, explained",
"lede": "The 450X and 450 Apex are quick enough to spin their rear wheel on a wet road. Multi-Mode Traction Control lets you choose how much help you get, with three settings for three kinds of surface.",
"img": M + "450x-mono-true-red-d.webp",
"img_alt": "Ather 450X",
"models": ["ather-450x", "ather-450-apex"],
"facts": [("Settings", "Rain · Road · Rally"), ("Models", "450X, 450 Apex"), ("Not on", "450S")],
"body": [
("The three settings", """
| Setting | Use it for | What it does |
|---|---|---|
| Rain | Wet roads, the monsoon, painted markings | Steps in earliest and most firmly |
| Road | Normal dry riding | Balanced intervention |
| Rally | Gravel, loose or unpaved surfaces | Allows more wheelspin so the scooter keeps moving |
"""),
("Why it matters with a powerful scooter", """
In Warp or Warp+, the 450's instant torque can overwhelm the rear tyre's grip on a wet surface. Traction control trims power the moment the rear wheel starts to spin, so you stay upright and keep moving. It is most valuable in exactly the conditions where riders are already tense.
"""),
("Our setting advice for Chennai", """
Use **Road** most of the year. Switch to **Rain** from the first heavy shower of the north-east monsoon — usually October — and on any day the roads are wet. **Rally** is for genuinely loose surfaces like a gravel track or a sandy approach road; on tarmac, Road or Rain is safer.
"""),
("Traction control vs SkidControl", """
Both manage wheelspin under power. Multi-Mode Traction Control on the 450X and Apex gives you three selectable levels to suit a sporty scooter. [SkidControl](@skidcontrol-explained) on the Rizta Z is tuned for a family scooter and works automatically.
"""),
("Tyres matter more than any setting", """
Traction control can only use the grip your tyres have. Before the monsoon, check the tread: if the grooves are shallow or the tyre shows cracks, replace it — worn tyres are the biggest wet-weather risk on any scooter. Keep pressures at the figure on the sticker or in your owner's manual, checked when the tyres are cold. We check tread and pressure at every periodic service and fit genuine replacement tyres.
"""),
],
"faqs": [
("Does the Ather 450S have traction control?", "No. Multi-Mode Traction Control is on the 450X and 450 Apex."),
("Which traction control mode should I use in the rain?", "Rain mode. It intervenes earliest and most firmly to limit wheelspin on wet surfaces."),
("Does traction control help when braking?", "No. Traction control manages wheelspin when accelerating. Smooth, progressive braking is still essential in the wet."),
],
"related": ["skidcontrol-explained", "riding-your-ather-in-the-chennai-monsoon", "warp-mode-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "autohold-and-reverse-park-assist-explained",
"cluster": "features",
"title": "Ather AutoHold and Reverse Park Assist Explained",
"desc": "How Ather's AutoHold stops roll-back on slopes and how Reverse Park Assist backs you out of tight spots — with tips for flyovers and basement ramps.",
"h1": "AutoHold and Reverse Park Assist, explained",
"lede": "Two small features that owners mention more than any other in their first week: AutoHold, which stops the scooter rolling back on a slope, and Reverse Park Assist, which backs it out of a tight spot under power.",
"img": M + "450-park-assist-d.webp",
"img_alt": "Ather Reverse Park Assist",
"models": ["ather-konarc", "ather-450s", "ather-rizta-s"],
"facts": [("AutoHold", "Holds the scooter on slopes"), ("Reverse", "Slow, powered reverse"), ("Konarc 2.1 kWh", "Brake-lever activated AutoHold")],
"body": [
("AutoHold", """
Stop on a slope — a flyover queue, a temple approach, a basement ramp — and AutoHold keeps the scooter from rolling back. When you twist the throttle, it releases smoothly and you pull away. No juggling of brake and throttle, and no lurch backwards into the car behind.

On the Konarc 2.1 kWh, AutoHold is activated with the brake lever; on the other variants it works as standard.
"""),
("Reverse Park Assist", """
Engage reverse and the scooter backs up slowly under its own power. On a 125 kg scooter with a pillion, that is the difference between paddling backwards out of a tight spot and simply rolling out. The speed is deliberately low so it stays easy to control.
"""),
("Where they help most", """
- **Apartment car parks**, where you are wedged between cars and a pillar.
- **Steep driveways** and ramps.
- **Flyover traffic** — Kathipara, Koyambedu, Vadapalani — where queues stop on an incline.
- **Senior and new riders**, for whom both features remove a source of stress. See our [senior riders guide](@ather-scooter-for-senior-riders).
"""),
("Tips for first-time users", """
Practise reverse in an empty space before using it beside parked cars, and look behind you rather than relying on hearing — the scooter is quiet. On a very steep or wet slope, keep a hand on the brake as AutoHold releases until you are used to how it feels.
"""),
],
"faqs": [
("Do all Ather scooters have reverse?", "Reverse Mode or Reverse Park Assist is listed across the current Ather range. Ask us to demonstrate it on the model you are considering."),
("Does AutoHold work on the Konarc 2.1 kWh?", "Yes, but on the 2.1 kWh variant it is activated with the brake lever."),
("Is reverse fast?", "No. Reverse speed is deliberately limited so it is easy to control in tight spaces."),
],
"related": ["ather-scooter-for-senior-riders", "charging-ather-at-home-in-a-chennai-apartment", "ather-konarc-buyers-guide"],
},
# ---------------------------------------------------------------------------
{
"slug": "crash-alert-and-safety-features-explained",
"cluster": "features",
"title": "Ather Safety Features: Crash Alert, FallSafe, Stop Signal",
"desc": "Ather's rider safety features explained: Crash Alert, FallSafe, the Emergency Stop Signal and auto indicator cut-off — what each does and where to find it.",
"h1": "Crash Alert, FallSafe and Ather's safety features",
"lede": "Some of Ather's most valuable features are ones you hope never to use. Here is what each safety feature does, so you know what to expect — and what to set up on delivery day.",
"img": M + "Ather-450-dash-Live-Location-Sharing.webp",
"img_alt": "Live location sharing on the Ather dashboard",
"models": ["ather-rizta-z", "ather-450x", "ather-konarc"],
"facts": [("Crash Alert", "Rizta Z"), ("FallSafe", "Most models (Konarc: 2.7 / 3.5 kWh)"), ("Emergency Stop Signal", "Flashes under hard braking")],
"body": [
("Crash Alert", """
If the Rizta Z detects a crash, Crash Alert notifies your chosen emergency contacts with your location and shows their details on the dashboard, so anyone helping you can reach them. It only works if contacts are set up in the Ather app — we do this with you at delivery.
"""),
("FallSafe", """
If the scooter falls over, FallSafe cuts power to the motor so the rear wheel does not keep spinning or drive the scooter along the ground. It is listed on the 450 series and Rizta, and on the Konarc's 2.7 and 3.5 kWh variants.
"""),
("Emergency Stop Signal", """
Under hard braking, the brake light flashes rapidly to warn the vehicle behind that you are stopping suddenly. In dense traffic, those extra fractions of a second for the driver behind matter.
"""),
("Live location sharing", """
On models with the touchscreen dashboard, you can share your live location with family from the scooter — reassuring for a late ride home or a long trip down the ECR.
"""),
("Set them up at delivery", """
Safety features that depend on contacts or the app do nothing until they are configured. At delivery we pair the scooter with your phone, add emergency contacts, and show you where each setting lives. If you bought elsewhere, any of our showrooms will help. See our [delivery day checklist](@ather-delivery-day-checklist).
"""),
("Tell your emergency contacts", """
Let the people you add as emergency contacts know they are listed, and what an alert from your scooter would mean. Keep their numbers up to date in the app — a contact who changed phones last year is no help. If several people ride the same scooter, make sure each rider's own family is reachable, not just the owner's.
"""),
],
"faqs": [
("Which Ather has Crash Alert?", "Crash Alert is listed for the Rizta Z. Ask us about availability on other models and software versions."),
("What does FallSafe do?", "It cuts power to the motor if the scooter falls over, so it does not keep driving or spinning the rear wheel."),
("Does the Ather flash its brake light in an emergency stop?", "Yes. The Emergency Stop Signal flashes the brake light under hard braking."),
],
"related": ["theft-and-tow-alerts-explained", "ather-rizta-family-guide", "ather-scooter-for-senior-riders"],
},
# ---------------------------------------------------------------------------
{
"slug": "theft-and-tow-alerts-explained",
"cluster": "features",
"title": "Ather Theft and Tow Alerts, Find My Scooter Explained",
"desc": "How Ather's anti-theft features work: Theft & Tow alerts, Find My Scooter, remote motor lock and ParkSafe — and how to set them up properly.",
"h1": "Theft and Tow alerts, explained",
"lede": "An Ather is a connected scooter, which makes it a hard one to steal quietly. Here is how its anti-theft features work, which models have them, and the settings worth checking today.",
"img": M + "1Tow&TheftAlerts.webp",
"img_alt": "Ather Tow and Theft alerts",
"models": ["ather-konarc", "ather-450x", "ather-rizta-z"],
"facts": [("Theft & Tow alerts", "Phone alert if moved"), ("Find My Scooter", "Location in the app"), ("Konarc", "2.7 / 3.5 kWh variants")],
"body": [
("Theft & Tow alerts", """
If the scooter is moved, lifted or towed while parked and locked, the Ather app sends an alert to your phone. You see it within seconds, not when you come back to an empty parking spot.
"""),
("Find My Scooter", """
The app shows where your scooter is. Useful after a theft, and just as useful in a mall basement when you cannot remember which level you parked on. Some models also let you ping the scooter so it signals where it is.
"""),
("Remote lock and the TheftSafe suite", """
Ather's anti-theft suite — including ParkSafe, LockSafe and remote locking, depending on model and software — lets you secure the motor from your phone so the scooter cannot be ridden away. Feature names and availability vary by model; we show you exactly what yours has at delivery.
"""),
("Which models have them", """
Theft & Tow alerts and Find My Scooter are listed across the 450 series and Rizta, and on the Konarc S 2.7 kWh and 3.5 kWh variants (not the 2.1 kWh). Most connected features rely on the scooter's mobile connection, so keep your connectivity plan active.
"""),
("Check these settings today", """
1. Notifications for the Ather app are allowed on your phone.
2. Your scooter shows as online in the app.
3. Family members who use the scooter have their own access, rather than sharing your login.

And do not rely on technology alone: park in lit areas and use a disc lock in public places.
"""),
],
"faqs": [
("Will my Ather alert me if someone tows it?", "Yes, on models with Theft & Tow alerts the app notifies you if the parked scooter is moved or towed."),
("Does the Konarc have theft alerts?", "Theft & Tow alerts and Find My Scooter are listed on the Konarc S 2.7 and 3.5 kWh variants."),
("Do theft features need a subscription?", "Connected features depend on the scooter's connectivity and software plan. We will explain what is included with your model and what AtherStack Pro adds."),
],
"related": ["crash-alert-and-safety-features-explained", "atherstack-pro-explained", "ather-delivery-day-checklist"],
},
# ---------------------------------------------------------------------------
{
"slug": "atherstack-pro-explained",
"cluster": "features",
"title": "AtherStack Pro Explained: What You Get and Is It Worth It",
"desc": "What AtherStack Pro adds to an Ather scooter, how it links to the battery warranty, which models include it, and how to decide if it is worth buying.",
"h1": "AtherStack Pro, explained",
"lede": "AtherStack is the software that runs every Ather. AtherStack Pro is the upgraded package that unlocks the advanced connected and ride features — and it is tied to the battery warranty in a way many buyers miss.",
"img": M + "Ather-450-dash-Google-Map-Platform.webp",
"img_alt": "Google Maps on the Ather dashboard",
"models": ["ather-450-apex", "ather-450x", "ather-rizta-z"],
"facts": [("Included with", "450 Apex"), ("Warranty link", "Free battery upgrade to 5 yr / 60,000 km"), ("Updates", "Over the air")],
"body": [
("What AtherStack does", """
Every Ather runs AtherStack: the dashboard, the app connection, ride modes, charging management and over-the-air (OTA) updates. OTA updates arrive like phone updates and have added real features to scooters already on the road — Infinite Cruise on the 450X is a recent example.
"""),
("What Pro adds", """
AtherStack Pro unlocks the advanced connected and rider-assistance features on supported models. Depending on model and software version this includes navigation features, ride insights, anti-theft tools and alerts. Because the exact list changes with updates, we show you the current Pro feature list for your model on the day, rather than printing one here that could go out of date.
"""),
("The battery warranty link", """
Ather's standard battery warranty is 3 years or 30,000 km. With AtherStack Pro, it gets a free upgrade to **5 years or 60,000 km**. AtherStack Pro is also the route to Ather's extended battery warranty of up to **10 years or 1,00,000 km**. For anyone planning to keep the scooter for years, that alone can justify it. Our [battery warranty guide](@ather-battery-warranty-explained) has the detail.
"""),
("Is it worth it?", """
- **Yes, almost always,** if you plan to keep the scooter more than three years or ride a lot — the warranty benefit is significant.
- **Yes** if you want the connected features day to day.
- **Maybe not** if you are buying a short-term runabout and will sell within a couple of years.

It is included with the [450 Apex](/scooters/ather-450-apex.html); on other models we will price it separately on your quote.
"""),
],
"faqs": [
("Is AtherStack Pro included with the 450 Apex?", "Yes. On other models it is optional."),
("Does AtherStack Pro extend the battery warranty?", "Yes. With AtherStack Pro the standard 3-year / 30,000 km battery warranty gets a free upgrade to 5 years / 60,000 km, and it is the route to the extended warranty of up to 10 years / 1,00,000 km."),
("Do Athers get updates without AtherStack Pro?", "Yes, AtherStack software updates are delivered over the air to Ather scooters; Pro unlocks additional features on supported models."),
],
"related": ["ather-battery-warranty-explained", "ather-450-apex-buyers-guide", "google-maps-on-the-ather-dashboard"],
},
# ---------------------------------------------------------------------------
{
"slug": "google-maps-on-the-ather-dashboard",
"cluster": "features",
"title": "Google Maps on the Ather Dashboard: How It Works",
"desc": "Which Ather scooters show Google Maps navigation on the dashboard, how Push Navigation and Pothole+ alerts work, and how it helps riding in Chennai.",
"h1": "Google Maps on the Ather dashboard",
"lede": "Navigating Chennai with a phone clamped to the handlebar is nobody's idea of fun. On the 450X, 450 Apex and Rizta Z, Google Maps runs on the scooter's own 7-inch touchscreen. Here is how it works.",
"img": M + "Ather-450-dash-Google-Map-Platform.webp",
"img_alt": "Google Maps on the Ather 450 dashboard",
"models": ["ather-450x", "ather-450-apex", "ather-rizta-z"],
"facts": [("Models", "450X, 450 Apex, Rizta Z"), ("Screen", "7-inch touchscreen"), ("Coming", "Konarc Z (listed)"), ("Not on", "450S, Rizta S, Konarc S")],
"body": [
("How it works", """
The scooter's dashboard runs navigation built on the Google Maps platform, using the scooter's own connection. Set a destination from the dashboard or the Ather app and you get turn-by-turn directions on the 7-inch screen in front of you, with your phone safely in your pocket.
"""),
("Features riders use most", """
- **Push Navigation** — send a destination from your phone (for example, a location someone shared on WhatsApp) straight to the scooter.
- **Pothole+ alerts** — warnings about rough patches other Ather riders have reported on your route.
- **WhatsApp on dash** — message previews on the dashboard on supported models.
- **Live location sharing** — let family follow your trip.
- **Live cricket scores** — for the long red-light waits.
"""),
("Which models have it", """
| Model | Google Maps on dashboard |
|---|---|
| 450 Apex | Yes |
| 450X | Yes |
| Rizta Z | Yes |
| 450S | No — DeepView display |
| Rizta S | No — DeepView display |
| Konarc S | No — Konarc Z listed as coming soon |
"""),
("Is it worth paying for?", """
If you regularly ride to new addresses — sales calls, deliveries, visiting relatives in parts of the city you do not know — dashboard navigation is one of the features owners say they would not give up. If your routes rarely change, a phone mount on the 450S or Rizta S does the job.
"""),
("Set off with your route ready", """
Set your destination before you ride, either on the dashboard or by pushing it from your phone through the app, rather than tapping the screen at a signal. Glance at the screen the way you would at a mirror, and let voice prompts through a Halo helmet do the rest. If you change plans mid-ride, pull over to re-route — it takes seconds when you are stopped.
"""),
],
"faqs": [
("Does the Ather 450S have Google Maps?", "No. The 450S has a DeepView display without built-in Google Maps. Maps is on the 450X, 450 Apex and Rizta Z."),
("Does the Ather dashboard need my phone for navigation?", "Navigation runs on the scooter's own dashboard using its connection; you can also push destinations from your phone through the app."),
("Will the Konarc get Google Maps?", "Ather lists built-in Google Maps for the Konarc Z, which is coming soon."),
],
"related": ["ather-450x-vs-450s", "ather-rizta-z-vs-rizta-s", "atherstack-pro-explained"],
},
# ---------------------------------------------------------------------------
{
"slug": "truerange-vs-idc-range",
"cluster": "features",
"title": "Ather TrueRange vs IDC Range: What Range Will I Get?",
"desc": "Why Ather quotes two range figures, IDC and TrueRange, what each means, the real-world range of every Ather, and what changes it on Chennai roads.",
"h1": "TrueRange vs IDC range: what will you actually get?",
"lede": "Every Ather has two range figures. The higher one is the IDC number used for certification; the lower one, TrueRange, is Ather's estimate for real riding. Knowing the difference saves a lot of disappointment.",
"img": M + "ather-app-Real-time-Charge-Status.webp",
"img_alt": "Ather app showing charge status",
"models": ["ather-konarc", "ather-450x", "ather-rizta-z", "ather-450s", "ather-rizta-s", "ather-450-apex"],
"facts": [("IDC", "Lab test cycle"), ("TrueRange", "Ather's real-world estimate"), ("Typical gap", "TrueRange ≈ 80% of IDC")],
"body": [
("Two numbers, two purposes", """
**IDC (Indian Driving Cycle)** is a standardised laboratory test used to certify vehicles. Every manufacturer uses it, so it is useful for comparing scooters with each other — but it is gentler than real roads.

**TrueRange** is Ather's own estimate of what a typical rider will see in mixed real-world riding. It is the number to plan your day around.
"""),
("Every Ather, both figures", """
| Model and battery | IDC range | TrueRange |
|---|---|---|
| Konarc S 2.1 kWh | 100 km | 80 km |
| Konarc S 2.7 kWh | 125 km | 100 km |
| Konarc S 3.5 kWh | 161 km | 130 km |
| 450S / 450X 2.9 kWh | 122 / 126 km | 105 km |
| 450S / 450X 3.5 kWh | 161 km | 130 km |
| 450 Apex 3.5 kWh | 165 km | 130 km |
| Rizta, smaller battery | 123 km | 100 km |
| Rizta 3.5 kWh | 161 km | 125 km |
"""),
("What changes your range", """
- **Ride mode.** Warp and Sport use far more energy than SmartEco and Eco.
- **Speed.** Range drops noticeably above 60 km/h.
- **Load.** A pillion and a full boot add weight the motor must move.
- **Stop-start traffic.** Repeated hard acceleration costs more than steady riding — though regeneration recovers some.
- **Tyre pressure.** Under-inflated tyres quietly eat range.
- **Heat.** Very hot afternoons and a battery left in direct sun can trim range slightly.
"""),
("Getting closer to TrueRange or beyond", """
Smooth throttle, SmartEco mode, correct tyre pressure and steady speeds will usually get you to the TrueRange figure and sometimes past it. Our [range tips guide](@how-to-get-more-range-from-your-ather) goes through each in detail.
"""),
],
"faqs": [
("What is TrueRange on an Ather?", "TrueRange is Ather's own estimate of real-world range in typical mixed riding, as opposed to the IDC laboratory figure used for certification."),
("Why is IDC range higher than real range?", "The IDC test cycle is gentler than real traffic: lower average speeds, no pillion and controlled conditions."),
("Which Ather has the most real-world range?", "With the 3.5 kWh battery, the Konarc S, 450S, 450X and 450 Apex all have a TrueRange estimate of about 130 km; the Rizta 3.5 kWh about 125 km."),
],
"related": ["how-to-get-more-range-from-your-ather", "ather-450-battery-2-9-vs-3-5-kwh", "ather-charging-cost-per-km"],
},
# ---------------------------------------------------------------------------
{
"slug": "ather-halo-smart-helmet-guide",
"cluster": "features",
"title": "Ather Halo Smart Helmet Guide: Features and Compatibility",
"desc": "What the Ather Halo smart helmet does — calls, music, navigation prompts, auto wear-detect — which scooters it pairs with, and sizing tips.",
"h1": "The Ather Halo smart helmet, explained",
"lede": "The Halo is Ather's smart helmet. It pairs with the scooter so calls, music and navigation prompts come through the helmet — no fiddly Bluetooth earpiece under the lining. Here is what it does and who should get one.",
"img": M + "halo-auto-wear-detect-desktop.webp",
"img_alt": "Ather Halo smart helmet",
"models": ["ather-450x", "ather-rizta-z", "ather-450-apex"],
"facts": [("Pairs with", "Your Ather scooter"), ("Auto wear-detect", "Connects when you put it on"), ("For children", "Ather Junior helmets")],
"body": [
("What it does", """
- **Calls** through the helmet's speakers and microphone, answered from the scooter's switchgear.
- **Music** controlled from the handlebar.
- **Navigation prompts** spoken in your ear on models with dashboard navigation.
- **Auto wear-detect**: the helmet connects when you put it on, with no buttons to press.
"""),
("Why owners rate it", """
Taking a call on a scooter usually means pulling over and wrestling with a helmet. With the Halo you answer from the handlebar and keep riding at a sensible pace, eyes on the road. Riders who navigate to unfamiliar addresses find the spoken directions even more useful than the calls.
"""),
("Fit and sizing", """
A smart helmet is a helmet first. Try sizes on at the showroom: it should be snug all round, not move when you shake your head, and not press painfully on your forehead. In Chennai's heat, ventilation matters too — ask to compare models. For young pillions, ask about **Ather Junior helmets**, sized for children.
"""),
("Where to buy", """
We stock the Halo range alongside our scooters and will pair it with your Ather before you leave. See our [Halo page](/halo-smart-helmet.html) for current options and prices.
"""),
("Using calls safely", """
A smart helmet makes calls possible on the move; it does not make them a good idea in every situation. Keep calls short in heavy traffic, pull over for anything that needs your full attention, and keep music low enough to hear horns and sirens. Riders who use the Halo mostly for navigation prompts and quick answers find it makes them safer, not more distracted.
"""),
],
"faqs": [
("Does the Ather Halo work with every Ather?", "The Halo is designed to pair with Ather scooters. Feature support can vary by model and software version — we pair and test it with your scooter at the showroom."),
("Can I answer calls with the Halo while riding?", "Yes. Calls come through the helmet and can be answered from the scooter's switchgear."),
("Does Ather make helmets for children?", "Yes, Ather Junior helmets are sized for children riding pillion."),
],
"related": ["google-maps-on-the-ather-dashboard", "ather-rizta-family-guide", "ather-delivery-day-checklist"],
},
]
