from helpme import Word_Practices, Colour_text_print


l = ["Apple", "mango", "yes", "Problem", "Red", "Yellow", 'Question', 'Game', 'Book', 'Pen', 'Mouse']

if __name__=="__main__":
    obj = Word_Practices()
    print("""Please! Enter [Y] for Continue 
          and [E] for Exit.         
    """)
    inp = input("                         :  ").lower()
    print()

    if inp == "" or inp =='yes' or inp == "y":
        obj.Green_Colour_text_print("Welcome to Word Practices Game.")
        for i in l:
            var = obj.UserInput(i)
            if var == 0:
                break
        else:
            print()
            print("              Total Word: ", len(l))
            print("       Total Right Score: ", obj.Right_count)
            print("       Total Wrong Score: ", obj.Wrong_Count)
            print()
            obj.Green_Colour_text_print("Thank you for using Word Practices Game.")
            print()
    else:
        Word_Practices().Right_count
        obj.Red_Colour_text_print("Thank you!")
            
