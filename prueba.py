from datetime import datetime

def main():
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Esto funciona")
    print(f"Hora actual: {hora_actual}")

if __name__ == "__main__":
    main()
