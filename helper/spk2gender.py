import os


class spk2gender(object):
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
            [f.write("{0} m\n".format(e)) for e in v]

