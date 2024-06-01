# first some information about the program and how to become a registered user
# this program and all the files it uses are copyrighted by Montana Interface Incorporated
# by having this program you are authorized to make two backup copies of each file including this one
# for more you should become a registered user
# For conditions, instructions, and  help see the file registerwithmii.doc
# second, the start of program actions
# we need to import some important outside programs, we need pandas and PySide6
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QPixmap, QFont, QValidator, QGuiApplication, QAction
from PySide6.QtWidgets import (QApplication, QVBoxLayout,
                               QLabel, QMainWindow, QWidget, QFileDialog, QLineEdit)
import time
from datetime import timedelta
# Third we must define and set the graphical user interface we will use
# it is called quizwindow.  You don't need to understand how it works
# but PySide6 is a powerful set of programming available in python and
# other popular programming languages.
class QuizWindow(QMainWindow):
    """
    Example skeleton to administer a quiz. Reed, edit as appropriate.
    """
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent, windowTitle="Quiz")
        # Set the application size.
        setf7 = [
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [10], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [0], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']],
            [['menu'], [2], [2000], [2], [0], [0], [30], [10], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
                'menufoot.mnc']]]
# filepath is read from controlstart.txt twice.  Here and at line 1694

        # f = open('c:/Users/Reed Howald/desktop/file1/outfile.txt', 'a')
        filepathi = './'
                                         #         filepathi = 'C:/Users/Reed Howald/Desktop/'
        f = open(filepathi + 'controlstart.txt', 'r')
        filepath = f.readline()
        currentrun = f.readline()
        print('71 filename is ', filepath + currentrun)
        print('72  currentrun is ', currentrun)
        ir = 0
        currentmenu = f.readline()
        filepathb = f.readline()
        currenttext = f.readline()
        print('77 runbi is ', runbi)
        get5f = f.readline()
        f.close()

        filepath = str(filepath)
        z = len(filepath) - 1
        filepath = filepath[:z]
        filepathb = './3file/'
        print('85 filepathb is ', filepathb, filepath)

#         n 'C:/Users/Reed Howald/desktop/filew/'
        firstrun = 'runfoot.rne'
        filename = filepath+firstrun
        f.close()
        print('line 91 filepath is ',  filepath, pic)
        fr = open(filepath + 'ccount.txt', 'r')
        cho = fr.readline()
        ccc = fr.readline()
        ccn = fr.readline()
        ccm = fr.readline()
        ccw = fr.readline()
        ccy = fr.readline()
        czz = fr.readline()
        czy = fr.readline()
        fr.close()
        setline = setf5[3][9]
        setcolumn = setf5[4][10]
        setfocus = runf[4][11]
        print('105', setline, setcolumn, setfocus)
        z = len(czy) - 1
        print('107 ccm is ', ccm, czz)
        czy = czy[:z]
        z = len(ccn) -1
        ccn = ccn[:z]
        self.input = QLineEdit()
#         if runf[3][8] == 837:
#             self.inut.setFocus()
        print('111 runf[4][10] is ', runf[4][10], runf[4][9])
