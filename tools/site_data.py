#!/usr/bin/env python3
"""
site_data.py  —  Version: V1
Single source of truth for everything repeated across the Pillai Auto site:
the four branches and the scooter line-up.

Edit values here, then run:  python tools/build_pages.py
That regenerates scooters/*.html and locations/*.html only. Every other page
is hand-written and is never touched by the generator.

Prices are indicative ex-showroom figures as of 22 August 2026.
"""

BUSINESS = {
    "name": "Pillai Auto",
    "legal": "Pillai Auto Private Limited",
    "domain": "https://www.pillaiauto.in",
    "phone_display": "+91 89258 15877",
    "phone_e164": "+918925815877",
    "whatsapp": "918925815877",
    "email": "sales@pillaiauto.in",          # TODO(client): confirm
    "hours": "Mon – Sat, 9:30 am – 7:30 pm · Sunday, 10:00 am – 6:00 pm",
}

# ---------------------------------------------------------------------------
# Branches.  Addresses are from public Ather dealer listings — TODO(client):
# check each one against the Google Business Profile, byte for byte, and add
# the branch-specific phone numbers before launch.
# ---------------------------------------------------------------------------
BRANCHES = [
    {
        "slug": "chennai-omr",
        "name": "Chennai — OMR, Kottivakkam",
        "short": "Chennai (OMR)",
        "city": "Chennai",
        "region": "TN",
        "street": "4/331A, Rajiv Gandhi Salai (OMR), Kottivakkam",
        "locality": "Chennai",
        "pin": "600041",
        "phone_display": "+91 89258 15877",
        "phone_e164": "+918925815877",
        "whatsapp": "918925815877",
        "lat": "12.9601", "lng": "80.2545",
        "blurb": "Our main showroom and the flagship Ather experience centre on OMR. "
                 "Full line-up on the floor, test rides from the door, service bays "
                 "and a finance desk in the same building.",
        "serves": "Kottivakkam, Thiruvanmiyur, Perungudi, Sholinganallur, Velachery, "
                  "Adyar, Navalur and the whole IT corridor.",
        "is_primary": True,
    },
    {
        "slug": "chengalpattu",
        "name": "Chengalpattu — GST Road",
        "short": "Chengalpattu",
        "city": "Chengalpattu",
        "region": "TN",
        "street": "SF. No. 86/2A1, GST Pulipakkam Road",
        "locality": "Chengalpattu",
        "pin": "603001",
        "phone_display": "+91 89258 15877",   # TODO(client): branch number
        "phone_e164": "+918925815877",
        "whatsapp": "918925815877",
        "lat": "12.6819", "lng": "79.9864",
        "blurb": "On the GST Road at Pulipakkam, convenient for Chengalpattu town, "
                 "Maraimalai Nagar and the Mahindra City belt.",
        "serves": "Chengalpattu, Maraimalai Nagar, Singaperumal Koil, Guduvancheri "
                  "and Kanchipuram district.",
        "is_primary": False,
    },
    {
        "slug": "pondicherry",
        "name": "Puducherry — 100 Ft Road",
        "short": "Puducherry",
        "city": "Puducherry",
        "region": "PY",
        "street": "No. 27, Sundarraja Nagar, 100 Ft Road",
        "locality": "Puducherry",
        "pin": "605004",
        "phone_display": "+91 89258 15877",   # TODO(client): branch number
        "phone_e164": "+918925815877",
        "whatsapp": "918925815877",
        "lat": "11.9416", "lng": "79.8083",
        "blurb": "The authorised Ather showroom for Puducherry, on 100 Ft Road at "
                 "Sundarraja Nagar. Sales, service and fast charging in one place.",
        "serves": "Puducherry, Villianur, Ariyankuppam, Bahour and Karaikal.",
        "is_primary": False,
    },
    {
        "slug": "chidambaram",
        "name": "Chidambaram — Cuddalore Bye-Pass Road",
        "short": "Chidambaram",
        "city": "Chidambaram",
        "region": "TN",
        "street": "Cuddalore Bye-Pass Road, Thillainayagapuram (beside Oxford English School)",
        "locality": "Chidambaram",
        "pin": "608102",
        "phone_display": "+91 89258 15877",   # TODO(client): branch number
        "phone_e164": "+918925815877",
        "whatsapp": "918925815877",
        "lat": "11.3990", "lng": "79.6912",
        "blurb": "Serving Chidambaram and the wider Cuddalore district from the "
                 "bye-pass road, with sales, service and delivery across the region.",
        "serves": "Chidambaram, Cuddalore, Neyveli, Kattumannarkoil and Sirkazhi.",
        "is_primary": False,
    },
]

