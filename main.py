class PasswordEngine:
    def __init__(self):
        self.omega = []
    def readomega(self):
        print("Zbiór znaków do hasła:")
        print(self.omega)
    def alphas(self):
        alphas = []
        for i in range(97, 123): alphas.append(chr(i))
        print(alphas)
        c = input("Jeśli chcesz mieć w haśle małe litery, wpisz \"Tak\":\t")
        if c.lower() == "tak":
            print("Dodano do puli małe litery")
            self.omega += alphas
    def alphab(self):
        alphab = []
        for i in range(65, 91): alphab.append(chr(i))
        print(alphab)
        c = input("Jeśli chcesz mieć w haśle duże litery, wpisz \"Tak\":\t")
        if c.lower() == "tak":
            print("Dodano do puli duże litery")
            self.omega += alphab
    def numbers(self):
        num = []
        for i in range(10): num.append(str(i))
        print(num)
        c = input("Jeśli chcesz mieć w haśle cyfry, wpisz \"Tak\":\t")
        if c.lower() == "tak":
            print("Dodano do puli cyfry")
            self.omega += num
    def special_charts(self):
        s = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}"
        print(s)
        spchar = []
        c = input("Jeśli chcesz mieć w znaki specjalne, wpisz \"Tak\":\t")
        if c.lower() == "tak":
            d = True
            spchar = []
            b = input("Wypisz bez spacji jakie chcesz mieć znaki specjalne, jeśli powyższe i odpowiadają wpisz \"Wszystkie\":\t")
            if b.lower() == "wszystkie":
                for z in s: spchar.append(z)
            else:
                 while d:
                    if b == "":b = input("Wypisz bez spacji jakie chcesz mieć znaki specjalne:\t")
                    for z in b:
                        if z in spchar or z == " ": continue
                        spchar.append(z)
                    print("Wybrane znaki specjalne")
                    print(spchar)
                    c = input("Jeśli Ci odpowiadają, wpisz \"Tak\":\t")
                    if c.lower() == "tak": d = False
                    b = ""
            self.omega += spchar
    def generate(self,repeat,length,count):
        import random
        n = len(self.omega)
        print("Wygenerowane hasła:")
        if repeat:
            for i in range(count):
                password = []
                for j in range(length):
                    x = random.randint(0,n-1)
                    password.append(self.omega[x])
                print("".join(password))
        else:
            if n < length:
                print("ERROR LENGTH > LEN(OMEGA)")
                return 0
            for i in range(count):
                password = random.sample(self.omega,length)
                print("".join(password))
Pass = PasswordEngine()
Pass.alphas()
Pass.alphab()
Pass.numbers()
Pass.special_charts()
Pass.readomega()
repe = False
c = input("Jeśli chcesz mieć w hasle powtarzające znaki, wpisz \"Tak\":\t")
if c.lower() == "tak":repe = True
n = int(input("Podaj długość hasła:\t"))
z = int(input("Podaj ile chcesz wygenerować haseł:\t"))
Pass.generate(repe,n,z)