#!/usr/bin/env python3
"""
guides_index.py  —  Version: V1  (12 Nov 2026; adds showroom-page guide links)

Collects the guide pages from the tools/guides_*.py content files.
Data only — safe to import from build_site.py and build_guides.py.
To add a guide: add a dict to the right content file and re-run build_site.py.
"""
from guides_models import GUIDES as _models
from guides_features import GUIDES as _features
from guides_compare import GUIDES as _compare
from guides_ownership import GUIDES as _ownership
from guides_local import GUIDES as _local

CLUSTERS = {
    "models":    {"label": "Choosing your Ather",
                  "intro": "Which model, which battery, which variant — matched to how you actually ride."},
    "compare":   {"label": "Ather vs Ather", "light": True,
                  "intro": "Side-by-side comparisons of the scooters people most often shortlist together."},
    "features":  {"label": "Features explained",
                  "intro": "What each Ather feature does on a real Chennai ride, and which models have it."},
    "ownership": {"label": "Owning an Ather", "light": True,
                  "intro": "Charging, service, warranty, registration, finance and the monsoon."},
    "local":     {"label": "Routes and commutes",
                  "intro": "Real trips across our four regions, planned around range and charging."},
}

GUIDES = _models + _compare + _features + _ownership + _local
by_guide = {g["slug"]: g for g in GUIDES}
assert len(by_guide) == len(GUIDES), "two guides share a slug"


# Guides linked from each showroom page (locations/<slug>.html).
BRANCH_GUIDES = {
    "chennai-omr":  ["omr-it-corridor-commute-on-an-ather", "charging-ather-at-home-in-a-chennai-apartment",
                     "riding-your-ather-in-the-chennai-monsoon", "which-ather-scooter-should-i-buy"],
    "chengalpattu": ["daily-commute-chengalpattu-to-chennai-on-an-ather", "ather-scooter-for-long-commutes",
                     "exchange-your-petrol-scooter-for-an-ather", "ather-service-schedule-and-costs"],
    "pondicherry":  ["chennai-to-puducherry-ecr-on-an-ather", "ev-registration-tamil-nadu-vs-puducherry",
                     "ather-charging-cost-per-km", "ather-finance-and-loan-documents"],
    "chidambaram":  ["chidambaram-cuddalore-neyveli-on-an-ather", "ather-konarc-buyers-guide",
                     "ather-battery-care-in-hot-weather", "ather-rizta-family-guide"],
}


def guides_for_branch(slug):
    return [by_guide[s] for s in BRANCH_GUIDES.get(slug, []) if s in by_guide]


def guides_for_model(slug, limit=4):
    """Guides that feature a model — used on the model pages."""
    pri = {"models": 0, "compare": 1, "features": 2, "ownership": 3, "local": 4}
    gs = [g for g in GUIDES if slug in g.get("models", [])]
    return sorted(gs, key=lambda g: (pri.get(g["cluster"], 9), g["models"].index(slug)))[:limit]