#         self.input.returnPressed.connect(self.on_user_input)

        #         readcsvfile(filename, setf5)
        print('115 in Quizwindow   ',setf5[1][3], setf5[1][6])
        print('line 116 width and height at ', runf[0][15], ' ', runf[0][14])
        # TODO: Set to the size the user chose last time.
        geometry = QGuiApplication.primaryScreen().availableGeometry()
        self.resize(geometry.width() // float(str(runf[0][15])), geometry.height() // float(str(runf[0][14])))
        # Central widget
        self._main = QWidget()
        self.setCentralWidget(self._main)
        # Main menu bar
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("File")
        self.menu_file.addAction(QAction("Exit", self, triggered=QApplication.instance().quit))
        self.menu_file.addAction(QAction("Choose Picture", self, triggered=self.choose_picture))
        # Initially display some instructions. A subset of HTML may be used to format.
        self.content = QLabel("Reed,"
                              "<p>Choose <b>File - Choose Picture</b> to show a picture from your file system.</p>"
                              "<p>Current correct answer is 'ca'.</p>"
                              "<p>Current incorrect answers are 'ia', 'ib', 'ic'</p>"
                              "<p>Current partial credit answers are 'pa', 'pb', 'pc'</p>"
                              "Change these with:"
                              "<ul>"
                              "<li>set_correct_answers()</li>"
                              "<li>set_incorrect_answers()</li>"
                              "<li>set_partial_credit()</li>"
                              "<ul>")
        ## keep the previous content to compare in the resizing function
        self.lastContentSize = self.content.size()
        self.prevPic = None
        # Set the font size
        font = QFont()
        font.setPointSize(20)
        self.content.setFont(font)
        # This lets you resize the window so the image is smaller than it's actual size
        self.content.setMinimumSize(1, 1)
        self.content.setWordWrap(True)
        self.picture_shown = None
        self.user_keys = QLineEdit()
        self.edit = QLineEdit()
        self.header = QLineEdit()
        self.input = QLineEdit()
        font.setPointSize (int(runf[0][12]))
# Variables for the bottom widget set here
    #     with open(filepath + "ivy.txt", 'r')as f2:
    #         ivy = f2.readline()
        if int(setf5[5][11])  == 193:
            font.setPointSize (int(setf5[0][12]))
            #font.setPointSize(12)
            print('158 using setf5 with ', setf5[0][12], runf[0][12], setf5[0][16])        #         irb = f2.readline()
    #         ivz = f2.readline()
#         self.on_user_input.setFocus(self)
#         print('136 ', ivy, ihx)
#         setline = setline[0:-1]
#         setfocus = setfocus[0:-1]
        if runf[3][7] == 894:
            self.user_keys.setFocus()
            print('166 with ', runf[3][7])
#             self.input.returnPressed.connect(self.on_user_input)
#             self.input.setFocus()
        self.resetfocus(self, setfocus)
        setfocus = int(setfocus)
        z = len(ccn) - 1
        ccn = ccn[:z]
        sp = ' '
        z = len(ccw) - 1
        ccw = ccw[:z]
#             print('150 setfocus = ', setfocus)
        print('177 setfocus = ', setfocus)
        self.input.returnPressed.connect(self.on_user_input)
        #         elif setfocus == 2:
        #             self.input.setFocus(self)          value = '239'
# #             value  = self.input.setText()
#             print('122 value is ', value, runf[1][6])
        setline = str(setf5[3][9])
#             runf[1][6] = int(value)
#             setf5[1][6] = int(value)
#         setline = str(runf[3][9])
#         setline = setline[0:-1]
        ivx = runf[3][8]
        print('190 bottom font set to ', int(runf[0][12]), ivx)
#         self.user_keys.setStyleSheet("QLineEdit {background: yellow;}")
        rz=str(runf[0][9])
        gz=str(runf[0][10])
        bz=str(runf[0][11])
        space=', '
        rgbb=rz+space+gz+space+bz
        print('196 '+rgbb, setline)
# ee        font = int(runf[0][12])
        if int(runf[5][9]) == 193:
#             font = int(setf5[0][12])
            print("200 font size ", runf[0][12], setf5[0][12])
#         self.user_keys.setStyleSheet("QLineEdit {background-color: rgb({r},{g},{b});}")
#         self.user_keys.setStyleSheet("QLineEdit {background-color: rgb(" + rz + "," + gz + "," + bz + ");}")
        self.user_keys.setStyleSheet("QLineEdit {background-color: rgb(" + rgbb + ");}")
#         self.user_keys.setStyleSheet("QLineEdit {background-color: rgb(220, 0, 100);}")
#         print("205 color  ",rz,gz,bz)
#                 "}")
#         self.user_keys.setStyleSheet("QLineEdit {background: (int(setf5[1][4]),int(setf5[1][5]),int(setf5[1][6]);}")
#         self.user_keys.setStyleSheet("QLineEdit {background: fromRgb(float(setf5[1][8]),float(setf5[1][9]),float(setf5[1][10]);}")
        self.user_keys.setFont(font)
        self.user_keys.setValidator(UserKeysValidator())
        self.user_keys.textEdited.connect(self.on_user_choice)
         # Lists of current multiple-choice answers (2-key combination)
        self.correct_answers = []
        self.incorrect_answers = []
#         self.partial_credit = []
#         self.set_correct_answers('ca,qt,nx,so,sb')
#         self.set_incorrect_answers('ia,ib,ic')
        print('222 filename is ', filename)
        fc = open(filepath + "chold2.txt", "r")
        chold2 = fc.read()
        filename = filepath + 'ir.txt'
        # The header is a typical widget
        fc = open(filepath + "chold.txt", 'r')
        chold = fc.read()
#         filepath = 'C:/Users/reedh/Desktop/pythonProject3/filez/'
        with open(filename, 'r')as f2:
            irs = f2.readline()
            irt = f2.readline()
            irr = f2.readline()
        print('233 irr = ', irr)
        ir = int(irr)
        print('235 ir = ', ir)
        tfile = str(runf[ir][2])
        print("237 tfile is ", tfile)
#         filepath = 'C:/Users/Reed Howald/Desktop/pythonProject3/filey/'
        fchoice = open(filepath + "choice.txt", 'r')
        choice = fchoice.read()
        print('241  ', tfile, ir, choice, filepath)
        fsize = runf[1][5]
        print('243 fsize is  ', fsize, runf[1][1])
        txf = 'You found this: '
        txg = 'special text '
        rowe = runf[3][9]
        if int(fsize) > 0:
            with open(filepath + tfile, 'r')as fd:
                txg = fd.read()
                fd.close()
            z = len(txg) - 1
            txf = txg[:z]
            print('253 txf is ', txf,'  ', setline)
        headerstring = txf + choice
        if runf[6][11] == 11:
            headerstring = txf + '  row is ' + str(ir)
            print('257 header is:  ', headerstring, txf, choice)
#         headerstring = 'You typed   ' + '  ' + str(choice)
#         setting edit widget size
        if int(setf5[5][11]) == 193:
            fsize = int(setf5[0][5])
            print('262 changing to ', fsize)
        else:
            fsize = int(runf[0][5])
        # fsize = 0
        font = QFont()
        print('267 edit font size set to ', fsize, runf[0][5], setf5[0][5], setf5[5][11])
        font.setPointSize(int(fsize))
        seteditfontsize = 'font-size:' + str(fsize) + 'pt '
#         font.setPointSize(int(str(runf[0][5])))
        self.header.setFont(font)
        acolon = ':'

        if int(runf[6][11]) == 25:
            if int(runf[6][10]) == 155:
                ccw = ccw + 1


#             headerstring = 'Congratulations! You picked a correct answer with '
            headerstring = 'wrong' + sp + sp
            headerstring = headerstring + ccn + acolon  + sp + ccm
            headerstring = headerstring + 'correct' + sp + ccw + acolon + 'You typed  ' + ccy
            print('282   headerstring is  ! ', headerstring)
        print('283 runf[6][11] is ', runf[6][11], ccm, ccw, ccy, runf[6][12])
        ii = 0
        if ccc == 3:
            tt = ccw[ii]
            while ii < 5:
                if choice == tt:
# dhoice is a duplicate
                    print('298 duplicate choice is  ', choice, ii, tt )
                    pic - dup.png
                    return()
            ii = ii+2







        ry = str(runf[ir - 0][6])
        gy = str(runf[ir - 0][7])
        by = str(runf[ir - 0][8])
#         ry = '255'
#         gy = '0'
#         by = '255'
        space = ', '
        rgba = ry + space + gy + space + by
        print('285 top ', rgba)
        self.header.setStyleSheet("QLineEdit {background-color: rgb("+rgba+");}")
#         self.header.setStyleSheet("QLineEdit {background-color: rgb(" + rgba + ");}")
        print("312 top widget color  ", ry, gy, by)
        print('313 runf[0][2] is ', runf[0][2], setf5[0][2])
        fsize = 53
        fsize = runf[1][5]
        settopfontsize = 'font-size:' + str(fsize) + 'pt '
#         self.header.setStyleSheet("background-color): magenta," + settopfontsize)
        print('318 top font size is ', fsize)
        self.header = QLineEdit()
        self.header = QLabel()
        #                                   "font-size: fsize;")


        head4 = 'The choice to get here was '
        self.header = QLabel()
        self.header.setStyleSheet("background-color: rgb("+rgba+");" +
                                    settopfontsize)
        self.header.setText(headerstring)
# the instructions for the edit widget use lines 200 through 259 at this time
        with open(filepath + "ivy.txt", 'r')as f2:
            ivy = f2.readline()
            ihx = f2.readline()
            irc = f2.readline()
            irb = f2.readline()
            ivz = f2.readline()
#             setline = f2.readline()
            print('337 ', ivy, ihx, ir)
        tfile = runf[ir][2]
        print('339 tfile = ', tfile, ir )
#         filepath = 'C:/Users/Reed Howald/Desktop/pythonProject3/filez/'
        fchoice = open(filepath + "choice.txt", 'r')
        choice = fchoice.read()
        tfile = str(tfile)
        with open(filepath + tfile, 'r')as f:
            txg = f.read()
            f.close()
        print('347 ', tfile, ir, ihx)
        z = len(txg) - 1
        txf = txg[:z]

        ix = int(setline)
        print('352 ivx = ', ivy, ir, setline, ix)
        sp = ' '
        sr = '\n'
        sp3 = '   '
        print('356  ', setline, ix)
        headerstring = txf
        headerstring = headerstring + '\n' + sp + str(runf[ix][1]) \
                       + sp + str(runf[ix][2]) + sp + str(runf[ix][3]) + sp + str(runf[ix][4]) \
                       + sp + str(runf[ix][5]) + sp3 + str(runf[ix][6]) + sp + str(runf[ix][7]) \
                       + sp + str(runf[ix][8]) + sp + str(runf[ix][9]) +sp +str(runf[ix][10]) \
                       + sp +str(runf[ix][11]) + sp3 + str(runf[ix][12]) + sp + str(runf[ix][13]) \
                       + sp + str(runf[ix][14]) + sp + str(runf[ix][15]) + sp + \
                       str(runf[ix][16]) + sp + str(runf[ix][17]  )

        print('366 edit is:  ', headerstring, txf)
        ufile = 'ed1.txt'
        with open(filepath + ufile, 'r')as f:
            tx1 = f.readline()
            tx2 = f.readline()
            tx3 = f.readline()
        ufile = runf[ir][int(ihx)+1]
        print('373 ', ufile)
#         with open(filepath + ufile, 'r') as f:
        ihx3 = int(ivx)
        with open(filepath + 'ihx3.txt', 'r') as fihx3:
            ihx3 = fihx3.readline()
        print("378 ihx3 is ", ihx3, ivx)
        ihx3 = 9
        tx4 = setf5[ix][ihx3]
        print('381 tx4 is ', tx4, ufile, ihx3, ix)
        tx4 = setf5[ix][ihx3]
        with open(filepathb + 'ed3.txt', 'r') as f:
 #             tx4 = f.readline()
            tx6 = f.readline()
            tx7 = f.readline()
            tx8 = f.readline()
            tx9 = f.readline()
            txa = f.readline()
            txb = f.readline()
        print('391 filepath ', filepath)
        ihx = int(ihx)
        fcolor = open(filepath + "colori.txt", 'r')
        colori = fcolor.read()
#         colori = int(colori)
        print('396 colori is ', str(colori), filepath)
#         colori = int(colori)
        print('384 txb is ', txb, txa)
        z = len(tx2) - 1
        tx2 = tx2[:z]
        z = len(tx3) - 1
        tx3 = tx3[:z]
        ihx2 = str(ivx)
        z = len(tx8) - 1
        tx8 = tx8[:z]
        z = len(tx9) - 1
        tx9 = tx9[:z]
        z = len(txa) - 1
        txa = txa[:z]
        z = len(txb) - 1
        txb = txb[:z]
        ihx3 = int(setf5[4][9])
#         ihx3 = setcolumn
        ihx4 = ihx3 + int(colori) - 1
        print('415 ihx4 ihx3 colori is   ', ihx4, ihx3, colori)
        print('416 tx8 and ihx4 are ', str(tx8), ihx4, str(tx9))
        colorarray = [tx8, tx9, txa, txb, tx8]
        headerstring = headerstring + tx1 + tx2 + ' Column ' + str(ihx4) + sp + ' is now ' + tx3 + \
                       str(runf[ix][ihx4]) + '\n' +tx6 + sp + str(colorarray[int(colori)])
        x =len(txb ) - 1
        txb = txb[:z]
        fsize = '33'
        fsize = runf[0][5]
        #         font.setPointSize(int(str(runf[1][6])))
        # print('234 font size set to ', runf[1][6])
        #         settopfontsize = "font-size:" + str(fsize) + "pt;"
        print('427 font size set to ', runf[2][5])
        irq = 0
        #         self.user_keys.setStyleSheet("QLineEdit {background: yellow;}")
        ry = str(runf[irq][6])
        gy = str(runf[irq][7])
        by = str(runf[irq][8])
        #         ry = '255'
        #         gy = '0'
        #         by = '255'
        space = ', '
        rgba = ry + space + gy + space + by
        print('436 edit color ', rgba)
        #         self.header.setStyleSheet("QLineEdit {background-color: rgb("+rgba+");}")
        #         self.header.setStyleSheet("QLineEdit {background-color: rgb(" + rgba + ");}")
        print("442 edit color  ", ry, gy, by)
        #
#         fsize = 3nnn
        fsize = int(runf[0][5])
        seteditfontsize = 'font-size:' + str(fsize) + 'pt '
        #         self.header.setStyleSheet("background-color): magenta," + settopfontsize)
        print('445 edit font size is ', fsize, ir)
        #         self.header = QLineEdit()
        self.edit = QLabel()
        #                                   "font-size: fsize;")
        #                                   "font-size: 25pt;")
        # Display some text in the header
        #         font.setPointSize(fsize)
        #         font.setPointSize(int(str(runf[1][6])))
        #         self.header.setStyleSheet("font-size: 51pt;")
        self.edit.setStyleSheet("background-color: rgb(" + rgba + ");" +
                                  seteditfontsize)
        self.edit.setText(headerstring)
#       start the input widget here for entering edit values
#    input INPUT widget starts here
#    line 183 is    self.input = QLineEdt()
        irq = ir
        ry = str(runf[irq][6])
        gy = str(runf[irq][7])
        by = str(runf[irq][8])
        #         ry = '255'
        #         gy = '0'
        #         by = '255'
        space = ', '
        rgba = ry + space + gy + space + by
        print(rgba)
        with open(filepath + 'chold2.txt', 'w') as f:
            f.write(choice)
        print("475 top  color  ", ry, gy, by)
        with open(filepath + 'chold.txt', 'w') as f:
            f.write(choice)
        fsize = int(runf[1][12])
        setinputfontsize = 'font-size:' + str(fsize) + 'pt '
        #         self.header.setStyleSheet("background-color): magenta," + settopfontsize)
        print('481 top font size is ', fsize, ir)
        self.user_keys.setFocus()
        self.input.setStyleSheet("background-color: rgb(" + rgba + ");" +
                                setinputfontsize)
        # Arrange the widgets in the window
        layout = QVBoxLayout(self._main)
        layout.addWidget(self.header)
#         if runf[1][4] > 256:
        layout.addWidget(self.edit)
        if int(runf[1][4]) > 31:
            layout.addWidget(self.input)
        layout.addWidget(self.content, stretch=1)
# stretch devotes all extra vertical space to this widget
        layout.addWidget(self.user_keys)

        print('495 runf[ir][13] is ', runf[ir][13], ir)
        if runf[ir][13]  == 29.5:
            ir = ir + 1
            choice = 'nb'
#             change(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)
            print('505: ' + filepath + ' ' + filename + ' ' + filepath + currentrun)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)
#         self.user_keys.setFocus()
#         if runf[1][9] == 16:
#             self.input.setFocus()

#         self.incorrect_answers = value.lower().split(',')
#         def set_partial_credit(self, value):
#         """
#         Set answers that will be given partial credit
#         :param value: a comma-delimited string of 2-letter answers
#         :return: None
       # self.partial_credit = value.lower().split(',')
    def resetfocus(self, setfocus, ir):
        setfocus = int(runf[3][9])
        print(f'512 in resetfocus ', setfocus)
        if setfocus == 1:
            QTimer.singleShot(0, self.user_keys.setFocus)
            print("473 with setfocus = ", setfocus)
        elif setfocus == 2:
            QTimer.singleShot(0, self.input.setFocus)
            print('476 setfocus = ', setfocus)
    def on_user_input(self):
