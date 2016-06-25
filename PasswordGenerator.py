def password_gen(number_letters, number_pwds=1):
    import random
    import string
    psw = []
    for i in range(number_pwds):
        psw.append("".join(random.sample(list(string.ascii_letters + string.digits + "!@#$%^&*()_+-:;\"\\|[]`<>"), number_letters)))
    print psw[i] for i in range(number_pwds)



print password_gen(6)
print password_gen(6, 5)