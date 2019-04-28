from __future__ import print_function

import napalm
import sys
import os


def main(config_file):

    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = 'Missing or invalid config file {0}'.format(config_file)
        raise ValueError(msg)

    print('Loading config file {0}.'.format(config_file))

    driver = napalm.get_network_driver('eos')

    device = driver(hostname='127.0.0.1', username='vagrant',
                    password='vagrant', optional_args={'port': 12443})

    print('Opening ...')
    device.open()

    print('Loading replacement candidate ...')
    device.load_replace_candidate(filename=config_file)


    print('\nDiff:')
    print(device.compare_config())


    try:
        choice = raw_input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()


    device.close()
    print('Done.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please supply the full path to "new_good.conf"')
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)