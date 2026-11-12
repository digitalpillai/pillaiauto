#!/usr/bin/env python3
"""
site_data.py  —  Version: V5  (12 Nov 2026: every WhatsApp link goes to 73581 05818.
V4: cards = studio shots, heroes = lifestyle
photos with phone versions, served from assets/media. V3: card backups. V2, 10 Nov: Konarc launched; specs, prices, warranty updated)
Single source of truth for everything repeated across the Pillai Auto site:
the four branches and the scooter line-up.

Edit values here, then run:  python tools/build_site.py
and then:                   python tools/sync_partials.py

Prices are indicative ex-showroom figures as of 10 November 2026.
"""

BUSINESS = {
    "name": "Pillai Auto",
    "legal": "Pillai Auto Private Limited",
    "domain": "https://www.pillaiauto.in",
    "phone_display": "+91 89258 15877",
    "phone_e164": "+918925815877",
    "whatsapp": "917358105818",
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
        "whatsapp": "917358105818",
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
        "whatsapp": "917358105818",
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
        "whatsapp": "917358105818",
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
        "whatsapp": "917358105818",
        "lat": "11.3990", "lng": "79.6912",
        "blurb": "Serving Chidambaram and the wider Cuddalore district from the "
                 "bye-pass road, with sales, service and delivery across the region.",
        "serves": "Chidambaram, Cuddalore, Neyveli, Kattumannarkoil and Sirkazhi.",
        "is_primary": False,
    },
]

M = "https://media.atherenergy.com/"

# Battery-warranty wording shared by every model (Ather spec sheets, Nov 2026).
WARRANTY = "3 yr / 30,000 km standard · extendable up to 10 yr / 1,00,000 km"

