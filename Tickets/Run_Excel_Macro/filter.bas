Sub Filter_by()
'
' Filter_by Macro
'

'
    Range("A1:B1").Select
    Selection.AutoFilter
    Range("B1").Select
    ActiveSheet.Range("$A$1:$B$33").AutoFilter Field:=2, Criteria1:="E"
    ActiveWorkbook.Save
End Sub
