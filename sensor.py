"""Platform for sensor integration."""
import serial
from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor platform."""
    async_add_entities([AcrelAdl10Sensor()])

class AcrelAdl10Sensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._serial_port = "/dev/ttyUSB0"  # Asigură-te că acest port este corect pentru setup-ul tău
        self._baud_rate = 9600
        self._serial_connection = serial.Serial(self._serial_port, self._baud_rate)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "ACREL ADL10 Smart Meter"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            self._serial_connection.write(b'YOUR_COMMAND_HERE')  # Trimite comanda necesară pentru a obține datele
            response = self._serial_connection.readline().decode('utf-8').strip()
            self._state = response  # Ajustează această linie pentru a procesa răspunsul
        except Exception as e:
            self._state = f"Error: {e}"
