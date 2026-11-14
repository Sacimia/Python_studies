def main():
    print("1) Portuguese")
    print("2) English")
    while True:
        option = input("Escolha o idioma / Choose your language (1/2): ").strip()
        if option == "1":
            import mansao_blackwood as game
            break
        if option == "2":
            import blackwood_manor as game
            break
        game.main()


if __name__ == "__main__":
    main() 
           