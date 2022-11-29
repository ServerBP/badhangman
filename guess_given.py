def guess(guess, answer, current_status, guessed):
    if guess in guessed:
        return "err1"
    if guess in answer:
        guessed.append(guess)
        l = 0
        indexes = [i for i, c in enumerate(answer) if c == guess]
        while l <= len(indexes)-1:
            current_status.update({indexes[l]: guess})
            l = l+1
    return current_status


s = "apple"
g = "p"
loa = "loa"
cs = {0: "_", 1: "_", 2: "_", 3: "_", 4: "_", }
guessed = ['']
cs = guess(g, s, cs, guessed, loa)
solstring = ''.join(cs.values())
print(solstring)
cs = guess("a", s, cs, guessed, loa)
solstring = ''.join(cs.values())
print(solstring)
