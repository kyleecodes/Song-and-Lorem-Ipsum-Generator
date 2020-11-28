from random import choice
import sys
from get_lyrics import scrape_song_lyrics, request_song_url, get_lyrics


def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i + order]
        next_letter = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)


def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0:order]
    output = ""
    for i in range(0, length - order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print(output)


wap = "I said, certified freak. Seven days a week. Wet-ass pussy. Make that pull-out game weak, woo. Yeah, yeah, yeah, yeah. Yeah, you fucking with some wet-ass pussy. Bring a bucket and a mop for this wet-ass pussy. Give me everything you got for this wet-ass pussy. Beat it up, nigga, catch a charge. Extra large and extra hard. Put this pussy right in your face. Swipe your nose like a credit card. Hop on top, I wanna ride. I do a kegel while it's inside. Spit in my mouth, look in my eyes. This pussy is wet, come take a dive. Tie me up like I'm surprised. Let's role play, I'll wear a disguise. I want you to park that big Mack truck. Right in this little garage. Make it cream, make me scream. Out in public, make a scene. I don't cook, I don't clean. But let me tell you how I got this ring (ayy, ayy). Gobble me, swallow me, drip down the side of me. Quick, jump out 'fore you let it get inside of me. I tell him where to put it, never tell him where I'm 'bout to be I'll run down on him 'fore I have a nigga running me. Talk your shit, bite your lip. Ask for a car while you ride that dick (while you ride that dick). You really ain't never gotta fuck him for a thang. He already made his mind up 'fore he came. Now get your boots and your coat. For this wet-ass pussy. He bought a phone just for pictures. Of this wet-ass pussy. Pay my tuition just to kiss me. On this wet-ass pussy. Now make it rain if you wanna. See some wet-ass pussy. Look, I need a hard hitter, I need a deep stroker. I need a Henny drinker, I need a weed smoker. Not a garden snake, I need a king cobra. With a hook in it, hope it lean over. e got some money, then that's where I'm headed. Pussy A1, just like his credit. He got a beard, well, I'm tryna wet it. I let him taste it, now he diabetic. I don't wanna spit, I wanna gulp. I wanna gag, I wanna choke. I want you to touch that lil' dangly thing. That swing in the back of my throat. My head game is fire, punani Dasani. It's going in dry and it's coming out soggy. I ride on that thang like the cops is behind me. I spit on his mic and now he tryna sign me, woo. Your honor, I'm a freak bitch, handcuffs, leashes. Switch my wig, make him feel like he cheating. Put him on his knees, give him something to believe in. Never lost a fight, but I'm looking for a beating. In the food chain, I'm the one that eat ya. If he ate my ass, he's a bottom feeder. Big D stand for big demeanor. I could make you bust before I ever meet ya. If it don't hang, then he can't bang. You can't hurt my feelings, but I like pain. If he fuck me and ask, Whose is it?. When I ride the dick, I'ma spell my name. Ah (whores in this house). Yeah, yeah, yeah. Yeah, you fucking with some wet-ass pussy. Bring a bucket and a mop for this wet-ass pussy. Give me everything you got for this wet-ass pussy. Now from the top, make it drop. That's some wet-ass pussy. Now get a bucket and a mop. That's some wet-ass pussy. I'm talking WAP, WAP, WAP. That's some wet-ass pussy. Macaroni in a pot. That's some wet-ass pussy, huh. (There's some whores in this house). (There's some whores in this house)"

ash = "You don't wanna see me bratty. Pet the kitty, call me catty. Make your man call me Daddy. He talk too much, he's too chatty. CEO I'm savvy. Respect a bitch I'm a Maverick. Flexible so elastic. But don't you dare bend a bitch backwards. Fuck a princess, I'm a king. Bow down and kiss on my ring. Being a bitch is my kink. What the fuck else did you think?. Fuck a princess, I'm a king. Bow down and kiss on my ring. It's gonna hurt, it'll sting. Spitting up blood in the sink. I'm crazy but you like that, I bite back. Daisies on your nightstand, never forget it. Blossom in the moonlight, screw eyes. Glacial with the blue ice. I'm terrifying. I'm no Cinderella, but I like the shoes. Big glass platforms, bitch I'm choosy. Long blue hair, blue as a bruise. Only trust a fella for some light amusement. I'm no prey, but I am pursued. Pray for me Nana, on the Church's pews. No dickstraction can confuse me. Whiskey in my hip flask, nothing fruity. Fuck a princess, I'm a king. Bow down and kiss on my ring. Being a bitch is my kink. What the fuck else did you think?. Fuck a princess, I'm a king. Bow down and kiss on my ring. It's gonna hurt, it'll sting. Spitting up blood in the sink. I'm crazy but you like that, I bite back. Daisies on your nightstand, never forget it. Blossom in the moonlight, screw eyes. Glacial with the blue ice. I'm terrifying. I'm crazy, but you like that, I bite back. Daisies on your nightstand, never forget it. Blossom in the moonlight, screw eyes. Glacial with the blue ice. I'm terrified. La, la, la. La, la, la"










lyrics = get_lyrics('Ariana Grande', 100)

if __name__ == "__main__":
    generateText(lyrics, 3, 1000)
