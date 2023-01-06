#import sys, os, inspect
#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
##parentdir = os.path.dirname(parentdir)
#sys.path.insert(0, parentdir)


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
