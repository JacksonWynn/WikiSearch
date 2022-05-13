from tkinter import *
from bs4 import BeautifulSoup
import requests

class GUI:
    
    def __init__(self, window) -> None:
        '''
        Initializer method creates the elements of the GUI window.
        '''
        self.window = window
        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text='Enter a query and I\'ll show you any\nWikipedia articles or article sections\nit relates to.')
        self.label_message.pack(padx=5, side='left')
        self.frame_message.pack(pady=10)
        self.frame_query = Frame(self.window)
        self.entry_query = Entry(self.frame_query)
        self.entry_query.pack(padx=5)
        self.frame_query.pack(pady=10)
        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='Submit', command=self.Clicked)
        self.button_submit.pack()
        self.frame_submit.pack(pady=10)
        
    def Clicked(self) -> None:
        '''
        Submit button click method scrapes Wikipedia article search for query, converts all results to string links,
        then writes each link containing the full original query to files.txt.
        '''
        url: str = "https://en.wikipedia.org/wiki/Special:AllPages/" + self.entry_query.get().replace(" ", "_")
        linksWritten: int = 0
        page: str = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('li', class_="allpagesredirect")
        links: str = []
        for i in lists:
            linkElement = str(i)
            links.append("https://en.wikipedia.org/" + linkElement[59:((linkElement.find("title=")) - 2)])
        outputFile = open("links.txt", "w")
        for i in links:
            if not(i.find(self.entry_query.get().replace(" ", "_")) == -1):
                outputFile.write(i + "\n\n")
                linksWritten += 1
        outputFile.close()
        if linksWritten == 0:
            self.label_message.config(text="Oops! Your query had no results.")
        else:
            self.label_message.config(text="Done!\nCheck links.txt on your computer.")