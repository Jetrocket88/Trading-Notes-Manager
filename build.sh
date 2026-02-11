pyinstaller \
    --noconfirm \
    --windowed \
    --name=NotesManager\
    src/main.py;

echo "running program now..."
./dist/NotesManager/NotesManager.exe;
