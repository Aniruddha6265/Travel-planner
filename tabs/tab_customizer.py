"""
tabs/tab_customizer.py — Tab 3: Vibe Customization & Dynamic Activity Swap.
Swap individual slots or regenerate entire days without wiping the rest.
"""

import streamlit as st
from llm_client import LLMClient


def render_customizer():
    """Render the Vibe Customization & Activity Swap tab."""
    st.markdown('<div class="section-title">🎨 Vibe Customization & Activity Swap</div>', unsafe_allow_html=True)

    itinerary = st.session_state.get("itinerary")
    if not itinerary or "days" not in itinerary:
        st.warning(
            "⚠️ No itinerary found! Please generate one in **Tab 2** first."
        )
        return

    days = itinerary["days"]
    prefs = st.session_state.preferences

    st.markdown(
        "Fine-tune your itinerary by swapping individual activities or regenerating entire days. "
        "The rest of your plan stays intact!"
    )

    # ── Single Activity Swap ──────────────────────────────
    st.markdown("### 🔄 Swap a Single Activity")

    col1, col2 = st.columns(2)
    with col1:
        day_options = [f"Day {d['day']} — {d.get('theme', '')}" for d in days]
        selected_day_idx = st.selectbox(
            "Select Day",
            range(len(day_options)),
            format_func=lambda i: day_options[i],
            key="swap_day",
        )

    selected_day = days[selected_day_idx]
    slots = selected_day.get("slots", [])

    with col2:
        slot_options = [
            f"{s.get('time', '')} — {s.get('activity', '')}" for s in slots
        ]
        selected_slot_idx = st.selectbox(
            "Select Activity to Swap",
            range(len(slot_options)),
            format_func=lambda i: slot_options[i],
            key="swap_slot",
        )

    # Show current activity details
    if slots:
        current_slot = slots[selected_slot_idx]
        st.markdown(
            f"""
            <div class="day-card" style="border-left-color: #FF6B6B;">
                <div style="font-size: 0.8rem; color: #888; margin-bottom: 4px;">Current Activity</div>
                <div style="font-weight: 600; color: #0B3D3D; font-size: 1.05rem;">
                    {current_slot.get('time', '')} — {current_slot.get('activity', '')}
                </div>
                <div style="color: #666; font-size: 0.9rem; margin-top: 4px;">
                    {current_slot.get('description', '')}
                </div>
                <div style="margin-top: 6px;">
                    <span class="tag-pill budget">💰 ${current_slot.get('cost_usd', 0):.0f}</span>
                    <span class="tag-pill interest">{current_slot.get('category', '').title()}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Swap instruction
    swap_instruction = st.text_input(
        "What would you like instead?",
        placeholder="e.g., 'Swap museum for outdoor market', 'Find a vegetarian lunch spot', 'Something more adventurous'",
        key="swap_instruction",
    )

    swap_col1, swap_col2 = st.columns(2)
    with swap_col1:
        swap_btn = st.button(
            "🔄 Swap This Activity",
            type="primary",
            use_container_width=True,
            disabled=not swap_instruction,
        )

    if swap_btn and swap_instruction:
        with st.spinner("🔄 Finding the perfect replacement..."):
            client = LLMClient(
                provider=st.session_state.api_provider,
                api_key=st.session_state.api_key,
                demo_mode=st.session_state.demo_mode,
            )
            day_num = selected_day["day"]
            new_slot = client.swap_activity(
                itinerary, day_num, selected_slot_idx, swap_instruction
            )

            if new_slot:
                # Store the old activity for diff display
                old_slot = dict(slots[selected_slot_idx])

                # Preserve the time and period from the original slot
                new_slot["time"] = old_slot["time"]
                new_slot["period"] = old_slot["period"]

                # Update the slot in the itinerary
                st.session_state.itinerary["days"][selected_day_idx]["slots"][selected_slot_idx] = new_slot

                # Recalculate day totals
                day_slots = st.session_state.itinerary["days"][selected_day_idx]["slots"]
                new_day_local = sum(s.get("cost_local", 0) for s in day_slots)
                new_day_usd = sum(s.get("cost_usd", 0) for s in day_slots)
                st.session_state.itinerary["days"][selected_day_idx]["day_total_local"] = new_day_local
                st.session_state.itinerary["days"][selected_day_idx]["day_total_usd"] = round(new_day_usd, 2)

                # Recalculate trip totals
                all_days = st.session_state.itinerary["days"]
                st.session_state.itinerary["trip_total_local"] = sum(d.get("day_total_local", 0) for d in all_days)
                st.session_state.itinerary["trip_total_usd"] = round(sum(d.get("day_total_usd", 0) for d in all_days), 2)
                rate_inr = itinerary.get("exchange_rate_to_inr", 83.5)
                rate_usd = itinerary.get("exchange_rate_to_usd", 1.0)
                total_usd = st.session_state.itinerary["trip_total_usd"]
                st.session_state.itinerary["trip_total_inr"] = round(total_usd * (rate_inr / rate_usd), 2)

                # Record swap history
                st.session_state.swap_history.append({
                    "day": day_num,
                    "old": old_slot,
                    "new": new_slot,
                    "instruction": swap_instruction,
                })

                st.success("✅ Activity swapped successfully!")

                # Show diff
                st.markdown(
                    f'<div class="swap-old">❌ {old_slot.get("activity", "")} — ${old_slot.get("cost_usd", 0):.0f}</div>'
                    f'<div class="swap-new">✅ {new_slot.get("activity", "")} — ${new_slot.get("cost_usd", 0):.0f}</div>',
                    unsafe_allow_html=True,
                )
                st.rerun()

    # ── Regenerate Entire Day ──────────────────────────────
    st.markdown("---")
    st.markdown("### 🔁 Regenerate an Entire Day")
    st.caption("Get a completely fresh set of activities for a specific day. All other days remain unchanged.")

    regen_col1, regen_col2 = st.columns(2)
    with regen_col1:
        regen_day_options = [f"Day {d['day']} — {d.get('theme', '')}" for d in days]
        regen_day_idx = st.selectbox(
            "Select Day to Regenerate",
            range(len(regen_day_options)),
            format_func=lambda i: regen_day_options[i],
            key="regen_day",
        )

    with regen_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        regen_btn = st.button(
            "🔁 Regenerate Day",
            type="secondary",
            use_container_width=True,
        )

    if regen_btn:
        with st.spinner("🎲 Creating a fresh day plan..."):
            client = LLMClient(
                provider=st.session_state.api_provider,
                api_key=st.session_state.api_key,
                demo_mode=st.session_state.demo_mode,
            )
            day_num = days[regen_day_idx]["day"]
            new_day = client.regenerate_day(itinerary, day_num, prefs)

            if new_day:
                # Replace the day in the itinerary
                new_day["day"] = day_num  # Preserve day number
                st.session_state.itinerary["days"][regen_day_idx] = new_day

                # Recalculate trip totals
                all_days = st.session_state.itinerary["days"]
                st.session_state.itinerary["trip_total_local"] = sum(d.get("day_total_local", 0) for d in all_days)
                st.session_state.itinerary["trip_total_usd"] = round(sum(d.get("day_total_usd", 0) for d in all_days), 2)
                rate_inr = itinerary.get("exchange_rate_to_inr", 83.5)
                rate_usd = itinerary.get("exchange_rate_to_usd", 1.0)
                total_usd = st.session_state.itinerary["trip_total_usd"]
                st.session_state.itinerary["trip_total_inr"] = round(total_usd * (rate_inr / rate_usd), 2)

                st.success(f"✅ Day {day_num} regenerated with theme: **{new_day.get('theme', '')}**")
                st.rerun()

    # ── Swap History ──────────────────────────────────────
    swap_history = st.session_state.get("swap_history", [])
    if swap_history:
        st.markdown("---")
        st.markdown("### 📝 Swap History")

        for i, swap in enumerate(reversed(swap_history)):
            with st.expander(f"Swap #{len(swap_history) - i}: Day {swap['day']} — \"{swap['instruction']}\""):
                st.markdown(
                    f'<div class="swap-old">❌ Old: {swap["old"].get("activity", "")} — ${swap["old"].get("cost_usd", 0):.0f}</div>'
                    f'<div class="swap-new">✅ New: {swap["new"].get("activity", "")} — ${swap["new"].get("cost_usd", 0):.0f}</div>',
                    unsafe_allow_html=True,
                )