M = "https://media.atherenergy.com/"

# ---------------------------------------------------------------------------
# Scooters.  Specs from Ather's own pages and published specification sheets,
# August 2026.  TODO(client): re-check prices whenever Ather revises them —
# they also appear in price-chennai.html and compare.html.
# ---------------------------------------------------------------------------
MODELS = [
    {
        "slug": "ather-450-apex",
        "name": "Ather 450 Apex",
        "family": "450",
        "order": 1,
        "status": "on-sale",
        "eyebrow": "The quick one",
        "tagline": "India's fastest electric scooter",
        "intro": "Warp+ mode, magnesium where it matters and 100 km/h on the clock. "
                 "The 450 Apex is the one you buy when the commute is also the fun part.",
        "price": 194946,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Ather-450-Apex-optin.webp",
        "card": M + "450%20Apex%20-%20%20-%20Product%20card.png",
        "stats": [("2.9", "s", "0 – 40 km/h"), ("100", "km/h", "Top speed"),
                  ("165", "km", "IDC range"), ("7", "kW", "Peak power")],
        "specs": [
            ("Peak power", "7 kW"), ("Torque", "26 Nm"),
            ("0 – 40 km/h", "2.9 s (Warp+)"), ("Top speed", "100 km/h"),
            ("Battery", "3.7 kWh"), ("IDC range", "165 km"),
            ("Charging (0–100%)", "About 5 hr 15 min"),
            ("Kerb weight", "111.6 kg"),
            ("Brakes", "Disc front 200 mm / disc rear 190 mm, CBS"),
            ("Dashboard", "17.7 cm (7\") TFT touchscreen"),
            ("Navigation", "Google Maps platform"),
            ("Software", "AtherStack Pro included"),
            ("Battery warranty", "Up to 5 years"),
        ],
        "colours": [("Indium Blue", "#2f5d92", M + "Ather-450-Apex-optin.webp")],
        "highlights": [
            ("Warp+", "A dedicated mode that unlocks the full 7 kW. 0–40 km/h in 2.9 seconds."),
            ("Magnesium build", "Lighter unsprung and structural components than the 450X, so it changes direction faster."),
            ("100 km/h", "Genuinely quick on the ECR and the OMR service roads, with the stability to use it."),
            ("AtherStack Pro", "Every connected feature switched on from day one, no add-on pack."),
        ],
        "buyers": "Riders who want the quickest scooter on the road and will actually use the performance.",
    },
    {
        "slug": "ather-450x",
        "name": "Ather 450X",
        "family": "450",
        "order": 2,
        "status": "on-sale",
        "eyebrow": "The all-rounder",
        "tagline": "Motorsport form, everyday sense",
        "intro": "6.4 kW, a 7-inch touchscreen and the full connected feature set. "
                 "The 450X is the one most Chennai buyers land on, and it is the one "
                 "we keep most stock of.",
        "price": 152498,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "ather-450-overtones-new-d.webp",
        "card": M + "Ather-450-electric-scooter.webp",
        "stats": [("3.3", "s", "0 – 40 km/h"), ("90", "km/h", "Top speed"),
                  ("161", "km", "IDC range"), ("6.4", "kW", "Peak power")],
        "specs": [
            ("Peak power", "6.4 kW"), ("Torque", "26 Nm"),
            ("0 – 40 km/h", "3.3 s"), ("Top speed", "90 km/h"),
            ("Battery", "2.9 kWh / 3.7 kWh"), ("IDC range", "126 km / 161 km"),
            ("Fast charge", "About 30 km in 10 min on Ather Grid"),
            ("Brakes", "Dual disc, CBS"),
            ("Dashboard", "17.7 cm (7\") TFT touchscreen"),
            ("Navigation", "Google Maps platform"),
            ("Magic Twist", "Yes"),
            ("Traction control", "Multi-Mode: Rain, Road, Rally"),
            ("Battery warranty", "Up to 8 years"),
        ],
        "colours": [
            ("Cosmic Black", "#15171a", M + "450x-mono-cosmic-black-d.webp"),
            ("True Red", "#b0202a", M + "450x-mono-true-red-d.webp"),
            ("Space Grey", "#4c5259", M + "450x-overtones-space-grey-d.webp"),
            ("Lunar Grey", "#8d949b", M + "450x-overtones-lunar-grey-d.webp"),
            ("Still White", "#edeff1", M + "450x-overtones-still-white-d.webp"),
            ("Stealth Blue", "#33506b", M + "450x-matte-stealth-blue-d.webp"),
            ("Hyper Sand", "#c8b391", M + "450x-matte-hyper-sand-d.webp"),
        ],
        "highlights": [
            ("Magic Twist", "Twist up to slow down and put charge back in the pack. One-hand riding in traffic."),
            ("7-inch touchscreen", "Google Maps, WhatsApp alerts, call and music control, live cricket scores."),
            ("Multi-Mode Traction Control", "Rain, Road and Rally — Rain earns its keep between October and December here."),
            ("Pothole+ alerts", "Warns you about rough patches other Ather riders have already hit."),
        ],
        "buyers": "The default choice. Solo commuters and enthusiasts who want the full feature set.",
    },
    {
        "slug": "ather-450s",
        "name": "Ather 450S",
        "family": "450",
        "order": 3,
        "status": "on-sale",
        "eyebrow": "The value one",
        "tagline": "The 450 ride, for less",
        "intro": "Same chassis, same motor, same 90 km/h. The 450S trims the "
                 "touchscreen and a couple of software features to land meaningfully "
                 "cheaper — and it is still a proper 450.",
        "price": 135999,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "450s-still-white-d.webp",
        "card": M + "Ather-450-electric-scooter.webp",
        "stats": [("3.9", "s", "0 – 40 km/h"), ("90", "km/h", "Top speed"),
                  ("161", "km", "IDC range"), ("6.4", "kW", "Peak power")],
        "specs": [
            ("Peak power", "6.4 kW"), ("Torque", "26 Nm"),
            ("0 – 40 km/h", "3.9 s"), ("Top speed", "90 km/h"),
            ("Battery", "2.9 kWh / 3.7 kWh"), ("IDC range", "122 km / 161 km"),
            ("Fast charge", "About 30 km in 10 min on Ather Grid"),
            ("Brakes", "Dual disc, CBS"),
            ("Dashboard", "17.7 cm (7\") DeepView™ display"),
            ("Navigation", "Turn-by-turn"),
            ("Magic Twist", "Not available"),
            ("Traction control", "Multi-Mode: Rain, Road, Rally"),
            ("Battery warranty", "Up to 8 years"),
        ],
        "colours": [
            ("Still White", "#edeff1", M + "450s-still-white-d.webp"),
            ("Cosmic Black", "#15171a", M + "450s-cosmic-black-d.webp"),
            ("True Red", "#b0202a", M + "450s-true-red-d.webp"),
            ("Stealth Blue", "#33506b", M + "450s-stealth-blue-d.webp"),
            ("Hyper Sand", "#c8b391", M + "450s-hyper-sand-d.webp"),
        ],
        "highlights": [
            ("Same hardware where it counts", "Identical motor, chassis and brakes to the 450X. The difference is the screen and software."),
            ("DeepView display", "A 7-inch non-touch display that stays readable in Chennai's midday sun."),
            ("Multi-Mode Traction Control", "Rain, Road and Rally, same as the 450X."),
            ("Up to 8-year battery warranty", "The same Eight70 cover as the rest of the range."),
        ],
        "buyers": "First-time EV buyers who want a 450 without paying for the touchscreen.",
    },
    {
        "slug": "ather-rizta-z",
        "name": "Ather Rizta Z",
        "family": "Rizta",
        "order": 4,
        "status": "on-sale",
        "eyebrow": "The family one",
        "tagline": "Built around the second seat",
        "intro": "56 litres of storage, a proper flat floorboard, a pillion backrest "
                 "as standard and a 7-inch touchscreen. The Rizta Z is the school-run "
                 "and grocery-run scooter that happens to be electric.",
        "price": 136999,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Rizta-Terracotta-Red-Duo-New-1.webp",
        "card": M + "Ather-rizta-electric-scooter.webp",
        "stats": [("80", "km/h", "Top speed"), ("161", "km", "IDC range"),
                  ("56", "L", "Total storage"), ("4.3", "kW", "Peak power")],
        "specs": [
            ("Peak power", "4.3 kW"), ("Torque", "22 Nm"),
            ("Top speed", "80 km/h"),
            ("Battery", "2.9 kWh / 3.7 kWh"), ("IDC range", "123 km / 161 km"),
            ("Charging (0–100%)", "About 5 hr 15 min on the 3.7 kWh pack"),
            ("Storage", "34 L boot + 22 L frunk = 56 L"),
            ("Kerb weight", "About 119 kg"),
            ("Brakes", "Disc front 200 mm / drum rear 130 mm, CBS"),
            ("Tyres", "90/90-12 front, 100/80-12 rear, tubeless"),
            ("Dashboard", "17.7 cm (7\") TFT touchscreen"),
            ("Navigation", "Google Maps, turn-by-turn"),
            ("Seat", "Premium dual-tone, pillion backrest standard"),
            ("Battery warranty", "Up to 8 years"),
        ],
        "colours": [
            ("Terracotta Red (Duo)", "#a8412f", M + "Rizta-Terracotta-Red-Duo-New-1.webp"),
            ("Terracotta Red (Super Matte)", "#93382a", M + "RizTA-Red-Super-Matte%20(1).webp"),
            ("Pangong Blue (Duo)", "#3a5f80", M + "Blue-Duo.png"),
            ("Pangong Blue (Mono)", "#33536f", M + "Blue-Mono.png"),
            ("Deccan Grey (Duo)", "#6f757b", M + "Grey-Duo.png"),
            ("Deccan Grey (Mono)", "#5f656b", M + "Grey-Mono.png"),
            ("Siachen White (Mono)", "#eef0f1", M + "White-Mono.png"),
            ("Alphonso Yellow (Duo)", "#d8a53a", M + "Yellow-Duo.png"),
            ("Cardamom Green (Duo)", "#5c7f60", M + "Green-Duo.png"),
        ],
        "highlights": [
            ("56 litres of storage", "34 L under the seat plus a 22 L frunk. Two helmets, or a week's groceries."),
            ("Flat floorboard", "Room for a gas cylinder, a school bag or a suitcase — the thing scooters are actually bought for."),
            ("Pillion backrest as standard", "Not an accessory. It comes fitted."),
            ("7-inch touchscreen", "Google Maps, calls, music and WhatsApp alerts, same as the 450X."),
        ],
        "buyers": "Families, and anyone who carries a pillion or luggage more days than not.",
    },
    {
        "slug": "ather-rizta-s",
        "name": "Ather Rizta S",
        "family": "Rizta",
        "order": 5,
        "status": "on-sale",
        "eyebrow": "The sensible one",
        "tagline": "The family scooter, keenly priced",
        "intro": "The same practical Rizta body, storage and backrest, with a "
                 "DeepView display instead of the touchscreen. Our cheapest way "
                 "into an Ather.",
        "price": 121499,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "White-Mono.png",
        "card": M + "Ather-rizta-electric-scooter.webp",
        "stats": [("80", "km/h", "Top speed"), ("161", "km", "IDC range"),
                  ("56", "L", "Total storage"), ("4.3", "kW", "Peak power")],
        "specs": [
            ("Peak power", "4.3 kW"), ("Torque", "22 Nm"),
            ("Top speed", "80 km/h"),
            ("Battery", "2.9 kWh / 3.7 kWh"), ("IDC range", "123 km / 161 km"),
            ("Charging (0–100%)", "About 8 hr 20 min on the 2.9 kWh pack"),
            ("Storage", "34 L boot + 22 L frunk = 56 L"),
            ("Kerb weight", "About 125 kg"),
            ("Brakes", "Disc front 200 mm / drum rear 130 mm, CBS"),
            ("Dashboard", "17.7 cm (7\") DeepView™ display"),
            ("Navigation", "Turn-by-turn"),
            ("Seat", "Standard black, pillion backrest standard"),
            ("Battery warranty", "Up to 8 years"),
        ],
        "colours": [
            ("Siachen White (Mono)", "#eef0f1", M + "White-Mono.png"),
            ("Deccan Grey (Mono)", "#5f656b", M + "Grey-Mono.png"),
            ("Pangong Blue (Mono)", "#33536f", M + "Blue-Mono.png"),
            ("Terracotta Red (Super Matte)", "#93382a", M + "RizTA-Red-Super-Matte%20(1).webp"),
        ],
        "highlights": [
            ("Lowest entry price in the range", "The cheapest new Ather we sell, and it is still a full-size family scooter."),
            ("Same 56 L storage", "Nothing is taken away from the boot or the frunk."),
            ("DeepView display", "Non-touch, high contrast, easy to read in direct sun."),
            ("Up to 8-year battery warranty", "Identical cover to the Rizta Z."),
        ],
        "buyers": "Budget-conscious family buyers, and anyone stepping off a 110cc petrol scooter.",
    },
    {
        "slug": "ather-konarc",
        "name": "Ather Konarc",
        "family": "Konarc",
        "order": 6,
        "status": "coming-soon",
        "launch_date": "29 August 2026",
        "eyebrow": "Launching 29 August 2026",
        "tagline": "Ather's mass-market scooter",
        "intro": "The production version of the EL01 concept, built on Ather's new "
                 "EL platform. It is unveiled at Ather Community Day on 29 August 2026. "
                 "Register your interest with us now and we will call you with real "
                 "prices and specifications the day they are announced.",
        "price": None,
        "price_note": "Price not yet announced",
        "hero": None,
        "card": None,
        "stats": [],
        "specs": [
            ("Platform", "New EL platform (EL01 concept, production form)"),
            ("Launch", "29 August 2026, Ather Community Day"),
            ("Expected price", "Reported around ₹1.00 – 1.25 lakh ex-showroom — not confirmed"),
            ("Battery", "EL platform supports 2 kWh to 5 kWh — Konarc pack not confirmed"),
            ("Wheels", "Reported 14-inch front, 12-inch rear — not confirmed"),
            ("Brakes", "Reported disc front, drum rear — not confirmed"),
            ("Display", "Reported 7-inch TFT with smartphone connectivity — not confirmed"),
            ("Range and motor", "Not disclosed by Ather"),
        ],
        "colours": [],
        "highlights": [
            ("A new platform, not a trim", "The EL platform is a fresh, scalable architecture rather than a variant of the 450 or Rizta."),
            ("Aimed at the mass market", "Ather's push into the volume segment currently held by petrol 110cc scooters."),
            ("Specs land on 29 August", "Ather has deliberately held back the details until Community Day."),
            ("Book your slot early", "Launch allocations move quickly. An early enquiry puts you near the front of our list."),
        ],
        "buyers": "Anyone waiting for a more affordable Ather. Register interest now, decide after the launch.",
    },
]

def by_slug(slug):
    return next(m for m in MODELS if m["slug"] == slug)

def on_sale():
    return [m for m in MODELS if m["status"] == "on-sale"]

def rupees(n):
    """Indian digit grouping: 152498 -> 1,52,498"""
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail
