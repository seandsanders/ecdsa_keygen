ecdsa_keygen
============

This is a minialistic ECDSA keypair generator. It generates a new key pair and prints hexlified versions
of the private and public keys.

##1. Installation
Create a python virtual environment (or don't, what do I care?)

    virutalenv ecdsa_keygen

Activate virtual environment

    cd ecdsa_keygen
    source bin/activate

Setup ecdsa_keygen

    git clone https://github.com/seandsanders/ecdsa_keygen
    (cd ecdsa_keygen; python setup.py develop)

##2. Usage
Just call it.

    python ecdsa_keygen.py

By default it uses the NIST256p curve. Mostly because that's what I was using it for.
If you want to use another curve, you can pass one in like this:

    python ecdsa_keygen.py --curve=nist192p

If you're dense there's help

    python ecdsa_keygen.py --help

OK not much help, but it's there.

##5. License

ECDSA keygen has been released under the MIT Open Source license.

###5.1 The MIT License

Copyright (C) 2014 Sean Sanders and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.