import argparse
from binascii import hexlify
from ecdsa import SigningKey, NIST256p
from ecdsa.curves import curves


def generate_ecdsa_keypair(curve):
    signing_key = SigningKey.generate(curve=curve)
    signing_key.to_string()
    verifying_key = signing_key.get_verifying_key()
    return signing_key, verifying_key


class ParseCurveAction(argparse.Action):
    CURVES_DICT = {curve.name.lower(): curve for curve in curves}

    def __call__(self, parser, namespace, values, option_string=None):
        value = self.CURVES_DICT[values]
        setattr(namespace, self.dest, value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--curve',
        choices=ParseCurveAction.CURVES_DICT.keys(),
        action=ParseCurveAction,
        default=NIST256p,
    )
    args = parser.parse_args()

    private, public = generate_ecdsa_keypair(args.curve)
    print "private: %s" % hexlify(private.to_string())
    print "public: %s" % hexlify(public.to_string())

if __name__ == '__main__':
    main()