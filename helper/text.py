import os


class text(object):
    def __init__(self, context):
        self.context = context

    def run(self):
        """
        Split train and test data.
        """
        t_root = '{0}/{1}'.format(self.context['egs']['root'], self.context['data']['dir'])
        for k, v in self.context['data']['split'].items():
            tgt = '{0}/{1}/{2}'.format(t_root, k, self.context['data']['text'][self.__class__.__name__])
            tgt_dir = os.path.dirname(tgt)
            if not os.path.exists(tgt_dir):
                os.makedirs(tgt_dir)
            f = open(tgt, 'w')
            for e in v:
                for i, digit in enumerate(self.context['data']['word']):
                    f.write("{0}_1_{0}_{1} one {2} {3}\n".format(e, i, self.context['data']['word'][e], self.context['data']['word'][i]))

