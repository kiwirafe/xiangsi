class FormatFuncs(object):
    def __init__(self):
        self.FormatList = [
            ".txt",
            ".doc",
            ".docx",
        ]
        
    def AppendFormat(self, fmt):
        if fmt in self.FormatList:
            return
        FContent = open("formats.py", "r").read()
        f = open("formats.py", "w")
        ListNum = FContent.find("]")
        FContent = FContent[:ListNum] + "\"" + fmt + "\",\n" +FContent[ListNum:]
        f.write(FContent)
        f.close()

    def RemoveFormat(self, fmt):
        FContent = open("formats.py", "r").read()
        f = open("formats.py", "w")
        FContent = FContent.replace("\"" + fmt + "\",\n", "")
        f.write(FContent)
        f.close()