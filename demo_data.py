"""
demo_data.py — Pre-built rich demo data for offline/demo mode.
Provides realistic fixture responses for all LLM-powered features.
"""


def get_demo_recommendations(preferences: dict) -> dict:
    """Return demo destination recommendations based on user vibe preference."""
    vibe = preferences.get("vibe", "Cultural")

    RECOMMENDATIONS = {
        "Cultural": {
            "recommendations": [
                {
                    "city": "Kyoto",
                    "country": "Japan",
                    "match_score": 96,
                    "highlight_tags": ["Ancient Temples", "Tea Ceremonies", "Cherry Blossoms", "UNESCO Sites"],
                    "avg_daily_cost_usd": 120,
                    "best_season": "Mar–May, Oct–Nov",
                    "description": "Immerse yourself in Japan's cultural heart — from the golden Kinkaku-ji temple to the serene bamboo groves of Arashiyama. Kyoto offers 17 UNESCO World Heritage sites, traditional geisha districts, and the most refined cuisine in East Asia.",
                },
                {
                    "city": "Istanbul",
                    "country": "Turkey",
                    "match_score": 91,
                    "highlight_tags": ["East-meets-West", "Bazaars", "Ottoman Heritage", "Bosphorus Views"],
                    "avg_daily_cost_usd": 65,
                    "best_season": "Apr–Jun, Sep–Nov",
                    "description": "Straddle two continents in a city where Byzantine mosaics meet Ottoman grandeur. Explore the Hagia Sophia, haggle in the Grand Bazaar, cruise the Bosphorus at sunset, and feast on world-class street food.",
                },
                {
                    "city": "Rome",
                    "country": "Italy",
                    "match_score": 89,
                    "highlight_tags": ["Ancient Ruins", "Renaissance Art", "Pasta & Gelato", "Vibrant Piazzas"],
                    "avg_daily_cost_usd": 110,
                    "best_season": "Apr–Jun, Sep–Oct",
                    "description": "Walk through 2,800 years of history — from the Colosseum to the Sistine Chapel. Rome is a living museum where every cobblestone tells a story, and every meal feels like a celebration.",
                },
            ]
        },
        "Beach": {
            "recommendations": [
                {
                    "city": "Bali",
                    "country": "Indonesia",
                    "match_score": 95,
                    "highlight_tags": ["Tropical Paradise", "Surf & Yoga", "Rice Terraces", "Temple Culture"],
                    "avg_daily_cost_usd": 55,
                    "best_season": "Apr–Oct",
                    "description": "From the cliffside temples of Uluwatu to the emerald rice paddies of Ubud, Bali blends spiritual depth with beachside bliss. Surf world-class breaks, eat incredible food for under $5, and watch sunsets that redefine beauty.",
                },
                {
                    "city": "Zanzibar",
                    "country": "Tanzania",
                    "match_score": 90,
                    "highlight_tags": ["Spice Island", "Turquoise Waters", "Stone Town Heritage", "Dhow Sailing"],
                    "avg_daily_cost_usd": 70,
                    "best_season": "Jun–Oct",
                    "description": "An archipelago of white-sand beaches, spice plantations, and Swahili culture. Explore the UNESCO-listed Stone Town, snorkel coral reefs, and dine on fresh seafood under the stars.",
                },
                {
                    "city": "Tulum",
                    "country": "Mexico",
                    "match_score": 87,
                    "highlight_tags": ["Bohemian Chic", "Cenotes", "Mayan Ruins", "Eco-Resorts"],
                    "avg_daily_cost_usd": 90,
                    "best_season": "Nov–Apr",
                    "description": "Where ancient Mayan ruins overlook Caribbean turquoise. Swim in mystical cenotes, lounge on powder-white beaches, and enjoy the boho-chic dining and nightlife scene.",
                },
            ]
        },
        "Mountains": {
            "recommendations": [
                {
                    "city": "Chamonix",
                    "country": "France",
                    "match_score": 94,
                    "highlight_tags": ["Mont Blanc", "Alpine Adventures", "Cable Cars", "Mountain Gastronomy"],
                    "avg_daily_cost_usd": 130,
                    "best_season": "Jun–Sep, Dec–Mar",
                    "description": "At the foot of Mont Blanc, Chamonix is the ultimate alpine playground. Hike glacial trails, ride the Aiguille du Midi cable car to 3,842m, and warm up with fondue and vin chaud.",
                },
                {
                    "city": "Cusco",
                    "country": "Peru",
                    "match_score": 92,
                    "highlight_tags": ["Inca Heritage", "Machu Picchu", "Andean Culture", "High-Altitude Treks"],
                    "avg_daily_cost_usd": 50,
                    "best_season": "May–Sep",
                    "description": "Gateway to Machu Picchu and the Sacred Valley. Cusco blends Inca stonework with Spanish colonial architecture, vibrant textiles, and hearty Andean cuisine at 3,400m elevation.",
                },
                {
                    "city": "Manali",
                    "country": "India",
                    "match_score": 88,
                    "highlight_tags": ["Himalayas", "Adventure Sports", "Hot Springs", "Tibetan Monasteries"],
                    "avg_daily_cost_usd": 30,
                    "best_season": "Mar–Jun, Sep–Nov",
                    "description": "Nestled in the Himalayas, Manali offers snow-capped peaks, rushing rivers, and pine forests. Paraglide over the Kullu Valley, trek to Solang, and soak in natural hot springs.",
                },
            ]
        },
        "Urban": {
            "recommendations": [
                {
                    "city": "Tokyo",
                    "country": "Japan",
                    "match_score": 97,
                    "highlight_tags": ["Neon Metropolis", "Street Food Capital", "Tech & Tradition", "Nightlife"],
                    "avg_daily_cost_usd": 100,
                    "best_season": "Mar–May, Sep–Nov",
                    "description": "The world's most electrifying city — where robot restaurants sit beside 400-year-old shrines. From Shibuya's scramble crossing to Tsukiji's sushi counters, Tokyo is sensory overload in the best way.",
                },
                {
                    "city": "New York",
                    "country": "United States",
                    "match_score": 93,
                    "highlight_tags": ["The City That Never Sleeps", "Broadway", "World Cuisine", "Iconic Skyline"],
                    "avg_daily_cost_usd": 180,
                    "best_season": "Apr–Jun, Sep–Nov",
                    "description": "From the High Line to Harlem jazz clubs, NYC is an endless tapestry of culture, food, and ambition. Catch a Broadway show, explore world-class museums, and eat your way through 100+ cuisines.",
                },
                {
                    "city": "Lisbon",
                    "country": "Portugal",
                    "match_score": 90,
                    "highlight_tags": ["Affordable European Capital", "Tram 28", "Pastéis de Nata", "Fado Music"],
                    "avg_daily_cost_usd": 75,
                    "best_season": "Mar–Oct",
                    "description": "Europe's sunniest capital charms with pastel-tiled buildings, hilltop viewpoints, and the hauntingly beautiful sound of Fado. Incredible food and wine at a fraction of Western European prices.",
                },
            ]
        },
    }

    return RECOMMENDATIONS.get(vibe, RECOMMENDATIONS["Cultural"])


