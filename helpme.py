from colorama import Fore, Back, Style



class Colour_text_print:
    def Red_Colour_text_print(self, text):
        print(Fore.RED + text)
    def Green_Colour_text_print(self, text):
        print(Fore.GREEN + text)



class Word_Practices(Colour_text_print):
    """This class define for Word Practices purpose."""
    
    def __init__(self):
        self.Right_count = 0
        self.Wrong_Count = 0
        
       
    def UserInput(self, Word):
        """This class define for taking the input from the user."""
        
        print()
        print()
        
        print("                     Word: ",Word)
        var = input("Please! Re-type this word:  ").lower()
        if var == 'exit' or var =='e':
            print()
            self.Green_Colour_text_print("Thank you for using Word Practices Game.")
            print()
            return 0
        else:
            if var != Word.lower():
                self.Green_Colour_text_print("              Your Answer:  ✖")
                self.Wrong_Count -= 1
            else:
                self.Green_Colour_text_print("              Your Answer:  ✔")
                self.Right_count += 1






            
            
            
            
            
