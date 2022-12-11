import logging
from typing import Any, Dict
import asyncio
# pylint: disable=import-error, no-member
import pyswitcherio
import voluptuous as vol

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.const import CONF_MAC, CONF_NAME, CONF_TYPE
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.restore_state import RestoreEntity

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "switcher_io"
DEFAULT_TYPE = "1"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_MAC): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_TYPE, default=DEFAULT_TYPE): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """IOSwitcher setup."""
    name = config.get(CONF_NAME)
    mac_addr = config[CONF_MAC]
    type = config.get(CONF_TYPE)
    add_entities([switcher_io(mac_addr, name, type)])


class switcher_io(SwitchEntity):
    """ioSwitcher."""

    def __init__(self, mac, name, type) -> None:
        """Initialize the ioSwitcher."""

        self._state = None
        self._last_run_success = None
        self._name = name
        self._type = type
        self._mac = mac
        self._power = False
        self._device = pyswitcherio.IOSwitcher(mac, int(type))

    def async_turn_on(self, **kwargs) -> None:
        """Turn device on."""
        result = asyncio.run(self._device.turn_on())
        if result:
            self._last_run_success = True
            self._power = True
        else:
            self._last_run_success = False

    def async_turn_off(self, **kwargs) -> None:
        result = asyncio.run(self._device.turn_off())
        if result:
            self._last_run_success = True
            self._power = False
        else:
            self._last_run_success = False

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return self._power

    @property
    def unique_id(self) -> str:
        """Return a unique, Home Assistant friendly identifier for this entity."""
        return self._mac.replace(":", "")+self._type

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._name

    @property
    def device_state_attributes(self) -> Dict[str, Any]:
        """Return the state attributes."""
        return {"last_run_success": self._last_run_success}
