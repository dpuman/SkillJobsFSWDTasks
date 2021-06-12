data = input("Enter The value: ")

messageOne = ""
messageTwo = ""

try:
    data = int(data)

    messageOne = f"This is intiger {data} "
except Exception:
    messageTwo = f"Not intiger "

    try:
        data = float(data)

        messageOne += f"This is float {data} "
    except Exception:
        messageTwo += f" Not float "

        try:
            data = str(data)

            messageOne += f"This is Alpha {data} "
        except Exception:
            messageTwo += f" Not alpha "

print(messageOne+" "+messageTwo)
