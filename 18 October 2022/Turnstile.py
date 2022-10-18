"""Turnstile"""
def main():
    """Turnstile"""
    count = 0
    status = "L"
    while True:
        command = input().upper()
        if command == "END":
            break
        if command == "C" and status == "L":
            status = "UL"
        if command == "P" and status == "UL":
            status = "L"
            count += 1
    print(count)
main()
