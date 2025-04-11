import streamlit as st
from streamlit_state_manager import StateManager


def main():
    st.title("Basic Counter App")

    # Initialize a counter in the global state
    StateManager.init("counter", 0)
    count = StateManager.get("counter")

    # Display the counter
    st.write(f"Current count: {count}")

    # Button to increment counter
    if st.button("Increment"):
        StateManager.set("counter", count + 1)
        st.rerun()

    # Button to reset counter
    if st.button("Reset"):
        StateManager.set("counter", 0)
        st.rerun()


if __name__ == "__main__":
    main()
