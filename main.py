"""
Main module.
"""

import hupper


def watch():
    """Watch files/"""
    reloader = hupper.start_reloader('server.server.main')

    # monitor an extra file
    reloader.watch_files(['server/*/py'])


if __name__ == '__main__':
    watch()
