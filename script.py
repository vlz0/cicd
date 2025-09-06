import platform, datetime

def main():
    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"Fecha y Hora desde Python: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()