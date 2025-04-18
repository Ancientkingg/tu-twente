# Copyright 2023 University of Twente

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from demkit.components.flow.el.elCable import ElCable

class DcCable(ElCable):
	def __init__(self,  name,  flowSim, nodeFrom, nodeTo, host):
		ElCable.__init__(self,  name, flowSim, nodeFrom, nodeTo, host)

		self.devtype = "ElectricityDirectCurrentCable"
		self.phases = 1
		self.hasNeutral = True

		self.current = [complex(0.0, 0.0)] * (self.phases+1)
		self.flowDirection = [1] * (self.phases+1)
		self.powered = [True] * (self.phases+1)

		# Mutual impedances of cables, are described in:
		# Reference: "Netten voor distributie van electriciteit" by Phase to Phase, 2012, section 8.2.8
		# https://phasetophase.nl/boek/index.html

		# Proper values can be obtained through the Types.xlsx file provided with the Gaia Demo download
		# The software, by Phase to Phase, can be obtained at: https://phasetophase.nl/vision-lv-network-design.html

		# The following values are and example
		self.impedance = [complex(0.26, 0.0), complex(0.26, 0.0)]

		self.length = 10    #in meters
		self.ampacity = 225 #capacity in amperes
		self.fuse = 0       #additional limit in amperes

	def voltageDrop(self, phase):
		if phase == 0 and not self.hasNeutral:
			return complex(0.0, 0.0)

		result = self.current[phase].real * self.scaledImpedance[phase].real

		return result
