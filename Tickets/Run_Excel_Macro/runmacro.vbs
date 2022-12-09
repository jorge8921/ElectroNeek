sub runmacro()

Set Application = CreateObject("Excel.Application")
Set Excel = Application.Workbooks.Open(WScript.Arguments(0))




Set Rutina = Excel.Application.Workbooks(1).VBProject.VBComponents.Import("C:\tmp\filter.bas")
Application.Run (Rutina.Name & ".Filter_by")








Excel.save
Excel.Application.Quit

End sub



   