def get_demo_itinerary(preferences: dict) -> dict:
    """Return a demo itinerary for the given preferences."""
    destination = preferences.get("destination", "Lisbon")
    duration = min(preferences.get("duration", 3), 5)  # Cap demo at 5 days

    DEMO_ITINERARY = {
        "destination": destination if destination else "Lisbon",
        "currency": "EUR",
        "currency_symbol": "€",
        "exchange_rate_to_usd": 1.08,
        "exchange_rate_to_inr": 90.5,
        "days": [
            {
                "day": 1,
                "theme": "Historic Heart & Alfama Discovery",
                "neighborhood_cluster": "Alfama / Baixa / Castelo",
                "slots": [
                    {
                        "time": "9:00 AM",
                        "period": "Morning Sightseeing",
                        "activity": "São Jorge Castle",
                        "description": "Start your trip at the hilltop castle with panoramic views over Lisbon's terracotta rooftops and the Tagus River. Explore the ramparts, archaeological ruins, and peacock-filled gardens.",
                        "cost_local": 10,
                        "cost_usd": 10.80,
                        "category": "attraction",
                    },
                    {
                        "time": "12:30 PM",
                        "period": "Lunch",
                        "activity": "Tasca do Chico (Alfama)",
                        "description": "Authentic Portuguese tavern in the heart of Alfama serving grilled sardines, bacalhau à brás, and house wine. Live Fado music in the evenings.",
                        "cost_local": 18,
                        "cost_usd": 19.44,
                        "category": "dining",
                    },
                    {
                        "time": "2:30 PM",
                        "period": "Afternoon Leisure",
                        "activity": "Alfama Walking Tour",
                        "description": "Wander the labyrinthine streets of Lisbon's oldest neighborhood. Discover hidden viewpoints (miradouros), street art, and the iconic Lisbon Cathedral (Sé).",
                        "cost_local": 0,
                        "cost_usd": 0,
                        "category": "exploration",
                    },
                    {
                        "time": "7:30 PM",
                        "period": "Evening Dining & Entertainment",
                        "activity": "Time Out Market",
                        "description": "Lisbon's famous food hall along the riverfront. Sample gourmet dishes from top Portuguese chefs under one roof — from ceviche to custard tarts.",
                        "cost_local": 25,
                        "cost_usd": 27.00,
                        "category": "dining",
                    },
                ],
                "day_total_local": 53,
                "day_total_usd": 57.24,
            },
            {
                "day": 2,
                "theme": "Belém's Golden Age & Waterfront",
                "neighborhood_cluster": "Belém / Ajuda",
                "slots": [
                    {
                        "time": "9:30 AM",
                        "period": "Morning Sightseeing",
                        "activity": "Jerónimos Monastery",
                        "description": "UNESCO World Heritage masterpiece of Manueline architecture. Marvel at the ornate cloisters, vaulted ceilings, and the tomb of Vasco da Gama.",
                        "cost_local": 10,
                        "cost_usd": 10.80,
                        "category": "attraction",
                    },
                    {
                        "time": "11:30 AM",
                        "period": "Morning Sightseeing",
                        "activity": "Pastéis de Belém",
                        "description": "The original home of Portugal's iconic custard tart since 1837. Queue up (it's worth it!) for warm, flaky pastéis dusted with cinnamon.",
                        "cost_local": 5,
                        "cost_usd": 5.40,
                        "category": "dining",
                    },
                    {
                        "time": "1:00 PM",
                        "period": "Lunch",
                        "activity": "Ponto Final (Cacilhas)",
                        "description": "Take the quick ferry across to Cacilhas for the best riverside dining in Lisbon. Fresh grilled fish with Lisbon's skyline as your backdrop.",
                        "cost_local": 20,
                        "cost_usd": 21.60,
                        "category": "dining",
                    },
                    {
                        "time": "3:30 PM",
                        "period": "Afternoon Leisure",
                        "activity": "Tower of Belém & Monument to the Discoveries",
                        "description": "Walk along the waterfront to see the iconic 16th-century tower and the impressive monument celebrating Portugal's Age of Exploration.",
                        "cost_local": 8,
                        "cost_usd": 8.64,
                        "category": "attraction",
                    },
                    {
                        "time": "7:00 PM",
                        "period": "Evening Dining & Entertainment",
                        "activity": "LX Factory",
                        "description": "Trendy industrial complex converted into a creative hub with restaurants, bars, boutiques, and street art. Try a craft cocktail at Rio Maravilha rooftop.",
                        "cost_local": 30,
                        "cost_usd": 32.40,
                        "category": "entertainment",
                    },
                ],
                "day_total_local": 73,
                "day_total_usd": 78.84,
            },
            {
                "day": 3,
                "theme": "Bohemian Bairro Alto & Chiado Culture",
                "neighborhood_cluster": "Bairro Alto / Chiado / Príncipe Real",
                "slots": [
                    {
                        "time": "10:00 AM",
                        "period": "Morning Sightseeing",
                        "activity": "National Tile Museum (Museu do Azulejo)",
                        "description": "Discover 500 years of Portugal's azulejo tradition in a stunning 16th-century convent. A must for design and art lovers.",
                        "cost_local": 5,
                        "cost_usd": 5.40,
                        "category": "attraction",
                    },
                    {
                        "time": "12:00 PM",
                        "period": "Lunch",
                        "activity": "Cervejaria Ramiro",
                        "description": "Legendary seafood restaurant famous for its giant tiger prawns, percebes (goose barnacles), and the traditional steak sandwich chaser.",
                        "cost_local": 35,
                        "cost_usd": 37.80,
                        "category": "dining",
                    },
                    {
                        "time": "2:30 PM",
                        "period": "Afternoon Leisure",
                        "activity": "Príncipe Real Gardens & Boutique Shopping",
                        "description": "Stroll through this chic neighborhood's garden square, browse independent boutiques, and visit the Embaixada concept store in a stunning Moorish palace.",
                        "cost_local": 15,
                        "cost_usd": 16.20,
                        "category": "shopping",
                    },
                    {
                        "time": "5:00 PM",
                        "period": "Afternoon Leisure",
                        "activity": "Tram 28 Ride",
                        "description": "Hop on Lisbon's most famous vintage tram for a rattling ride through the city's steepest, most picturesque neighborhoods.",
                        "cost_local": 3,
                        "cost_usd": 3.24,
                        "category": "transport",
                    },
                    {
                        "time": "8:00 PM",
                        "period": "Evening Dining & Entertainment",
                        "activity": "Fado Night in Bairro Alto",
                        "description": "End your trip with an unforgettable evening of live Fado music at a traditional casa de fados. Sip port wine as soulful voices fill the candlelit room.",
                        "cost_local": 40,
                        "cost_usd": 43.20,
                        "category": "entertainment",
                    },
                ],
                "day_total_local": 98,
                "day_total_usd": 105.84,
            },
            {
                "day": 4,
                "theme": "Sintra Day Trip — Fairytale Palaces",
                "neighborhood_cluster": "Sintra (Day Trip, 40 min by train)",
                "slots": [
                    {
                        "time": "8:30 AM",
                        "period": "Morning Sightseeing",
                        "activity": "Train to Sintra + Pena Palace",
                        "description": "Take the scenic train from Rossio station to Sintra. Visit the colorful Pena Palace perched atop the Sintra Mountains with breathtaking views.",
                        "cost_local": 18,
                        "cost_usd": 19.44,
                        "category": "attraction",
                    },
                    {
                        "time": "12:00 PM",
                        "period": "Lunch",
                        "activity": "Tascantiga (Sintra)",
                        "description": "Charming local restaurant serving traditional Portuguese dishes like arroz de pato (duck rice) and fresh market-driven specials.",
                        "cost_local": 15,
                        "cost_usd": 16.20,
                        "category": "dining",
                    },
                    {
                        "time": "2:00 PM",
                        "period": "Afternoon Leisure",
                        "activity": "Quinta da Regaleira",
                        "description": "Explore the mysterious estate with its iconic Initiation Well, underground tunnels, grottos, and lush gardens filled with symbolism.",
                        "cost_local": 10,
                        "cost_usd": 10.80,
                        "category": "attraction",
                    },
                    {
                        "time": "7:00 PM",
                        "period": "Evening Dining & Entertainment",
                        "activity": "Sunset Drinks at Park Bar (Lisbon)",
                        "description": "Back in Lisbon, head to this hidden rooftop bar atop a parking garage for panoramic sunset views over the city with craft cocktails.",
                        "cost_local": 20,
                        "cost_usd": 21.60,
                        "category": "entertainment",
                    },
                ],
                "day_total_local": 63,
                "day_total_usd": 68.04,
            },
            {
                "day": 5,
                "theme": "Modern Lisbon & Parque das Nações",
                "neighborhood_cluster": "Parque das Nações / Graça",
                "slots": [
                    {
                        "time": "9:30 AM",
                        "period": "Morning Sightseeing",
                        "activity": "Oceanário de Lisboa",
                        "description": "One of the world's best aquariums, designed by Peter Chermayeff. The central tank with ocean sunfish, sharks, and rays is mesmerizing.",
                        "cost_local": 25,
                        "cost_usd": 27.00,
                        "category": "attraction",
                    },
                    {
                        "time": "12:30 PM",
                        "period": "Lunch",
                        "activity": "Mercado da Ribeira (Modern Wing)",
                        "description": "Another visit to the market — this time exploring the fresh produce side and grabbing a gourmet lunch from a different chef stall.",
                        "cost_local": 18,
                        "cost_usd": 19.44,
                        "category": "dining",
                    },
                    {
                        "time": "2:30 PM",
                        "period": "Afternoon Leisure",
                        "activity": "Graça Viewpoint & Feira da Ladra",
                        "description": "Visit the highest viewpoint in Lisbon for final panoramic photos, then browse the famous flea market for vintage souvenirs.",
                        "cost_local": 10,
                        "cost_usd": 10.80,
                        "category": "shopping",
                    },
                    {
                        "time": "7:30 PM",
                        "period": "Evening Dining & Entertainment",
                        "activity": "Farewell Dinner at Belcanto",
                        "description": "End your Lisbon journey at José Avillez's 2-Michelin-star restaurant for a creative tasting menu celebrating modern Portuguese cuisine.",
                        "cost_local": 85,
                        "cost_usd": 91.80,
                        "category": "dining",
                    },
                ],
                "day_total_local": 138,
                "day_total_usd": 149.04,
            },
        ],
        "trip_total_local": 425,
        "trip_total_usd": 459.00,
        "trip_total_inr": 38467.50,
    }

    # Trim to requested duration
    DEMO_ITINERARY["days"] = DEMO_ITINERARY["days"][:duration]
    total_local = sum(d["day_total_local"] for d in DEMO_ITINERARY["days"])
    total_usd = sum(d["day_total_usd"] for d in DEMO_ITINERARY["days"])
    DEMO_ITINERARY["trip_total_local"] = total_local
    DEMO_ITINERARY["trip_total_usd"] = round(total_usd, 2)
    DEMO_ITINERARY["trip_total_inr"] = round(total_usd * 83.5, 2)

    return DEMO_ITINERARY


