# User-Configuration-Manager
A simple Python project that allows users to manage their settings using a dictionary-based configuration system. This project includes functions to **add**, **update**, **delete**, and **view** user settings.

It was built as part of a freeCodeCamp lab project and follows the required user stories and test conditions.

---

## Features

- Add new settings
- Update existing settings
- Delete settings
- View all current settings in a readable format
- All keys and values are normalized to lowercase for consistency

---

### `delete_setting(settings, key)`
Deletes an existing setting.

**Parameters:**
- `settings` (dict): The settings dictionary
- `key` (str): The key to delete

**Returns:**
- Success message or error message

---

### `view_settings(settings)`
Displays all current settings.

**Parameters:**
- `settings` (dict): The settings dictionary

**Returns:**
- A formatted string of settings or a message if no settings exist

---

## Example

```python
test_settings = {
    "theme": "dark",
    "language": "en",
    "notifications": True
}

add_setting(test_settings, ("font_size", "medium"))
update_setting(test_settings, ("theme", "light"))
delete_setting(test_settings, "language")
print(view_settings(test_settings))
