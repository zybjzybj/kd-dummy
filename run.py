from helpers.audio import audio
import yaml

if __name__ == '__main__':
    name = "context.yaml"
    context = yaml.load(open(name))
    a = audio(context)
    a.run()
