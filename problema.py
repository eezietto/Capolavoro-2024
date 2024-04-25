from manim import *

class ProblemIllustration(Scene):
    def construct(self):
        
        # Set the color of the background
        self.camera.background_color = LOGO_WHITE
        
        
        # Plane      
        plane = NumberPlane(
            x_range = (-1, 13, 1),
            y_range = (-2, 7, 1),
            color = LOGO_BLACK,
            
            background_line_style = {
                "stroke_color": GREY,
                "stroke_opacity": 0.25
            }
        )
        plane.axes.set_color(LOGO_BLACK)
        
        
        # Wheel Group
        r = 1
        ex_wheel = Circle(r, color = "#553311", 
                          fill_color = "#553311", fill_opacity = 0.5)
        in_wheel = Circle(r * 0.8, color = "#553311", 
                          fill_color = "#553311", fill_opacity = 0.5 )
        wheel = VGroup(ex_wheel, in_wheel)
        
        
        # Ball
        ball = Circle(r * 0.1, color = "#332211",
                      fill_color = "#332211", fill_opacity = 0.85)
                
        
        # Trajectory
        trace = TracedPath(ball.get_center, stroke_color = LOGO_BLACK)
                 

        # Animations
        def create_objects():
               
            self.add(plane)
            
            # create the wheel group
            self.play(Create(wheel), run_time = 1.5)
            self.play(AnimationGroup(wheel.animate.move_to([-4.5, -1, 0])), 
                    run_time = 2)
            
            # make the ball spin in the circle
            self.play(Create(ball), 
                    ball.animate.move_to(ex_wheel.get_top()))
            
        
        def get_angle():
            
            # get the two radii for the angle
            line_A = Line(center, first_pos, color = LOGO_BLACK, stroke_width = 2)
            line_B = Line(center, pos_in, color = LOGO_BLACK, stroke_width = 2)
            
            # show the angle and the associated text
            angle = Angle(line_A, line_B, radius = .3, other_angle = False,
                          color = LOGO_BLACK, stroke_width = 2)
            tex = MathTex(r"\theta", color = LOGO_BLACK).move_to(
                Angle(
                line_A, line_B, radius = 0.2 + 3 * SMALL_BUFF, other_angle = False
            ).point_from_proportion(0.2)
            )
            
            self.play(Create(line_A), Create(line_B))
            self.play(Create(angle), Create(tex))
            
        
        def ball_rotating():
        
            self.play(Rotate(ball, 10.472, rate_func = linear,
                          about_point = ex_wheel.get_center()), run_time = 2)
                  
        
        def ball_falling():
            
            # make the ball fall and trace trajectory
            self.add(trace)
            self.play(ball.animate(path_arc = -PI/1.5).
                    shift(RIGHT * 10 + DOWN * 1),
                    run_time = 3,
                    rate_func = linear)
            
            
        def get_distance():
            
            # make the distance appear
            dist_line = Line(pos_in, pos_fin)
            dist = Brace(dist_line, color = LOGO_BLACK, stroke_width = .5)
            dist_text = dist.get_text("s").set_color(LOGO_BLACK)
            
            self.play(Create(dist))
            self.play(Create(dist_text))
            
        
        create_objects()
        # get the very first position of the ball
        first_pos = ball.get_center()
        center = in_wheel.get_center()
        
        ball_rotating()
        # get the initial position of the ball
        pos_in = ball.get_center()
        
        get_angle()
        
        ball_falling()
        # get the final position of the ball
        pos_fin = ball.get_center()
        
        get_distance()
        
        self.wait(2)
