sub runmacro()

Set Application = CreateObject("Excel.Application")
Set Excel = Application.Workbooks.Open(WScript.Arguments(0))




Set Rutina = Excel.Application.Workbooks(1).VBProject.VBComponents.Import("E:\AUTOMATIZACION\archivos\duplicados.bas")
Application.Run (Rutina.Name & ".borraduplicados")








Excel.save
Excel.Application.Quit

End sub



   