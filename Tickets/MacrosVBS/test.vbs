Sub Eliminar_Filas()

 

Dim xlApp, Book, Sheet
Set xlApp = CreateObject("Excel.Application")
Set Book = xlApp.Workbooks.Open(WScript.Arguments(0))

Set Sheet = Book.Sheets("Activos Sin ROQ Cross")
      Sheet.Range("A18:A" & Sheet.Rows.Count).RowHeight = 65
      Sheet.Columns("A:Z").ColumnWidth = 14



MsgBox "Filas eliminadas", vbInformation, "DAM"


Book.Save
Book.Close True
xlApp.Quit


End Sub