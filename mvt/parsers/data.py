from typing import Tuple

import attrs

from schemas.data import DataSchemas


@attrs.define
class DataParser:
    def _split_data(self, data: str) -> DataSchemas:
        data_split = data.split(" ")
        data_schema = data_split[3]
        data_value = data_schema.split(",")
        result = DataSchemas(
            data_length=data_value[0],
            imei=data_value[1],
            command_type=data_value[2],
            event_code=data_value[3],
            latitude=data_value[4],
            longitude=data_value[5],
            date_and_time=data_value[6],
            position_status=data_value[7],
            number_satellites=data_value[8],
            gsm_signal_strength=data_value[9],
            speed=data_value[10],
            direction=data_value[11],
            hdop=data_value[12],
            altitude=data_value[13],
            mileage=data_value[14],
            run_time=data_value[15],
            base_station_info=data_value[16],
            io_port_status=data_value[17],
            analog_input_value=data_value[18],
            geo_france_number=data_value[19]
        )

        return result

    def parse(self, data: str) -> DataSchemas:
        return self._split_data(data)


if __name__ == "__main__":
    t = DataParser()
    r= t.parse("2022-04-28 02:14:52+0000 [Meitrack,2,182.2.41.88] $$g154,863083037661362,AAA,35,-6.988226,110.429756,220428021044,A,5,8,0,344,1.1,31,1498020,3007875,510|10|12CA|A94F,0000,0001|0002|0000|02DF|0102,00000011,*FB")
    print(r)