# ---------------------------------------------------------------------------
# Scooters.  Specs and starting prices from Ather's own pages and published
# specification sheets, 10 November 2026.  TODO(client): re-check prices
# whenever Ather revises them — they also appear in price-chennai.html and
# compare.html (both generated from this list).
# ---------------------------------------------------------------------------
MODELS = [
    {
        "slug": "ather-konarc",
        "name": "Ather Konarc",
        "family": "Konarc",
        "order": 1,
        "status": "on-sale",
        "eyebrow": "New · just launched",
        "tagline": "Make life look easy",
        "intro": "Ather's newest scooter, built on the new EL platform: a metal body on a "
                 "steel unibody chassis, a 14-inch front wheel, long-travel suspension and "
                 "a sealed Silent Gear Drive that stretches service to once a year. "
                 "Introductory price from ₹99,999.",
        "price": 99999,
        "price_note": "Introductory ex-showroom, Konarc S",
        "hero": M + "PDPKVDesktop.webp",   # lifestyle photo, phone version picked automatically
        "card": M + "1-Celestial-Gold-desk.webp",   # studio shot (media library)
        "card_alts": [],
        "stats": [("200", "km", "IDC range*"), ("70", "km/h", "Top speed"),
                  ("31", "L", "Boot space"), ("2", "hr", "Home charge 0–80%")],
        "specs": [
            ("Variants", "Konarc S: 2.1 / 2.7 / 3.5 kWh · Konarc Z coming soon"),
            ("Peak power", "4.0 kW (2.1 kWh) / 4.7 kW"),
            ("Torque", "16 Nm"),
            ("0 – 40 km/h", "4.7 s (5.0 s on 2.1 kWh)"),
            ("Top speed", "70 km/h (Konarc Z: 80 km/h)"),
            ("Battery", "2.1 / 2.7 / 3.5 kWh"),
            ("IDC range", "100 / 125 / 161 km · up to 200 km listed by Ather"),
            ("TrueRange", "80 / 100 / 130 km"),
            ("Home charging (0–80%)", "2 hr – 3 hr 10 min with the combined charger · 4 hr – 5 hr 40 min on 450 W"),
            ("Fast charge", "Up to 15 km in 10 min on Ather Grid (13 km on 2.1 kWh)"),
            ("Storage", "31 L boot"),
            ("Wheels", "14-inch front / 12-inch rear alloys, 90/90-14 and 100/90-12 tyres"),
            ("Suspension", "Telescopic fork 90 mm / monoshock 100 mm travel"),
            ("Brakes", "220 mm disc front (130 mm drum on 2.1 kWh) / 130 mm drum rear, CBS"),
            ("Build", "Metal body, steel unibody chassis, Silent Gear Drive"),
            ("Kerb weight", "126.5 – 129 kg"),
            ("Dashboard", "DeepView™ — 10.7 cm (4.2\") on 2.1 kWh, 17.7 cm (7\") on the others"),
            ("Service interval", "1 year"),
            ("Battery warranty", WARRANTY),
        ],
        "colours": [
            ("Celestial Gold", "#c9a24b", M + "1-Celestial-Gold-desk.webp"),
            ("Lumen Copper", "#b8734a", M + "2-Lumen-Copper-desk.webp"),
            ("Quartz White", "#eceae4", M + "3-Quartz-White-desk.webp"),
            ("Majestic Grey", "#6b6e72", M + "4-Majestic-Grey-desk.webp"),
        ],
        "highlights": [
            ("Under a lakh, introductory", "₹99,999 ex-showroom for the Konarc S — the most affordable way into an Ather."),
            ("Built for our roads", "14-inch front wheel, 90/100 mm suspension travel and 16 cm ground clearance take Chennai's broken patches in stride."),
            ("Metal body, steel chassis", "Tougher than plastic panels, and a sealed Silent Gear Drive means servicing just once a year."),
            ("2-hour home charging", "With the combined charger, 0–80% at home takes as little as two hours. It is included on the 3.5 kWh variant."),
        ],
        "buyers": "Anyone stepping off a 110cc petrol scooter who wants an Ather at a lower price.",
    },
    {
        "slug": "ather-450-apex",
        "name": "Ather 450 Apex",
        "family": "450",
        "order": 2,
        "status": "on-sale",
        "eyebrow": "The quick one",
        "tagline": "India's fastest electric scooter",
        "intro": "Warp+ mode, Infinite Cruise and 100 km/h on the clock. "
                 "The 450 Apex is the one you buy when the commute is also the fun part.",
        "price": 194946,                       # TODO(client): Ather doesn't publish an Apex price online — confirm
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Ather-450-apex-electric-scooter-model.webp",   # lifestyle photo, phone version picked automatically
        "card": M + "450xahr-indium-blue-electric-scooter.webp",   # studio shot (media library)
        "card_alts": [],
        "stats": [("2.9", "s", "0 – 40 km/h"), ("100", "km/h", "Top speed"),
                  ("165", "km", "IDC range"), ("7", "kW", "Peak power")],
        "specs": [
            ("Peak power", "7 kW"), ("Torque", "26 Nm"),
            ("0 – 40 km/h", "2.9 s (Warp+)"), ("Top speed", "100 km/h"),
            ("Battery", "3.5 kWh"), ("IDC range", "165 km"), ("TrueRange", "130 km"),
            ("Charging", "0–80% in 3 hr 25 min · 0–100% in 4 hr 30 min (900 W)"),
            ("Fast charge", "Up to 30 km in 10 min on Ather Grid"),
            ("Kerb weight", "111.6 kg"),
            ("Brakes", "200 mm triple-piston disc front / 190 mm disc rear, CBS"),
            ("Dashboard", "17.7 cm (7\") TFT touchscreen"),
            ("Navigation", "Google Maps platform"),
            ("Cruise control", "Infinite Cruise — City Cruise, Hill Control, Crawl Control"),
            ("Software", "AtherStack Pro included"),
            ("Battery warranty", WARRANTY),
        ],
        "colours": [("Indium Blue", "#2f5d92", M + "450xahr-indium-blue-electric-scooter.webp")],
        "highlights": [
            ("Warp+", "A dedicated mode that unlocks the full 7 kW. 0–40 km/h in 2.9 seconds."),
            ("Infinite Cruise", "City Cruise, Hill Control and Crawl Control take the effort out of OMR stop-go traffic."),
            ("100 km/h", "Genuinely quick on the ECR and the OMR service roads, with the stability to use it."),
            ("AtherStack Pro", "Every connected feature switched on from day one — and the route to the 10-year battery warranty."),
        ],
        "buyers": "Riders who want the quickest scooter on the road and will actually use the performance.",
    },
    {
        "slug": "ather-450x",
        "name": "Ather 450X",
        "family": "450",
        "order": 3,
        "status": "on-sale",
        "eyebrow": "The all-rounder",
        "tagline": "Motorsport form, everyday sense",
        "intro": "6.4 kW, a 7-inch touchscreen, the new Infinite Cruise and the full connected "
                 "feature set. The 450X is the one most Chennai buyers land on, and it is the one "
                 "we keep most stock of.",
        "price": 148998,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Ather-450-electric-scooter-front-view.webp",   # lifestyle photo, phone version picked automatically
        "card": M + "450x-hyper-sand-electric-scooter.webp",   # studio shot (media library)
        "card_alts": [],
        "stats": [("3.3", "s", "0 – 40 km/h"), ("90", "km/h", "Top speed"),
                  ("161", "km", "IDC range"), ("6.4", "kW", "Peak power")],
        "specs": [
            ("Peak power", "6.4 kW"), ("Torque", "26 Nm"),
            ("0 – 40 km/h", "3.3 s"), ("Top speed", "90 km/h"),
            ("Battery", "2.9 kWh / 3.5 kWh"), ("IDC range", "126 km / 161 km"),
            ("TrueRange", "105 km / 130 km"),
            ("Charging (0–80%)", "5 hr 10 min (450 W) / 3 hr 25 min (900 W)"),
            ("Fast charge", "Up to 15 km / 30 km in 10 min on Ather Grid"),
            ("Brakes", "200 mm triple-piston disc front / 190 mm disc rear, CBS"),
            ("Dashboard", "17.7 cm (7\") TFT touchscreen"),
            ("Navigation", "Google Maps platform"),
            ("Magic Twist", "Yes"),
            ("Cruise control", "Infinite Cruise"),
            ("Traction control", "Multi-Mode: Rain, Road, Rally"),
            ("Battery warranty", WARRANTY),
        ],
        "colours": [
            ("Cosmic Black", "#15171a", M + "450x-mono-cosmic-black-d.webp"),
            ("True Red", "#b0202a", M + "450x-mono-true-red-d.webp"),
            ("Space Grey", "#4c5259", M + "450x-overtones-space-grey-d.webp"),
            ("Lunar Grey", "#8d949b", M + "450x-overtones-lunar-grey-d.webp"),
            ("Still White", "#edeff1", M + "450x-overtones-still-white-d.webp"),
            ("Stealth Blue", "#33506b", M + "450x-matte-stealth-blue-d.webp"),
            ("Hyper Sand", "#c8b391", M + "450s-hyper-sand-d.webp"),
        ],
        "highlights": [
            ("Infinite Cruise", "Cruise control reimagined for cities — City Cruise, Hill Control and Crawl Control, delivered over the air."),
            ("7-inch touchscreen", "Google Maps, WhatsApp alerts, call and music control, live cricket scores and Voice on Ather."),
            ("Multi-Mode Traction Control", "Rain, Road and Rally — Rain earns its keep between October and December here."),
            ("Pothole+ alerts", "Warns you about rough patches other Ather riders have already hit."),
        ],
        "buyers": "The default choice. Solo commuters and enthusiasts who want the full feature set.",
    },
    {
        "slug": "ather-450s",
        "name": "Ather 450S",
        "family": "450",
        "order": 4,
        "status": "on-sale",
        "eyebrow": "The value one",
        "tagline": "The 450 ride, for less",
        "intro": "Same chassis, same dual disc brakes, same 90 km/h. The 450S trims the "
                 "touchscreen, a little power and a few software features to land meaningfully "
                 "cheaper — and it is still a proper 450.",
        "price": 135999,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Ather-450X-vs-Ather-450S-electric-scooter-model.webp",   # lifestyle photo, phone version picked automatically
        "card": M + "450s-cosmic-black-electric-scooter.webp",   # studio shot (media library)
        "card_alts": [],
        "stats": [("3.9", "s", "0 – 40 km/h"), ("90", "km/h", "Top speed"),
                  ("161", "km", "IDC range"), ("5.4", "kW", "Peak power")],
        "specs": [
            ("Peak power", "5.4 kW"), ("Torque", "22 Nm"),
            ("0 – 40 km/h", "3.9 s"), ("Top speed", "90 km/h"),
            ("Battery", "2.9 kWh / 3.5 kWh"), ("IDC range", "122 km / 161 km"),
            ("TrueRange", "105 km / 130 km"),
            ("Charging (0–80%)", "5 hr 10 min (450 W) / 3 hr 25 min (900 W)"),
            ("Fast charge", "Up to 15 km in 10 min on Ather Grid"),
            ("Brakes", "200 mm triple-piston disc front / 190 mm disc rear, CBS"),
            ("Dashboard", "17.7 cm (7\") DeepView™ display"),
            ("Navigation", "Not available"),
            ("Magic Twist", "Not available"),
            ("Traction control", "Not available"),
            ("Battery warranty", WARRANTY),
        ],
        "colours": [
            ("Hyper Sand", "#c8b391", M + "450s-hyper-sand-d.webp"),
            ("Cosmic Black", "#15171a", M + "450x-mono-cosmic-black-d.webp"),
            ("True Red", "#b0202a", M + "450x-mono-true-red-d.webp"),
            ("Still White", "#edeff1", M + "450x-overtones-still-white-d.webp"),
            ("Stealth Blue", "#33506b", M + "450x-matte-stealth-blue-d.webp"),
        ],
        "highlights": [
            ("Same chassis and brakes", "Identical frame, suspension and dual disc brakes to the 450X. The difference is the screen, the motor tune and software."),
            ("DeepView display", "A 7-inch non-touch display that stays readable in Chennai's midday sun."),
            ("Up to 161 km IDC", "The 3.5 kWh pack gives the same IDC range as the 450X — about 130 km in real riding."),
            ("Up to 10-year battery warranty", "3 years as standard, extendable up to 10 years / 1,00,000 km — same as the rest of the range."),
        ],
        "buyers": "First-time EV buyers who want a 450 without paying for the touchscreen.",
    },
    {
        "slug": "ather-rizta-z",
        "name": "Ather Rizta Z",
        "family": "Rizta",
        "order": 5,
        "status": "on-sale",
        "eyebrow": "The family one",
        "tagline": "Built around the second seat",
        "intro": "56 litres of storage, a proper flat floorboard, a pillion backrest, "
                 "SkidControl and a 7-inch touchscreen that now speaks Tamil. The Rizta Z is "
                 "the school-run and grocery-run scooter that happens to be electric.",
        "price": 136999,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Ather-Rizta-family-electric-scooter.webp",   # lifestyle photo, phone version picked automatically
        "card": M + "rizz1-terracotta-red-dt-electric-scooter.webp",   # studio shot (media library)
        "card_alts": [],
        "stats": [("80", "km/h", "Top speed"), ("161", "km", "IDC range"),
                  ("56", "L", "Total storage"), ("4.3", "kW", "Peak power")],
        "specs": [
            ("Peak power", "4.3 kW"), ("Torque", "22 Nm"),
            ("0 – 40 km/h", "4.7 s"), ("Top speed", "80 km/h"),
            ("Battery", "2.7 / 2.9 / 3.5 kWh"), ("IDC range", "123 km / 161 km"),
            ("TrueRange", "100 km / 125 km"),
            ("Charging (0–100%)", "7 hr 25 min (450 W) / 4 hr 30 min (900 W, 3.5 kWh)"),
            ("Fast charge", "Up to 15 km / 30 km in 10 min on Ather Grid"),
            ("Storage", "34 L boot + 22 L frunk = 56 L"),
            ("Kerb weight", "125 kg"),
            ("Brakes", "Disc front 200 mm / drum rear 130 mm, CBS"),
            ("Tyres", "90/90-12 front, 100/80-12 rear, tubeless"),
            ("Dashboard", "17.7 cm (7\") TFT touchscreen, Tamil and three more languages"),
            ("Navigation", "Google Maps platform"),
            ("Safety", "SkidControl, Crash Alert, FallSafe, Emergency Stop Signal"),
            ("Seat", "Premium dual-tone, pillion backrest standard"),
            ("Battery warranty", WARRANTY),
        ],
        "colours": [
            ("Terracotta Red (Duo)", "#a8412f", M + "Rizta-Terracotta-Red-Duo-New-1.webp"),
            ("Terracotta Red (Super Matte)", "#93382a", M + "RizTA-Red-Super-Matte%20(1).webp"),
            ("Pangong Blue (Duo)", "#3a5f80", M + "Blue-Duo.png"),
            ("Pangong Blue (Super Matte)", "#33536f", M + "Blue-Mono.png"),
            ("Deccan Grey (Duo)", "#6f757b", M + "Grey-Duo.png"),
            ("Deccan Grey (Mono)", "#5f656b", M + "Grey-Mono.png"),
            ("Siachen White (Mono)", "#eef0f1", M + "White-Mono.png"),
            ("Alphonso Yellow (Duo)", "#d8a53a", M + "Yellow-Duo.png"),
            ("Cardamom Green (Duo)", "#5c7f60", M + "Green-Duo.png"),
        ],
        "highlights": [
            ("56 litres of storage", "34 L under the seat plus a 22 L frunk. Two helmets, or a week's groceries."),
            ("SkidControl", "Keeps the Rizta composed on wet, sandy or bumpy roads — useful through the north-east monsoon."),
            ("Tamil dashboard", "The 7-inch touchscreen now runs in Tamil, Hindi, Malayalam and Kannada, with a dark mode for night rides."),
            ("Crash Alert", "Notifies family with your location if something goes wrong, and shows their contact on the dash."),
        ],
        "buyers": "Families, and anyone who carries a pillion or luggage more days than not.",
    },
    {
        "slug": "ather-rizta-s",
        "name": "Ather Rizta S",
        "family": "Rizta",
        "order": 6,
        "status": "on-sale",
        "eyebrow": "The sensible one",
        "tagline": "The family scooter, keenly priced",
        "intro": "The same practical Rizta body, storage and backrest, with a "
                 "DeepView display instead of the touchscreen. The keenly priced way "
                 "into the Rizta family.",
        "price": 121999,
        "price_note": "Ex-showroom, indicative",
        "hero": M + "Ather-Rizta-family-electric-scooter-floor-board.webp",   # lifestyle photo, phone version picked automatically
        "card": M + "rizs1-pangong-blue-mono-electric-scooter.webp",   # studio shot (media library)
        "card_alts": [],
        "stats": [("80", "km/h", "Top speed"), ("161", "km", "IDC range"),
                  ("56", "L", "Total storage"), ("4.3", "kW", "Peak power")],
        "specs": [
            ("Peak power", "4.3 kW"), ("Torque", "22 Nm"),
            ("0 – 40 km/h", "4.7 s"), ("Top speed", "80 km/h"),
            ("Battery", "2.7 / 2.9 / 3.5 kWh"), ("IDC range", "123 km / 161 km"),
            ("TrueRange", "100 km / 125 km"),
            ("Charging (0–100%)", "7 hr 25 min (450 W) / 4 hr 30 min (900 W, 3.5 kWh)"),
            ("Fast charge", "Up to 15 km in 10 min on Ather Grid"),
            ("Storage", "34 L boot + 22 L frunk = 56 L"),
            ("Kerb weight", "125 kg"),
            ("Brakes", "Disc front 200 mm / drum rear 130 mm, CBS"),
            ("Dashboard", "17.7 cm (7\") DeepView™ display"),
            ("Navigation", "Not available"),
            ("Seat", "Standard black, pillion backrest standard"),
            ("Battery warranty", WARRANTY),
        ],
        "colours": [
            ("Siachen White (Mono)", "#eef0f1", M + "White-Mono.png"),
            ("Deccan Grey (Mono)", "#5f656b", M + "Grey-Mono.png"),
            ("Pangong Blue (Super Matte)", "#33536f", M + "Blue-Mono.png"),
            ("Terracotta Red (Super Matte)", "#93382a", M + "RizTA-Red-Super-Matte%20(1).webp"),
        ],
        "highlights": [
            ("The keenly priced Rizta", "A full-size family scooter from ₹1,21,999 ex-showroom."),
            ("Same 56 L storage", "Nothing is taken away from the boot or the frunk."),
            ("DeepView display", "Non-touch, high contrast, easy to read in direct sun."),
            ("Up to 10-year battery warranty", "Identical cover to the Rizta Z — 3 years standard, extendable to 10."),
        ],
        "buyers": "Budget-conscious family buyers, and anyone stepping off a 110cc petrol scooter.",
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
