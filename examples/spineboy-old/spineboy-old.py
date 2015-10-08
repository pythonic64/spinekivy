from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

from spinekivy.skeletonrenderer import SkeletonRenderer
from spinekivy.sprite import Sprite


class MainScreen(Widget):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.skeleton_renderer = renderer = SkeletonRenderer()
        renderer.scale = 1.0
        renderer.load('assets', 'spineboy-old')
        renderer.skeleton.x = 320
        renderer.skeleton.y = 100
        renderer.sprites = [Sprite() for _ in renderer.skeleton.draw_order]
        renderer.state.set_animation_by_name(0, 'walk', True)
        renderer.state.add_animation_by_name(0, 'jump', False, 3.0)
        renderer.state.add_animation_by_name(0, 'walk', True, 0)
        for sprite in renderer.sprites:
            self.canvas.add(sprite)
        renderer.update(0)
        renderer.draw()

    def update(self, dt):
        renderer = self.skeleton_renderer
        renderer.update(dt)
        renderer.draw()


class SpineBoyOldApp(App):

    def build(self):
        return MainScreen()

    def on_start(self):
        super(SpineBoyOldApp, self).on_start()
        Clock.schedule_interval(self.root.update, 0)


if __name__ == '__main__':
    SpineBoyOldApp().run()
