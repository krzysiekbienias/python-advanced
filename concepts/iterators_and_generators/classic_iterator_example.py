class KlasycznyIterator:
    def __init__(self):
        self.obecna_liczba = 1
        self.maksimum = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.obecna_liczba > self.maksimum:
            raise StopIteration
        
        wynik = self.obecna_liczba
        self.obecna_liczba += 2
        return wynik

# Użycie:
if __name__=="__main__":
    moj_iterator = KlasycznyIterator()
    for liczba in moj_iterator:
        print(liczba)