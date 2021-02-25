import PySimpleGUI as sg
import sys,os,webbrowser
import Welcome
import pyttsx3
import google_trans_new as gt

if __name__ !="__main__":
    class windowTwo:
        def __init__(self):

            #Text to Speech initials
            self.__engine=pyttsx3.init()
            self.__voices=self.__engine.getProperty("voices")

            #Google translator initials
            self.__translator=gt.google_translator()

            #Window layout
            self.__layout2=[
                        [sg.Text("Gender:"),sg.Combo(["Male","Female"],size=(10,1),readonly=True,key="voice",default_value="Male"),
                        sg.Text("Speech rate:"),sg.Slider((0,140),default_value=65,orientation='horizontal',key="rateS",pad=((0,0),(0,20)))],
                        [sg.Text("Language:",pad=((0,0),(0,20))),sg.Combo(["English","Hindi"],size=(10,1),readonly=True,key="lang",default_value="English",pad=((0,0),(0,20)))],

                        [sg.Text("File",pad=((0,0),(50,50))),sg.InputText(readonly=True,key="text",pad=((0,0),(50,50))),
                        sg.FileBrowse("Browse File",file_types=(("Text Files","*.txt"),),key="input",enable_events=True,pad=((0,0),(50,50)))],

                        [sg.Button("convert",size=(10,1),pad=((10,10),(20,0))),sg.Button("Save to File",size=(10,1),pad=((10,10),(20,0)))],
                        [sg.Button("Back",size=(10,1),pad=((10,10),(20,0))),sg.Button("Exit",size=(10,1),pad=((10,10),(20,0)))]
                    ]

            #Window initials
            self.__window2=sg.Window("FILE CONVERSION",self.__layout2,size=(500,500),element_justification="c")

            #Main Loop
            while True:

                #Events and values of window widgets
                self.__event2,self.__values2=self.__window2.read()

                #Gender and Language selection
                try:
                    if self.__values2["lang"]=="English":
                        self.__langCode="en"
                        if self.__values2["voice"]=="Male":
                            self.__engine.setProperty("voice",self.__voices[0].id)
                        if self.__values2["voice"]=="Female":
                            self.__engine.setProperty("voice",self.__voices[3].id)
                    
                    if self.__values2["lang"]=="Hindi":
                        self.__langCode="hi"
                        if self.__values2["voice"]=="Male":
                            self.__engine.setProperty("voice",self.__voices[2].id)
                        if self.__values2["voice"]=="Female":
                            self.__engine.setProperty("voice",self.__voices[1].id) 
                except:
                    pass
                

                #Exit and close window
                if self.__event2 in (None,sg.WIN_CLOSED,"Exit"):
                    sys.exit()

                #Browse file to convert
                if self.__event2=="input":
                    self.__values2["text"]=r"{}".format(self.__values2["input"])

                #Convert button working
                if self.__event2=="convert":
                    with open(self.__values2["text"]) as f:
                        self.__s=f.read()
                        if self.__s !="":
                            if self.__translator.detect(self.__s)[0]==self.__langCode:
                                self.__engine.setProperty("rate",int(60+self.__values2["rateS"]))
                                self.__engine.say(self.__s)
                                self.__engine.runAndWait()
                            else:
                                self.__translated=self.__translator.translate(self.__s,lang_tgt=self.__langCode)
                                self.__engine.setProperty("rate",int(60+self.__values2["rateS"]))
                                self.__engine.say(self.__translated)
                                self.__engine.runAndWait()
                        else:
                            sg.PopupQuickMessage("The file choosen is empty",auto_close_duration=3)

                
                #Saving audio file in mp3 format
                if self.__event2=="Save to File":
                    with open(self.__values2["text"]) as f:
                        self.__s=f.read()
                        if self.__s !="":
                            while True:
                                self.__Foname=sg.popup_get_folder("Choose the folder to save the file")
                                if self.__Foname==None:
                                    break  

                                if not os.path.isdir(self.__Foname):
                                    sg.popup("Invalid Folder")
    
                                else:
                                    self.__Fname=sg.popup_get_text("Enter file name")
                                    if self.__Fname!=None:
                                        if self.__translator.detect(self.__s)[0]==self.__langCode:
                                            self.__engine.setProperty("rate",int(60+self.__values2["rateS"]))
                                            self.__engine.save_to_file(self.__s,self.__Foname+"\\"+self.__Fname+".mp3")
                                            self.__engine.runAndWait()
                                            webbrowser.open_new(self.__Foname)
                                        
                                        else:
                                            self.__translated=self.__translator.translate(self.__s,lang_tgt=self.__langCode)
                                            self.__engine.setProperty("rate",int(60+self.__values2["rateS"]))
                                            self.__engine.save_to_file(self.__translated,self.__Foname+"\\"+self.__Fname+".mp3")
                                            self.__engine.runAndWait()
                                            webbrowser.open_new(self.__Foname)
                                    break
                        else:
                            sg.PopupQuickMessage("The file choosen is empty",auto_close_duration=3)

                #Window navigation
                if self.__event2=="Back":
                    self.__window2.hide()
                    Welcome.welcome()
