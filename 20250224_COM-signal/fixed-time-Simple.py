# This is the example to use Fixed Time (Simple). You cannot use Daily signal for this type #

import os
import win32com.client as com

NUM_SG = 2
SG_program = [[1.0, 25.0, 3.0, 0.0], [31.0, 54.0, 3.0, 0]]

# Open Vissim and load Base model
Vissim = com.gencache.EnsureDispatch("Vissim.Vissim.23") #
path = os.getcwd()
Vissim.LoadNet(f'{path}\Base.inpx')

# Add Signal Controller and Groups
SC = Vissim.Net.SignalControllers.AddSignalController(0)
[SC.SGs.AddSignalGroup(0) for i in range(NUM_SG)]

# Set Fixed Time "Simple" and cycle time for SC and signal program for SG
SC.SetAttValue('Type', 'FixedTimeSimple')
SC.SetAttValue('CycTm', 60)
SC.SGs.SetMultipleAttributes(['EndRed', 'EndGreen', 'Amber', 'RedAmber'], SG_program)

# Add Signal Heads
SH1 = Vissim.Net.SignalHeads.AddSignalHead(0, Vissim.Net.Links.ItemByKey(1).Lanes.ItemByKey(1), 80)
SH2 = Vissim.Net.SignalHeads.AddSignalHead(0, Vissim.Net.Links.ItemByKey(2).Lanes.ItemByKey(1), 80)
SH1.SetAttValue('SG', '1-1')
SH2.SetAttValue('SG', '1-2')