import os
import sys
from pathlib import Path

import fire
import logging


class Cmd(object):
    def start_server(self, port=9000, base_url='http://localhost'):
        meta = class_loader('mockrtb.http.RtbHttpEndpoint')
        endpoint = meta()
        endpoint.run(port, base_url)


def class_loader(fq_class_name):
    cls_name = fq_class_name.rsplit('.', 1)[-1]
    mod = __import__(fq_class_name, fromlist=[cls_name])
    return getattr(mod, cls_name)


def main():
    logging.basicConfig(level=logging.INFO)
    pkg_path = Path(os.path.dirname(__file__)) / '..'
    sys.path.append(os.path.abspath(pkg_path))
    logging.info(sys.path)
    fire.Fire(Cmd)


if __name__ == '__main__':
    main()
