class Nakladak:

    def __init__(self, _naklad=0):
        self._naklad = _naklad

    def naloz(self, naloz_kolik):
        if naloz_kolik + self._naklad >= 100:
            self._naklad = 100
        else:
            self._naklad += naloz_kolik

    def vyloz(self, vyloz_kolik):
        if - vyloz_kolik + self._naklad <= 0:
            self._naklad = 0
        else:
            self._naklad -= vyloz_kolik
    def vypis(self):
        print("Nakladak ma nalozeno {} jednotek."
              .format(self._naklad))