#         self.input.setFocus()
        print(f'The user typed in {self.input.displayText()}')
        print('525  runf[3][9] is ', runf[3][9])
        value = 2
#         value = self.input.displayText()
#         setline = int(runf[3][9])
        setcolumn = int(runf[3][10])
        print('530 value is ', value, runf[setline][setcolumn], setline, setcolumn)
        setline = int(setf5[3][9])
#         runf[setline][setcolumn] = int(value)
        setf5[setline][setcolumn] = int(value)
        setcolumn = setcolumn + 1
        print('----537---------------------')
#         self.user_keys.setFocus()
    @Slot()
    def on_header(self, value):
        """
#         Check the user's answer and display an appropriate message.
#         If the user's answer is not known do nothing. The user must edit the answer.
#         :param value: The user's supplied answer.
#         :return: None
        """
        choice = value.lower()
#         filepath = 'C:/Users/Reed Howald/desktop/fileu/'

        fchoice = open(filepath + "choice.txt", 'w')
#         fchoice.write(choice)
#         fchoice.close()   replaced by better code
        with open(filepath + 'choice.txt', 'w')as f:
            f.write(choice)
        with open(filepathb + 'choice.txt', 'w')as f:
            f.write(choice)

#          if choice in self.correct_answers:
        if len(choice) == 1:
             time.sleep(1)
             self.show_text('This answer is <span style="font-weight: bold; color: green">Choice</span>')
             self.user_keys.setText(choice)
             dely = 52
             time.sleep(dely)
        print('562 choice ', choice,'  ', dely)
        value = choice
#         filepath = 'C:/Users/Reed Howald/desktop/fileu/'
#             fchoice = open(filepath+"choice.txt", 'r+')
#             fchoice.write(choice)
# exit() here also leaves the program completely
#             exit()
#             close.window()
#             delay1 = 200
#             delay1 = int(runf[2][4])
#             print('187 delay1 = ', delay1)
#             QTimer.singleShot(delay1, self.close)


    @Slot()
    def choose_picture(self):
        """
        Asks the user for picture file and displays it. This is currently a slot so that it can be connected
        to a menu or button.
        :return: None
        """
        picture_file_name, _filter = QFileDialog.getOpenFileName(self, "Open Image", ".",
                                                                 "Image Files (*.png *.jpg *.bmp)")
        if picture_file_name:
            self.show_picture(picture_file_name)
    def show_picture(self, filename):
        """
        Loads a picture from the file system and displays it
        :param filename: The path to a picture file
        :return: None
        """
        self.picture_shown = QPixmap(filename)
        self.update_scaled_picture()
    def update_scaled_picture(self):
        """
        If a current picture is set, scale it for the current content size and display it
        :return: None
        """
        if self.picture_shown is not None and (self.content.size() != self.lastContentSize or self.picture_shown != self.prevPic):
            # Qt.FastTransformation makes text very unreadable
            # Qt.KeepAspectRatioByExpanding fills up the current self.content from the origin of the pixmap (will truncate on small screens)
            print('QuizWindow::update_scaled_picture self.content.size is: (' + str(self.content.width()) + ', ' + str(self.content.height()) + ')')
            self.content.setPixmap(self.picture_shown.scaled(self.content.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.lastContentSize = self.content.size()
            self.prevPic = self.picture_shown
    def show_text(self, text):
        """
        Replaces current content with a text string
        :param text: The text to display.
        :return: None
        """
        self.picture_shown = None
        self.content.setText(text)
    def resizeEvent(self, event):
        """
        This gets called when the user resizes the window. If a picture is shown, rescale for the current
        content size.
        :param event: An event object passed by the GUI with information on the resize operation. Ignored for now.
        :return: None
        """
        self.update_scaled_picture()
    @Slot()
    def on_user_choice(self, value) :
        """
        Check the user's answer and display an appropriate message.
        If the user's answer is not known do nothing. The user must edit the answer.
        :param value: The user's supplied answer.
#         :return: None
        """
        choice = value.lower()
#         filepath = 'C:/Users/Reed Howald/desktop/file1/'
#         fchoice = open(filepath + "choice.txt", 'w')
#         fchoice.write(choice)
#         fchoice.close()   replaced by better code
#         print('631 filepath is ', filepath, filepath)
#         if filepath == filepathb:
        filepathb = './3file/'
        with open(filepath + 'choice.txt', 'w')as f:
            f.write(choice)
        with open(filepathb + 'choice.txt', 'w')as f:
            f.write(choice)
#         if choice in self.correct_answers:
        if runf[ir][14] == 1.037:
            print('641 quick return  ir = ', ir)

            return()
        if len(choice) == 1:
#             time.sleep(1)
#             self.show_text('This answer is <span style="font-weight: bold; color: green">Choice</span>')
            self.user_keys.setText(choice)
#             time.sleep(1)
            print('651 ', choice)
#             value = choice
#             filepath = 'C:/Users/Reed Howald/desktop/file1/'
#             fchoice = open(filepath+"choice.txt", 'r+')
#             fchoice.write(choice)
# exit() here also leaves the program completely
#             exit()
#             close.window()
#             delay1 = 200
# # #             print('309 header is:  ', headertext)

#             self.header.setText(headertext)
            delay1 = int(runf[2][4])
            print('664 delay1 = ', delay1)
            QTimer.singleShot(delay1, self.close)

# self.close()
            return(value)
#         elif choice in self.incorrect_answers:
#             self.show_text('This answer is <span style="font-weight: bold; color: red">INCORRECT</span>')
#             self.user_keys.setText(None)
#         elif choice in self.partial_credit:
#             self.show_text('This answer receives <span style="font-weight: bold">PARTIAL CREDIT</span>')
#             self.user_keys.setText(None)
class UserKeysValidator(QValidator):
    """
    Validator objects can be used to restrict what the user may type in a QLineEdit (and probably other widgets).
    Here any 2-character string is accepted. The QValidator.Invalid return will prevent the user from typing
    more than 2 characters at a time.
    """
    def validate(self, value, length):
        if length > 2:
            return QValidator.Invalid
        if length == 2:
# exit() here leaves the program completely
#             exit()
            return QValidator.Acceptable
#             delay1 = 200
            delay = runf[1][3]
            QTimer.singleShot(delay1, self.close)
#             self.close()
        return QValidator.Intermediate
# caution:  This ends setting up the graphiocal user interface
# This program does not work if implementing the GUI comes here
# It is essential to read the input files before the first picture
# is shown
# We want to go next to main()
# and main should look like the following:
# main()
#     print('starting the program footquiz.py')
#     print('This is designed to give a quiz on humanfeet')
#     currentrun = 'runpic.rnd'
#     currentmenu = 'menufoot.mnc'
#     ir = 0
#     readfiles(currentrun, currentmenu, ir)
def usewindow(runf, menuf, ir, pic, choice, setf5, getf5):
#     pic = 'C:/Users/Reed Howald/desktop/file1/footmenu1.png'
    pic = filepath+'footmenu1.png'
#     app = QApplication()
#     w = QuizWindow()
#     w.content.setPixmap(QPixmap(pic))
#     w.show()
#     app.exec_()
# These are the five lines I need to take out to get it to work how I want
    return(choice)
def initialize2(xxxf):
    xxxf = [[[0],['menu'], [15],[20],[30], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.1]],
           [[0],['menu'], [3000], [21], [22], [20], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.2]],
            [[1],['menu'], [3000], [2000], [40], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.3]],
            [[3],['menu'], [3000], [2000], [1], [2], 300, [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.4]],
            [[3],['menu'], [3000], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.5]],
            [[4],['menu'], [3000], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.6]],
            [[5],['menu'], [3000], [2000], [0], [0], [0], [30], [10], [10], [10], [0], [0], [0.], [0.], [0.3], [0.1], [0.7]],
            [[6],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [0.8]],
            [[7],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [0.9]],
            [[8],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.0]],
            [[9],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.1]],
            [[10],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.2]],
            [[11],['menu'], [3000], [200], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.3]],
            [[12],['menu'], [3000], [200], [15], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3],[0.1], [1.4]],
            [[13],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.5]],
            [[14],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.6]],
            [[15],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.7]],
            [[16],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.8]],
            [[17],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [1.9]],
            [[18],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [2.0]],
            [[19],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [2.1]],
            [[20],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [2.2]],
            [[21],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [2.3]],
            [[22],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [2.4]]]
    return(xxxf)
# main(0)
choice = 'nb'
ir = 0
# runf = [[['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
# ['menufoot.mnc']],
#         [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#             'menufoot.mnc']]]
menuf = [[[1], ['mf'], [' screenshot (9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.], [1.],
          [0.], [1.], [' Foot quiz']],
         [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.], [1.],
          [0.], [1.], ['Foot quiz']],
         [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.], [1.],
          [0.], [1.], ['Foot quiz']]]
# pic = "C:/Users/Reed Howald/PycharmProjects/footp/screenshot (9).png"
filepath = 'C:/Users/Reed Howald/desktop/file1/'
pic = filepath+'screenshot (9).png'
runf = [[['menu'], [3000], [21], [22], [20], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
               ['menufoot.mnc']],
            [['menu'], [1500], [20], [30], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
                ['menufoot.mnc']],
            [['menu'], [1500], [20], [30], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
                ['menufoot.mnc']],
            [['menu'], [1500], [20], [30], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
                ['menufoot.mnc']],
            [['menu'], [3000], [21], [22], [20], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
             ['menufoot.mnc']]]
setf5 = [[['menu'], [1500], [20], [30], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
            ['menufoot.mnc']],
           [['menu'], [3000], [21], [22], [20], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
               'menufoot.mnc']]]
getf5 = [[['menu'], [1500], [20], [30], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
            ['menufoot.mnc']],
           [['menu'], [3000], [21], [22], [20], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
               'menufoot.mnc']]]
