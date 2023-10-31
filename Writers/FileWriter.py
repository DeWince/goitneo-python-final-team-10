import pickle
from pathlib import Path


class FileWriter:
    DO_SAVE = True

    def __init__(self, filename="phonebook"):
        self.file = filename
        if type(filename) == str:
            self.file = Path(__file__).parent / filename
        # end if
    # end def

    def save(self, data):
        if FileWriter.DO_SAVE:
            try:
                with open(self.file, 'wb') as f:
                    pickle.dump(data, f)
            except:
                raise Exception("write")
            # end with
        # end if
    # end def

    def load(self):
        if not self.file.exists():
            return
        # end if

        with open(self.file, "rb") as f:
            try:
                return pickle.load(f)
            except:
                raise Exception("read")
            # end try
        # end with
    # end def
# end class
