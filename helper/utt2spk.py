import glob
import os


class utt2spk(object):
    def __init__(self, context):
        self.context = context

    def run(self):
        """
        Split train and test data.
        """
        src_root = '{0}/{1}'.format(self.context['egs']['root'], self.context['audio']['target']['dir'])
        tgt_root = '{0}/{1}'.format(self.context['egs']['root'], self.context['data']['dir'])
        for k, v in self.context['data']['split'].items():
            src = '{0}/{1}'.format(src_root, k)
            tgt = '{0}/{1}/{2}'.format(tgt_root, k, self.context['data']['text'][self.__class__.__name__])
            tgt_dir = os.path.dirname(tgt)
            if not os.path.exists(tgt_dir):
                os.makedirs(tgt_dir)
            f = open(tgt, 'w')
            for e in v:
                file_list = glob.glob('{0}/*/1_{1}*'.format(src, e))
                #print(file_list)
                [f.write("{0} {1}\n".format("{0}_{1}".format(e, os.path.basename(file).split('.')[0]), e)) for file in sorted(file_list)]

