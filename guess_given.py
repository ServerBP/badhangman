def guess(guess, answer, current_status, guessed, correct_guesses):
    msg = "err0"
    if guess in guessed:
        msg = "err1"
    else:
        if guess in answer:
            guessed.append(guess)
            correct_guesses.append(guess)
            l = 0
            indexes = [i for i, c in enumerate(answer) if c == guess]
            while l <= len(indexes)-1:
                current_status.update({indexes[l]: guess})
                l = l+1
        else: msg = "err0"
    return msg, current_status, guessed, correct_guesses
