REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Classes\.leox /f /ve /t REG_SZ /d "LeoxFile"
REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Classes\LeoxFile /f /ve /t REG_SZ /d "Leox File"
REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Classes\LeoxFile\DefaultIcon /f /ve /t REG_SZ /d "%~dp0Icons\LeoxDoc.ico"

REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Classes\LeoxFile\shell /f /ve /t REG_SZ /d "open"
REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Classes\LeoxFile\shell\open /f /ve /t REG_SZ /d "open"
REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Classes\LeoxFile\shell\open\command /f /ve /t REG_SZ /d "\"C:\void\sdk\Python27\python.exe\" \"%~dp0src\leo.py\" \"%%1\""
