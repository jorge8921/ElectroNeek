Function TestMacros(color1, color2)
Dim xlApp, EmailBook
Set xlApp = CreateObject("Excel.Application")
Set EmailBook = xlApp.Workbooks.Open(WScript.Arguments(0))
EmailBook.Sheets("data").Range("B2:B3").Interior.ColorIndex = color1
EmailBook.Sheets("data").Range("B4:B5").Interior.ColorIndex = color2
EmailBook.Save
EmailBook.Close True
xlApp.Quit
TestMacros = "DONE"
End Function