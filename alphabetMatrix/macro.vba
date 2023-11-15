Sub UpdateValuesBasedOnColor()
    Dim rng As Range
    Dim cell As Range
    
    ' Set the range to the desired grid of cells
    Set rng = ThisWorkbook.Sheets("Sheet1").Range("A1:W55")  ' Update with your sheet name and range
    
    For Each cell In rng
        If cell.Interior.Color = RGB(255, 255, 0) Then  ' Yellow
            cell.Value = 0
        ElseIf cell.Interior.Color = RGB(0, 0, 0) Then  ' Black
            cell.Value = 1
        End If
    Next cell
End Sub

' Macro made by ChatGPT