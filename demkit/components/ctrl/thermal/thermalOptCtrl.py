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


from demkit.components.ctrl.optCtrl import OptCtrl

#MultiCommodity optimization basis.
#Note, wherever you find a c-index, the c is for commodity
class ThermalOptCtrl(OptCtrl):
	def __init__(self,  name,  host):
		#params
		OptCtrl.__init__(self,  name,  host)

		self.type = "controllers"
		self.timeBase = 900
		
		#System
		self.commodities = ['HEAT']
		self.weights = {'HEAT': 1}