import secrets, sys
from eth_account import Account

while 1:
    try:
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key)

        with open('words.txt', 'r') as file:
            for line in file:

                max = len(line.rstrip()) + 2
                print('\r' + acct.address, end='')

                if acct.address[2:max] == line.rstrip():
                    print('\n' + private_key + '\n' + ('=' * (66)))

                    with open("found.txt", "a") as file_object:
                        file_object.write('\n' + acct.address + '\n' + private_key + '\n' + ('=' * (66)))
    except KeyboardInterrupt:
        sys.exit('\nBye!')