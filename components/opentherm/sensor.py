from typing import Any, Dict

import esphome.config_validation as cv
from esphome.components import sensor

from . import const, schema, validate, generate

DEPENDENCIES = [ const.OPENTHERM ]
COMPONENT_TYPE = const.SENSOR

def get_entity_validation_schema(entity: schema.SensorSchema) -> cv.Schema:
    schema_params = {
        "accuracy_decimals": entity["accuracy_decimals"],
        "state_class": entity["state_class"]
    }
    
    if "unit_of_measurement" in entity:
        schema_params["unit_of_measurement"] = entity["unit_of_measurement"]
    if "device_class" in entity:
        schema_params["device_class"] = entity["device_class"]
    if "icon" in entity:
        schema_params["icon"] = entity["icon"]
    
    return sensor.sensor_schema(**schema_params)

CONFIG_SCHEMA = validate.create_component_schema(schema.SENSORS, get_entity_validation_schema)

async def to_code(config: Dict[str, Any]) -> None:
    await generate.component_to_code(
        COMPONENT_TYPE, 
        schema.SENSORS,
        sensor.Sensor, 
        generate.create_only_conf(sensor.new_sensor), 
        config
    )
