pyinstaller \
    --noconfirm \
    --windowed \
    --name=NotesManager\
    src/main.py;

echo "./dist/NotesManager/NotesManager.exe"
./dist/NotesManager/NotesManager.exe;
