from jinja2 import Environment, PackageLoader


# Gravitational Constant
# TODO: Remove if none of the templates need this for calculations
G = 6.673*(10**-11)


def getGalaxyConfigFile():
    pass


class propertyNode(object):
    template = ""
    description = ""
    radius = None
    mass = None
    gravParameter = None
    gASL = None
    rotates = False
    rotationPeriod = 0
    initialRotation = 0
    tidallyLocked = False
    isHomeWorld = False
    sphereOfInfluence = None

    def __init__(
        self,
        template="",
        description="",
        radius=None,
        mass=None,
        gravParameter=None,
        gASL=None,
        rotates=False,
        rotationPeriod=0,
        initialRotation=0,
        tidallyLocked=False,
        isHomeWorld=False,
        sphereOfInfluence=None,
        timewarpAltitudeLimits=None
            ):

        self.env = Environment(
            loader=PackageLoader('galaxygen', 'templates'),
        )
        self.description = description
        if self.template == "":
            self.template = 'properties.txt'
        if radius:
            self.radius = radius
        if mass:
            self.mass = mass
        if gravParameter:
            self.gravityParam = gravParameter
        if gASL:
            self.gASL = gASL
        if rotates:
            self.rotates = rotates
            if rotationPeriod:
                self.rotationPeriod = rotationPeriod
            if 0 <= initialRotation <= 359:
                self.initialRotation = initialRotation
        self.tidallyLocked = tidallyLocked
        self.isHomeWorld = isHomeWorld
        self.sphereOfInfluence = sphereOfInfluence
        self.timewarpAltitudeLimits = timewarpAltitudeLimits

    def __str__(self):
        templateName = self.template
        template = self.env.get_template(templateName)
        return template.render(props=self)
