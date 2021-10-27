# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.


import turtle, random, time, math

start = time.time()
score = 5

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50, init_dist=400):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()
        self.runner.setx(-init_dist / 2)

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()
        self.chaser.setx(0)
        self.chaser.setheading(180)

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()
        self.drawer.sety(200)

    def is_catch(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, ai_timer_msec=1000):
        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser)
        self.chaser.run_ai(self.runner)
        ai_timer_msec=500

        # TODO: You can do something here.
        is_catched = self.is_catch()
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setposition(-75,100)
        
        elapse = time.time()
        global score
        if is_catched == True:
            score -= ai_timer_msec/200
        else :
            score +=0.3
        if score < 0 :
            canvas.bye()
        self.drawer.write(f'Is catched? {is_catched}/ Elapse:{elapse-start:.0f}/ Score :{score:.2f}')

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move = 5, step_turn=15):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers

        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        pass


class LessRandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=25, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        
    def run_ai(self,oppoenent): 
        opp_pos = oppoenent

        mode1 = random.random()*2-1
        mode2 = random.random()*2-1
        pos = (mode1*100,mode2*100)

        opp_h = self.towards(opp_pos)
       
        self.seth(opp_h)
    
        self.setposition(pos)
    

if __name__ == '__main__':
    canvas = turtle.Screen()
    runner = LessRandomMover(canvas)
    chaser = ManualMover(canvas)
    canvas.title("Turtle Chaser")
    canvas.setup(width=250,height=250)

    game = RunawayGame(canvas, runner, chaser)
    game.start()
    canvas.mainloop()