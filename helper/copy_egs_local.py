import shutil
import os


class copy_egs_local(object):
    def __init__(self, context):
        self.context = context

    def run(self):
        """
        Copy lexicon.txt into target dir.
        """
        src = '{0}/{1}'.format(os.path.dirname(self.context['egs']['root']), self.context['data']['text'][self.__class__.__name__]['src'])
        tgt = '{0}/{1}'.format(self.context['egs']['root'], self.context['data']['text'][self.__class__.__name__]['tgt'])
        tgt_dir = os.path.dirname(tgt)
        if not os.path.exists(tgt_dir):
            os.makedirs(tgt_dir)
        shutil.copy(src, tgt)

