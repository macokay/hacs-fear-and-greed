"""Fear and Greed Index sensors."""
import logging
from datetime import timedelta

import aiohttp

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity

from .const import API_URL, DOMAIN, SCAN_INTERVAL_MINUTES

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(minutes=SCAN_INTERVAL_MINUTES)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Fear and Greed sensors from config entry."""
    coordinator = FearAndGreedCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([
        FearAndGreedValueSensor(coordinator),
        FearAndGreedClassificationSensor(coordinator),
    ])


class FearAndGreedCoordinator(DataUpdateCoordinator):
    """Coordinator that fetches data from the alternative.me API."""

    def __init__(self, hass):
        super().__init__(
            hass,
            _LOGGER,
            name="Fear and Greed Index",
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self):
        """Fetch latest data from alternative.me."""
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL) as response:
                response.raise_for_status()
                data = await response.json(content_type=None)
                return data["data"][0]


class FearAndGreedValueSensor(CoordinatorEntity, SensorEntity):
    """Sensor exposing the numeric Fear and Greed value (0-100)."""

    _attr_name = "Fear and Greed Index"
    _attr_unique_id = "fear_and_greed_value"
    _attr_icon = "mdi:gauge"
    _attr_native_unit_of_measurement = None

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def native_value(self):
        return int(self.coordinator.data["value"])

    @property
    def extra_state_attributes(self):
        return self.coordinator.data


class FearAndGreedClassificationSensor(CoordinatorEntity, SensorEntity):
    """Sensor exposing the text classification (Extreme Fear / Fear / Neutral / Greed / Extreme Greed)."""

    _attr_name = "Fear and Greed Classification"
    _attr_unique_id = "fear_and_greed_classification"
    _attr_icon = "mdi:emoticon-outline"

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def native_value(self):
        return self.coordinator.data["value_classification"]
