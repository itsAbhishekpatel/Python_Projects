from Sample_madlibs import hp, code, hungergame, zombie
import random

if __name__ == "__main__":
    template = random.choice([hungergame,hp,code,zombie])
    template.madlib()


