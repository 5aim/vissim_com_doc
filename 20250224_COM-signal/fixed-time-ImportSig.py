# This is the example to use Fixed Time by importing sig file #

import os
import win32com.client as com

NUM_SG = 2

# Open Vissim and load Base model
Vissim = com.gencache.EnsureDispatch("Vissim.Vissim.23") #
path = os.getcwd()
Vissim.LoadNet(f'{path}\Base.inpx')

# Add Signal Controller and Groups
SC = Vissim.Net.SignalControllers.AddSignalController(0)
[SC.SGs.AddSignalGroup(0) for i in range(NUM_SG)]

# Set the internal supply data and (option) program number
SC.SetAttValue('SupplyFile2', '2SGs.sig')
SC.SetAttValue('ProgNo', 1000)

# Save and reopen the file to import it into inpx -> This procedure is necessary in this case.
Vissim.SaveNetAs(f'{path}\AfterImport.inpx')
Vissim.LoadNet(f'{path}\AfterImport.inpx')

# Add Signal Heads
SH1 = Vissim.Net.SignalHeads.AddSignalHead(0, Vissim.Net.Links.ItemByKey(1).Lanes.ItemByKey(1), 80)
SH2 = Vissim.Net.SignalHeads.AddSignalHead(0, Vissim.Net.Links.ItemByKey(2).Lanes.ItemByKey(1), 80)
SH1.SetAttValue('SG', '1-1')
SH2.SetAttValue('SG', '1-2')