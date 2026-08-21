print("==Uraume-San==")

senha_correta = "Sukuna"
tentativas = 3

while tentativas > 0:

    senha = input("Who are you? ")

    if senha == senha_correta:
        print("Welcome Master Sukuna!")
        break

    tentativas -= 1
    print("You are not Him, go away...")
    print(f"Attempts remaining: {tentativas}")

if tentativas == 0:
    print("Access blocked!")

else:
    # Login validado
    while True:
        print("\n=== Uraume Powers ===")
        print("[1] Dispositive Info")
        print("[0] Exit")

        opcao = input("Choose: ")

        if opcao == "1":
            print("Dispositive Info force selected")

        elif opcao == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option!")
