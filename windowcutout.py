# Copyright 2014 NeuroData (http://neurodata.io)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

#
#   windowCutout
#   Window image cutouts for datasets have low range of pixel values
#   The following mathematical operation is performed
#   below minWindow = 0, above maxWindow = 255
#   outputVal = (inputVal - minWin)* (255/(maxWin - minWin))
#
def windowCutout ( cutout, window ):
  """Window image cutouts for datasets that have low range of pixel values"""
  
  [min_win, max_win] = window
  np.clip( cutout, min_win, max_win, out=cutout)
  np.subtract( cutout, min_win, out=cutout)
  # np.multiply( cutout, 255.0/(max_win-min_win), out=cutout)
  return np.multiply( cutout, 255.0/(max_win-min_win)).astype(dtype=np.uint16, copy=False)
