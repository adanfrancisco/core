"""
EMANE Bypass model for CORE
"""
from core.conf import Configuration
from core.emane import emanemodel
from core.enumerations import ConfigDataTypes


class EmaneBypassModel(emanemodel.EmaneModel):
    name = "emane_bypass"

    # values to ignore, when writing xml files
    config_ignore = {"none"}

    # mac definitions
    mac_library = "bypassmaclayer"
    mac_config = [
        Configuration(
            _id="none",
            _type=ConfigDataTypes.BOOL,
            default="0",
            options=["True", "False"],
            label="There are no parameters for the bypass model."
        )
    ]

    # phy definitions
    phy_library = "bypassphylayer"
    phy_config = []

    # override config groups
    @classmethod
    def config_groups(cls):
        return "Bypass Parameters:1-1"
