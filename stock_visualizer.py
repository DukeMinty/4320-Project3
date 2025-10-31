# ---------- End Screen Loop ----------
while True:
    main()
    again = input("\nWould you like to search another stock? (y/n): ").lower()
    if again != 'y':
        print("\nThanks for using Stock Data Visualizer! Goodbye!")
        break
