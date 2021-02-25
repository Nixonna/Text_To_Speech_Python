import PySimpleGUI as sg
import ConvertFile
import ConvertText
import sys
class welcome:
    def __init__(self):

        #Tooltip text
        self.__tooltip_text1="Type the text in the space provided \n and convert them to speech."
        self.__tooltip_text2="Upload a text file and convert them \n to speech."


        #window layout
        self.__layout=[
            [sg.Button("Convert Text",size=(10,1),pad=((0,0),(150,20)),tooltip=self.__tooltip_text1)],
            [sg.Button("Convert Files",size=(10,1),pad=((0,0),(0,20)),tooltip=self.__tooltip_text2)],
            [sg.Button("Exit",size=(10,1))]
        ]


        #window initials
        self.__window=sg.Window("TEXT TO SPEECH CONVERTOR",self.__layout,size=(500,500),element_justification="c")

        #Main Loop
        while True:

            #Events and values of window widgets
            self.__event,_=self.__window.read()

            #Opens convert text window
            if self.__event=="Convert Text":
                self.__window.hide()
                ConvertText.windowOne()

            #opens convert files window
            if self.__event=="Convert Files":
                self.__window.hide()
                ConvertFile.windowTwo()
            
            #window close and exit
            if self.__event in (None,"Exit",sg.WIN_CLOSED):
                sys.exit()


#Main driver code
if __name__=="__main__":
    welcome()