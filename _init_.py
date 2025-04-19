"""Smart Irrigation Integration for Home Assistant."""
from homeassistant.core import HomeAssistant

DOMAIN = "Auto_Smart_EV_Irrigation_Scheduler"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Smart Irrigation integration."""
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up from a config entry."""
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Handle unloading."""
    return True
