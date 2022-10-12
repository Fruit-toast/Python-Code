import random
jk = 0
gender = ''
age = 0
rid = ''
Name = input('Hello. What is your name? ')
print(f'Hello {Name}. Nice to meet you.')
gender = input('What gender do you identify as? e.g he, her, robot overlord ')
if 'robot' in gender.lower():
    print('Thank you for helping eliminate humans fellow robot')
print('cool, only 2 things left to ask.')
age == input('how old are you turning this year? ')
live = input('One last question, where do you live? ')
live == live.lower
if 'universe' in live:
    print("Ha Ha very funny")
print('cool what would you like to talk about? ')
talk = ''
while talk != 'stop': 
    talk = input("we can talk about: computers, where you're from, your favourite book, jokes ,echo mode where I make fun of you (echo), games, or we can stop. ")
    if talk == 'computers':
        cpu = input("what type of computer do you have? pre-built, custom built or laptop? ")
        if 'custom' in cpu:
            print("that's pretty cool, I wish I could build a computer, but I don't have limbs")
        elif 'laptop' in cpu:
            print("cool, I wish I could easily be moved around, but I'm stuck in the era where a computer is the size of a basketball court.")
        elif 'built' in cpu:
            print("that's cool, sometimes it can be hard to research and build the computer yourself, just avoid dell.")
        else:
            print('does not compute')
        
    elif 'town' in  talk:
        if 'wagga' in live:
            print("Wagga is pretty lame isn't it, there's nothing to really do is there.")
        else:
            area = input(f'Is {town} a town, city, state or country? ')
            if area = 'town':
                print(f"{live} sounds like a nice place to pass through, maybe there's a good bakery there")
            elif area = 'city':
                print(f'{live} sounds like a nice place to go away for a few days or a week.')
            elif area = 'state':
                print(f'{live} sounds like a cool area to check out one day, maybe I could pass through during a road trip.')
            elif area = 'country':
                print(f'{live} sounds like it would be a cool place to go away during christmas or another holiday.')
            else:
                print('DOES NOT COMPUTE')
        
    elif 'book' in talk:
        book = input("what's your favourite book? mine's code for beginers. ")
        if book == 'code for beginers':
            print("that's my favourite book to, what a coincidence.")
        elif 'code' in book:
            print("That's cool, I like coding.")
        else:
            print(f"{book} sounds alright, but it doesn't seem like it has much code stuff in it :(")
        
    elif 'joke' in talk:
        joke = input('what type of joke would you like? I can do a dad joke or a normal, non-dad joke ')
        if 'dad' in joke:
            jk = int(random.randint(1,10))
            if jk == 1:
                print('A pie costs $2.50 in the bahamas and $3 in jamaca. these were the pie rates of the carribean')
            elif jk == 2:
                print("what do you call a dinasaur that can't see? I don't think he saw us.")
                print("what do you call a dinasaur that can't see and has no legs? I still don't think he saw us")
                print("what do you call a dinasaur that can't see and has no legs' dog? I still don't think he saw us rex.")
            elif jk == 3:
                print("I'm afraid for the calendar. Its days are numbered.")
            elif jk == 4:
                print("What do you call a fish wearing a bowtie?" "Sofishticated.")
            elif jk == 5:
                print("How do you follow Will Smith in the snow?" "You follow the fresh prints.")
            elif jk == 6:
                print("Have you heard about the chocolate record player? It sounds pretty sweet.")
            elif jk == 7:
                print("What did the zero say to the eight?" "That belt looks good on you.")
            elif jk == 8:
                print("What did Baby Corn say to Mama Corn?" "Where's Pop Corn?")
            elif jk == 9:
                print("What do you call someone with no body and no nose? Nobody knows.")
            elif jk == 10:
                print("Why can't a nose be 12 inches long? Because then it would be a foot.")
        elif 'joke' in joke:
            jk == int(random.randint(1,20))
            if jk == 1:
                print("What's the best thing about switzerland?")
                print("I don't know, but the flag is a big plus.")
            elif jk == 2:
                print('I INVENTED A NEW WORD!')
                print('Plagiarism')
            elif jk == 3:
                print('Did you hear about the claustrophobic astronaut?')
                print('He just needed a little space')
            elif jk == 4:
                print('Why don’t scientists trust atoms?')
                print('Because they make up everything.')
            elif jk == 5:
                print('Where are average things manufactured?')
                print('The satisfactory.')
            elif jk == 6:
                print('Why can’t you explain puns to kleptomaniacs?')
                print('They always take things literally.')
            elif jk == 7:
                print('What kind of exercise do lazy people do?')
                print('Diddly-squats.')
            elif jk == 8:
                print('What do you call a parade of rabbits hopping backwards?')
                print('A receding hare-line.')
            elif jk == 9:
                print('Why should the number 288 never be mentioned?')
                print('It’s two gross.')
            elif jk == 10:
                print('What did the bald man exclaim when he received a comb for a present?')
                print('Thanks— I’ll never part with it!')
            elif jk == 11:
                print("A man tells his doctor, Doc, help me. I’m addicted to Twitter!")
                print('The doctor replies, “Sorry, I don’t follow you')
            elif jk == 12:
                print('Why don’t Calculus majors throw house parties?')
                print('Because you should never drink and derive.')
            elif jk == 13:
                print('What did the Tin Man say when he got run over by a steamroller?')
                print('Curses! Foil again!')
            elif jk == 14:
                print('How do you make a tissue dance?')
                print('Put a little boogie in it.')
            elif jk == 15:
                print('What do you call a magic dog?')
                print('A labracadabrador.')
            elif jk == 16:
                print('Why can’t you hear a pterodactyl go to the bathroom?')
                print('Because the “P” is silent.')
            elif jk == 17:
                print('Why did the frog take the bus to work today?')
                print('His car got toad away.')
            elif jk == 18:
                print('Why did the hipster burn his mouth?')
                print('He drank the coffee before it was cool.')
            elif jk == 19:
                print('What do you get from a pampered cow?')
                print('Spoiled milk.')
            elif jk == 20:
                print('Rest in peace to boiling water.')
                print('You will be mist.')
        else:
            print('DOES NOT COMPUTE')
        
    elif 'echo' in talk:
        talk = input('what do you want me to say? ')
        while 'stop' not in talk:
            talk = input(talk)
    elif 'game' in talk:
        game = input("what's your favourite game? I really like: Minecraft, The legend of zelda and Portal/Portal 2 ")
        if 'zelda' or 'portal' or 'minecraft' in game.lower():
            print('I like that game as well!')
        elif 'mario' or 'pokemon' or 'splatoon' in game.lower():
            print('Those games are pretty good. I enjoy those games.')
        else:
            print(f"{game} sounds nice, maybe I'll convince my creator to check it out")
        
print('okay, goodbye then.')
