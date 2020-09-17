import fpdf
from datetime import datetime
import os, sys, subprocess

class Recipt:
    '''Generate recipt for users'''

    @staticmethod
    def check_balance(id,balance):
        '''This function create a recipt bill for checking balance and open the file'''
        recipt = fpdf.FPDF('P', 'mm' ,(115,93))
        recipt.add_page()
        recipt.set_font('Arial', '', 9)

        text1 = "Welcome To Banking System".center(75,"-")
        text2 = f"Client ID: {id} \n Date: {datetime.now()} \n Check Balnace \n Amount: {balance} \n"
        text3 = "Thank You".center(80,"-")
        text= f"{text1} \n {text2} {text3}"

        recipt.multi_cell(100,10,text, border=0,align='c')
        recipt.output(f"{id}-recipt.pdf")

        #open the recipt file
        run_file(f"{id}-recipt.pdf")

        

def run_file(filename):
    '''' 
        This Function opens the pdf file after it has been created.
        os.startfile() is python function which opens file in windows only.
        to make it work in all part we have to check platform and run it.
        win32 == windows
        darwin == unix
        but in other systems we run a programm using subprocess.call()
        which is used to run the operating system command line commands using our code
        ex: to run program in linux we say (xdg-open 'filename')  in terminal.
        so to run the command we use subprocess.call() method

        Note: I write this code using many resources. 
        (stackoverflow, studied: os.startfile(), sys.platform(), subprocess.call())

    '''
    platform = sys.platform
    if platform == "win32":
        os.startfile(filename)
    elif platform == "darwin":
        subprocess.call(["open", filename])
    else:
        # for linux
        subprocess.call(["xdg-open", filename])