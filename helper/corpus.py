import os


class corpus(object):
    def __init__(self, context):
        self.context = context

    def run(self):
        """
        Split train and test data.
        """
        tgt_root = '{0}/{1}'.format(self.context['egs']['root'], self.context['data']['dir'])
        tgt = '{0}/{1}'.format(tgt_root, self.context['data']['text'][self.__class__.__name__])
        tgt_dir = os.path.dirname(tgt)
        if not os.path.exists(tgt_dir):
            os.makedirs(tgt_dir)
        f = open(tgt, 'w')
        for i in self.context['data']['word']:
            for j in self.context['data']['word']:
                f.write("one {0} {1}\n".format(i, j))