runf = initialize2(runf)
setf5 = initialize2(setf5)
menuf = initialize2(menuf)
# setg6 = initialize2(setg6)
getf5 = initialize2(getf5)
usewindow(runf, menuf, ir, pic, choice, setf5, getf5)
print('choice now is ', choice)
# oldmain()
def writecsvfile(filename, xxxf, imax):
#     imax = xxxf[1][3]
    ip = 0
#    with open('runfoot.rnn', 'w') as f:
#       writer = csv.writer(f, delimiter = '&')
#       writer.writerows(setf5, deliniter = '&')
#       writer.writerows(setf5)
    dataframe_good = pd.DataFrame(xxxf)
#     dataframe_bad = pd.DataFrame(setf5)
#     df.to_csv(filename, delimiter = '&')
#     df.to_csv(filename)
#     df.to_csv(filename, sep='&', header=None, names=None)
#     df.to_csv(filename, sep='&', header=None, name=None)
    dataframe_good.to_csv(filename, sep='&', index=False)
#     dataframe_good.to_csv(filename, sep='&', header=None, index=False)
#     dataframe_bad.to_csv(filename, sep='&', header=None, index=False)
#     df = pd.DataFrame(setf5)
#     df.to_csv(filename)
    print('writing  ', filename)
#     with open(filename) as csvDataFile:
#         xxff = csv.reader(csvDataFile, delimite,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16r = '&')
#               )
#     while ip < 17:
#         row = xxxf[ip]
#   with open(filename, 'w', newline = '\') as csvfile:
#     with open(filename, 'w') as csvfile:
#             writer = csv.writer(csvfile, delimiter = '&')
#             writer.writerow(row)
#             ip = ip + 1
    print('line 810 with ip = ', ip)
    ip = ip + 1
#     csvfile.close()
    return()
def writecsvfileold(filename, xxxf, imax):
#     imax = xxxf[1][3]
    ip = 0
    with open('runfoot.rnj', 'w') as f:
      writer = csv.writer(f, delimiter = '&', header = NONE)
#       writer.writerows(setf5, deliniter = '&')
#
#
#       writer.writerows(setf5)
#     df = pd.DataFrame(setf5)
#     df.to_csv(filename)
    print('writing  ', filename)
#     with open(filename) as csvDataFile:
#         xxff = csv.reader(csvDataFile, delimiter = '&')
#               )
#     while ip < 17:
#         row = xxxf[ip]
#   with open(filename, 'w', newline = '\') as csvfile:
#     with open(filename, 'w') as csvfile:
#             writer = csv.writer(csvfile, delimiter = '&')
#             writer.writerow(row)
#             ip = ip + 1
    print('line 837 with ip = ', ip)
    ip = ip + 1
#     csvfile.close()
    return()
def readcsvfile(filename, xxxf):
#     sixteen = [0],[1],[2]
    filelines = 24
#     for iz in sixteen:
#     xxxf[0] = []
    print('845 reading  ', filename)
#     with open(filename) as csvDataFile:
#         xxff = csv.reader(csvDataFile, delimiter = '&')
#     with open(filename) as infile:
#         xxxftemp = infile.read()
#         print(xxxftemp)
#         print("line 462 ", xxxftemp[2],xxxftemp[8])
#     with open(filename):
#         xf = pd.read_csv(filename, sep = '&')

    yf = pd.read_csv(filename, sep = '&')
#         print ('read runf[3][4] as  ', xxff)
    print(yf)
#     print('642 yf.iat[2,6]  = ', yf.iat[2,6])
#     xreturn(filename, xxxf)
    imay = yf.iat[0,4]
#     print('580 imax = ', imay)
    imax = int(imay)
    print('848 imax = ', imax)
    ir5 = -1
    ic = 1
    while ir5 < imax:
        ic = 0
        ir5 = ir5+1
        while ic < 18:
#             print('829 ir5 ic are ', ir5, ic)
            xxxf[ir5][ic] = yf.iat[ir5,ic]
            ic = ic + 1
#             print('474 ir ic ', ir, ic)
#         ir = ir+1
    print('876 xxxf set with ir5 ic of ',ir5, ic)
#     print('654 xxxf[4][17] is ', xxxf[4][17], xxxf[5][17])
    print(xxxf)
    print('879 xxxf[1][3] = ', xxxf[1][3], xxxf[1][4])
    print('880 ', xxxf[1][3], xxxf[3][9])
    return(filename, xxxf)
#         iy = -1
#         val = []
#         filelines = 20
#         for row in xxxftemp:
#             iy = iy + 1
#         print(xxxftemp)
#         close()
#         return(filename, xxxf)
#             if iy > int(filelines):
#                 print('451 the number of lines read was ', filelines)
#                 return(filename, xxxf)
#             print('in readcsvfile, iy = ', iy)
#             iw = 0
#             while iw < len(row)-4:
#             while iw < 18:
#                 print('Line 464 iy and iw are ', iy, iw, row[4])
#                 print(iw)
#                 print(' row has  ', row[iw])
#                 xxxf[iy][iw] = row[iw]
#                 print('a ',iy)
#                 if iy == 1:
#                 print('line 427 with xxxf[1][3] = ', xxxf[1][3], row[3])
#                     filelines = row[4]
#                     print(filelines)
#                 val.append(row[iw])
#                 print('line 487 with ', iy,' ',iw)
#                 xxxf[iy][iw] = val[iw]
#                 val = []
#                 iw = iw + 1
#             iy = iy + 1
#           runfiw = 0
            #
#           print('line 372 with ', iy, ' ', iw)
#             print(row)
#             val.append(row[0])
#             print('value is', val)
#             row[iy]
#             iw = 0
#             for column in row:
#                 val.append[column]
#                 if iw == 16:
#                     print('xxff value is  ', column)
#                 iw = iw + 1
#                 xxxf[iy][iw] = column
#             print('value  ', val)
#             for iw in range(10):
#                 iw = iw + 1
#                 print(34)
#                 xxxf[iy].append[row[iw]]
#                 print('num',iy,"  ",iw)
#          print ('read runf[4][3] as  ', xxxf[4][3] )
#          dates.append(row[0])
#         scores.append(row[1])
#     return(filename, xxxf)
# Running starts with main()
# main() calls readfiles((currentrun, currentmenu, ir)
# which reads the correct files to start the selected quiz
# for this program these are runfoot.rnc and menufoot.mnc
# The short main program calls this big subroutine which is the
# heart of the program and is called readfiles(currentrun, currentmenu, ir)
def initialize2(xxxf):
    xxxf = [[[0],['menu'], [1500], [20], [30], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[[1],'menu'], [3000], [21], [22], [20], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[2],['menu'], [3000], [2000], [40], [20], [1], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[3],['menu'], [3000], [2000], [4], 200, 300, [11], [1.0], [1.0], 200, [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[4],['menu'], [3000], [2000], [0], [1], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[4],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[5],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[6],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[7],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[8],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[9],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[10],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[11],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[12],['menu'], [3000], [20], [15], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[13],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3],[0.1], ['men.mnc']],
           [[14],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3],[0.1], ['men.mnc']],
           [[15],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[16],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[17],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[18],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[19],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[20],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[21],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']],
           [[22],['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], ['men.mnc']]]
    print('Line 951 in initialize2() with xxxf[15][2] = ', xxxf[15][2])
    return(xxxf)
def readfiles(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk, currentrun):
#     filepath = 'C:/Users/Reed Howald/desktop/file1/'
    filename = filepath + currentrun
    print("971 READING  ", currentrun, runf)
#     runf = csv.reader(filepath + currentrun, delimiter = '&')
#     menuf = csv.reader(filepath + currentmenu, delimiter = '&')
#     runf =  [],[16]
#     if ir == -1:
#     initialize2(runf)
#     initialize2(setf5)
#     print('line 572 with runf[0][3] = ', runf[0][3], runf[1][1])
#     print('573  ', runf[0,3])
#     runf = [[['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1],
#             ['menufoot.mnc']],
#            [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#           [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']],
#             [['menu'], [3000], [2000], [0], [0], [0], [30], [1.0], [1.0], [1.0], [0.], [0.], [0.], [0.], [0.3], [0.1], [
#                 'menufoot.mnc']]]
# We need to specify the structure of runf and menuf when starting
#     menuf = [[[1],['mf'],[' screenshot (9).png'],[14],[600],[900],[550],[60],[10],[2],[0.],[0],[0.],[1.],[1.],[0.],[1.],[' Foot quiz']],
#               [[1], ['mf'], ['screenshot(9).png'],[14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.], [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.], [1.],
#               [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.] [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']],
#              [[1], ['mf'], ['screenshot(9).png'], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.],
#               [1.], [0.], [1.], ['Foot quiz']]]
    ir = ir + 1
#     ir = ira
###   [[1], [mf], [screenshot(9).png], [14], [600], [900], [550], [60], [10], [2], [0.], [0], [0.], [1.], [1.],
 ###  [0.], [1.], [Foot quiz]],
##   [0.], [1.], [Foot quiz]],
    print('1039 setf5 ', setf5[3][6])
#     print(runf[2][16])
    filename2 = filepath + currentrun
    filename3 = filepathb + str(get5f)
    print("1043 filename2 is ", filename2 , 'ir is ', ir, getf5)
    if currentrun != 'rs.rna':
        if int(setf5[3][6]) > 60:
            readcsvfile(filename2, setf5)
        print("1047 read ", filename2, ' ir is ', ir, setf5[3][11])
    print('1048 runf[2][3] = ', ir, runf[2][3], setf5[2][3] )
#     if int(runf[2][4]) == 10:
    if editrun != 'rs.rna':
        readcsvfile(filename, runf)
#         readcsvfile(filename3, setf5)
        if int(runf[4][11])  == 12:
            readcsvfile(filename3, setf5)
    print('line 1055 ir = ', ir, runf[4][11])
    print('1056 setf5[4][11] = ', setf5[4][11], runf[4][11], filename3)
#     readcsvfile(filename, getf5)
#     print(runf[3][7])
    print('1059 runf[4][11] is ', runf[4][11])
    print('1060 setf5[2][6] = ', setf5[2][6])
    print('1061 iz  ir =    ', ir)
#     open
#     filename = 'runfoot.xls'
#     writeexcel(setf5, filename, ir, f, filepath, editrun)
    print('NOW 1065 runf AND setf5 are ', runf[0][2], setf5[0][2])
#     f.close()   replaced with better code below
    with open(filepath + 'outfile.txt', 'a+')as f:
	    f.write('output for today\n')
#     f.write(filename+'\n')
    # The runfile has now been read
# Use it to set the menu file to be read
#     currentmenu = runf[ir-1][3]
#     currentmenu = str(runf[ir+1][17])
#     currentmenu = runf[ir][17]
#     currentmenu = 'menuf3.mne'
#     irc = lnt(setf5[5][9])
    irc = int(setf5[5][11])
    print('1077 ir = ', ir, irc)
#     ch = fc.write('')
#     print(str(runf.iloc[1][16]))
    if irc == -1:
        fpk = filepath
        irc = irc + 1
    if irc != 1:
        ir = 1
    currentmenu = runf[ir-1][3]
    if setf5[4][9] == 11:
        currentmenu = setf5[ir-1][3]
    print('1088 ir is ', ir, runf[ir-1][3])
    print(currentmenu, 'is the file being read for menuf at line 1089 ')
    filename = filepath + str(currentmenu)
    if currentmenu != 'ms.mna':
        print('1092  MENU  ', currentmenu)
        readcsvfile(filename, menuf)
    print('ir  = ', ir)
    print(menuf[3][5])
    print('menuf has been read from a file with  ', menuf[7][2] )
# the two files have been read with values in runf and menuf
# now it is time to start doing things
# and what to do is fixed by the value of runf[0][0]
# And the doing is done in subroutine dorunf
#     initialize2(setf5)
    fchoice = open(filepath+ 'choice.txt', 'r+')
    print("1104 ira is ", ira, irb, fpk)
    print("1115 readfiles: " + filepath + currentrun)
    dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk)
#     app = QApplication()
#     w = QuizWindow()
#     w.show()
#     app.exec_()
def switchba(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb):

    print('line 1111 in switchba() with ir = ', ir, runbi, ira, irb )
    filepathx = filepath
    filepath = filepathb
    filepathb = filepathx
    irx = ira
#     ira = irb
    irb = irx
    imax = 24
    i5 = -1
    iv = -1
    while iv < imax:
        iv = iv + 1
        while i5 < 18:
            ix = runf[iv][i5]
            runf[iv][i5] = setf5[iv][i5]
            setf5[iv][i5] = ix
            i5 = i5 + 1
# swithching is done
    print('1129 ira is now ', ira, i5, filepath)
    ir = ira
    return()
    print("1144 switchba: " + filepath + " " + filepathb)
    dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb)

def dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk):
#     irc = lnt(setf5[5][9])
    fchoice = open(filepath + 'choice.txt', 'r')
    choice = fchoice.read()
    print('1151 dorunf() with ir = ', ir, choice, runf[ir][4], ira)
    if int(ir) > 27:
        quit()
    ik = 1
    iy = 1
    print('1144 setf6[ir][1] = ' ,setf5[ir][1], ir, runf[ir][1])
    with open(filepath + 'ir.txt', 'w' )as f2:
        irb = 0
        f2.write(str(ir))
        f2.write('\n')
        f2.write(str(ik) + '\n')
        f2.write(str(ir) + '\n')
        f2.write(str(irb) + '\n')
    irc = 3
    while ik < 4:
        if runf[ir][iy]  == 'display':