def get_demo_swap(day: int, slot_index: int, instruction: str) -> dict:
    """Return a demo swapped activity."""
    return {
        "time": "2:30 PM",
        "period": "Afternoon Leisure",
        "activity": "Outdoor Street Market & Local Crafts",
        "description": f"Based on your request: '{instruction}'. Explore a vibrant local street market with handmade crafts, fresh produce, vintage finds, and live street musicians. A perfect way to soak in the local culture.",
        "cost_local": 8,
        "cost_usd": 8.64,
        "category": "exploration",
    }


def get_demo_day_regeneration(day: int, preferences: dict) -> dict:
    """Return a demo regenerated day."""
    return {
        "day": day,
        "theme": "Regenerated — Local Hidden Gems",
        "neighborhood_cluster": "Off-the-beaten-path",
        "slots": [
            {
                "time": "10:00 AM",
                "period": "Morning Sightseeing",
                "activity": "Local Neighborhood Walking Tour",
                "description": "Discover a charming residential neighborhood that most tourists miss. Chat with locals, admire street art, and find the best corner café.",
                "cost_local": 0,
                "cost_usd": 0,
                "category": "exploration",
            },
            {
                "time": "1:00 PM",
                "period": "Lunch",
                "activity": "Family-Run Local Restaurant",
                "description": "A generations-old family restaurant serving authentic home-style cooking. The kind of place only locals know about.",
                "cost_local": 12,
                "cost_usd": 12.96,
                "category": "dining",
            },
            {
                "time": "3:00 PM",
                "period": "Afternoon Leisure",
                "activity": "Artisan Workshop Visit",
                "description": "Visit a local artisan's workshop — ceramics, textiles, or woodwork depending on the city. Watch craftspeople at work and pick up a unique souvenir.",
                "cost_local": 15,
                "cost_usd": 16.20,
                "category": "shopping",
            },
            {
                "time": "7:00 PM",
                "period": "Evening Dining & Entertainment",
                "activity": "Sunset Rooftop Cocktails & Tapas",
                "description": "End the day at a rooftop bar with panoramic views, craft cocktails, and small plates as the city lights up below.",
                "cost_local": 28,
                "cost_usd": 30.24,
                "category": "entertainment",
            },
        ],
        "day_total_local": 55,
        "day_total_usd": 59.40,
    }


