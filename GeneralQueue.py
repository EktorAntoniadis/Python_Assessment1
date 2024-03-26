
# Αυτή η κλάση είναι γενική για όλες τις ουρές που μπορούν να χρησιμοποιήσουν άλλα αντικείμενα.
class GeneralQueue:
    def __init__(self):
        self.items = []

    # Βάζει ένα στοιχείο μέσα στη λίστα.
    def enqueue(self, item):
        self.items.append(item)

    # Βγάζει το πρώτο στοιχείο από τη λίστα
    def dequeue(self):
        return self.items.pop(0)
    
    # Βγάζει ένα συγκεκριμένο στοιχείο από τη λίστα
    def priority_dequeue(self, item):
        return self.items.remove(item)
    
    # Βγάζει το συνολικό αριθμό στοιχείων μέσα στη λίστα
    def size(self):
        return len(self.items)
    
    # Δείχνει αν η λίστα είναι άδεια
    def isEmpty(self):
        return self.items == []