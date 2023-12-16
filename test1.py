import clr
# clr.AddReference("C:\\Users\\stomn\\source\\repos\\CampaignSweeper\\bin\\Release\\CampaignSweeper.dll")
clr.AddReference(r"C:\Users\stomn\OneDrive - Skellig Automation\Documents\Git\share\CampaignSweeper.dll")
from CampaignSweeper import CMINTERFACE

# Create an instance of the C# class
csharp_obj = CMINTERFACE()



message = csharp_obj.DidClassImport()
print(message)  # Output: Hello from C#!

csharp_obj._domain = "hello"
print(csharp_obj._domain )