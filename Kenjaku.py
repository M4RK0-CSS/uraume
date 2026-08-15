print("==𝙳𝙴𝙰𝙳 𝙱𝙾𝙳𝚈==")

senha_correta = "Kenjaku"
tentativas = 3

while tentativas > 0:

    senha = input("Who are you? ")

    if senha == senha_correta:
        print("Welcome Kenjaku-sama!")
        break

    tentativas -= 1
    print("You are not Him, go away...")
    print(f"Attempts remaining: {tentativas}")

if tentativas == 0:
    print("Access blocked!")

else:
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
