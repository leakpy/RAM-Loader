import sys

def allocate_memory(mb_count):
    return bytearray(mb_count * 1024 * 1024)

def main():
    try:
        mb_count = int(input("Enter the number of megabytes to be added: "))
        data =allocate_memory(mb_count)
        print(f"{mb_count} megabytes are allocated in RAM.")
    except ValueError:
        print("Please enter a integer.")
        sys.exit(1)

    try:
        while True:
            command = input("Enter 'stop', to free up memory and exit the program: ").strip().lower()
            if command == "stop":
                print("RAM cleared, Everything completed successfully.")
                break
    except KeyboardInterrupt:
        print("\nThe program was interrupted by the user.")
    finally:
        del data

if __name__ == "__main__":
    main()
