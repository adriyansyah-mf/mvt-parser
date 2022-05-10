import attrs
from typing import List

@attrs.define
class DataSchemas:
    data_length: str
    imei: str
    command_type: str
    event_code: str
    latitude: str
    longitude: str
    date_and_time: str
    position_status: str
    number_satellites: str
    gsm_signal_strength: str
    speed: str
    direction: str
    hdop: str
    altitude: str
    mileage: str
    run_time: str
    base_station_info: str
    io_port_status: str
    analog_input_value: str
    geo_france_number: str
