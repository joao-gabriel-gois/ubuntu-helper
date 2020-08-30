class colors:
    PU = '\033[95m'
    BL = '\033[94m'
    GR = '\033[92m'
    YE = '\033[93m'
    RE = '\033[91m'
    END = '\033[0m'
    BLD = '\033[1m'
    UNDLN = '\033[4m'


if __name__ == "__main__":
    c = colors()
    print(
      f'{c.PU}  test {c.END}\n',
      f'{c.BL} test {c.END}\n',
      f'{c.GR} test {c.END}\n',
      f'{c.YE} test {c.END}\n',
      f'{c.RE} test {c.END}\n',
      f'{c.PU}{c.BLD} test {c.END}\n',
      f'{c.PU}{c.UNDLN} test {c.END}\n',
    )
