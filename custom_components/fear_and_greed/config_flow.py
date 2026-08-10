"""Config flow for Fear and Greed Index."""

import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN


class FearAndGreedConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fear and Greed Index."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="Fear and Greed Index", data={})

        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))
