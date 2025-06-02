# Streamlit State Manager

The Streamlit State Manager `StateManager` is essentially a wrapper around [Streamlit's](https://github.com/streamlit/streamlit) native `st.session_state` dictionary, that simplifies how you interact with it.

## Features

1. **Cleaner Code**: Reduces boilerplate for initialization and access
2. **Error Prevention**: Reduces common pitfalls like missing initialization
3. **Namespacing**: Naturally groups related state variables
4. **Consistency**: Provides a consistent interface for state operations
5. **Maintainability**: Makes it easier to refactor state structure

## Installation

```bash
pip install streamlit-state-manager
```

## Use Cases

### StateManager

For simple apps **StateManager** provides a straightforward approach that's easy to implement and use.

#### 1. Simplified Access Patterns

**Streamlit**

```python
# Check if exists, initialize, then get
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
count = st.session_state["counter"]

# Updating value
st.session_state["counter"] += 1
```

**StateManager**

```python
from streamlit_state_manager import StateManager

# Get with auto-initialization
count = StateManager.get("counter", 0)

# Updating value
StateManager.set("counter", count + 1)
```

#### 2. Prevention of Common Errors

**Streamlit**

```python
# Potential KeyError if key doesn't exist
value = st.session_state["maybe_missing_key"]

# Forgetting to check existence before using
st.session_state["counter"] += 1  # Error if counter doesn't exist
```

**StateManager**

```python
# Safe access with optional default
value = StateManager.get("maybe_missing_key", default_value=None)
```

### NamespaceManager

For complex apps with multiple components you can use **NamespaceManager** to help you organize state and prevent key collisions.

#### 1. Structure Organization

**Streamlit**

```python
if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""
if "user_preferences" not in st.session_state:
    st.session_state["user_preferences"] = {}
```

Create a **NamespaceManager** through **StateManager**

```python
user = StateManager.create_namespace("user")
user.init("name", "")
user.init("email", "")
user.init("preferences", {})
```

#### 2. Namespace Management

**Streamlit**

```python
# Clearing all user-related keys
for key in list(st.session_state.keys()):
    if key.startswith("user_"):
        del st.session_state[key]
```

Use **NamespaceManager** through **StateManager**

```python
# Clearing all user-related keys
StateManager.clear_namespace("user")
```

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
