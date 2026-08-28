"""Test diagnostics.py's threading of config_entry_id through to device lookup (#992)."""

from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.smartthinq_sensors.const import DOMAIN, LGE_DEVICES
from custom_components.smartthinq_sensors.diagnostics import (
    async_get_config_entry_diagnostics,
)


async def test_async_get_config_entry_diagnostics_with_no_devices(hass):
    """Smoke test: config_entry_id threads through _async_devices_as_dict
    without error even when there are no LG devices registered yet."""
    entry = MockConfigEntry(domain=DOMAIN)
    entry.add_to_hass(hass)
    hass.data.setdefault(DOMAIN, {})[LGE_DEVICES] = {}

    result = await async_get_config_entry_diagnostics(hass, entry)

    assert result[LGE_DEVICES] == {}
    assert "entry" in result
