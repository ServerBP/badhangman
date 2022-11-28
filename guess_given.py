def guess(guess, answer, current_status, guessed, loa, already_solved):

    if guess in answer:
        guessed.append(guess)
        l = 0
        indexes = [i for i, c in enumerate(answer) if c == guess]
        print(indexes)
        print(len(indexes))
        while l <= len(indexes)-1:
            already_solved.update({indexes[l]: guess})
            l = l+1
        print(already_solved)


s = "apple"
g = "l"
alr = {0: "a"}
loa = "loa"
cs = "status"
guessed = ['']
guess(g, s, cs, guessed, loa, alr)
