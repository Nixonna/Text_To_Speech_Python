import PySimpleGUI as sg
import pyttsx3
import sys,os
import webbrowser
import Welcome
import google_trans_new as gt

if __name__!="__main__":
    class windowOne:
        def __init__(self):

            #Text to Speech initials
            self.__engine=pyttsx3.init()
            self.__voices=self.__engine.getProperty("voices")

            #Google translator initials
            self.__translator=gt.google_translator()

             
            #Window layout
            self.__layout=[
                    [sg.Text("Gender:"),sg.Combo(["Male","Female"],size=(10,1),readonly=True,key="voice",default_value="Male"),
                    sg.Text("Speech rate:"),sg.Slider((0,140),default_value=65,orientation='horizontal',key="rateS",pad=((0,0),(0,20)))],
                    [sg.Text("Language:"),sg.Combo(["English","Hindi"],size=(10,1),readonly=True,key="lang",default_value="English")],

                    [sg.Multiline(size=(60,10),key='textbox')],
                    [sg.Button("SAY",size=(10,1),pad=((10,10),(20,0))),sg.Button("Save to File",size=(10,1),pad=((10,10),(20,0)))],
                    [sg.Button("Back",size=(10,1),pad=((10,10),(20,0))),sg.Button("Exit",size=(10,1),pad=((10,10),(20,0)))]
                    ]   

            #Window initials
            self.__window=sg.Window("TEXT CONVERSION",self.__layout,size=(500,500),element_justification="c")


            #Main loop
            while True:

                #Events and values of window widgets
                self.__event,self.__values=self.__window.read()

                #Gender and Language selection
                try:
                    if self.__values["lang"]=="English":
                        self.__langCode="en"
                        if self.__values["voice"]=="Male":
                            self.__engine.setProperty("voice",self.__voices[0].id)
                        if self.__values["voice"]=="Female":
                            self.__engine.setProperty("voice",self.__voices[3].id)
                    
                    if self.__values["lang"]=="Hindi":
                        self.__langCode="hi"
                        if self.__values["voice"]=="Male":
                            self.__engine.setProperty("voice",self.__voices[2].id)
                        if self.__values["voice"]=="Female":
                            self.__engine.setProperty("voice",self.__voices[1].id) 
                except:
                    pass
                
                #Exit and close window
                if self.__event in (None,"Exit",sg.WIN_CLOSED):
                    sys.exit()

                #Say button working
                if self.__event == "SAY":
                    if self.__values["textbox"]!="\n":
                        if self.__translator.detect(self.__values["textbox"])[0]==self.__langCode:
                            self.__engine.setProperty("rate",int(60+self.__values["rateS"]))
                            self.__engine.say(self.__values["textbox"])
                            self.__engine.runAndWait()
                        else:
                            self.__translated=self.__translator.translate(self.__values["textbox"],lang_tgt=self.__langCode)
                            self.__engine.setProperty("rate",int(60+self.__values["rateS"]))
                            self.__engine.say(self.__translated)
                            self.__engine.runAndWait()
                    else:
                        sg.PopupQuickMessage("Text space is empty",auto_close_duration=3)


                #Saving audio file in mp3 format
                if self.__event=="Save to File":
                    if self.__values["textbox"]!="\n":
                        while True:
                            self.__Foname=sg.popup_get_folder("Choose the folder to save the file")
                            if self.__Foname==None:
                                break  

                            if not os.path.isdir(self.__Foname):
                                sg.popup("Invalid Folder")
  
                            else:
                                self.__Fname=sg.popup_get_text("Enter file name")
                                if self.__Fname!=None:
                                    if self.__translator.detect(self.__values["textbox"])[0]==self.__langCode:
                                        self.__engine.setProperty("rate",int(60+self.__values["rateS"]))
                                        self.__engine.save_to_file(self.__values["textbox"],self.__Foname+"\\"+self.__Fname+".mp3")
                                        self.__engine.runAndWait()
                                        webbrowser.open_new(self.__Foname)
                                    
                                    else:
                                        self.__translated=self.__translator.translate(self.__values["textbox"],lang_tgt=self.__langCode)
                                        self.__engine.setProperty("rate",int(60+self.__values["rateS"]))
                                        self.__engine.save_to_file(self.__values["textbox"],self.__Foname+"\\"+self.__Fname+".mp3")
                                        self.__engine.runAndWait()
                                        webbrowser.open_new(self.__Foname)
                                break
                    else:
                        sg.PopupQuickMessage("Text space is empty",auto_close_duration=3)

                #Window navigation
                if self.__event=="Back":
                    self.__window.hide()
                    Welcome.welcome()