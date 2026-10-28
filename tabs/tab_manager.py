"""
tabs/tab_manager.py — Tab 4: Trip Management & Offline PDF Export.
Save, load, delete trips and generate downloadable PDF guides.
"""

import streamlit as st
from trip_store import TripStore
from pdf_export import generate_pdf


def render_manager():
    """Render the Trip Management & PDF Export tab."""
    st.markdown('<div class="section-title">💼 Trip Management & Export</div>', unsafe_allow_html=True)

    itinerary = st.session_state.get("itinerary")
    prefs = st.session_state.preferences

    # ── Save Current Trip ──────────────────────────────────
    st.markdown("### 💾 Save Current Trip")

    if itinerary:
        destination = itinerary.get("destination", prefs.get("destination", "Unknown"))
        duration = len(itinerary.get("days", []))
        total_usd = itinerary.get("trip_total_usd", 0)

        st.markdown(
            f"📍 **{destination}** · {duration} days · ~${total_usd:.0f} USD"
        )

        save_col1, save_col2 = st.columns([3, 1])
        with save_col1:
            trip_name = st.text_input(
                "Trip Name",
                value=f"{destination} Adventure",
                placeholder="Give your trip a name...",
                key="save_trip_name",
            )
        with save_col2:
            st.markdown("<br>", unsafe_allow_html=True)
            save_btn = st.button(
                "💾 Save Trip",
                type="primary",
                use_container_width=True,
            )

        if save_btn and trip_name:
            trip_id = TripStore.save_trip(trip_name, prefs, itinerary)
            st.success(f"✅ Trip saved as **{trip_name}**! (ID: {trip_id})")
            st.rerun()
    else:
        st.info("ℹ️ Generate an itinerary in **Tab 2** first, then come back here to save it.")

    # ── PDF Export ──────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📄 Export as PDF")

    if itinerary:
        st.markdown(
            "Download a beautifully formatted offline PDF guide with your complete itinerary, "
            "budget breakdown, emergency contacts, and packing checklist."
        )

        export_col1, export_col2 = st.columns([1, 3])
        with export_col1:
            try:
                pdf_bytes = generate_pdf({"itinerary": itinerary}, prefs)
                destination_slug = itinerary.get("destination", "trip").lower().replace(" ", "_")
                filename = f"{destination_slug}_itinerary.pdf"

                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_bytes,
                    file_name=filename,
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(f"Error generating PDF: {e}")
        with export_col2:
            st.caption(
                "Your PDF includes:\n"
                "- 📋 Trip overview & preferences\n"
                "- 📅 Day-by-day itinerary with costs\n"
                "- 💰 Budget summary (local currency + USD + INR)\n"
                "- 🚨 Emergency contacts for your destination\n"
                "- ✅ Safety & packing checklists\n"
                "- 📝 Personal notes section"
            )
    else:
        st.info("ℹ️ Generate an itinerary in **Tab 2** to enable PDF export.")

    # ── Trip History ──────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📚 Trip History")

    trips = TripStore.list_trips()

    if not trips:
        st.info("📭 No saved trips yet. Generate and save your first trip!")
        return

    st.markdown(f"**{len(trips)} saved trip(s)**")

    for trip in trips:
        trip_id = trip["id"]
        trip_col1, trip_col2, trip_col3, trip_col4 = st.columns([4, 1, 1, 1])

        with trip_col1:
            # Trip info card
            saved_at = trip.get("saved_at", "")[:10]
            st.markdown(
                f"""
                <div class="trip-history-card">
                    <div>
                        <strong>{trip['name']}</strong>
                        <div style="font-size: 0.8rem; color: #888;">
                            📍 {trip['destination']} · {trip['duration']} days ·
                            {trip['budget_level']} · ~${trip['total_cost_usd']:.0f}
                        </div>
                        <div style="font-size: 0.75rem; color: #aaa;">Saved: {saved_at}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with trip_col2:
            if st.button("📂 Load", key=f"load_{trip_id}", use_container_width=True):
                _load_trip(trip_id)

        with trip_col3:
            if st.button("📄 PDF", key=f"pdf_{trip_id}", use_container_width=True):
                _export_saved_trip_pdf(trip_id)

        with trip_col4:
            if st.button("🗑️ Delete", key=f"del_{trip_id}", use_container_width=True):
                TripStore.delete_trip(trip_id)
                st.success(f"Deleted **{trip['name']}**")
                st.rerun()


def _load_trip(trip_id: str):
    """Load a saved trip into the active session."""
    trip_data = TripStore.load_trip(trip_id)
    if trip_data:
        st.session_state.itinerary = trip_data.get("itinerary")
        # Restore preferences
        saved_prefs = trip_data.get("preferences", {})
        for key, value in saved_prefs.items():
            st.session_state.preferences[key] = value
        st.session_state.swap_history = []
        st.success(f"✅ Loaded **{trip_data['name']}** — switch to Tab 2 to view your itinerary!")
        st.rerun()


def _export_saved_trip_pdf(trip_id: str):
    """Generate and offer PDF download for a saved trip."""
    trip_data = TripStore.load_trip(trip_id)
    if trip_data:
        try:
            itin = trip_data.get("itinerary", {})
            saved_prefs = trip_data.get("preferences", {})
            pdf_bytes = generate_pdf({"itinerary": itin}, saved_prefs)
            dest_slug = itin.get("destination", "trip").lower().replace(" ", "_")
            st.download_button(
                label=f"📥 Download {trip_data['name']}",
                data=pdf_bytes,
                file_name=f"{dest_slug}_itinerary.pdf",
                mime="application/pdf",
                key=f"dl_{trip_id}",
            )
        except Exception as e:
            st.error(f"Error: {e}")
