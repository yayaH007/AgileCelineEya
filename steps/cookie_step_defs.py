from behave import *


from dataclasses import dataclass

from cookie import Cookie


@dataclass
class ManageBiblioSteps:
    _taste: str
    _pepite: int
    cookie : Cookie




    @Given("i buy a {taste} cookie")
    def step_impl_1(self, taste):
        self.cookie=Cookie(taste)
        self._taste=self.cookie.get_gout()
        assert self._taste is not None

    @when ("I check for pepites")
    def step_impl_3(self):
        self._pepite = self.cookie.get_gout_pepite()
        assert self._pepite is not None


    @then("the pepites number is {nb_pepite}")
    def step_impl_3(self, nb_pepite):
        assert self._pepite == int(nb_pepite)
