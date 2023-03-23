from manim import *

class Bullet(Triangle):
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 0,
        "length": DEFAULT_ARROW_TIP_LENGTH,
        "start_angle": PI,
        "aspect": 1.5,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stretch_to_fit_height(self.CONFIG['length']*3)
        self.stretch_to_fit_width(self.CONFIG['length'] * self.CONFIG['aspect'])
        self.points[5:7] += np.array([self.CONFIG['length'], 0, 0])
        self.scale(0.5)

    def get_angle(self):
        return angle_of_vector(self.get_vector())

    def get_vector(self):
        return self.point_from_proportion(0.5) - self.get_start()

class TestBullet(Scene):
    CONFIG={
        'time':3,
    }
    def construct(self):
        vqueue1 = VGroup()
        vqueue2 = VGroup()
        self.an = 0

        def update_bullet1(obj, dt):
            obj.add(Bullet().scale(0.7).rotate(self.CONFIG['time'] * 10 + self.an * 10))
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(np.linalg.norm(k.get_center() - ORIGIN)) > 7:
                    obj.remove(k)
            self.an += 1 * DEGREES

        def update_bullet2(obj, dt):
            obj.add(Bullet().scale(0.7).rotate(PI + self.CONFIG['time'] * 10 + self.an * 10))
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(np.linalg.norm(k.get_center() - ORIGIN)) > 7:
                    obj.remove(k)
            self.an += 1 * DEGREES

        # vqueue1.add_updater(update_bullet1)
        # vqueue2.add_updater(update_bullet2)
        self.add(vqueue1,vqueue2)
        self.wait(5)