class game:
    def __init__(self):
        print ('welcom in our game')
        print('''
            press The game number:
               1:Mutipication table
               2:Remove Dublicated chars
            ''')
        user_choice=int(input('Enter Your choice Number :'))
        if user_choice == 1:
            self.Mutipication_table()
        elif user_choice == 2:
            self.remove_duplicates()
        else:
            print('please Enter A valiad Choice')

    def Mutipication_table(self):
        start=int(input('Enter start :'))
        end=int(input('enter end :'))

        for x in range (start,end+1):
           for y in range(1,13):
               z=x*y
               print(f'{x}x{y}={z}')
           print('--------------')

    def remove_duplicates(self):
        
        word=input('Enter aword :')
        letters=[]
        for letter in word:
            if letter in letters:
               continue
            else:
                letters.append(letter)
        print(letters)

g = game()



