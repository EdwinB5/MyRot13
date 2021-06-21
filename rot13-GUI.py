from tkinter import *
from random import randrange
from rot13 import *
from tkinter import ttk
from tkinter import messagebox

class AppRot13:

	def __init__(self, root):
		root.title('Rot13: ' + str(myTitle(randrange(5))) + ' | @EdwinB5' )
		root.resizable(False,False)
		root.iconbitmap('icon.ico')
		root.config(bg='white')
		window_width, window_height = 650,430
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()

		position_top = int(screen_height/2 - window_height/2)
		position_right = int(screen_width/2 - window_width/2)

		root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

		myFrame = Frame(root)
		myFrame.config(bg='white')
		myFrame.pack()

		rotNumber = 13

		self.textLabel = Label(myFrame, text='Rot' + str(rotNumber))
		self.textLabel.config(font=("Courier", 30), bg='white', pady=20)
		self.textLabel.grid(row=0, column=1, columnspan=5)

		self.textToEncrypt = Text(myFrame, width="27", height="15")
		self.textToEncrypt.grid(row=2, column=1)

		self.scrollVert=Scrollbar(myFrame, command=self.textToEncrypt.yview)
		self.scrollVert.grid(row=2, column=2, sticky="nswe")

		self.textToEncrypt.config(yscrollcommand=self.scrollVert.set)

		self.textEncrypted = Text(myFrame, width="27", height="15")
		self.textEncrypted.grid(row=2, column=4)

		self.scrollVert=Scrollbar(myFrame, command=self.textEncrypted.yview)
		self.scrollVert.grid(row=2, column=5, sticky="nswe")

		self.textEncrypted.config(yscrollcommand=self.scrollVert.set)

		self.rotationList = ttk.Combobox(myFrame, state='readonly', width=8, height=2, justify='center')
		self.rotationList.grid(row=2, column=3)

		self.rotationList['values'] = ['ROT1','ROT2','ROT3','ROT4','ROT5',
							'ROT6','ROT7','ROT8','ROT9','ROT10',
							'ROT11','ROT12','ROT13','ROT14','ROT15',
							'ROT16','ROT17','ROT18','ROT19','ROT20','ROT21',
							'ROT22','ROT23','ROT24','ROT25']

		encryptLabel = Label(myFrame, text="Text to be encrypted: ")
		encryptLabel.config(bg='white', font=("Courier", 13))
		encryptLabel.grid(row=1, column=1, columnspan=2, sticky='nswe', pady=10)

		encryptedLabel = Label(myFrame, text="Text encrypted: ")
		encryptedLabel.config(bg='white', font=("Courier", 13))
		encryptedLabel.grid(row=1, column=4, columnspan=2, sticky='nswe', pady=10)

		sendButton = Button(myFrame, text="Send", command=self.encryptText)
		sendButton.config(bg="white", font=("Courier", 13))
		sendButton.grid(row=3, column=3, padx=25)

	def encryptText(self):
			valRot = self.rotationList.get()
			rotationNumber = 0
			self.textEncrypted.delete('1.0', END)
			textRot = self.textToEncrypt.get('1.0', END)

			if valRot == '':
				messagebox.showinfo("Information", "Please select an option for encrypt")
			elif valRot == 'ROT1':
				rotationNumber = 1
			elif valRot == 'ROT2':
				rotationNumber = 2
			elif valRot == 'ROT3':
				rotationNumber = 3
			elif valRot == 'ROT4':
				rotationNumber = 4
			elif valRot == 'ROT5':
				rotationNumber = 5
			elif valRot == 'ROT6':
				rotationNumber = 6
			elif valRot == 'ROT7':
				rotationNumber = 7
			elif valRot == 'ROT8':
				rotationNumber = 8
			elif valRot == 'ROT9':
				rotationNumber = 9
			elif valRot == 'ROT10':
				rotationNumber = 10
			elif valRot == 'ROT11':
				rotationNumber = 11
			elif valRot == 'ROT12':
				rotationNumber = 12
			elif valRot == 'ROT13':
				rotationNumber = 13
			elif valRot == 'ROT14':
				rotationNumber = 14
			elif valRot == 'ROT15':
				rotationNumber = 15
			elif valRot == 'ROT16':
				rotationNumber = 16
			elif valRot == 'ROT17':
				rotationNumber = 17
			elif valRot == 'ROT18':
				rotationNumber = 18
			elif valRot == 'ROT19':
				rotationNumber = 19
			elif valRot == 'ROT20':
				rotationNumber = 20
			elif valRot == 'ROT21':
				rotationNumber = 21
			elif valRot == 'ROT22':
				rotationNumber = 22
			elif valRot == 'ROT23':
				rotationNumber = 23
			elif valRot == 'ROT24':
				rotationNumber = 24
			elif valRot == 'ROT25':
				rotationNumber = 25

			if valRot != "" and len(textRot) < 1000:
				self.textLabel.config(text='Rot' + str(rotationNumber))
				encryptedText = myRot(textRot, rotationNumber)
				self.textEncrypted.insert('1.0', encryptedText)
				
			elif len(textRot) >= 1000:
				messagebox.showinfo("Information", "Please enter an amount less than 1000 characters")


if __name__ == '__main__':
	root = Tk()
	AppRot13(root)
	root.mainloop()
