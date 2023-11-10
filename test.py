import clr #import clr from pythonnet

#load our dll file(mine is in my C:\\ folder)
clr.AddReference("C:\\Users\\stomn\\source\\repos\\CampaignSweeperDLL\\bin\\Debug\\CampaignSweeperDLL.dll")

#import our calculator class from Our C# namespace MyCalculator
from CampaignSweeperDLL import CMCLASS

calc = CMCLASS() #create our Calculator object

#calling our methoths and printing
print("Addition: "+str(calc.add(3, 2)))
print("Subtraction: "+str(calc.subtract(3, 2)))
print("Multiplication: "+str(calc.multiply(3, 2)))
print("Division: "+str(calc.divide(3, 2)))