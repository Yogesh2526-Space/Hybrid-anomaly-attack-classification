strComputer = "." 'Can set to remote machine.

dim colItems, objItem

On Error Resume Next
Set oWMI = GetObject _
      ("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\SecurityCenter")

strText=strText & vbCrLF & vbCrLf & "Antivirus Information" & vbCrLf
Set colItems = oWMI.ExecQuery("Select * from AntiVirusProduct")
for each objItem in colItems
    strText=strText & "------------------------------------------------------" & vbCrLf
    strText=strText & "companyName: " & objItem.companyName & vbCrLf
    strText=strText & "displayName: " & objItem.displayName & vbCrLf
'    strText=strText & "instanceGuid: " & objItem.instanceGuid & vbCrLf
    strText=strText & "onAccessScanningEnabled: "
    strText=strText & objItem.onAccessScanningEnabled  & vbCrLf
    strText=strText & "productUptoDate: " & objItem.productUptoDate & vbCrLf
    strText=strText & "versionNumber: " & objItem.versionNumber & vbCrLf
    strText=strText & "------------------------------------------------------" & vbCrLf
next
WScript.echo strText