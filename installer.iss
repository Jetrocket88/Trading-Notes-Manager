[Setup]
AppName=NotesManager
AppVersion=1.0
DefaultDirName={pf}\NotesManager
DefaultGroupName=NoetsManager
OutputBaseFilename=NotesInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\NotesManager\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\NotesManager"; Filename: "{app}\NotesManager.exe"
Name: "{commondesktop}\NotesManager"; Filename: "{app}\NotesManager.exe"

[Run]
Filename: "{app}\NotesManager.exe"; Description: "Launch MyApp"; Flags: nowait postinstall skipifsilent
