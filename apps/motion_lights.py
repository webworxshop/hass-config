import appdaemon.plugins.hass.hassapi as hass

class MotionLight(hass.Hass):

    def initialize(self):
        self.motion_sensor = self.args['motion_sensor']
        self.light = self.args['light']
        self.timeout = self.args['timeout']

        self.timer = None
        self.listen_state(self.motion_callback, self.motion_sensor, new = "on")

    def set_timer(self):
        if self.timer is not None:
            self.cancel_timer(self.timer)
        self.timer = self.run_in(self.timeout_callback, self.timeout)

    def is_light_times(self):
        #return self.now_is_between("sunset - 00:10:00", "sunrise + 00:10:00")
        return True

    def motion_callback(self, entity, attribute, old, new, kwargs):
        if self.is_light_times():
            self.turn_on(self.light)
            self.set_timer()

    def timeout_callback(self, kwargs):
        self.timer = None
        self.turn_off(self.light)

class BrightnessControlledMotionLight(MotionLight):

    def initialize(self):
        self.last_door = "Other"
        for door in self.args['bedroom_doors']:
            self.listen_state(self.bedroom_door_callback, door, old = "off", new = "on")
        for door in self.args['other_doors']:
            self.listen_state(self.other_door_callback, door, old = "off", new = "on")

        super().initialize()

    def bedroom_door_callback(self, entity, attribute, old, new, kwargs):
        self.last_door = "Bedroom"
        self.log("Last door is: {}".format(self.last_door))

    def other_door_callback(self, entity, attribute, old, new, kwargs):
        self.last_door = "Other"
        self.log("Last door is: {}".format(self.last_door))

    def motion_callback(self, entity, attribute, old, new, kwargs):
        if self.is_light_times():
            #if self.now_is_between("07:00:00", "20:00:00") or 
            if self.last_door != "Bedroom":
                self.turn_on(self.light, brightness_pct = 100)
            else:
                self.turn_on(self.light, brightness_pct = 1)
            self.set_timer()

