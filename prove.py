from manim import *

class Tries(Scene):
    def construct(self):
        plane = NumberPlane()
        
        line = Line(start = [1, -1, 0], 
                    end = [2, 3, 0], color = RED)
        b = line.get_vector()     
        
        self.add(plane, line)
        
        return b
    
class Rotation(Scene):
    def construct(self):
        
        circle = Circle(1, color = RED,
            fill_color = RED, fill_opacity = 0.5)
        ball = Circle(0.2, color = WHITE,
            fill_color = WHITE, fill_opacity = 0.75).shift(circle.get_top())  
        
        self.play(Create(circle), Create(ball))
        self.play(Rotate(ball, 2*PI*2, about_point = circle.get_center(),
                         rate_func = linear), run_time = 5)
        
        self.wait(2)
        
class MovingGroup(Scene):
    def construct(self):
        
        circle1 = Circle(1, color = RED)
        circle2 = Circle(0.5, color = GREEN)
        group = VGroup(circle1, circle2)
        
        self.play(Create(group))
        self.play(AnimationGroup(group.animate.move_to([1, 1, 0])))
        
        self.wait(2)
        
class RadiusCircle(MovingCameraScene):
    def construct(self):
        
        pass
    
class FollowPath(Scene):
    def construct(self):
        
        square = Square(1, color = BLUE)
        path = Line(LEFT*5, RIGHT*5, stroke_opacity = .5)
        path.points[1:3] += UP*2
        square.move_to(path.point_from_proportion(alpha = 0))
        
        self.add(square, path)
        self.play(MoveAlongPath(square, path), run_time = 3)
        self.wait()
        
class DissipatingPath(Scene):
    def construct(self):
        
        a = Dot()
        path = Axes().plot(lambda x: -0.5 * x ** 2)
        
        self.add(a, path)
        self.play(MoveAlongPath(a, path), rate_func = linear)
        self.wait()
        
class TracedPathProblem(Scene):
    def construct(self):
        dot = Dot(color=RED)
        
        trace = TracedPath(dot.get_center,stroke_color=RED)
        
        self.add(dot,trace)
        self.play(dot.animate.shift(RIGHT),run_time=2)
        path = trace.copy()
        self.play(path.animate.shift(2*UP+RIGHT)) #do not want tracing here
        self.wait()
        
class ball_jump(Scene):
    def construct(self):
        
        plane = NumberPlane()
        
        ball = Circle(0.2, color = RED, fill_opacity = 0.5).move_to([-3, 1, 0])
        trace = TracedPath(ball.get_center, stroke_color = WHITE)
        
        self.add(plane, ball, trace)
        self.play(ball.animate(path_arc = -PI/1.5).shift(RIGHT * 5 + DOWN * 1.5), run_time = 3)
        
        self.wait()
        
class plane_setup(Scene):
    def construct(self):
        
        self.camera.background_color = LOGO_BLACK
        
        plane = Axes(
            x_range = np.array([-8, 8, 0.5]),
            y_range = np.array([-4, 4, 0.5]),
            x_length = 13,
            y_length = 7,
            tips = False,
        )
        
        a = Dot([1, 1, 0], color = RED)
        
        self.add(plane)
        plane.add(a)
        
        self.wait(5)
        
class normal_plane(Scene):
    def construct(self):
        
        normal_plane = NumberPlane(
            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 0.3
            }
        )
        self.add(normal_plane)
        
        second_plane = NumberPlane(
            x_range = (-1, 13, 1),
            y_range = (-1, 7, 1),
            
            background_line_style = {
                "stroke_opacity": 0
            }
        )
        self.add(second_plane)
        
        a = Dot(color = BLUE_C)
        
        self.add(a)

class distance(Scene):
    def construct(self):
        
        
        dot1 = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        
        line = Line(dot1.get_center(), dot2.get_center(), color = ORANGE)
        b1 = Brace(line)
        
        self.add(line, b1)

class angle(Scene):
    def construct(self):
        
        line_A = Line([0, 0, 0], [3, 0, 0])
        line_B = Line([0, 0, 0], [-2, 3, 0])
        
        a = Angle(line_A, line_B, radius = .5, other_angle = False, color = BLUE)

        theta = MathTex(r"\theta", color = RED).move_to(Angle(
            line_A, line_B, radius=0.5 + 3 * SMALL_BUFF
        ))
        
        theta.set_color_by_tex("start", RED)
        theta.set_color_by_tex("end", RED)

        self.add(line_A, line_B, a, theta)  

        