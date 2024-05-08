from manim import *

class VelocityImage(Scene):
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
        plane.axes.set_color(GREY)
        
        stroke = 4
        
        # Wheel Group
        r = 2
        ex_wheel = Circle(r, color = "#553311", 
                          fill_color = "#553311", fill_opacity = 0.5)
        in_wheel = Circle(r * 0.8, color = "#553311", 
                          fill_color = "#553311", fill_opacity = 0.5 )
        wheel = VGroup(ex_wheel, in_wheel)
        
        
        # Ball
        ball = Circle(r * 0.1, color = "#332211",
                      fill_color = "#332211", fill_opacity = 0.85)
        ball.move_to(ex_wheel.get_top())
        pos_in = ball.get_center()
        ball.rotate(10.472, about_point = ex_wheel.get_center())
        pos_fin = ball.get_center() 
        
        
        # Angle
        center = in_wheel.get_center()
        
        line_A = Line(wheel.get_center(), ex_wheel.get_bottom(), color = LOGO_BLACK, stroke_width = stroke)
        line_B = Line(center, pos_fin, color = LOGO_BLACK, stroke_width = stroke)
        
        angle1 = Angle(line_A, line_B, radius = .5, other_angle = False,
                    color = LOGO_BLACK, stroke_width = stroke)
        tex_angle1 = MathTex(r"\theta", color = LOGO_BLACK).move_to(
            Angle(
            line_A, line_B, radius = 0.4 + 4 * SMALL_BUFF, other_angle = False
        ).point_from_proportion(0.4)
        )


        # Tangent Vector
        tan = TangentLine(ex_wheel, alpha = 0.917, length = 5, color = RED)
        v = Arrow(ball.get_center(), tan.get_end(), color = LOGO_BLACK, 
                  stroke_width = stroke)
        tex_v = MathTex(r"\vec{v}", color = LOGO_BLACK).move_to(
            v.get_top() + RIGHT * 0.8)
        
        v_par = Arrow(ball.get_center(), 
                      [2.9, -1, 0],
                      color = LOGO_BLACK,
                      stroke_width = stroke,
                      buff = 1)
        tex_v_par = MathTex(r"\vec{v_{\parallel}}", color = LOGO_BLACK).move_to(
            v_par.get_end() + UP * 0.2 + RIGHT * 0.3
        )
        
        v_per = Arrow(ball.get_center(),
                      [ball.get_center()[0], 1.3, 0],
                      color = LOGO_BLACK,
                      stroke_width = stroke)
        tex_v_per = MathTex(r"\vec{v_{\perp}}", color = LOGO_BLACK).move_to(
            v_per.get_top() + UP * 0.3 + RIGHT * 0.2
        )
        
        angle2 = Angle(v, v_par, radius = .5, other_angle = True,
                       color = LOGO_BLACK, stroke_width = stroke)
        tex_angle2 = MathTex(r"\alpha", color = LOGO_BLACK).move_to(
            Angle(
            v, v_par, radius = 0.4 + 4 * SMALL_BUFF, other_angle = True
        ).point_from_proportion(0.4)
        )
                
             
        def show():
            self.add(plane, wheel, ball)
            self.add(line_A, line_B, angle1, tex_angle1)
            self.add(v, tex_v, 
                     angle2, tex_angle2,
                     v_par, tex_v_par, 
                     v_per, tex_v_per)
            
        show()
        