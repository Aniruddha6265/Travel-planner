"""
pdf_export.py — Beautifully formatted offline PDF travel itinerary guide.
Uses fpdf2 for zero system dependency PDF generation.
"""

from fpdf import FPDF
from demo_data import EMERGENCY_CONTACTS


def _safe(text: str) -> str:
    """Sanitize text for fpdf2's latin-1 encoding by replacing
    Unicode currency symbols with ASCII-safe equivalents."""
    replacements = {
        "\u20b9": "INR ",   # ₹
        "\u20ac": "EUR ",   # €
        "\u00a5": "JPY ",   # ¥
        "\u00a3": "GBP ",   # £
        chr(9744): "[ ]",   # ☐ checkbox
    }
    for char, repl in replacements.items():
        text = text.replace(char, repl)
    # Fallback: replace any remaining non-latin-1 chars
    return text.encode("latin-1", errors="replace").decode("latin-1")


class TravelPDF(FPDF):
    """Custom PDF class for travel itinerary generation."""

    # Color palette
    TEAL_DEEP = (11, 61, 61)
    TEAL_MED = (26, 107, 107)
    TEAL_LIGHT = (45, 155, 155)
    CORAL = (255, 107, 107)
    GOLD = (244, 162, 97)
    CREAM = (255, 248, 240)
    WHITE = (255, 255, 255)
    DARK_TEXT = (51, 51, 51)

    def header(self):
        """Custom header for each page."""
        if self.page_no() > 1:
            self.set_fill_color(*self.TEAL_DEEP)
            self.rect(0, 0, 210, 12, "F")
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(*self.WHITE)
            self.set_xy(10, 3)
            title = getattr(self, "_trip_title", "Travel Itinerary")
            self.cell(0, 6, title, align="L")
            self.ln(14)

    def footer(self):
        """Custom footer with page numbers."""
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def _section_title(self, title: str):
        """Render a styled section title."""
        self.ln(4)
        self.set_fill_color(*self.TEAL_MED)
        self.set_text_color(*self.WHITE)
        self.set_font("Helvetica", "B", 13)
        self.cell(0, 10, f"  {title}", fill=True, ln=True)
        self.set_text_color(*self.DARK_TEXT)
        self.ln(3)

    def _sub_title(self, title: str):
        """Render a styled sub-title."""
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*self.TEAL_DEEP)
        self.cell(0, 7, title, ln=True)
        self.set_text_color(*self.DARK_TEXT)
        self.ln(1)

    def _info_row(self, label: str, value: str):
        """Render a label-value info row."""
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*self.TEAL_MED)
        self.cell(45, 6, label + ":", align="R")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*self.DARK_TEXT)
        self.cell(0, 6, "  " + str(value), ln=True)