#         print("display running with choice of  ", choice)
            iraa = ira + 1
            irbb = irb + 1

            print('1159 picture choices ', runf[iraa][3], setf5[iraa][3], runf[irbb][3], setf5[irbb][3])
            print('1160 runf[3][10] is ', runf[3][10], setf5[5][11])
            pic = runf[ir][3]
            pic = filepath + pic
            print('1163 controls and pic  ', setf5[5][9], setf5[5][11], pic)
            if setf5[5][9] == 9:











                print('1178 runf[3][10] is  ', runf[3][10], runf[3][11])
#             if int(setf5[3][10]) == 74:
#                 pic = setf5[ir][3]
#                 print(ir,' = ir  1164' , pic, runf[3][11], setf5[3][11])
#                 pic = filepathb+setf5[ir][3]
            prevChoice = choice
            if int(runf[3][10]) == 62:
                pic = filepath + runf[ir][3]
                print('1184 used 62 ', runf[3][10], runf[3][11])
                display(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
#                 runf[3][11] = 192
            if int(setf5[5][9]) == 2:
                pic = filepath + runf[iraa][3]
#             print('1172 runf[3][14]  ', runf[3][14], irc)
#             setf5[5][11] = int(setf5[5][11])
#             setf5[5][9] = int(setf5[5][9]) + 1
#             irc = setf5[5][9]
#             if irc > 4:
#                 pic = filepath + setf5[irbb][3]
            setf5[5][11] = int(setf5[5][11])
            if setf5[5][11] == 193:
                print('1197  ', setf5[3][11], irc)
                setf5[5][11] = setf5[5][11] + 1
                pic = setf5[irbb][3]
                pic = filepathb +pic
                print('1181 got here ', setf5[iraa][4], irc)
            else:
                setf5[5][11] = setf5[5][11] - 1
                print('1204 setf5[5][11] decreased to ', setf5[5][11], ira)
            setf5[5][11] = int(setf5[5][11])

            setf5[5][9] = int(setf5[5][9])
            setf5[5][9] = setf5[5][9] + 2
# print the results now here
            print('1210 CONTROLS are ', setf5[5][9], setf5[5][11], pic)
            if setf5[5][9]  > 7:
                if setf5[5][11] == 193:
                    pic = filepath + setf5[ir][3]
                else:
                    pic = filepathb + runf[1][3]
            print('1216 setf5[ir][3] is ', setf5[ir][3], runf[ir][3])
            print('1217 key values: ',irc, setf5[3][10], runf[5][11], setf5[5][11])
            if int(setf5[5][9]) == 2:
                pic = filepath + runf[irbb][3]
            print('1220 pic is ', pic, choice, ir, ira, irb, irc)
            print('1221 runf setf5 getf5 ', runf[0][2], setf5[0][2] )
            print('1222 runf[3][10] etc are : ', runf[3][10], setf5[3][10], runf[3][11], setf5[3][11])
            print("line 1223 display running with choice of  ", choice, ir, irc, setf5[5][11], pic)
            setf5[5][9]  = setf5[5][9] + 2
            if setf5[5][9] == 10:
                pic = filepathb + runf[1][3]
            print('1227 setf5[5][9] ie ', setf5[5][9], ir, pic)
            display(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
            printf("1241 dorunf recursion (display): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
        elif runf[ir][iy] == 'pause':
            time.sleep = runf[ir][2]
            ir = ir + 1
            printf("1246 dorunf recursion (pause): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
#             quit()
        elif runf[ir][iy] == 'menu':
            print('1234 menu line in runf ', runf[ir][3],'   ', ir)
            print('1237 runf[ir][5] is ', runf[ir][5])
            ik = ir
#             if runf[ir][5] == 9:
#                 ir = ir + 1
            print('1193 ir is ', ir, runf[ir][3])
            if ir > -1:
#                 filename = filepath + runf[ir][16]
                currentmenu = runf[ir][3]
                filename = filepath + str(currentmenu)
                print('1198 MENU  READING   ', currentmenu)
                if currentmenu != 'ms.mna':
                    readcsvfile(filename, menuf)
            print(menuf[3][5])
#             if runf[ir][5] == 9:
#                 ir = ir + 1
            print('1203 runf[ir][5] is ', runf[ir][5], ir)
            ir = ir + 1

#             ik = 3
            print('did menu with ', ik)
            printf("1271 dorunf recursion (menu): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel,filepathb, ira, irb, fpk)
#             return()
        elif runf[ir][iy] == 'quit':
#             f.write('choosing to quit with '+choice+'\n')
#             f = open('c:/Users/Reed Howald/desktop/file1/outfile.txt', 'a')
#             f = open(filepath+'outfile.txt','a+')
#             f.write('output in outfile.txt' + '\n')
#             f.close()
            with open(filepath + 'outfile.txt', 'a+')as f:
	            f.write('output in outfile.txt' + '\n')
            quit()
#             return()
#         pic = filepath + menuf[1][2]
#         print('ready for show_picture() with  ', pic)
#         choice = 'ac'
        elif runf[ir][iy] == 'transfer':
#             ir = runf[ir][1]
            currentrun = runf[ir][2]
            currentmenu = runf[ir][3]
            print('1199 transfer to ', currentrun)
            ir = runf[ir][4]
            ir = int(ir)
#            0 currentmenu = runf[ir][3]
            print(currentrun, ir, 'line 1203 ', currentmenu)
            readfiles(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk, currentrun)
#(currentrun, c         app = QApplication()  # Create an application
        elif runf[ir][iy] == 'transferb':
            print('1208 transferb current run is  ', runf[ir][2] )
            currentrun = runf[ir][2]
            switchba(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel,filepathb, ira, irb)
            ir = irb
#             currentrun = setf5[ir][2]
            currentmenu = runf[ir][3]
            print('1213 TRANSFERB runf[0][2] etc. are ', runf[0][2], setf5[0][2], currentrun, currentmenu )
            print('1214 transferb to ', currentrun)
            ir = runf[ir][4]
            ir = int(ir)
            fk = filepath
            filepath = filepathb
            filepathb = fk
            filepath = './3file/'
            print('1222 fileoath is ', filepath, currentrun)
            readfiles(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk, currentrun)
# urrentmenu, ir, f, flepath, editrun, get5f, filepathb, ira, irb)
#                 (currentrun, currentmenu, ir, f, filepath, editrun, get5f, filepathb, ira, irb)
#             switchba(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)

#             currentmenu = runf[ir][3]
            print(currentrun, ir, 'line 1385 ', currentrun)
            readfiles(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk, currentrun)
#         app = QApplication()  # Create an application
        elif runf[ir][iy] == 'count':
            print('1309 in count   prevChoice is ', fchoice , ir)
        #         show_picture(self, pic)
#         display(runf, menuf, pic, choice)
#         self.show_picture(pic)
#         app = QApplication()  # Create an application
#         quiz = QuizWindow()  # Create the quiz window
#         quiz.show_picture(pic)
#         quiz.show()  # Make the window visible
#         quiz.show_picture(pic)
#         app = QApplication()
#         w = QMainWindow()
#         w = QuizWindow()
#         show_picture(self, pic)
#         w.show()
#         app.exec_()
            ir = ir+1
            printf("1340 dorunf recursion (count): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
        elif runf[ir][iy] == 'change':
            print('1195 change with ir =', ir)
            if int(runf[ir][6]) > 11:
                change(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
            with open(filepath + "ivy.txt", 'r')as f2:
                ivy = f2.readline()
                ihx = f2.readline()
                irc = f2.readline()
                irb = f2.readline()
                ivz = f2.readline()
                setline = f2.readline()
                z = len(ivy) - 1
                ivy = ivy[:z]
                z = len(ihx) - 1
                ihx = ihx[:z]
                z = len(irc) - 1
                irc = irc[:z]
                z = len(irb) - 1
                irb = irb[:z]
                z = len(ivz) - 1
                ivz = ivz[:z]
                print('1259 ', ivy, ihx, irb, irc, ivz, runf[ir][6])
            ivy = int(ivy)
            ihx = int(ihx)
            ivz = int(ivz)
            ir = ir + 1
            irc = ir
            irb = 5
            if choice == 'ao':
                print ('1223 with ', choice, ' ', ihx)
                ivy = ivy + 1
                ihx = 1
#                 with open(filepath + 'ivy.txt', 'w' ) as f2:
#                     f2.write(str(ivy) + '\n')
#                     f2.write(str(ihx) + '\n')
#                     f2.write(str(irb) + '\n')
#                      f2.write(str(irc) + '\n')
#                 dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f)
            elif choice == 'ov':
                print('1284 with ', choice)
                ihx = ihx + 1
                if ihx > 18:
                    ihx = 1
                    ivy = ivy + 1

#                 f2.write(ihx)
#                 f2.write(irc)
            elif choice == 'iv':
                print('1240 ihx is ', ihx, ivy, ivz)
                print('1206 with ', choice, ' ', ihx, ivz)
                with open(filepath + 'ivy.txt', 'w') as f2:
                    f2.write(str(ivy) + '\n')
                    f2.write(str(ihx) + '\n')
                    f2.write(str(irb) + '\n')
                    f2.write(str(irc) + '\n')
                    f2.write(str(ivz) + '\n')
                    f2.write(str(setline) + '\n')
#                 f2.write(irb)
                setg6 = pd.read_excel(filepath + 'runcommands.xls')
                # setg6
                print('1249 setg6.iloc[2,5] = ', setg6.iloc[2,5])
                print('at line 1299 with ', choice)
# I need to find the current value for setf5[ivy][ihx] in setg6
                valc = setf5[ivy][ihx]
                izz = 0
                while izz < 18:
                    value = setg6.iloc[izz, ihx + 4]
                    if value == valc:
                        ihz = izz
                        print("1258 ihz = ", ihz, izz, valc)
#                       izz = 22
                        setf5[ivy][ihx] = setg6.iloc[izz + 1, ihx + 4]
                        print('1266 with a new value of ', setf5[ivy][ihx], ivy, ihx)
                        ihx = ihx + 1
                        izz = 23
                    izz = izz+ 1



#             value = setg6.iloc[ihx][ivy + 1]
#             value = setg6.iloc[ivz +1, ihx + 4]
#             print('1043 value is ', value, ivy, ihx, ivz)
#             setf5[ivy][ihx] = value
            printf("1425 dorunf recursion (change): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)

        elif runf[ir][iy] == 'edit':
            print('1331 edit is called with ir = ', ir)
            if runf[1][11] == 7:
                editg(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)
#        call the subrouting editf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5)#        editf()
            editf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)
            iq = ir
            print('at line 1327 in dorunf, not editf')
            ir = ir + 1
            d = timedelta()
            (d.days, d.seconds)
            dseconds = d.seconds
            daykeep = d.days
            print('1343 the value of daykeep is ', daykeep, dseconds)
            currentedit = 'runfoot.rnj'
#             setf5=runf
            filename = filepath + currentedit
#             filename = filepath + currentmenu
            print('1341 EDIT  READING   ', currentedit, iq, runf[iq][4])
#             readcsvfile(filename, setf5)
            print('setf5[2][4] is  ', setf5[2][4])
            filename = filepath + 'runfoot.rnj'
            print('line 1352 runf[ik][4] with iq = ', iq, runf[iq][4])
            filename = filepath + 'runfoottodaylast.rne'
            filename = filepath + filename
            setf5 = pd.read_excel(filepath + ctexcel)
            write('1356 reading ', ctexcel )
            writecsvfile(filename, setf5, imax)
#                 filename = filepath + 'runfoottodaylast.rne'
#                 writecsvfile(filename, setf5, imax)
        elif runf[ir][iy] == 'switch':
            print('line 1392 in dorunf with ', runf[ir][iy],'  ', ir)
            switchba(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)
            #           dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)      filename = filepath + 'runfoot.rne'
#                 writecsvfile(filename, setf5)
#             quit()
#              setf5 =
#             value = setf5[]
        elif runf[ir][iy] == 'skip':
            print('1451 using skip command')
            ir = ir+1
            printf("1469 dorunf recursion (skip): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb,fpk )
            return()

        elif runf[ir][iy] == 'writetosetf5':
            irc = 0
            irb = 1
            ivz = 2
            with open(filepath + "ivy.txt", 'r')as f2:
                ivy = f2.readline()
                ihx = f2.readline()
                irc = f2.readline()
                irb = f2.readline()
                ivz = f2.readline()
                setline = f2.readline()
            setline = int(setline)
            ihx = int(ihx)
            irb = int(irb)
            irc = int(irc)
            ivz = int(ivz)
            print('1472 writing to setf5 ', setline, ir, iy, ivy, ihx)
            ir = ir + 1
            ivz = 2
            ijx = 0
            ivy = int(ivy)
            ivz = int(runf[3][4])
            ivz = int(ivz)
            print('1479 ivz = ', ivz, setline)
            while ijx < 17:
                setf5[setline - 1][ijx] = getf5[ivz][ijx]
                ijx = ijx + 1
            print("1483 ", setf5[setline - 1][3])
            setline = setline + 1
            filename = filepath + 'newrun.rng'
            imax = 8
            if setline > 8:
                imax = setline
            ihx = int(ihx)
            irb = int(irb)
            irc = int(irc)
            ivz = int(ivz)
            print('1493 ',filename, ' ', imax)
            writecsvfile(filename, setf5, imax)
            with open(filepath + 'ivy.txt', 'w') as f2:
                f2.write(str(ivy) + '\n')
                f2.write(str(ihx) + '\n')
                f2.write(str(irb) + '\n')
                f2.write(str(irc) + '\n')
                f2.write(str(ivz) + '\n')
                f2.write(str(setline) + '\n')
            print('1502 finish writetosetf5() setline is ', setline, ivz)
            printf("1520 dorunf recursion (writetosetf5): " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)
            return ()
#         elif runf[ir][iy] == 'change':
#             print('1226 subroutine change ', ir)
#             dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)
#             return ()
        print ('Something is wrong with a run file ')
        print('1510 choice = ', choice)
        print(runf[ir][0], ' is not found')
        print(runf[ir][1], runf[ir][2])
        ir = ir + 1
#         quit()
#         return()
        printf("1534 dorunf recursion (fall through?) " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
#     elif runf[ir][0] == 'quit':
#         quit()
    return()
#         choice = gettwokeystrokes(choice)
#         checkchoice(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f)
#         )
#
def editf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel):
    print('line 1525 in editf with ir = ', ir, choice)
    iq = ir
    ir = ir + 1
    d = timedelta()
#     d = datetime()
    (d.days, d.seconds)
    dseconds = d.seconds
    daykeep = d.days
    print('1390 the value of daykeep is ', daykeep, dseconds)
    currentedit = 'runfoot.rnk'
#     setf5=runf
#     initialize2(setf5)
#     runbi = 'runTOxlsx.xlsx'
    filename = filepath + runbi
    print('1506 EDIT  WRITING   ', runbi, iq, runf[iq][4])
#     readcsvfile(filename, setf5)
#     print('setf5[2][4] is  ', setf5[2][4])
#     filename = filepath + 'runfoot.rne'
#     print('line 875 setf5[ik][4] with iq = ', iq, setf5[iq][4])
#     print('line 796 values '. setf5[1][3], setf5[1][4], setf5[1][5]. setf5[1][6], setf5[1][7], setf5[1][8]
#           . setf5[1][10], setf5[1][11], setf5[1][12])
#     if int(str(setf5[iq][4])) == 11:
#         filename = filepath + 'runfoottodaylast.rne'
#         writecsvfile(filename, setf5)
    print('1516 in edit with filename = ', filename, ctexcel)
#     imax = setf5[1][3]
    imax = 20
    print('line 1470 with imax = ', imax)
    setf5 = pd.read_excel(filepath + ctexcel)
    print('line 1494 setf5 = ', setf5)
    writecsvfile(filename, setf5, imax)
#     if int(runf[ir][1])  > 1:
    filename = filepath + runbi
#         imax = setf5[1][3]
#         print('line 832 with imax = ', imax)
    writecsvfile(filename, setf5, imax)
#     filename = filepath + 'runfoot.rne'
#     writecsvfile(filename, setf5)
#     cvswriter.writerows(setf5)
#     with open('runfoot.rne', 'w') as f:
#       writer = csv.writer(f)
#       writer.writerows(setf5)
    printf("1586 editf: " + filepath + " " + filepathb)
    dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)
def display(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk):
# Subroutine to display a picture on the screen
    print('1568 displaying ir = ', ir, ' and ', choice, pic , '  ', filepathb)
# pic = 'C:/Users/Reed Howald/desktop/file1/footmenu1.png'
#     app = QA
#     pplication()
    w = QuizWindow()
    # w.content.setScaledContents(True)
    w.show_picture(pic)
    w.show()
    # FORCE resizing picture?
    w.update_scaled_picture()
    print('after show ... width: ' + str(w.content.width()) + ' height: ' + str(w.content.height()))
    app.exec() # soon to be replaced with exec() without the underscore
    fchoice = open(filepath+ 'choice.txt', 'r')
    choice = fchoice.read()
    z = len(choice) - 1
    if z > 1:
        choice = choice[:z]
    print("1581 returned with ", choice, ir, z)
    print('in display() line 1582'
          ' with ', choice)
    fchoice.close()
#     close(app)
    checkchoice(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk)
    return (choice)
def checkchoice(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, detf5, ctexcel, filepathb, ira, irb, fpk):
    print('checkchoice line 1590 with ', choice, ir )
    ccount(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, detf5, ctexcel, filepathb, ira, irb, fpk)
#     f = open('c:/Users/Reed Howald/desktop/file1/outfile.txt','a+')
    f = open(filepath+'outfile.txt','a+')
    f.write(str(choice)+'\n')
    f.close()
    if choice == '4':
        ir = ir + 1
        printf("1623 checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk)
    elif choice == '1':
        ir = ir + 1
        printf("1627 checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk)
# This is a shortcut for anyone who finds nx too cumbersome to type
    elif choice == '2':
        ir = ir + 2
        printf("1632 (skip ahead) checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
    elif choice == '8':
        ir = ir - 1
        printf("1636 (-1) checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
    elif choice == '7':
        ir = ir - 2
        printf("1640 (-2) checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
    elif choice == '3':
        print('1612 choice of ', choice, ira, irb,ir)
#         switchba(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)
        iraa =ira + 1
        irbb = irb+1

        print('1617 picture choices ', runf[iraa][3], setf5[iraa][3], runf[irbb][3], setf5[irbb][3] )
        iq = int(runf[4][8])
        if iq == 2:
            fic = 'rchcd.rng'
            filename = filepathb + fic
            mic = 'mcc.mnb'
            readcsvfile(filename, setf5)
            filename = filepathb + mic

            readcsvfile(filename, menuf)
            runf[4][8] = int(runf[4][8]) +1
        print('1628 iq is ', iq, runf[4][8], pic)
        ir = ir - 1
        pic = runf[irbb][3]
        fp = filepath
        filepath = filepathb
        filepathb = fp
#         pic = runf[1][3]
        pic = filepath + pic
        print('1636 pic is ', pic, ir , choice)
        printf("1668 checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
    elif choice == '9':
        ir = 0
        printf("1672 checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
    elif choice == '0':
        print('closing the python program')
        quit()
    elif choice == '5':
        begin = 9
        ir = 0
        currentrun = 'live.rne'
        rbrestart(currentrun, currentmenu, filepath, ir, begin)
    elif choice == '6':
        ir = ir + 1
        printf("1684 checkchoice " + choice + ": " + filepath + " " + filepathb)
        dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
    iv = 1
    print(menuf[1][4],' Line 1653 ', menuf[1][5])
    ir = ir + 1
    iw = 0
#     while iv < int(str(menuf[1][4])):
    print('1657 menuf[5][2] = ', menuf[5][2])
#     choice = str(choice)
    while iv < int(str(menuf[1][4])) + 1:
#         print('1663 choice=',choice)
#         print('1664 size choice=', len(choice))
#         print('1663 mi=', str(menuf[iv][2]))
#         print('1664 size mi=', len(str(menuf[iv][2])))
#         print('964 menuf[1][4] is ', menuf[1][4])
#         print('965 menuf[iv][2] = ', menuf[iv+1][2], iv)
#         print('967 menuf[4][2] = ', menuf[4][3])
#         print('967 menuf[4][2] = ', menuf[4][2])
        if choice == str(menuf[iv][2]):

            print('1670 menuf[iv][2] = ', menuf[iv][2])
#             currentrun = menuf[iv][16]
            iz = int(menuf[iv][6])
            iz = iz +1
            iz = iz + 1
            value = menuf[iv][4]
            fvalue = 115
            if iz < 9:
#                 setf5[0][iz] = value
                runf[2][11]  = value
                print('1680 the value is ', value, choice, iz, ir, iv)
            if iz > 8:
                iw = int(menuf[iv][5])
                iz = iz - 1
                print('1684 the value is ', value, choice, iz, ir, iv, iw)
#                 fvalue = 1.0/float(menuf[iv][iz])
       #          print('990 the value is ', fvalue, choice, iz, ir, iv, iw)
                if choice != 'er':
                    setf5[0][iz] = fvalue
                    runf[ir][iz] = fvalue
   #              print('987 the value is ', fvalue, choice, iz, ir, iv, iw)
#             iz = int(menuf[iv][5])
#             setf5[1][iz] = menuf[iv][4]
#             print('li3ne 910 ', setf5[1][iz])
#             print('line 917 ', setf5[1][3])
            print('1695 iz  = ', iz, ir, iv, iw, value)
            runf[2][11] = value
            if iz == 6:
                change(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
#             setf5[1][iz] = value
#             runf[1][int(iz)] = setf5[1][iz]
            if iz < 8:
                print('1702 ', str(value), iz, runf[0][6])
#             runf[0][iz] = value
            elif iz > 7:
                runf[0][iz] = fvalue
            print('1706 New value at ', runf[0][iz], iz, ir, iv, iw, value, ira)
#             ir = ir+ 1
#             print('line 1009 selecting new ', currentrun)qt
#             ir = 0
            print("1710 iz = ", iz, ir, iv, iw, value)
#             switch = int(menuf[iw][6])

            switch = int(menuf[iv][6])
            print("1709 switch is ", switch, ira)
            fchoice = open(filepath + 'choice.txt', 'r')
            choice = fchoice.read()

            print('in checkchoice 1713 with:  ', choice, switch)
            if switch < 16:
                currentrun = menuf[iv][3]
                print('1686 new currentrun is ', currentrun)
                ir = 0
                ia = ir
                ib = 0
                if currentrun != 'rs.rna':
                    readfiles(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk, currentrun)
#                         (currentrun, currentmenu, ir, f, filepath, 'editany.rne', get5f, filepathb, ia, ib)
#             ir =00 ir + 1
#             ir = 5
            print('1730 ir = ', ir, iz, iv, ira)
#             pic = runf[ir][17]
            print(pic)
            printf("1767 checkchoice " + choice + ": " + filepath + " " + filepathb)
            dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
            iv = 197
        print(iv)
#         dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f)
#         print(setf5[1][iz])
        iv = iv +1
#         iv = 120
#         dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f)
    print('1736 You typed ', choice, 'Please try again with a correct two letter combination')
#     f = open('c:/Users/Reed Howald/desktop/file1/outfile.txt','a+')
#     f.write('BAD '+ str(choice)+' not recognized here\n')
#     f.close()       replaced with better code
    with open(filepath + 'outfile.txt', 'a+')as f:
        f.write('BAD ' + str(choice) + ' not recognized here\n')
    ir = ir - 2
    print('1743 a bad choice has been made typing ', choice)
    pic = 'abc.png'
    pic = filepath + pic
    display(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
#     print('In checkchoice with an invalid choice of  ', choice)
#     return()
    printf("1789 checkchoice " + choice + ": " + filepath + " " + filepathb)
    dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)

def writeexcel(setf5, filename, ir, f, filepath, editrun):
        print('1751 write excel file of setf5  ', filename )
        writer = ExcelWriter(filepath + 'runfoot.xlsx')
        df = pd.DataFrame({'a': [1, 3, 5, 7, 4, 5, 6, 4, 7, 8, 9],
                           'b': [3, 5, 6, 2, 4, 6, 7, 8, 7, 8, 9]})
#         df.to_excel("C:/Users/Reed Howald/Desktop/7file/avid.xlsx")
        df = pd.DataFrame(setf5)
        print('1728 df is  ', df)
        df.to_excel(filepath + ctexcel)
#         df.to_excel(writer,'Sheet1', index = False)

def change(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk):
    print('!!  1768 1768  in subroutine change() ', ir, ira, irb)
    print('1769 filepaths are ', fpk, filepath, filepathb, ira)
#     if ira == -1:
#         irq = 0#       ira = ira + 4
#         fpq = filepath
#     irq = irq +1


    fcolor = open(fpk + "colori.txt", 'r')
    colori = fcolor.read()
    print('1778 fcolor is ', fcolor, ' filepathb, fpk,')

    print('1780 colori = ', colori, filepath, filepathb)
    colori = int(colori)
    print('1782 colori = ', colori, ira, irb)
#     if colori == 1:
#         fpk = filepath
    imax = 11
    iskip = 1
    if colori > 3:
        colori = 0
#         with open(fpk + 'colori.txt', 'w')as f:
#             f.write(str(colori))
        print('1791 colori is ', colori, iskip, fpk)
        #         imax = setf5[1][3]
        #         print('line 832 with imax = ', imax)
        filename = filepath + runf[0][2]
        writecsvfile(filename, runf, imax)
        print('1796 NOW PRINTING ',filename, colori, ir)
        iskip = 2
    print('1798 filepaths are ', filepath, filepathb, fpk)
    #     fcolor = open(filepath + "colori.txt", 'w')
#     with open(filepathb + 'colori.txt', 'w')as f:
#         f.write(str(colori))
#     with open(filepath + 'colori.txt', 'w')as f:
#         f.write(str(colori))
#     close(f)
    value = runf[2][11]
    iv = 3
    ih = int(runf[iv+1][10])
    ivhp = int(runf[iv][9])
    ih = ih - 2
    ih = ih+colori
    iv2 = int(runf[iv - 1][9])
    print('1812 iv2 is  ', iv2, ih, iv, iskip, ivhp, value)
    if iskip == 1:
        runf[iv2][ih] = value
        setf5[iv2][ih] = value
        ihx3 = ih
        fihx3 = open(filepath + 'ihx3.txt', 'w')
        fihx3.write(str(ihx3))
        print('1819 here with ', ih, iv, runf[iv2][ih])
    print("1820 runf[0][9] is now ", runf[iv2][ih], iv2, ih)
    print('1821 ', runf[iv2][ih] , iv2, ih, value)
    print('1822 colori is ', colori, iv2, ih, ira)
    colori = colori + 1
    iskip = 1
    with open(fpk + 'colori.txt', 'w')as f:
        f.write(str(colori))
#     w = QuizWindow()
#     w.content.setPixmap(QPixmap(pic))
#     w.show()


#     quit()
    #     colori = int(colori)

#     self.input.setFocus()
#     w = QuizWindow()11111111
#     w.content.setPixmap(QPixmap(pic))
#     w.show()
#     app.exec_()

#     colori = colori + 1
    if colori > 3:
        colori = 0
#         fcolor = open(fpk + "colori.txt", 'w')
#         fcolor.write(str(colori))
        #         imax = setf5[1][3]
        print("1847 fpk is ", fpk, filepathb, colori)
        #         print('line 832 with imax = ', imax)
        filename = filepathb + runf[0][2]
        writecsvfile(filename, runf, imax)
        print('1851 NOW PRINTING ', filename, colori, ir)
        iskip = 2

    #     fcolor = open(filepath + "colori.txt", 'w')
    #     fcolor.write(str(colori))

    #     with open(filepath + 'colori.txt', 'w')as f:
    #         f.write(str(colori))
    #
#     switchba(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)
    print("1861 ira is ", ira, irb, choice)
    printf("1898 change " + choice + ": " + filepath + " " + filepathb)
    dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb, fpk)
#     quit()
#     dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel)
#     print('1434 in subroutine change() ', ir)



def rbrestart(currentrun, currentmenu, filepath, ir, begin):
    print('1870 in sbrestart with begin = ', begin)
#     fkeep = open(filepath + 'keepfile.txt', 'r+')
#     if begin == 0:
#         print('if statment activated')
#         fkeep = open(filepath + 'keepfile.txt','r+')nnb
#         fkeep.write(currentrun)
#         fkeep.write("\n")
#         fkeep.write(currentmenu)
#         keeprun = currentrun
#         keepmenu = currentmenu
#         begin = 9qt
    keeprun = 'live.rne'
    keepmenu = 'menuf3.mne'
#     return()
    currentrun = keeprun
    currentmenu = keepmenu
    ir = 0
    readfiles(currentrun, currentmenu, ir, f, filepath, editrun, get5f)
    return()
def editg(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel):
    print('1674 in subroutine editg with ir = ', ir)
#  This subroute is designed to convert a run file to an xlsx file
    filename = filepath + ctexcel
    writeexcel(getf5, filename, ir, f, filepath, editrun)


    ir = ir + 1
    printf("1934 editg " + choice + ": " + filepath + " " + filepathb)
    dorunf(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, runbi, ctexcel, filepathb, ira, irb)

def ccount(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, detf5, ctexcel, filepathb, ira, irb, fpk):
    print('1901 !!IN ccount WITH choice = ', choice)
    ccx = runf[5][8]
    print('1903 ccx  IS ', ccx, choice)
    if ccx != 12:
        return()
    fr = open(filepath +'ccount.txt', 'r')
    cho = fr.readline()
    ccc = fr.readline()
    ccn = fr.readline()
    ccm = fr.readline()
    ccw = fr.readline()
    ccy = fr.readline()
    czz = fr.readline()
    czy = fr.readline()
    fr.close()

    print('1916 ccn is ', ccn, ccm, choice)
    print('1917 ccw is  ', ccw, ccy)
#     choice = string(choice)
    fchoice = open(filepath+ 'choice.txt', 'r')
    choice = fchoice.read()
    z = len(choice) - 1
    if z > 1:
        choice = choice[:z]

    fc = open(filepath + 'chold.txt', "r")
    chold = fc.read()
    fd = open(filepath + 'chold2.txt', "r")
    chold2 = fd.read()
    if runf[5][9] != 15:
        ccn = int(ccn) + 1
        ccm = ccm[0:-1]
        ccm = ccm + ' ' + str(choice)
        print('1933 ccn is now ', ccn , ccm)
        print('1934 cchold is ', chold, choice, ccy)
        if czy == 2:
            return()
#         f2.write(str(ccw) + '\n')
        print('WRONG choice is ', choice, ccc, ccn)
#     fc = open(filepath + 'chold.txt', r)
        with open(filepath + 'ccount.txt', 'w') as f2:
            f2.write(str(cho) + '')
            f2.write(str(ccc) + '')
            f2.write(str(ccn) + '\n' )
            f2.write(str(ccm) + '\n')

            f2.write(str(ccw))
            f2.write(str(ccy))
            f2.write(str(czz) )
            f2.write(str(czy) )
            f2.close()

            ccn = int(ccn) + 1
            ccm = ccm[0:-1]
            ccm = ccm + ' ' + chold
            print('1955 ccy is now ', ccy, czz)

        return()
  # main()
# PROGRAM F0000OR CORRECT CHOICES
    print('1960 right choice is ', choice, ccx, cho )
    print('RIGHT CHOICE WITH ', choice, ccc, runf[5][9])
# check for a duplicate cnoice
    ii = 0
    print('1964 ccw is ',ccw,' this ', ccn, ccm, ccw, ccy  )
#     test = czz[ii]
    z = len(ccy) - 1
    ccy = ccy[:z]
    ccw = ccw[0:-1]
    ccw = int(ccw) + 1
#     ccy = ccy[0:-1]
    ccy = ccy + ' ' + str(choice)
    print('1972 ccw is now ', ccw, ccy)

#     ccn = int(ccn) + 1
#     ccy = ccy[0:-1]
#     ccy = ccy + ' ' + chold2
    prlint('1977 ccn is now ', ccn, ccm)
    print('1978 cchold is ', chold, choice, ccy)
    if czy == 2:
        return ()
    #         f2.write(str(ccw) + '\n')
    print('RIGHT is ', choice, czz, czy)
    #
    with open(filepath + 'ccount.txt','w') as f2:
        f2.write(str(cho) + '')
        f2.write(str(ccc) + '')
        f2.write(str(ccn) + '')
        f2.write(str(ccm) + '')
        f2.write(str(ccw) + '\n')
        f2.write(str(ccy) + '\n')
        f2.write(str(czz) + ' ')
        f2.write(str(czy) + '\n')
        f2.close()
#     return()
    wa = 'wrong   ' + ccn + '  ' + ccm
    wb = 'correct ' + str(ccw) + '  ' + ccy
    with open(filepath + 'tmc.txt', 'w') as f2:
        f2.write(wa)
        f2.write(wb)
        f2.close()



    print('1996 cho ccc are ', cho, ccc)
    print('1997 ccn ccm are ', ccn, ccm)
    print('1998 ccw ccy are ', ccw, ccy)
    print('1999 czz czy are ', czz, czy)
#     s5 = fr.readline()
    return()
#     s7 = fr.readline()
#     s8 = fr.readline()
#     fr.close()
    print('2005 ccount.txt has been written with czz = ', czz)





    return()

# Here is the starting place for poly7.py!!!!
# the following print statement will fe the first thing this python program does
print('2015 starting the program polyr8.py')
print('2016 his is a polynomial quiz ')
# currentrun = 'runfoot.rne'
# currentmenu = 'menuf3.mne'
# f = open('c:/Users/Reed Howald/desktop/file1/outfile.txt', 'a')
# filepathi = 'C:/Users/Reed Howald/Desktop/8poly/'
filepathi = './'
f = open(filepathi+'controlstart.txt', 'r')
filepath=f.readline()
currentrun=f.readline()
print('2024 filepath is ', filepath + currentrun)
print('2025 currentrun is ', currentrun)
ir = 0
currentmenu=f.readline()
filepathb=f.readline()
runbi=f.readline()
ctexcel=f.readline()
# ira = f.readline()
# irb = f.readline()
print('2036 runbi is ', runbi)
get5f=f.readline()
fpk = f.readline()
ira = f.readline()
irb = f.readline()
f.close()
ira = int(ira)
irb =  int(irb)
# ctexcel = ctexcel[0:-1]
print(filepath)
string=filepath
filepath=string[0:-2]+'/'
string=filepathb
filepathb=string[0:-2]+'/'
print('2047 filepathb is ', filepathb, irb)
print('2058 starting with ', currentrun, get5f)
print(currentmenu)
currentrun=currentrun[0:-1]
# currentrun=currentrun+'/'
currentmenu=currentmenu[0:-1]
runbi = runbi[0:-1]
editrun = runbi
get5f = get5f[0:-1]
# print('1349 getf5 is '. getf5)
colori = 1
with open(filepath + 'colori.txt', 'w')as f:
    f.write(str(colori))
# f = open(filepath+'outfile.txt','a')
# f.write('output in outfile.txt'+'\n')
# f.close()
with open(filepath + 'outfile.txt', 'a+')as f:
	f.write('output in outfile.txt=' + '\n')
with open(filepath + 'ivy.txt', 'w') as f2:
    f2.write('0\n')
    f2.write('1\n')
    f2.write( '0\n')
    f2.write('0\n')
    f2.write('0\n')
    f2.write('0\n')
    f2.write('1\n')
app = QApplication()
ir = 0
ira = -1
begin = 2
with open(filepath + 'ty1.txt', 'w')as f4:
    f4.write('The file to be written is  ' + ctexcel + '  ')
with open(filepath + 'tdone.txt' , 'w')as f4:
    f4.write('  CONGRATULATIONS  ' + ctexcel + '  ')
print(currentrun)

print(currentmenu)
ctexcel = ctexcel[0:-1]
fr = open(filepath + 'ccountbegin.txt', 'r')
cho = fr.readline()
ccc = fr.readline()
ccn = fr.readline()
ccm = fr.readline()
ccw = fr.readline()
ccy = fr.readline()
czz = fr.readline()
czy = fr.readline()
fr.close()

with open(filepath + 'ccount.txt', 'w') as f2:
    f2.write(str(cho) + '')
    f2.write(str(ccc) + '')
    f2.write(str(ccn))
    f2.write(str(ccm) + '')
    f2.write(str(ccw) + '')
    f2.write(str(ccy) + '')
    f2.write(str(czz) + '')
    f2.write(str(czy) + '')
    f2.close()

wa = 'wrong   ' + ccn + '  ' + ccm
wb = 'correct ' + ccw + '  ' + ccy
with open(filepath + 'tmc.txt', 'w' ) as f2:
    f2.write(wa)
    f2.write(wb)
    f2.close()
# print('1694, editrun)
# filepath =,  'C:/Users/Reed Howald/desktop/file1/'
fchoice = filepath
fpk = filepath
readfiles(runf, menuf, ir, pic, choice, fchoice, filepath, setf5, f, getf5, ctexcel, filepathb, ira, irb, fpk, currentrun)
#     (currentrun, currentmenu, ir, f, filepath, editrun, get5f, filepathb, ira, irb)
# This is the end of polyr8.py


