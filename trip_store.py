"""
trip_store.py — JSON-based trip persistence using Streamlit session state.
Zero external database dependencies.
"""

import json
import os
from datetime import datetime
from typing import Optional
import streamlit as st


class TripStore:
    """Manages trip persistence via session state with optional file backup."""

    STORAGE_FILE = "saved_trips.json"

    @staticmethod
    def _ensure_store():
        """Ensure saved_trips exists in session state."""
        if "saved_trips" not in st.session_state:
            st.session_state.saved_trips = {}
            TripStore._load_from_file()

    @staticmethod
    def _load_from_file():
        """Attempt to load saved trips from local JSON file."""
        try:
            if os.path.exists(TripStore.STORAGE_FILE):
                with open(TripStore.STORAGE_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    st.session_state.saved_trips = data
        except (json.JSONDecodeError, IOError, OSError):
            pass  # Silently fail — session state is primary store

    @staticmethod
    def _save_to_file():
        """Attempt to persist trips to local JSON file."""
        try:
            with open(TripStore.STORAGE_FILE, "w", encoding="utf-8") as f:
                json.dump(
                    st.session_state.saved_trips, f, indent=2, default=str
                )
        except (IOError, OSError):
            pass  # Silently fail on Cloud deployments

    @staticmethod
    def save_trip(name: str, preferences: dict, itinerary: dict) -> str:
        """Save a trip and return its ID."""
        TripStore._ensure_store()

        trip_id = f"trip_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        trip_data = {
            "id": trip_id,
            "name": name,
            "destination": itinerary.get("destination", preferences.get("destination", "Unknown")),
            "duration": len(itinerary.get("days", [])),
            "budget_level": preferences.get("budget_level", "Moderate"),
            "total_cost_usd": itinerary.get("trip_total_usd", 0),
            "saved_at": datetime.now().isoformat(),
            "preferences": preferences,
            "itinerary": itinerary,
        }

        st.session_state.saved_trips[trip_id] = trip_data
        TripStore._save_to_file()
        return trip_id

    @staticmethod
    def list_trips() -> list:
        """Return a list of saved trip summaries."""
        TripStore._ensure_store()
        trips = []
        for trip_id, data in st.session_state.saved_trips.items():
            trips.append({
                "id": trip_id,
                "name": data.get("name", "Untitled Trip"),
                "destination": data.get("destination", "Unknown"),
                "duration": data.get("duration", 0),
                "budget_level": data.get("budget_level", "Moderate"),
                "total_cost_usd": data.get("total_cost_usd", 0),
                "saved_at": data.get("saved_at", ""),
            })
        # Sort by saved_at descending (newest first)
        trips.sort(key=lambda x: x["saved_at"], reverse=True)
        return trips

    @staticmethod
    def load_trip(trip_id: str) -> Optional[dict]:
        """Load a specific trip by ID."""
        TripStore._ensure_store()
        return st.session_state.saved_trips.get(trip_id)

    @staticmethod
    def delete_trip(trip_id: str) -> bool:
        """Delete a trip by ID. Returns True if deleted."""
        TripStore._ensure_store()
        if trip_id in st.session_state.saved_trips:
            del st.session_state.saved_trips[trip_id]
            TripStore._save_to_file()
            return True
        return False

    @staticmethod
    def get_trip_count() -> int:
        """Return the number of saved trips."""
        TripStore._ensure_store()
        return len(st.session_state.saved_trips)
