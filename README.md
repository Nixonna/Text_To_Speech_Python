# Text_To_Speech_Python
Text to Speech GUI using various libraries of Python 3.0 <br>
Please read this carefully before you proceed. Once you satisfy all the prerequisites, then run the **Welcome.py** file.


# Prerequisites:

1.	**PySimpleGUI module** (using pip install)

    This module will be used to design the GUI of the application.
    
    The PySimpleGUI cookbook:
    
    https://pysimplegui.readthedocs.io/en/latest/
    
2.	**Pyttsx3 module** (using pip install)

    This module is used for Text-To-Speech (TTS) conversion. This is an offline convertor module that uses three TTS engines:
    
    •	Sapi5 -SAPI5 on windows
    
    •	nsss – NSSpeechSynthesizer on Mac OS X
    
    •	espeak – eSpeak on every other platform
    
    Reference to working of the module:
    
    https://pypi.org/project/pyttsx3/
    
3.	**Google_trans_new module** (using pip install)
    
    The command to install this module:
        
    **pip install google_trans_new**
    
    This is a python API for google translator, since this application gives you an option to translate a text in one language to speech in another language, we use this API for     this purpose.
    
    Reference to working of this module:
    
    https://pypi.org/project/google-trans-new/
    
    This application can convert an English text to English speech and Hindi speech. You can select the languages before you begin the conversion.
    
    To use the Hindi TTS, you will have to install the Microsoft TTS for the Hindi language. Without this the application will throw an error. I will further add an option to       convert only to English if Hindi is not installed.
    
    Once the Hindi TTS is installed, there has to be few changes made in the registry to make the pttsx3 module to identify those languages. The following steps will show you       how to do it:
    
    1.	Open the registry of your system.
    
    2.	Navigate to this directory: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens
    
    3.	If you have installed the Hindi TTS then you will see two following sub directories:
        
        **MSTTS_V110_hiIN_HemantM (Male voice)**
        
       **MSTTS_V110_hiIN_KalpanaM (Female voice)**
    
    4.	Export these two directories by right-clicking and then select export.
    
    5.	Once exported, Open the .reg file using a text-editor application.
    
    6.	Replace all “Speech_OneCore” to “Speech”. (Be careful with the spelling or else it will cause errors).
    
    7.	Save the file and close it.
    
    8.	Run these two .reg files using windows registry editor and click ok to make changes.
    
    9.	Now you are ready to go with the Hindi TTS.
    
I am working on getting the prerequisites to install on their own if they are not installed in the system already so that you will not have to worry about getting the settings right.
