class sepedah:
  def __init__(self, merk):
    self._merk = merk

class SepedahBalap(sepedah):
  def __init__(self, merk, total_gear):
    super().__init__(merk)
    self._total_gear = total_gear

  def pamer(self):
    # akses _merk dari subclass
    print(
      f'Ini sepedah {self._merk} dengan total gear {self._total_gear}'
    )
    
ferrari = SepedahBalap('cortex', 2)
ferrari.pamer()