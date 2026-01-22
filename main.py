test_settings = {
    "theme": "dark",
    "language": "en",
    "notifications": True
}


def add_setting(settings, key_value_pair):
    key, value = key_value_pair

    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, key_value_pair):
    key, value = key_value_pair

    key = str(key).lower()
    value = str(value).lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, key):
    key = str(key).lower()

    if key not in settings:
        return "Setting not found!"
    del settings[key]
    return f"Setting '{key}' deleted successfully!"
