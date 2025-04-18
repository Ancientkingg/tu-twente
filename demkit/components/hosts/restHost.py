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


from demkit.components.hosts.host import Host
from demkit.components.api.eveApi import EveApi
import time as tm
from datetime import datetime as dt

class RestHost(Host):
	def __init__(self, name="host", port = 5000, restApi = None, timeDelayBase: int = 1):
		self.liveOperation = True
		Host.__init__(self, name="host")

		self.enableFlowSim = False
		self.port = port
		self.address = "http://localhost"
		self.timeDelayBase = timeDelayBase
		self.restApi = restApi
		#FIXME: Need some mechanism to obtain the IP Address of the system, for now we hardcode default to localhost. T200



	def startup(self):
		Host.startup(self)

		if self.restApi is None:
			self.restApi = EveApi(self, self.port)

	def startSimulation(self):
		#startup all entities
		self.startup()

		#simulate time
		for t in range(0,  self.intervals):
			self.logMsg("Simulating @ "+dt.fromtimestamp(self.currentTime).strftime('%Y-%m-%d %H:%M:%S'))
			self.timeTick(self.currentTime)
			self.currentTime = self.currentTime + self.timeBase
			tm.sleep(self.timeDelayBase)

		#do a soft shutdown
		self.shutdown()

	def timeTick(self, time, absolute = True):
		self.executeCmdQueue()
		if not self.pause:
			Host.timeTick(self, time, absolute)

			self.requestTickets(time)
			while (len(self.tickets) > 0):
				self.announceNextTicket(time)

			self.storeStates()
			self.postTickLogging(time)