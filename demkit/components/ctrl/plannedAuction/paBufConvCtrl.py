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



from demkit.components.ctrl.bufConvCtrl import BufConvCtrl
from demkit.components.ctrl.auction.bufConvAuctionCtrl import BufConvAuctionCtrl

# TimeShiftable controller
class PaBufConvCtrl(BufConvCtrl, BufConvAuctionCtrl):
    def __init__(self,  name,  dev,  ctrl,  host):
        BufConvAuctionCtrl.__init__(self,  name, None, None, None)
        BufConvCtrl.__init__(self,   name,  dev,  ctrl,  host)

        self.useEventControl = False
        
        self.devtype = "BufferConverterController"
       
    def preTick(self, time, deltatime=0):
        BufConvCtrl.preTick(self, time)
        BufConvAuctionCtrl.preTick(self, time)    
        
    def timeTick(self, time, deltatime=0):
        BufConvCtrl.timeTick(self, time)
        BufConvAuctionCtrl.timeTick(self, time)    