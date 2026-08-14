print("==𝙳𝙴𝙰𝙳 𝙱𝙾𝙳𝚈==")

senha = input("Who are you? ")

if senha == "Kenjaku":
    print("Welcome Kenjaku-sama!")

    # Login validado
    while True:
        print("\n=== Kenjaku's Brain ===")
        print("[1] Kenjaku's brute force")
        print("[0] Exit")

        opcao = input("Choose: ")

        if opcao == "1":
            print("Kenjaku's brute force selected")

        elif opcao == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option!")

else:
    print("You are not Him, go away...")
