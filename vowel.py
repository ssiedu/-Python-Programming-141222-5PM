alpha=input("Enter any character : ")
match alpha.lower():
    case 'a'|'e'|'o'|'u'|'i':
        print("vowel")
    
    case _:
        print("Consonent")
