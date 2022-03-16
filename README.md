# README

### Python script to find specific ethereum addresses that start with a predefined hex word.
#

Ethereum addressses 

You get a public address for your account by taking the last 20 bytes of the Keccak-256 hash of the public key and adding 0x to the beginning.
#
*The "0x" prefix means hexadecimal and it's a way to tell programs, contracts, APIs that the input should be interpreted as a hexadecimal number.*

more info and credit -> https://ethereum.stackexchange.com/questions/503/what-is-the-0x-i-see-around-ethereum-for-example-i-see-addresses-that-start-wit

Usually the public key is generated from the private key using the Elliptic Curve Digital Signature Algorithm, this means we do not have any direct control over how the public key will look like.

more info -> https://ethereum.org/en/developers/docs/accounts/
#
## external library eth-account
more info -> https://pypi.org/project/eth-account/
#
With this script you can try and force find specific ethereum addresses that start with what can be called hex words. Words that can be represented using hex values.

Hex uses 16 digits including 0-9, just as the decimal system does, but also uses the letters A, B, C, D, E, and F (equivalent to a, b, c, d, e, f) to represent the numbers 10-15.

Some examples are: dead, beef, c0ffee, b00b5 (kek).

more info on hex words -> https://en.wikipedia.org/wiki/Hexspeak,
https://www.calculator.net/hex-calculator.html


# run
#### prerequisites
### ->linux
install python3 -> https://www.python.org/downloads/,
install git -> https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
### ->windows
install python -> https://www.python.org/downloads/release/python-3102/,
intall git -> https://git-scm.com/download/win,
install microsoft c++ build tools -> https://visualstudio.microsoft.com/visual-cpp-build-tools/
#
```[extra]```consider using a virtual environment in order not to break dependencies, more info -> https://docs.python.org/3/library/venv.html
#
### linux
```bash
python3 -m pip install eth-account
git clone https://github.com/softspork/find-eth-address.git
cd find-eth-address
python3 find.py
```
```bash
python3 -m pip install eth-account;git clone https://github.com/softspork/find-eth-address.git;cd find-eth-address;python3 find.py
```
![demo](https://user-images.githubusercontent.com/86022395/158577758-46016735-644b-4395-89ae-b29e069e2cb7.gif)
#
### windows
```cmd
pip install eth-account
git clone https://github.com/softspork/find-eth-address.git
cd find-eth-address
python3 find.py
```

```cmd
pip install eth-account && git clone https://github.com/softspork/find-eth-address.git && cd find-eth-address && python3 find.py
```
#
#### using 123,111,222 as demo hex words to preview how it works
![demo2](https://user-images.githubusercontent.com/86022395/158577775-4e864190-405c-4b5c-8576-9f82e980d7db.gif)
#
## found.txt
this is were the public and private keys will be saved.
![image](https://user-images.githubusercontent.com/86022395/158565749-d4b36668-8e32-461e-bbd7-963e8167fdd9.png)
![image](https://user-images.githubusercontent.com/86022395/158571165-df450f78-acfc-4e72-816a-e5e6f1752fc2.png)
#
## words.txt
this is were you define what hex words to search for.
![image](https://user-images.githubusercontent.com/86022395/158573566-c86e9843-658d-4e14-86c7-108577f49e5f.png)
#
### Example on Opensea
![image](https://user-images.githubusercontent.com/86022395/158588020-c1ec8fcf-f327-4800-95a2-b6ea466d5349.png)
### Example on Web3 games with leaderboards. Below example is for https://www.arcadenfts.com tournaments.
![image](https://user-images.githubusercontent.com/86022395/158588909-d7d49cb9-8f2d-4be3-96c5-320c809f1893.png)