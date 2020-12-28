from mg import manager_create
import sys

manager = manager_create()
manager.file_read(sys.argv[1])
manager.argv_read()
