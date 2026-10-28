"""Quick integration test for the travel planner modules."""
from demo_data import get_demo_recommendations, get_demo_itinerary, get_demo_swap, get_demo_day_regeneration, EMERGENCY_CONTACTS
from pdf_export import generate_pdf

print("All imports successful")

# Test recommendations
recs = get_demo_recommendations({"vibe": "Beach"})
print(f"Recommendations: {len(recs['recommendations'])} cities")

# Test itinerary
itin = get_demo_itinerary({"duration": 3})
print(f"Itinerary: {len(itin['days'])} days for {itin['destination']}")

# Test swap
swap = get_demo_swap(1, 2, "outdoor market")
print(f"Swap result: {swap['activity']}")

# Test day regeneration
regen = get_demo_day_regeneration(2, {"interests": ["Food"]})
print(f"Regenerated day: {regen['theme']}")

# Test PDF generation
pdf = generate_pdf(
    {"itinerary": itin},
    {"budget_level": "Moderate", "travel_party": "Solo", "pace": "Moderate", "interests": ["Food", "History"]},
)
print(f"PDF generated: {len(pdf)} bytes")

# Test emergency contacts
assert "Japan" in EMERGENCY_CONTACTS
assert "default" in EMERGENCY_CONTACTS
print(f"Emergency contacts: {len(EMERGENCY_CONTACTS)} countries")

print("\nALL TESTS PASSED ✅")