# Emergency contacts by country for PDF export
EMERGENCY_CONTACTS = {
    "Japan": {"police": "110", "ambulance": "119", "fire": "119", "tourist_helpline": "03-3501-3224", "us_embassy": "+81-3-3224-5000"},
    "Turkey": {"police": "155", "ambulance": "112", "fire": "110", "tourist_helpline": "+90-312-309-0692", "us_embassy": "+90-312-455-5555"},
    "Italy": {"police": "113", "ambulance": "118", "fire": "115", "tourist_helpline": "+39-06-4686-2837", "us_embassy": "+39-06-46741"},
    "Indonesia": {"police": "110", "ambulance": "118", "fire": "113", "tourist_helpline": "+62-21-500-373", "us_embassy": "+62-21-5083-1000"},
    "Tanzania": {"police": "112", "ambulance": "114", "fire": "114", "tourist_helpline": "+255-22-211-1044", "us_embassy": "+255-22-229-4000"},
    "Mexico": {"police": "911", "ambulance": "911", "fire": "911", "tourist_helpline": "+52-55-5089-7500", "us_embassy": "+52-55-5080-2000"},
    "France": {"police": "17", "ambulance": "15", "fire": "18", "tourist_helpline": "+33-1-4267-2222", "us_embassy": "+33-1-4312-2222"},
    "Peru": {"police": "105", "ambulance": "117", "fire": "116", "tourist_helpline": "+51-1-574-8000", "us_embassy": "+51-1-618-2000"},
    "India": {"police": "100", "ambulance": "108", "fire": "101", "tourist_helpline": "1363", "us_embassy": "+91-11-2419-8000"},
    "Portugal": {"police": "112", "ambulance": "112", "fire": "112", "tourist_helpline": "+351-21-342-1623", "us_embassy": "+351-21-727-3300"},
    "United States": {"police": "911", "ambulance": "911", "fire": "911", "tourist_helpline": "N/A", "us_embassy": "N/A (Domestic)"},
    "default": {"police": "112", "ambulance": "112", "fire": "112", "tourist_helpline": "Contact your embassy", "us_embassy": "Contact your embassy"},
}
