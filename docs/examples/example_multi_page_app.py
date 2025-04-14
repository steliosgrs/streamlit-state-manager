import streamlit as st
from streamlit_state_manager import StateManager


def init_state():
    """Initialize all application state."""
    # Global app state
    StateManager.init("page", "home")
    StateManager.init("user_logged_in", False)

    # Create namespaces for different sections
    user = StateManager.create_namespace("user")
    user.init("id", None)
    user.init("name", "")
    user.init("role", "")

    cart = StateManager.create_namespace("cart")
    cart.init("items", [])
    cart.init("total", 0.0)

    settings = StateManager.create_namespace("settings")
    settings.init("theme", "light")
    settings.init("notifications", True)


def main():
    # Initialize state on first run
    # Using that ensures initialization runs only once
    if "initialized" not in st.session_state:
        init_state()
        st.session_state["initialized"] = True

    # App header
    st.title("E-commerce App")

    # Navigation
    pages = ["Home", "Products", "Cart", "Settings"]
    current_page = st.sidebar.radio(
        "Navigation", pages, index=pages.index(StateManager.get("page").capitalize())
    )
    StateManager.set("page", current_page.lower())

    # Login status
    user = StateManager.create_namespace("user")
    if not StateManager.get("user_logged_in"):
        with st.sidebar.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.form_submit_button("Login"):
                # Simulate login check
                if username and password:
                    StateManager.set("user_logged_in", True)
                    user.set("name", username)
                    user.set("role", "customer")
                    st.rerun()
                else:
                    st.error("Please enter credentials")
    else:
        st.sidebar.write(f"Logged in as: {user.get('name')}")
        if st.sidebar.button("Logout"):
            StateManager.set("user_logged_in", False)
            user.clear()
            st.rerun()

    # Render current page
    if StateManager.get("page") == "home":
        render_home_page()
    elif StateManager.get("page") == "products":
        render_products_page()
    elif StateManager.get("page") == "cart":
        render_cart_page()
    elif StateManager.get("page") == "settings":
        render_settings_page()


def render_home_page():
    st.header("Welcome to our store!")
    # Home page content here...


def render_products_page():
    st.header("Products")

    products = [
        {"id": 1, "name": "Product A", "price": 19.99},
        {"id": 2, "name": "Product B", "price": 29.99},
        {"id": 3, "name": "Product C", "price": 39.99},
    ]

    cart = StateManager.create_namespace("cart")

    for product in products:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{product['name']}** - ${product['price']}")
        with col2:
            if st.button("Add to Cart", key=f"add_{product['id']}"):
                # Add to cart
                items = cart.get("items")
                items.append(product)
                cart.set("items", items)

                # Update total
                cart.set("total", cart.get("total") + product["price"])
                st.success(f"Added {product['name']} to cart!")


def render_cart_page():
    st.header("Shopping Cart")

    cart = StateManager.create_namespace("cart")
    items = cart.get("items")

    if not items:
        st.info("Your cart is empty.")
    else:
        for i, item in enumerate(items):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{item['name']}** - ${item['price']}")
            with col2:
                if st.button("Remove", key=f"remove_{i}"):
                    # Remove from cart
                    cart.set("total", cart.get("total") - item["price"])
                    items.pop(i)
                    cart.set("items", items)
                    st.rerun()

        st.write(f"**Total: ${cart.get('total'):.2f}**")

        if st.button("Checkout"):
            # Process checkout
            st.success("Order placed successfully!")
            cart.set("items", [])
            cart.set("total", 0.0)
            st.rerun()


def render_settings_page():
    st.header("Settings")

    settings = StateManager.create_namespace("settings")

    # Theme setting
    theme = st.selectbox(
        "Theme", ["light", "dark"], index=["light", "dark"].index(settings.get("theme"))
    )
    settings.set("theme", theme)

    # Notification setting
    notifications = st.checkbox("Enable Notifications", settings.get("notifications"))
    settings.set("notifications", notifications)

    if st.button("Save Settings"):
        st.success("Settings saved!")


if __name__ == "__main__":
    main()
