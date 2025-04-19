import pytest
from homeassistant.setup import async_setup_component
from custom_components.auto_smart_ev_irrigation_scheduler import DOMAIN

@pytest.mark.asyncio
async def test_setup(hass):
    """Test the integration is set up correctly."""
    assert await async_setup_component(hass, DOMAIN, {DOMAIN: {}})
    assert DOMAIN in hass.data
