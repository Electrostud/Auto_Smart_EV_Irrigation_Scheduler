from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class AutoSmartEVConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Auto Smart EV Irrigation Scheduler."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLLING

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Auto Smart EV Irrigation Scheduler", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("location"): str,
                vol.Required("api_key"): str,
                vol.Optional("soil_type", default="loamy"): vol.In(["sandy", "loamy", "clay"]),
            }),
            errors=errors
        )
