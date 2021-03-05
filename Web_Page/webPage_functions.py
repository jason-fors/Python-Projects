import webbrowser
import os

def makeWebPage(filename):
    """
    Creates the original web page the user wanted,
    if the html file does not already exist in the current directory.
    Requires filename as argument.
    """    
    folderPath = os.getcwd()
    folderDirectory = os.listdir(path=folderPath)
    if filename not in folderDirectory:  # Checks to see if web page file already exists.
        pyWebPage = open(filename, "w")
        pyWebPage.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\tStay tuned for our amazing summer sale!\n\t\t</h1>\n\t</body>\n</html>")


def openPage(url):
    """
    Opens user's web page.
    Requires file's url as argument.
    """
    webbrowser.open_new_tab(url)


def writeBody(filename, newBody):
    """
    Overwrites entire html file, with updated new body content.
    Requires filename and body content as arguments.
    """
    pyWebPage = open(filename, "w")
    pyWebPage.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\t{}\n\t\t</h1>\n\t</body>\n</html>".format(newBody))

def getBody(filename):
    """
    Returns the current content from the fourth line. Would need to be updated to
    handle multiple lines of new content.
    Requires filename as argument.
    """   
    pyWebPage = open(filename, "r")
    webContent = pyWebPage.readlines()  # Reading lines of html file into variable.
    return webContent[3][3:]    # Returning the fourth line, after the tabs. Not very adaptable.
        
    

if __name__ == "__main__":
    pass


