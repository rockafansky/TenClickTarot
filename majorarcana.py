import sys
import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Major Arcana"

directions = [True, False]
CARDLIST = [
['The World', 'Fulfillment, Harmony, Completion.', 'Incompletion, Lack of Closure.', 'theworld.png'],
['Judgment', 'Reflection, Reckoning, Awakening.', 'Lack of Self Awareness, Doubt, Self-Loathing.', 'judgment.png'],
['The Sun', 'Joy, Success, Celebration, Positivity.', 'Negativity, Depression, Sadness.', 'thesun.png'],
['The Moon', 'Unconscious, Illusions, Intuition.', 'Confusion, Fear, Misinterpretation.', 'themoon.png'],
['The Star', 'Hope, Faith, Rejuvenation.', 'Faithlessness, Discouragement, Insecurity.', 'thestar.png'],
['The Tower', 'Sudden Upheaval, Broken Pride, Disaster', 'Disaster Avoidance or Delay, Fear of Suffering.', 'thetower.png'],
['The Devil', 'Addiction, Materialism, Playfulness.', 'Freedom, Release, Restoring Control.', 'thedevil.png'],
['Temperance', 'Compromise, Patience, Finding Meaning.', 'Extremes, Excess, Lack of Balance.', 'temperance.png'],
['Death', 'Endings, Beginnings, Change.', 'Fear of Change, Holding on, Stagnation, Decay.', 'death.png'],
['The Hanged Man', 'Sacrifice, Release, Martyrdom.', 'Stalling, Needless Sacrifice, Fear of Sacrifice.', 'thehangedman.png'],
['Justice', 'Cause and Effect, Clarity, Truth.', 'Dishonesty, Blame, Unfairness.', 'justice.png'],
['The Wheel of Fortune', 'Change, Cycles, Destiny.', 'Lack of and Desire for Control, Bad Luck.', 'thewheeloffortune.png'],
['The Hermit', 'Contemplation, Search for Truth, Inner Guidance.', 'Loneliness, Isolation, Losing Your Way.', 'thehermit.png'],
['Strength', 'Inner Strength, Bravery, Compassion, Focus.', 'Self Doubt, Weakness, Insecurity.', 'strength.png'],
['The Chariot', 'Direction, Control, Willpower.', 'Lack of Control, Lack of Direction, Aggression.', 'thechariot.png'],
['The Lovers', 'Partnership, Duality, Union.', 'Loss of Balance, One-Sidedness, Lack of Harmony.', 'thelovers.png'],
['The Hierophant', 'Tradition, Conformity, Morality, Ethics.', 'Rebellion, Subversiveness, New Approaches.', 'thehierophant.png'],
['The Emperor', 'Authority, Structure, Control, Fatherhood.', 'Tyranny, Rigidity, Coldness.', 'theemperor.png'],
['The Empress', 'Motherhood, Fertility, Nature.', 'Dependence, Smothering, Emptiness.', 'theempress.png'],
['The High Priestess', 'Intuitive, Unconscious, Inner Voice.', 'Lack of Center, Lost Inner Voice, Repression.', 'thehighpriestess.png'],
['The Magician', 'Willpower, Desire, Creation, Manifestation.', 'Trickery, Illusions, Out of Touch.', 'themagician.png'],
['The Fool', 'Innocence, New Beginnings, Freedom of Spirit.', 'Recklessness, Naiveté, Inconsideration.', 'thefool.png']
]
random.shuffle(CARDLIST)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.clicked = 0
        self.current_state = 0
        self.Upright = False
        self.direc = 0
        self.direc2 = 0
        self.direc3 = 0

    def setup(self):
        self.clicked = 0
        arcade.start_render()

    def update(self, delta_time):
        self.text_angle += 1
        self.time_elapsed += delta_time

    def on_draw(self):
        arcade.start_render()
        width = 200
        height = 50
        if self.current_state == 0: #title screen
            width = 600
            height = 100
            arcade.draw_text("Ten Click Tarot.", 10, 400, arcade.color.WHITE, 60, font_name = 'CAP', width=800, align="center", anchor_y = 'bottom')
            width = 200
            height = 50
            arcade.draw_text("Click anywhere to begin.", 10, 350, arcade.color.WHITE, 20, font_name = 'CAP', width=800, align="center")
        elif self.current_state == 1: #introduction
            arcade.draw_text("You will pick three cards, ", -100, 250, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            arcade.draw_text("representing the Past, Present, and Future.", -100, 200, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture("cardbacksingle.png")
            arcade.draw_texture_rectangle(400, 500, 300, 400, texture, 0)
        elif self.current_state == 2: #first selection
            arcade.draw_text("Pick your first card.", -100, 50, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture("cardbackpage.png")
            scale = .6
            arcade.draw_texture_rectangle(400, 420, scale * texture.width, scale * texture.height, texture, 0)
        elif self.current_state == 3: #past card
            if self.Upright == True:
                self.direc = "Upright"
                info = CARDLIST[0][1]
            else:
                self.direc = "Reversed"
                info = CARDLIST[0][2]
            card = CARDLIST[0][0]
            arcade.draw_text("Past - " + str(card) + " - " + str(self.direc), -100, 250, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            arcade.draw_text(str(info), -100, 200, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture(CARDLIST[0][3])
            if self.direc == "Reversed":
                arcade.draw_texture_rectangle(380, 520, 300, 400, texture, 180)
            else:
                arcade.draw_texture_rectangle(380, 520, 300, 400, texture, 0)
        elif self.current_state == 4: #second selection
            arcade.draw_text("Pick your second card.", -100, 50, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture("cardbackpage.png")
            scale = .6
            arcade.draw_texture_rectangle(400, 420, scale * texture.width, scale * texture.height, texture, 0)
        elif self.current_state == 5: #present card
            if self.Upright == True:
                self.direc2 = "Upright"
                info = CARDLIST[1][1]
            else:
                self.direc2 = "Reversed"
                info = CARDLIST[1][2]
            card = CARDLIST[1][0]
            arcade.draw_text("Present - " + str(card) + " - " + str(self.direc2), -100, 250, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            arcade.draw_text(str(info), -100, 200, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture(CARDLIST[1][3])
            if self.direc2 == "Reversed":
                arcade.draw_texture_rectangle(380, 520, 300, 400, texture, 180)
            else:
                arcade.draw_texture_rectangle(380, 520, 300, 400, texture, 0)
        elif self.current_state == 6: #third selection
            arcade.draw_text("Pick your third card.", -100, 50, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture("cardbackpage.png")
            scale = .6
            arcade.draw_texture_rectangle(400, 420, scale * texture.width, scale * texture.height, texture, 0)
        elif self.current_state == 7: #future card
            if self.Upright == True:
                self.direc3 = "Upright"
                info = CARDLIST[2][1]
            else:
                self.direc3 = "Reversed"
                info = CARDLIST[2][2]
            card = CARDLIST[2][0]
            arcade.draw_text("Future - " + str(card) + " - " + str(self.direc3), -100, 250, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            arcade.draw_text(str(info), -100, 200, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture(CARDLIST[2][3])
            if self.direc3 == "Reversed":
                arcade.draw_texture_rectangle(380, 520, 300, 400, texture, 180)
            else:
                arcade.draw_texture_rectangle(380, 520, 300, 400, texture, 0)
        elif self.current_state == 8: #all cards
            texture = arcade.load_texture(CARDLIST[0][3])
            if self.direc == "Reversed":
                arcade.draw_texture_rectangle(180, 520, 200, 300, texture, 180)
            else:
                arcade.draw_texture_rectangle(180, 520, 200, 300, texture, 0)
            texture = arcade.load_texture(CARDLIST[1][3])
            if self.direc2 == "Reversed":
                arcade.draw_texture_rectangle(380, 520, 200, 300, texture, 180)
            else:
                arcade.draw_texture_rectangle(380, 520, 200, 300, texture, 0)
            texture = arcade.load_texture(CARDLIST[2][3])
            if self.direc3 == "Reversed":
                arcade.draw_texture_rectangle(580, 520, 200, 300, texture, 180)
            else:
                arcade.draw_texture_rectangle(580, 520, 200, 300, texture, 0)
            arcade.draw_text("The cards have spoken!", -100, 300, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
        elif self.current_state == 9: #credits
            arcade.draw_text("Credits", -100, 750, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            arcade.draw_text("Colorized by PaintsChainer.", -100, 250, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            arcade.draw_text("Tarot Interpretations by Labyrinthos.", -100, 175, arcade.color.WHITE, 20, font_name = 'CAP', width = 1000, align="center")
            texture = arcade.load_texture("katelucas.png")
            scale = .6
            arcade.draw_texture_rectangle(400, 520, scale * texture.width,scale * texture.height, texture, 0)
        else:
            sys.exit()

    def on_mouse_press(self, x, y, button, modifiers):
        self.current_state += 1
        self.Upright = random.choice(directions)
        self.on_draw()

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
