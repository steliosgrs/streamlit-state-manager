import streamlit as st
from streamlit_state_manager import StateManager


def main():
    st.title("User Profile Example")

    # Create a namespaced manager for user profile
    profile = StateManager.create_namespace("profile")

    # Initialize profile state with defaults
    profile.init("name", "")
    profile.init("email", "")
    profile.init("preferences", {})

    # Form for editing profile
    with st.form("profile_form"):
        name = st.text_input("Name", profile.get("name"))
        email = st.text_input("Email", profile.get("email"))

        # Preference options
        st.subheader("Preferences")
        dark_mode = st.checkbox(
            "Dark Mode", profile.get("preferences").get("dark_mode", False)
        )
        notifications = st.checkbox(
            "Enable Notifications",
            profile.get("preferences").get("notifications", True),
        )

        # Save button
        if st.form_submit_button("Save Profile"):
            # Update profile data
            profile.set("name", name)
            profile.set("email", email)
            profile.set(
                "preferences", {"dark_mode": dark_mode, "notifications": notifications}
            )
            st.success("Profile saved!")

    # Show current state
    with st.expander("Current Profile Data"):
        st.json(
            {
                "name": profile.get("name"),
                "email": profile.get("email"),
                "preferences": profile.get("preferences"),
            }
        )

    # Reset button
    if st.button("Reset Profile"):
        profile.clear()
        st.rerun()


if __name__ == "__main__":
    main()
