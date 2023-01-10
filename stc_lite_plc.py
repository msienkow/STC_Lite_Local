# Copyright 2023 Sani-Matic Inc. (sanimatic.com)

import stc_lite_mysql
from stc_logging import SaniTrendLogging
from pylogix import PLC, lgx_response
from dataclasses import dataclass, field
from math import isinf

plc_log = SaniTrendLogging('plc_errors')