import esphome.codegen as cg
import esphome.config_validation as cv
#from esphome import automation
#from esphome.automation import maybe_simple_id
from esphome.components import i2c, binary_sensor, text_sensor
from esphome.const import (
    CONF_ID,
    CONF_RESET_PIN
)
from esphome import pins

MULTI_CONF = True

AUTO_LOAD = [ "binary_sensor", "text_sensor" ]

DEPENDENCIES = ['i2c']

respeaker_lite_ns = cg.esphome_ns.namespace('respeaker_lite')
RespeakerLite = respeaker_lite_ns.class_('RespeakerLite', i2c.I2CDevice, cg.Component)
#MuteSpeakerAction = respeaker_lite_ns.class_("MuteSpeakerAction", automation.Action)
#UnmuteSpeakerAction = respeaker_lite_ns.class_("UnmuteSpeakerAction", automation.Action)

CONF_MUTE_STATE= "mute_state"
CONF_FIRMWARE_VERSION= "firmware_version"
DEFAULT_ADDRESS = 0x42

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(RespeakerLite),
        cv.Required(CONF_RESET_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_MUTE_STATE): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_FIRMWARE_VERSION): text_sensor.text_sensor_schema(),
    }
).extend(i2c.i2c_device_schema(DEFAULT_ADDRESS))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    pin = await cg.gpio_pin_expression(config[CONF_RESET_PIN])
    cg.add(var.set_reset_pin(pin))

    if CONF_MUTE_STATE in config:
        mute_state = await binary_sensor.new_binary_sensor(config[CONF_MUTE_STATE])
        cg.add(var.set_mute_state(mute_state))

    if CONF_FIRMWARE_VERSION in config:
        firmware_version = await text_sensor.new_text_sensor(config[CONF_FIRMWARE_VERSION])
        cg.add(var.set_firmware_version(firmware_version))


# RESPEAKER_LITE_ACTION_SCHEMA = maybe_simple_id({cv.GenerateID(): cv.use_id(RespeakerLite)})

# async def respeaker_lite_action(config, action_id, template_arg, args):
#     var = cg.new_Pvariable(action_id, template_arg)
#     await cg.register_parented(var, config[CONF_ID])
#     return var

# automation.register_action(
#     "respeaker_lite.mute_speaker", MuteSpeakerAction, RESPEAKER_LITE_ACTION_SCHEMA
# )(respeaker_lite_action)
# automation.register_action(
#     "respeaker_lite.unmute_speaker", UnmuteSpeakerAction, RESPEAKER_LITE_ACTION_SCHEMA
# )(respeaker_lite_action)