def generate_pdf(trip_data: dict, preferences: dict) -> bytes:
    """Generate a beautifully formatted PDF travel itinerary.

    Args:
        trip_data: The itinerary data dict.
        preferences: User preferences dict.

    Returns:
        PDF as bytes for download.
    """
    itinerary = trip_data.get("itinerary", trip_data)
    destination = itinerary.get("destination", "Your Destination")
    days = itinerary.get("days", [])
    currency = itinerary.get("currency", "USD")
    currency_symbol = itinerary.get("currency_symbol", "$")

    pdf = TravelPDF()
    pdf._trip_title = f"{destination} — Travel Itinerary"
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # ── Cover Page ──────────────────────────────────────────
    pdf.add_page()

    # Teal gradient header block
    pdf.set_fill_color(*TravelPDF.TEAL_DEEP)
    pdf.rect(0, 0, 210, 120, "F")
    pdf.set_fill_color(*TravelPDF.TEAL_MED)
    pdf.rect(0, 100, 210, 20, "F")

    # Gold accent line
    pdf.set_fill_color(*TravelPDF.GOLD)
    pdf.rect(60, 95, 90, 3, "F")

    # Title text
    pdf.set_text_color(*TravelPDF.WHITE)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_xy(0, 30)
    pdf.cell(0, 8, "YOUR PERSONALIZED", align="C", ln=True)
    pdf.set_font("Helvetica", "B", 28)
    pdf.cell(0, 14, "TRAVEL ITINERARY", align="C", ln=True)
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 18)
    pdf.cell(0, 10, destination.upper(), align="C", ln=True)

    # Trip details below header
    pdf.set_text_color(*TravelPDF.DARK_TEXT)
    pdf.set_xy(0, 135)
    pdf.set_font("Helvetica", "", 11)

    details = [
        f"Duration: {len(days)} Days",
        f"Budget Level: {preferences.get('budget_level', 'Moderate')}",
        f"Travel Party: {preferences.get('travel_party', 'Solo')}",
        f"Pace: {preferences.get('pace', 'Moderate')}",
        f"Interests: {', '.join(preferences.get('interests', []))}",
    ]
    for detail in details:
        pdf.cell(0, 7, detail, align="C", ln=True)

    # Budget summary
    pdf.ln(8)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(*TravelPDF.TEAL_DEEP)
    total_usd = itinerary.get("trip_total_usd", 0)
    total_inr = itinerary.get("trip_total_inr", 0)
    total_local = itinerary.get("trip_total_local", 0)
    pdf.cell(0, 10, _safe(f"Estimated Total: {currency_symbol}{total_local} ({currency}) | ${total_usd:.0f} USD | INR {total_inr:.0f}"), align="C", ln=True)

    # ── Trip Overview Page ──────────────────────────────────
    pdf.add_page()
    pdf._section_title("Trip Overview")

    pdf._info_row("Destination", destination)
    pdf._info_row("Duration", f"{len(days)} days")
    pdf._info_row("Budget Level", preferences.get("budget_level", "Moderate"))
    pdf._info_row("Travel Party", preferences.get("travel_party", "Solo"))
    pdf._info_row("Pace", preferences.get("pace", "Moderate"))
    pdf._info_row("Interests", ", ".join(preferences.get("interests", [])))
    pdf._info_row("Currency", f"{currency} ({currency_symbol})")
    pdf._info_row("Exchange Rate", f"1 {currency} = ${itinerary.get('exchange_rate_to_usd', 1):.2f} USD")
    pdf.ln(4)

    # Daily cost summary table
    pdf._sub_title("Daily Budget Summary")
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(*TravelPDF.TEAL_DEEP)
    pdf.set_text_color(*TravelPDF.WHITE)
    pdf.cell(20, 7, "Day", border=1, align="C", fill=True)
    pdf.cell(70, 7, "Theme", border=1, align="C", fill=True)
    pdf.cell(35, 7, f"Cost ({currency})", border=1, align="C", fill=True)
    pdf.cell(30, 7, "Cost (USD)", border=1, align="C", fill=True)
    pdf.cell(35, 7, "Cost (INR)", border=1, align="C", fill=True)
    pdf.ln()

    pdf.set_text_color(*TravelPDF.DARK_TEXT)
    pdf.set_font("Helvetica", "", 9)
    rate_to_inr = itinerary.get("exchange_rate_to_inr", 83.5)
    rate_to_usd = itinerary.get("exchange_rate_to_usd", 1)

    for day in days:
        day_usd = day.get("day_total_usd", 0)
        day_local = day.get("day_total_local", 0)
        day_inr = day_usd * (rate_to_inr / rate_to_usd) if rate_to_usd else 0

        bg = TravelPDF.CREAM if day["day"] % 2 == 0 else TravelPDF.WHITE
        pdf.set_fill_color(*bg)
        pdf.cell(20, 7, str(day["day"]), border=1, align="C", fill=True)
        theme = day.get("theme", "")[:35]
        pdf.cell(70, 7, theme, border=1, fill=True)
        pdf.cell(35, 7, _safe(f"{currency_symbol}{day_local}"), border=1, align="C", fill=True)
        pdf.cell(30, 7, f"${day_usd:.0f}", border=1, align="C", fill=True)
        pdf.cell(35, 7, f"INR {day_inr:.0f}", border=1, align="C", fill=True)
        pdf.ln()

    # Totals row
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(*TravelPDF.GOLD)
    pdf.cell(20, 7, "", border=1, fill=True)
    pdf.cell(70, 7, "TOTAL", border=1, fill=True)
    pdf.cell(35, 7, _safe(f"{currency_symbol}{total_local}"), border=1, align="C", fill=True)
    pdf.cell(30, 7, f"${total_usd:.0f}", border=1, align="C", fill=True)
    pdf.cell(35, 7, f"INR {total_inr:.0f}", border=1, align="C", fill=True)
    pdf.ln(10)

    # ── Day-by-Day Itinerary ──────────────────────────────
    for day in days:
        pdf.add_page()
        pdf._section_title(f"Day {day['day']} — {day.get('theme', '')}")

        # Neighborhood cluster badge
        cluster = day.get("neighborhood_cluster", "")
        if cluster:
            pdf.set_font("Helvetica", "I", 9)
            pdf.set_text_color(*TravelPDF.TEAL_MED)
            pdf.cell(0, 6, f"Neighborhood: {cluster}", ln=True)
            pdf.set_text_color(*TravelPDF.DARK_TEXT)
            pdf.ln(2)

        # Activity table
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_fill_color(*TravelPDF.TEAL_DEEP)
        pdf.set_text_color(*TravelPDF.WHITE)
        pdf.cell(22, 7, "Time", border=1, align="C", fill=True)
        pdf.cell(35, 7, "Period", border=1, align="C", fill=True)
        pdf.cell(50, 7, "Activity", border=1, align="C", fill=True)
        pdf.cell(25, 7, f"{currency}", border=1, align="C", fill=True)
        pdf.cell(25, 7, "USD", border=1, align="C", fill=True)
        pdf.ln()

        pdf.set_text_color(*TravelPDF.DARK_TEXT)
        pdf.set_font("Helvetica", "", 8)

        for i, slot in enumerate(day.get("slots", [])):
            bg = TravelPDF.CREAM if i % 2 == 0 else TravelPDF.WHITE
            pdf.set_fill_color(*bg)

            pdf.cell(22, 7, slot.get("time", ""), border=1, align="C", fill=True)
            pdf.cell(35, 7, slot.get("period", "")[:20], border=1, fill=True)
            activity = slot.get("activity", "")[:28]
            pdf.cell(50, 7, activity, border=1, fill=True)
            pdf.cell(25, 7, f"{currency_symbol}{slot.get('cost_local', 0)}", border=1, align="C", fill=True)
            pdf.cell(25, 7, f"${slot.get('cost_usd', 0):.0f}", border=1, align="C", fill=True)
            pdf.ln()

        # Day total
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_fill_color(*TravelPDF.GOLD)
        pdf.cell(107, 7, "Day Total", border=1, align="R", fill=True)
        pdf.cell(25, 7, f"{currency_symbol}{day.get('day_total_local', 0)}", border=1, align="C", fill=True)
        pdf.cell(25, 7, f"${day.get('day_total_usd', 0):.0f}", border=1, align="C", fill=True)
        pdf.ln(6)

        # Activity descriptions
        pdf.set_font("Helvetica", "", 8)
        for slot in day.get("slots", []):
            desc = slot.get("description", "")
            if desc:
                pdf.set_font("Helvetica", "B", 8)
                pdf.set_text_color(*TravelPDF.TEAL_MED)
                pdf.cell(0, 5, f"{slot.get('activity', '')}:", ln=True)
                pdf.set_font("Helvetica", "", 8)
                pdf.set_text_color(*TravelPDF.DARK_TEXT)
                pdf.multi_cell(0, 4, desc)
                pdf.ln(1)

    # ── Emergency Contacts ──────────────────────────────────
    pdf.add_page()
    pdf._section_title("Emergency Contacts & Essential Info")

    # Determine country from destination
    country = _extract_country(itinerary)
    contacts = EMERGENCY_CONTACTS.get(country, EMERGENCY_CONTACTS["default"])

    pdf._info_row("Country", country)
    pdf._info_row("Emergency Police", contacts.get("police", "112"))
    pdf._info_row("Ambulance", contacts.get("ambulance", "112"))
    pdf._info_row("Fire Department", contacts.get("fire", "112"))
    pdf._info_row("Tourist Helpline", contacts.get("tourist_helpline", "Contact local tourism board"))
    pdf._info_row("US Embassy", contacts.get("us_embassy", "Contact your embassy"))

    pdf.ln(6)

    # Personal safety checklist
    pdf._sub_title("Personal Safety Checklist")
    safety_items = [
        "Keep digital copies of passport, visa, and travel insurance on your phone",
        "Share your itinerary with a trusted friend or family member",
        "Register with your embassy's travel notification program",
        "Keep emergency cash separate from your main wallet",
        "Note the address of your accommodation in the local language",
        "Save offline maps of your destination on your phone",
        "Carry a basic first-aid kit with any personal medications",
        "Keep your hotel's phone number saved in your contacts",
    ]
    pdf.set_font("Helvetica", "", 9)
    for item in safety_items:
        pdf.cell(6, 6, chr(9744))  # Checkbox symbol
        pdf.cell(0, 6, f"  {item}", ln=True)

    # ── Packing Checklist ──────────────────────────────────
    pdf.ln(6)
    pdf._sub_title("Packing Essentials")

    packing_items = [
        "Passport & travel documents",
        "Travel insurance details",
        "Phone charger & universal adapter",
        "Comfortable walking shoes",
        "Weather-appropriate clothing",
        "Sunscreen & sunglasses",
        "Reusable water bottle",
        "Day backpack / crossbody bag",
        "Local currency / travel card",
        "Medications & prescriptions",
        "Portable battery pack",
        "Travel-size toiletries",
    ]
    for item in packing_items:
        pdf.cell(6, 6, chr(9744))
        pdf.cell(0, 6, f"  {item}", ln=True)

    # ── Final page: Notes ──────────────────────────────────
    pdf.ln(10)
    pdf._sub_title("Personal Notes")
    for _ in range(8):
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(8)

    # Footer disclaimer
    pdf.ln(6)
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(150, 150, 150)
    pdf.multi_cell(
        0, 4,
        "Disclaimer: All costs are estimates and may vary. Please verify current prices, opening hours, and availability before your trip. "
        "This itinerary was generated by the Personalized Travel Itinerary Planner. Safe travels!",
    )

    return pdf.output()


def _extract_country(itinerary: dict) -> str:
    """Extract the country from itinerary data, with fallback."""
    country = itinerary.get("country", "")
    if country:
        return country

    # Try to infer from destination name
    dest = itinerary.get("destination", "").lower()
    country_map = {
        "tokyo": "Japan", "kyoto": "Japan", "osaka": "Japan",
        "istanbul": "Turkey",
        "rome": "Italy", "florence": "Italy", "milan": "Italy", "venice": "Italy",
        "bali": "Indonesia", "jakarta": "Indonesia",
        "zanzibar": "Tanzania",
        "tulum": "Mexico", "mexico city": "Mexico", "cancun": "Mexico",
        "chamonix": "France", "paris": "France", "nice": "France",
        "cusco": "Peru", "lima": "Peru",
        "manali": "India", "delhi": "India", "mumbai": "India", "goa": "India",
        "lisbon": "Portugal", "porto": "Portugal",
        "new york": "United States", "los angeles": "United States",
    }
    for city, country_name in country_map.items():
        if city in dest:
            return country_name
    return "default"
