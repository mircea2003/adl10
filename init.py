"""The ACREL ADL10 integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "acrel_adl10"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the ACREL ADL10 component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up ACREL ADL10 from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True
